import qrcode

url = input("Enter the url to make a qrcode: ")
filename = input("Enter the filename: ")
if not(filename.endswith(".png")):
    filename = filename + ".png"

img = qrcode.make(url)
img.save(filename)
