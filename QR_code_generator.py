import qrcode
from PIL import Image

# img = qr.make("https://www.youtube.com/watch?v=5yROWrlcprE")
# img.save("arijit_song.png")
qr  = qrcode.QRCode(version = 1 ,
                    error_correction = qrcode.constants.ERROR_CORRECT_H,
                    box_size = 10, border = 2)
qr.add_data("https://www.youtube.com/watch?v=5yROWrlcprE")
qr.make(fit = True)
img = qr.make_image(fill_color = "blue", back_color="pink")
img.save("ar1.png")