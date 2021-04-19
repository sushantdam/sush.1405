import pyqrcode
import png
from pyqrcode import QRCode
QRstring = "https://www.youtube.com/"
url = pyqrcode.create(QRstring)
url.png('Desktop\\qr.png', scale = 8)