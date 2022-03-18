import qrcode
input_data = "https://github.com/dalienst"

qr = qrcode.QRCode(
    version = 1,
    box_size = 10,
    border = 5)

qr.add_data(input_data)
qr.make(fit=True)

img = qr.make_image(fill='orange', back_color='white')
img.save('gitlink.png')