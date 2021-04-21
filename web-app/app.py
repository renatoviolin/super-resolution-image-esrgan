import sys
import os
sys.path.insert(0, os.path.realpath(os.path.pardir))

from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, HTMLResponse
import uuid
from PIL import Image
import cv2
import logging
from esrgan import engine
import numpy as np

logger = logging.getLogger("uvicorn.error")

IMAGES_FOLDER = './images'
app = FastAPI()
app.mount("/static", StaticFiles(directory="templates/static"), name="static")
app.mount("/images", StaticFiles(directory=IMAGES_FOLDER), name="images")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", context={'request': request})


@app.post("/process", response_class=HTMLResponse)
async def index(request: Request, file: UploadFile = File(...)):
    try:
        name = str(uuid.uuid4()).split('-')[0]

        ext = file.filename.split('.')[-1]
        file_name = f'{IMAGES_FOLDER}/{name}_input.{ext}'
        with open(file_name, 'wb+') as f:
            f.write(file.file.read())
        f.close()

        input_image = Image.open(file_name)
        input_size = input_image.size

        upsample = input_image.resize((int(input_image.size[0]) * 4, int(input_image.size[1] * 4)), resample=Image.BICUBIC)
        up_size = upsample.size
        upsample.save(f'images/{name}_upsample.{ext}')

        # generate image
        img_gan = engine.generate(np.array(input_image))
        cv2.imwrite(f'images/{name}_gan.{ext}', cv2.cvtColor(img_gan, cv2.COLOR_BGR2RGB))
        gan_size = f'({img_gan.shape[1]}, {img_gan.shape[0]})'

        result = {
            'img_input': f'images/{name}_input.{ext}',
            'img_upsample': f'images/{name}_upsample.{ext}',
            'img_gan': f'images/{name}_gan.{ext}',
            'input_size': str(input_size),
            'up_size': str(up_size),
            'gan_size': str(gan_size),
        }

        return JSONResponse(status_code=200, content={'result': result})

    except Exception as ex:
        logger.error(ex)
        return JSONResponse(status_code=400, content={'error': ex})
