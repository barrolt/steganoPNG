import cv2
import math
import numpy as np
import random

from .vigenere import Vigenere
from pathlib import Path
import ntpath

from main import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets, QtGui

class LSB():
    def __init__(self):
        self.mask_one = [1, 2, 4, 8, 16, 32, 64, 128]
        self.mask_or = self.mask_one.pop(0)

        self.mask_zero = [254, 253, 251, 247, 239, 223, 191, 127]
        self.mask_and = self.mask_zero.pop(0)

        self.curr_pos = 0
        self.curr_channel = 0

        self.encrypted = False

        self.temp = 0
        self.lcg = None
        self.curr_lcg = 0
        self.lcg_modulus = 97
        self.lcg_multiplier = 13
        self.lcg_increment = 3
        self.lcg_seed = 0

    def reset(self):
        self.mask_one = [1, 2, 4, 8, 16, 32, 64, 128]
        self.mask_or = self.mask_one.pop(0)

        self.mask_zero = [254, 253, 251, 247, 239, 223, 191, 127]
        self.mask_and = self.mask_zero.pop(0)

        self.curr_pos = 0
        self.curr_channel = 0

        self.temp = 0
        self.lcg = None
        self.curr_lcg = 0
        self.lcg_modulus = 97
        self.lcg_multiplier = 13
        self.lcg_increment = 3
        self.lcg_seed = 0

    def readImage(self, filename):
        self.reset()

        try:
            image = cv2.imread(filename)

            self.path = filename
            print("filename in readimage", self.path)

            self.image = image
            self.height, self.width, self.channels = image.shape
            print("height in readimage ", self.height)
            print("width in readimage ", self.width)
            print("channels in readimage ", self.channels)
            self.size = self.width * self.height
            print("size in readimage ", self.size)
            self.map = list(range(self.size))
#            print("map in readimage", map)
        except Exception as exception:
            return 'FAILED'

    def writeImage(self, filename):
        cv2.imwrite(filename, self.image)

    def get_xy(self, z):
        x = z // self.width
        y = z % self.width

#        print("x = ", x)
#        print("y = ", y)

        return x, y

    #untuk berpindah antar pos dan channel
    def next_pos(self):
        if (self.curr_channel == (self.channels - 1)):
            self.curr_channel = 0

#            print("next pos awal")
#            print("curr channel ", self.curr_channel)
#            print("curr pos ", self.curr_pos)
#            print("channel ", self.channels)

            if (self.curr_pos == (len(self.map) - 1)):
                self.curr_pos = 0
                print(len(self.map))

                if (self.mask_or == 128):
                    print("maskor next pos = 128")
                    return 'FAILED'
                else:
                    print("maskor next pos != 128")
                    print("maskor sebelum pop ", self.mask_or)
                    print("maskand sebelum pop ", self.mask_and)
                    self.mask_or = self.mask_one.pop(0)
                    self.mask_and = self.mask_zero.pop(0)
                    print("maskor sesudah pop ", self.mask_or)
                    print("maskand sesudah pop ", self.mask_and)
            else:
#                print("gak masuk if ke-2 next pos")
                self.next_lcg()
                if (self.curr_lcg == 95):
                    self.temp += 100
                self.curr_pos = self.temp + self.lcg[self.curr_lcg]
                print("curr pos setelah else = ", self.curr_pos)
        else:
#            print("gak masuk if ke-1 next pos")
            self.curr_channel += 1

    def read_bit(self):

        x, y = self.get_xy(self.map[self.curr_pos])
#        print("map di readbit ", self.map)
#        print("x, y = ", x, y)
        val = self.image[x, y][self.curr_channel]
#        print("val awal ", val)
#        print("bit val awal ", format(val, '08b')) 
        #kalau ganjil jadi 1, kalau genap 0
        val = int(val) & self.mask_or
#        print("val hasil ", val)

        self.next_pos()

        if (val > 0):
            return 1
        else:
            return 0

    def read_bits(self, N):
        bits = 0
        print("N di readbits ", N)

        for i in range(N):
            b = bits
#            print("bits << 1 = ", b << 1)
            bits = (bits << 1) | self.read_bit()
#            print("bits di readbits ", bits)

#        print("bits = ", bits)
        return bits

    def make_lcg(self):
        x = 96
        self.lcg = [0] * (x)
        self.lcg[0] = self.lcg_seed

        for i in range(1, x):
            self.lcg[i] = ((self.lcg[i - 1] * self.lcg_multiplier) + self.lcg_increment) % self.lcg_modulus

    def next_lcg(self):
        if (self.curr_lcg == (len(self.lcg) - 1)):
            self.curr_lcg = 0
        else:
            self.curr_lcg += 1


    #untuk memasukan nilai biner ke warna
    def put_value(self, bits):
#        print("bits di putvalue ", bits)
        for b in bits:
            x, y = self.get_xy(self.map[self.curr_pos])
            val = list(self.image[x, y])
#            print("val di putvalue ", val)
#            print("curr channel di putvalue ", self.curr_channel)
#            print("maskor di putvalue ", self.mask_or)
#            print("maskand di putvalue ", self.mask_and)
#            print("val[", self.curr_channel, "] = ", val[self.curr_channel])

            if (int(b) == 1):
                val[self.curr_channel] = int(val[self.curr_channel]) | self.mask_or
            else:
                val[self.curr_channel] = int(val[self.curr_channel]) & self.mask_and

#            print("val[", self.curr_channel, "] after = ", val[self.curr_channel])
            self.image[x, y] = tuple(val)
#            print("image di putvalue ", self.image)
            self.next_pos()

    def embed(self, path, output = None):
        key = self.key_input_text.text()

        filename = path.split('/')[-1]
        filedata = len(filename)
        print("filename di embed ", filename)
        print("lenght filedata di embed ", filedata)
        content = open(path, 'rb').read()
        print("content di embed ", content)
        data = len(content)
        print("length data(content) di embed ", data)
        self.make_lcg()
#        print("width ", self.width)
#        print("height ", self.height)
#        print("channles ", self.channels)

        print("encrypted ", self.encrypted)

        if (self.encrypted):
            print("masuk encrypt")
            vig = Vigenere(key)
            content = vig.encryptFile(path)
            print("content vigenere ", content)
            self.put_value(format(26, '08b'))
        else:
            print("masuk else encrypt")
            self.put_value(format(13, '08b'))

        print("putvalue format filedata 16bit ")
        self.put_value(format(filedata, '016b'))
        print("putvalue format data 64bit ")
        self.put_value(format(data, '064b'))

        print("putvalue format filename 8bit")
        for byte in filename:
            print("byte di filename embed", byte)
            self.put_value(format(ord(byte), '08b'))

        print("putvalue format content 8bit ")
        for byte in content:
            print("byte di content embed ", format(int(byte), '08b'))
            self.put_value(format(int(byte), '08b'))

        old_filename = ntpath.basename(self.path).split('.')
#        print("oldfilenbame ", old_filename)

        if (output == None):
            output = str(Path(self.path).parent) + '/' + old_filename[0] + '_embedded.' + old_filename[1]
            print('output', output)
            self.writeImage(output)
        else:
            output += '.' + old_filename[1]
            print('output', output)
            self.writeImage(output)

        return output

    def extract(self, output = None):
        key = self.key_input_text.text()
        print("key di extract ", key)

        self.make_lcg()

        encrypted = self.read_bits(8)
        print("ecrypt di extract ", encrypted)

        filedata = self.read_bits(16)
        filename = bytearray()
        print("filedata di extract ", filedata)
        print("filename di extract ", filename)

        data = self.read_bits(64)
        content = bytearray()
        print("data di extract ", data)
        print("content di extraact ", content)

        print("byte filedata")
        for byte in range(filedata):
            filename.extend([self.read_bits(8)])

        print("byte data")
        for byte in range(data):
            content.extend([self.read_bits(8)])

        filename = filename.decode()
        old_filename = filename.split('.')
        print("filename decode ", filename)
        print("oldfilename di extract ", old_filename)

        if (output == None):
            output = str(Path(self.path).parent) + '/' + old_filename[0] + '_extracted.' + old_filename[1]

            with open(output, 'wb') as f:
                f.write(content)

            if (encrypted == 26):
                vig = Vigenere(key)
                v = vig.decryptFile(output, output)
                print("vig decrypt file ", v)
        else:
            output += '.' + old_filename[1]

            with open(output, 'wb') as f:
                f.write(content)

            if (encrypted == 26):
                vig = Vigenere(key)
                v = vig.decryptFile(output, output)
                print("vig decrypt file ", v)

        return output

    @staticmethod
    def psnr(image_one, image_two):
        real = cv2.imread(image_one)
        embedded = cv2.imread(image_two)

        mse = np.mean((real - embedded) ** 2)
        print("nilai mse ", mse)

        if (mse == 0):
            return 100

        max_pixel = 256.0
        psnr = 20 * math.log10(max_pixel / math.sqrt(mse))

        return psnr

    def render(self, window:Ui_MainWindow):
        self.image_lsb_widget = QtWidgets.QWidget(window.option_frame)
        self.image_lsb_widget.setObjectName("image_lsb_widget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.image_lsb_widget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget = QtWidgets.QWidget(self.image_lsb_widget)
        self.widget.setObjectName("widget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.encryption_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.encryption_checkbox.setObjectName("encryption_checkbox")
        self.verticalLayout_2.addWidget(self.encryption_checkbox)
        self.horizontalLayout_5.addWidget(self.groupBox)

        self.verticalLayout_6.addWidget(self.widget)

        self.groupBox_4 = QtWidgets.QGroupBox(self.image_lsb_widget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.key_input_text = QtWidgets.QLineEdit(self.groupBox_4)
        self.key_input_text.setObjectName("key_input_text")
        self.horizontalLayout_2.addWidget(self.key_input_text)
        self.verticalLayout_6.addWidget(self.groupBox_4)
        window.horizontalLayout_4.addWidget(self.image_lsb_widget)

        self.retranslateUi()

        self.key_input_text.setMaxLength(25)
        self.onlyInt = QtGui.QIntValidator(1, 7)
        self.encryption_checkbox.stateChanged.connect(self.enable_encrypted)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox.setTitle(_translate("MainWindow", "Encryption"))
        self.encryption_checkbox.setText(_translate("MainWindow", "Enable"))

        self.groupBox_4.setTitle(_translate("MainWindow", "Key"))

    def enable_encrypted(self, state):
        self.encrypted = bool(state)


