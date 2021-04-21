# Generating high-res images using ESRGAN-PyTorch

This repository show the code to upscale pictures by 4x using [ESRGAN](https://github.com/xinntao/ESRGAN).

Given a low resolution picture, the goal is to upscale by 4x and compare with the Bicubic Algorithm.

As you can see, the results are very good. Try yourself

### Demo
![Demo](screenshot/demo.gif)



### Endpoint available
| Endpoint | Description
| --- | ---
| http://localhost:8000/ |  Front-end to perform style transfer.


### Install
1. Clone this repository
```bash
git clone https://github.com/renatoviolin/Deploying-YOLOv5-fastapi-celery-redis-rabbitmq.git
cd Deploying-YOLOv5-fastapi-celery-redis-rabbitmq
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Start web-application
```bash
cd web-app
uvicorn app:app --host 0.0.0.0 --port 8000
```

### Running on Google Colab
You can running on colab using ngrok. [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1fVHpgU3OKQtp5_gJ5_aXhx24zg0ba5lQ?usp=sharing)


### References
[ESRGAN](https://github.com/xinntao/ESRGAN)


#### BibTeX
    @InProceedings{wang2018esrgan,
        author = {Wang, Xintao and Yu, Ke and Wu, Shixiang and Gu, Jinjin and Liu, Yihao and Dong, Chao and Qiao, Yu and Loy, Chen Change},
        title = {ESRGAN: Enhanced super-resolution generative adversarial networks},
        booktitle = {The European Conference on Computer Vision Workshops (ECCVW)},
        month = {September},
        year = {2018}
    }
