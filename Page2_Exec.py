from PyQt5 import QtCore, QtGui, QtWidgets
from Page1 import Page1_MainWindow_GUI
from Page2 import Page2_MainWindow_GUI
import sys


class Page2_EXEC(QtWidgets.QMainWindow,Page2_MainWindow_GUI):

	def __init__(self, parent=None):
		QtWidgets.QMainWindow.__init__(self, parent)

		self.setupUi(self)
		self.pushButton.clicked.connect(self.test_end)
		#self.pushButton_2.clicked.connect(self.close_app)

		self.text_Fullname_2 = self.label.text()
		self.text_Age_2 = self.label_2.text()
		self.text_Phonenumber = self.label_3.text()

		self.time = QtCore.QTime(00,00,00)
		text = self.time.toString('hh:mm:ss')
		self.label_6.setText("Time:  " + text)
		
		self.timer = QtCore.QTimer(self)
		self.timer.timeout.connect(self.showTime)
		self.timer.start(1000)

		self.show()
		# sys.exit(app.exec_())

	def showTime(self):
		#time = QtCore.QTime.currentTime()
		self.time = self.time.addSecs(1)
		text = self.time.toString('hh:mm:ss')
		self.label_6.setText("Time:  " + text)

	def get_info(self, Name, Age, Phone, Gender):
		self.text_Fullname_2 = Name
		self.text_Age_2 = Age
		self.text_Phonenumber_2 = Phone
		self.text_Gender_2 = Gender
		print(self.text_Fullname_2, self.text_Age_2, self.text_Phonenumber, self.text_Gender_2)

	def close_app(self):
		choice = QtWidgets.QMessageBox.question(self, 'Error', "Please fill all the fields!", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
		if choice == QtWidgets.QMessageBox.Yes:
			sys.exit()

	def test_start(self):
		self.test = True
		file = open('data.txt', 'w+')
		file.write(self.text_Fullname_2 + " " + self.text_Age_2 + " " + self.text_Phonenumber + " " + self.text_Gender_2)

	def test_end(self):
		self.test = False
		self.close()
		#QtWidgets.QApplication.quit()
		print(self.test)

		return self.test

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Page2_EXEC()