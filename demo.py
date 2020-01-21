import qrcode
#qr = qrcode.make('hello')
#qr.save('myqr.jpg')

qr = qrcode.QRCode(
	version=1,
	box_size=15,
    border=5
	)
data ='https://github.com/rishigole42'
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('github.png')