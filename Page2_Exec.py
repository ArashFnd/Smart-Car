from PyQt5 import QtCore, QtGui, QtWidgets
from Page1 import Page1_MainWindow_GUI
from Page2 import Page2_MainWindow_GUI
import websocket
import sys
import os


class Page2_EXEC(QtWidgets.QMainWindow,Page2_MainWindow_GUI):

	test = QtCore.pyqtSignal(bool)

	def __init__(self, parent=None):
		QtWidgets.QMainWindow.__init__(self, parent)

		self.setupUi(self)
		self.pushButton.clicked.connect(self.test_end)
		self.pushButton_2.clicked.connect(self.close_app)

		self.text_Fullname_2 = self.label.text()
		self.text_Age_2 = self.label_2.text()
		self.text_Phonenumber = self.label_3.text()

		self.time = QtCore.QTime(00,00,00)
		text = self.time.toString('hh:mm:ss')
		self.label_6.setText("Time:  " + text)
		
		self.timer = QtCore.QTimer(self)
		self.timer.timeout.connect(self.showTime)
		self.timer.start(1000)

		self.car_data_timer = QtCore.QTimer()
		self.car_data_timer.timeout.connect(self.car_data_timer_tick)
		self.car_data_timer.start(100)

		self.show()

	def showTime(self):
		#time = QtCore.QTime.currentTime()
		self.time = self.time.addSecs(1)
		text = self.time.toString('hh:mm:ss')
		self.label_6.setText("Time:  " + text)

	def car_data_timer_tick(self):

		try:
			self.ws.send("nothing")
			result = self.ws.recv()
			print(result)
			self.file.write(str(result+'\n'))
		except Exception as e:
			print('error in tick', e)

	def get_info(self, Name, Age, Phone, Gender):
		self.text_Fullname_2 = Name
		self.text_Age_2 = Age
		self.text_Phonenumber_2 = Phone
		self.text_Gender_2 = Gender
		print(self.text_Fullname_2, self.text_Age_2, self.text_Phonenumber, self.text_Gender_2)

	def close_app(self):
		choice = QtWidgets.QMessageBox.question(self, 'Confirm', "Are you sure you want to quit?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
		if choice == QtWidgets.QMessageBox.Yes:
			sys.exit()

	def test_start(self, file_name):
		
		while True:
			try:
				self.ws = websocket.WebSocket()
				# ws.connect("ws://192.168.43.1/ws") # Arash cellphone
				self.ws.connect("ws://192.168.43.190/ws") # Shahab cellphone
				# ws.connect("ws://192.168.4.1/ws") # nodmcu hotspot
				print('connected to car')
				break
			except Exception as e:
				print('cant connect to car',e)
				print('retrying!')
		
		self.test.emit(True)
		self.file = open(file_name, 'w+')
		self.file.write(self.text_Fullname_2 + " " + self.text_Age_2 + " " + self.text_Phonenumber_2 + " " + self.text_Gender_2 + "\n")

	def test_end(self):
		self.test.emit(False)
		self.file.close()
		self.car_data_timer.stop()
		self.close()
		#QtWidgets.QApplication.quit()

		return self.test

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Page2_EXEC()