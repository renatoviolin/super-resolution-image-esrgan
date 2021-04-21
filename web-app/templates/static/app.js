var show = false
var interval

var show_and_hide = function (increased_size) {
    if (show) {
        $("#show-label").html('ESRGAN: ' + increased_size)
        $("#show-label").css('background-color', '#009b4d')
        $('#a_gan').show()
        $('#a_upsample').hide()
        show = false
    } else {
        $("#show-label").html('BICUBIC: ' + increased_size)
        $("#show-label").css('background-color', '#cf5d00')
        $('#a_upsample').show()
        $('#a_gan').hide()
        show = true
    }
}

$(document).ready(function () {
    $("#row_results").hide()
    $('#btn-process').on('click', function () {
        var form_data = new FormData();
        form_data.append('file', $('#input_file').prop('files')[0]);

        $.ajax({
            url: '/process',
            type: "post",
            data: form_data,
            enctype: 'multipart/form-data',
            contentType: false,
            processData: false,
            cache: false,
            beforeSend: function () {
                $("#row_results").hide()
                $(".overlay").show()
                clearInterval(interval)
            },
        }).done(function (jsondata, textStatus, jqXHR) {
            result = jsondata['result']

            $('.img_input').attr('src', `${result["img_input"]}`)
            $('#a_input').attr('href', `${result["img_input"]}`)

            $('.img_upsample').attr('src', `${result["img_upsample"]}`)
            $('#a_upsample').attr('href', `${result["img_upsample"]}`)

            $('.img_gan').attr('src', `${result["img_gan"]}`)
            $('#a_gan').attr('href', `${result["img_gan"]}`)

            $('#label-input').html(`INPUT: ${result["input_size"]}`)

            increased_size = result["gan_size"]
            $("#row_results").show()
            show_and_hide(increased_size)
            $(".overlay").hide()

            interval = setInterval(function () {
                show_and_hide(increased_size)
            }, 3000);

        }).fail(function (jsondata, textStatus, jqXHR) {
            console.log(jsondata)
            $(".overlay").hide()
        });

    })
})