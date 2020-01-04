from PyQt5 import QtCore, QtGui, QtWidgets
from Page1 import Page1_MainWindow_GUI
from Page2 import Page2_MainWindow_GUI
from Page2_Exec import Page2_EXEC
import sys

class Page1_EXEC(QtWidgets.QMainWindow,Page1_MainWindow_GUI):

	def __init__(self, parent=None):
		QtWidgets.QMainWindow.__init__(self, parent)

		self.text_Gender = ''
		self.text_Fullname = ''
		self.text_Age = ''
		self.text_Phonenumber = ''

		self.setupUi(self)
		self.pushButton.clicked.connect(self.open_Page2)
		self.pushButton_2.clicked.connect(self.close_app)
		self.checkBox.toggled.connect(self.task_checkBox)
		self.checkBox_2.toggled.connect(self.task_checkBox_2)
		self.show()
		sys.exit(app.exec_())

	def task_checkBox(self):
		if self.checkBox.isChecked():
			self.checkBox_2.setChecked(False)
			self.text_Gender = 'Male'

	def task_checkBox_2(self):
		if self.checkBox_2.isChecked():
			self.checkBox.setChecked(False)
			self.text_Gender = 'Female'

	def close_app(self):
		choice = QtWidgets.QMessageBox.question(self, 'Confirm', "Are you sure you want to quit?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
		if choice == QtWidgets.QMessageBox.Yes:
			sys.exit()

	def open_Page2(self):

		self.text_Fullname = self.lineEdit.text()
		self.text_Age = self.lineEdit_2.text()
		self.text_Phonenumber = self.lineEdit_3.text()

		if self.text_Gender == '' or self.text_Fullname == '' or self.text_Age == '' or self.text_Phonenumber == '':
			choice = QtWidgets.QMessageBox.question(self, 'Error', "Please fill all the fields!", QtWidgets.QMessageBox.Ok)
		else:
			self.window_Page2 = QtWidgets.QMainWindow()
			self.ui_Page2 = Page2_EXEC(self.window_Page2)
			self.ui_Page2.get_info(self.text_Fullname, self.text_Age, self.text_Phonenumber, self.text_Gender)
			self.ui_Page2.label.setText("Name:  " + self.text_Fullname)
			self.ui_Page2.label_2.setText("Age:     " + self.text_Age)
			self.ui_Page2.label_3.setText("Phone:  " + self.text_Phonenumber)
			self.ui_Page2.label_4.setText("Gender: " + self.text_Gender)
			self.ui_Page2.test_start()
			test = self.ui_Page2.pushButton_2.clicked.connect(self.ui_Page2.close_app)
			if test is False:
				self.text_Fullname = ''
				self.text_Age = ''
				self.lineEdit.clear()


			# print(self.text_Fullname, self.text_Age, self.text_Phonenumber, self.text_Gender)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Page1_EXEC()