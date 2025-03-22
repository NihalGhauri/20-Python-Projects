import qrcode

data = "https://nihal-khan.vercel.app/"

qr = qrcode.QRCode(version=1, box_size=10, border=5)


qr.add_data(data)

qr.make(fit=True)
img= qr.make_image(fill_color = 'blue', back_color = 'white')

img.save('C:/Users/Nihal Khan Ghauri/Downloads/qr_code.png')


