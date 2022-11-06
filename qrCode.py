import pyqrcode

import shutil

import os

import png

from pyqrcode import QRCode


def moveFunction():
    source = os.getcwd() + "/" + name + ".png"

    destination = os.getcwd() +"/images/" + name + ".png"


    shutil.move(source, destination)

s = input("Enter url : ")

name = input("Enter image name : ")

url = pyqrcode.create(s)

url.png(name + '.png', scale=6)

moveFunction();



