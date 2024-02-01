"""
this code was adapted from 
vincentbudianto github
at https://github.com/vincentbudianto/Stego-Helper
"""

import mimetypes

from bcknd import *
import os, sys, subprocess

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

class Ui_MainWindow(object):
    def __init__(self):
        self.stego_list = [
            ("Image LSB", LSB()),
         ]
        self.stego = self.stego_list[0]
        self.file_name = ''
        self.file_type = ''
        self.file_extension = ''
        self.result_file_path = ''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayout_0 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_0.setObjectName("horizontalLayout_0")
        self.divide = QtWidgets.QWidget(self.centralwidget)
        self.divide.setObjectName("divide")
        self.horizontalLayout_0.addWidget(self.divide, 5)

        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.divide)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.header_frame = QtWidgets.QFrame(self.divide)
        self.header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_frame.setObjectName("header_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.header_frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.open_media_button = QtWidgets.QPushButton(self.header_frame)
        self.open_media_button.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.open_media_button.setFont(font)
        self.open_media_button.setObjectName("open_media_button")
        self.horizontalLayout_3.addWidget(self.open_media_button)
        self.verticalLayout_5.addWidget(self.header_frame)

        ### MULAI IMAGE LSB
        self.option_frame = QtWidgets.QFrame(self.centralwidget)
        self.option_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.option_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.option_frame.setObjectName("option_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.option_frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        # INSERT OPTIONS #

        self.verticalLayout_5.addWidget(self.option_frame)
        self.footer_frame = QtWidgets.QFrame(self.centralwidget)
        self.footer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer_frame.setObjectName("footer_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.footer_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(self.footer_frame)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.embeed_button = QtWidgets.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.embeed_button.setFont(font)
        self.embeed_button.setObjectName("embeed_button")
        self.horizontalLayout_6.addWidget(self.embeed_button)
        self.extract_button = QtWidgets.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.extract_button.setFont(font)
        self.extract_button.setObjectName("extract_button")
        self.horizontalLayout_6.addWidget(self.extract_button)
        self.verticalLayout.addWidget(self.widget_2)
        self.groupBox_5 = QtWidgets.QGroupBox(self.footer_frame)

        self.info_text = QtWidgets.QPlainTextEdit(self.footer_frame)
        self.info_text.setObjectName("info_text")
        self.verticalLayout.addWidget(self.info_text)
        self.verticalLayout_5.addWidget(self.footer_frame)
        
        ### TAMPIL IMAGE
        self.divide_2 = QtWidgets.QWidget(self.centralwidget)
        self.divide_2.setObjectName("divide_2")
        self.horizontalLayout_0.addWidget(self.divide_2, 5)

        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.divide)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.header_frame_2 = QtWidgets.QFrame(self.divide_2)
        self.header_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_frame_2.setObjectName("header_frame_2")
        self.label = QtWidgets.QLabel(self.header_frame_2)
        self.label.setGeometry(QtCore.QRect(35, 0, 100, 21))
        self.label.setObjectName("label")
        self.graphicsView = QtWidgets.QGraphicsView(self.header_frame_2)
        self.graphicsView.setGeometry(QtCore.QRect(25, 22, 575, 280))
        self.graphicsView.setSizeIncrement(QtCore.QSize(0, 0))
        self.graphicsView.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graphicsView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.graphicsView.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_7.addWidget(self.header_frame_2)

        self.footer_frame_2 = QtWidgets.QFrame(self.divide_2)
        self.footer_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer_frame_2.setObjectName("footer_frame_2")
        self.label_2 = QtWidgets.QLabel(self.footer_frame_2)
        self.label_2.setGeometry(QtCore.QRect(35, 303, 100, 21))
        self.label_2.setObjectName("label_2")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.footer_frame_2)
        self.graphicsView_2.setGeometry(QtCore.QRect(25, 325, 575, 280))
        self.graphicsView_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.graphicsView_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graphicsView_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.graphicsView_2.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.verticalLayout_7.addWidget(self.footer_frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.open_media_button.clicked.connect(self.openMediaFile)
        self.open_media_button.clicked.connect(self.checkPath)

        self.embeed_button.clicked.connect(self.embedding)
        self.extract_button.clicked.connect(self.extract)

        self.stego[1].render(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Steganografi"))

        self.open_media_button.setText(_translate("MainWindow", "Open Media File"))
        self.embeed_button.setText(_translate("MainWindow", "Embeed"))
        self.extract_button.setText(_translate("MainWindow", "Extract"))
        self.label.setText(_translate("MainWindow", "Original Image"))
        self.label_2.setText(_translate("MainWindow", "Stegoimage"))

    def openMediaFile(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "Select Media File",
            "",
            "All Files (*)",
        )
        if fileName:
            print(fileName)
            self.file_name = fileName
            self.appendInfoText("Media file : " + self.file_name)
            mime = mimetypes.guess_type(fileName)
            if mime[0]:
                print(mime)
                self.file_type = mime[0].split('/')[0]
                self.file_extension = mime[0].split('/')[1]

    def checkPath(self):
        image_path = self.file_name
        if os.path.isfile(image_path):
            scene = QtWidgets.QGraphicsScene()
            pixmap = QPixmap(image_path)
            item = QtWidgets.QGraphicsPixmapItem(pixmap)
            item.setScale(0.25)
            scene.addItem(item)
            self.graphicsView.setScene(scene)

    def embedding(self):
          if self.stego[0] == 'Image LSB':
            if self.file_type != 'image' or self.file_extension not in ['bmp', 'png']:
                self.info_text.setPlainText("Container file extension has to be .bmp or .png")
                return -1

            inputFileName, _ = QtWidgets.QFileDialog.getOpenFileName(
                None,
                "Select Input File",
                "",
                "All Files (*)",
            )
            if inputFileName:
                self.stego[1].readImage(self.file_name)
                self.appendInfoText("Container file read")

                fileName, _ = QtWidgets.QFileDialog.getSaveFileName(
                    None,
                    "Select File to Save Output Text",
                    "",
                    "All Files (*)",
                )
                result = 'FAILED'

                self.appendInfoText("Embedding")

                if fileName:
                    result = self.stego[1].embed(path = inputFileName, output = fileName)
                else:
                    result = self.stego[1].embed(path = inputFileName)

                if result == 'FAILED':
                    self.appendInfoText("Container file size is too small")
                else:
                    self.result_file_path = result
                    self.appendInfoText("Counting PSNR")
                    self.appendInfoText("PSNR = " + str(self.stego[1].psnr(self.file_name, self.result_file_path)))
                    image_path_result = self.result_file_path
                    if os.path.isfile(image_path_result):
                        scene_2 = QtWidgets.QGraphicsScene()
                        pixmap_2 = QPixmap(image_path_result)
                        item_2= QtWidgets.QGraphicsPixmapItem(pixmap_2)
                        item_2.setScale(0.25)
                        scene_2.addItem(item_2)
                        self.graphicsView_2.setScene(scene_2)

            else:
                self.appendInfoText("Error when reading input file")
                return -1

    def extract(self):
          if self.stego[0] == 'Image LSB':
            if self.file_type != 'image' or self.file_extension not in ['bmp', 'png']:
                self.info_text.setPlainText("Container file extension has to be .bmp or .png")
                return -1

            self.info_text.setPlainText("Start Extraction Process")
            self.stego[1].readImage(self.file_name)
            self.appendInfoText("Container file read")

            fileName, _ = QtWidgets.QFileDialog.getSaveFileName(
                None,
                "Select File to Save Output File",
                "",
                "All Files (*)",
            )

            result = 'FAILED'
            self.appendInfoText("Extracting")
            if fileName:
                result = self.stego[1].extract(output = fileName)
            else:
                result = self.stego[1].extract()

            self.result_file_path = result
            self.appendInfoText("Finished extracting in " + result)

    def appendInfoText(self, text):
        self.info_text.appendPlainText(text)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

