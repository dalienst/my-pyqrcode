import qrcode
#generating QR code using the make() function
img = qrcode.make("Hello, this is my first QR Code")
# saving the image file
img.save("qr-img.jpg")