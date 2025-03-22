from pyzbar.pyzbar import decode
from PIL import Image

img= Image.open('C:/Users/Nihal Khan Ghauri/Downloads/qr_code.png')

result = decode(img)

print(result)