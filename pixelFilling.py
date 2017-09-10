# 
# 
# Author: Robin Gautam
# Email: robin.gautam341@gmail.com
# Title: GUI for pixel filling / Swapping
# 

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Window(QMainWindow):
	"""docstring for Window"""
	def __init__(self):
		app = QApplication(sys.argv)
		super(Window, self).__init__()
		frame = QWidget()
		layout = QFormLayout()
		hbox = QVBoxLayout()

		frame.setWindowTitle('Pixel Filling and Swapping process')
		frame.setGeometry(200, 200, 300, 500)

		# Labels
		heading = QLabel('Apply Pixel Filling')
		heading.setStyleSheet("font-size: 30px; qproperty-alignment: AlignJustify; font-family: Calibri;")
		zfLabel = QLabel('Zoom factor')
		widthLabel = QLabel('Image Width')
		heightLabel = QLabel('Image Height')
		self.selectedFileLabel = QLabel(' ')

		self.outputMessages = QTextEdit()
		self.outputMessages.setReadOnly(True)
		font = self.outputMessages.font()
		font.setFamily('Courier')
		font.setPointSize(10)

		# Inputs
		self.zfInput = QLineEdit()
		self.widthInput = QLineEdit()
		self.heightInput = QLineEdit()

		# Buttons
		startBtn = QPushButton('Process image', self)
		selectFileBtn = QPushButton('Choose', self)
		self.swappingChoice = QRadioButton('Pixel Swapping')
		self.fillingChoice = QRadioButton('Pixel Filling')

		startBtn.clicked.connect(self.process)
		selectFileBtn.clicked.connect(self.getFile)

		hbox.addWidget(self.swappingChoice)
		hbox.addWidget(self.fillingChoice)
		hbox.addStretch()
		layout.addRow(heading)
		layout.addRow(zfLabel, self.zfInput)
		layout.addRow(widthLabel, self.widthInput)
		layout.addRow(heightLabel, self.heightInput)
		layout.addRow(selectFileBtn, self.selectedFileLabel)
		layout.addRow(hbox)
		layout.addRow(startBtn)
		layout.addRow(self.outputMessages)

		frame.setLayout(layout)
		frame.show()
		sys.exit(app.exec_())
		
	def process(self):
		# Debug. TODO: Remove later
		print('Processing')
		print('zf: ' + self.zfInput.text())
		print('width: ' + self.widthInput.text())
		print('height: ' + self.heightInput.text())
		print('path: ' + self.selectedFileLabel.text())
		if self.swappingChoice.isChecked():
			print('Run algo for Pixel Swapping')
		else:
			print('Run algo for Pixel Filling')
		# Enter the algorithm in a different thread
		zf = self.zfInput.text()
		width = self.widthInput.text()
		height = self.heightInput.text()
		path = self.selectedFileLabel.text()

		messageLog = 'Log: \n'
		# messageLog = pixelFilling(path, zf, width, height)
		# Return File names with paths
		messageLog = messageLog + 'Processed'

		# Share the result 
		# Display a message
		self.outputMessages.setText(messageLog)
		messageBox = QMessageBox()
		messageBox.setText('Done')
		messageBox.setWindowTitle('Process status')
		messageBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
		# messageBox.buttonClicked.connect(msgbtn)
		notificationFeedback = messageBox.exec_()

	def getFile(self):
		fileName = QFileDialog.getOpenFileName(self, 'Open File')
		self.selectedFileLabel.setText(fileName)
		print(fileName)

def run():
	startUp = Window()

run()