import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

myqr = qrcode.make('http://www.youtube.com/@LahiruDilshan-ct4mq')
myqr1 = qrcode.make('https://www.youtube.com/watch?v=y1zJiHcoTA4&list=PLpUo7TyHQvlu0KzY9b-od1y4zKQ6kkPvk&pp=0gcJCaIEOCosWNin ')

myqr.save("myqr.png", scale = 8)
myqr1.save("myqr1.png", scale = 7)



b = decode(Image.open("myqr.png"))
print(b[0].data.decode('ascii'))
