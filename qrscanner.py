import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

myqr = qrcode.make('http://www.youtube.com/@LahiruDilshan-ct4mq')
myqr1 = qrcode.make('https://youtu.be/pQw5GGpEmI8?si=w_gGzXWQyPgnlFIj')

myqr.save("myqr.png", scale = 8)
myqr1.save("myqr1.png", scale = 7)



b = decode(Image.open("myqr.png"))
print(b[0].data.decode('ascii'))
