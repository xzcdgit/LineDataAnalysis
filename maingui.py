# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maingui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(754, 644)
        MainWindow.setTabletTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("1.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_16.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout.addWidget(self.lineEdit_16, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout.addWidget(self.pushButton_22, 3, 0, 1, 2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_4)
        font = QtGui.QFont()
        font.setKerning(True)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 2)
        self.gridLayout_9.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_23 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout_2.addWidget(self.pushButton_23, 3, 0, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_39.setFont(font)
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)
        self.label_39.setObjectName("label_39")
        self.gridLayout_2.addWidget(self.label_39, 2, 3, 1, 1)
        self.pushButton_24 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_24.setObjectName("pushButton_24")
        self.gridLayout_2.addWidget(self.pushButton_24, 3, 1, 1, 1)
        self.pushButton_26 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_26.setObjectName("pushButton_26")
        self.gridLayout_2.addWidget(self.pushButton_26, 3, 3, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_37.setFont(font)
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.gridLayout_2.addWidget(self.label_37, 2, 1, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_33.setFont(font)
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.gridLayout_2.addWidget(self.label_33, 0, 1, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_34.setFont(font)
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.gridLayout_2.addWidget(self.label_34, 0, 2, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_29.setFont(font)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.gridLayout_2.addWidget(self.label_29, 0, 0, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_38.setFont(font)
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.gridLayout_2.addWidget(self.label_38, 2, 2, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_35.setFont(font)
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.gridLayout_2.addWidget(self.label_35, 0, 3, 1, 1)
        self.pushButton_25 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_25.setObjectName("pushButton_25")
        self.gridLayout_2.addWidget(self.pushButton_25, 3, 2, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_36.setFont(font)
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.gridLayout_2.addWidget(self.label_36, 2, 0, 1, 1)
        self.checkBox_10 = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkBox_10.setObjectName("checkBox_10")
        self.gridLayout_2.addWidget(self.checkBox_10, 1, 0, 1, 1)
        self.checkBox_11 = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkBox_11.setObjectName("checkBox_11")
        self.gridLayout_2.addWidget(self.checkBox_11, 1, 1, 1, 1)
        self.checkBox_12 = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkBox_12.setObjectName("checkBox_12")
        self.gridLayout_2.addWidget(self.checkBox_12, 1, 2, 1, 1)
        self.checkBox_13 = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkBox_13.setObjectName("checkBox_13")
        self.gridLayout_2.addWidget(self.checkBox_13, 1, 3, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_5, 0, 1, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_27 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_27.setObjectName("pushButton_27")
        self.horizontalLayout.addWidget(self.pushButton_27)
        self.pushButton_29 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_29.setObjectName("pushButton_29")
        self.horizontalLayout.addWidget(self.pushButton_29)
        self.pushButton_30 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_30.setObjectName("pushButton_30")
        self.horizontalLayout.addWidget(self.pushButton_30)
        self.pushButton_28 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_28.setObjectName("pushButton_28")
        self.horizontalLayout.addWidget(self.pushButton_28)
        self.gridLayout_9.addWidget(self.groupBox_7, 1, 0, 1, 2)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_40 = QtWidgets.QLabel(self.groupBox_6)
        self.label_40.setObjectName("label_40")
        self.gridLayout_3.addWidget(self.label_40, 0, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.groupBox_6)
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 1, 0, 1, 1)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout_3.addWidget(self.lineEdit_15, 1, 1, 1, 1)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.gridLayout_3.addWidget(self.lineEdit_17, 0, 1, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_6, 2, 0, 1, 2)
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_8)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_4.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_8, 3, 0, 1, 2)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_11.addWidget(self.pushButton, 3, 0, 1, 2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_17 = QtWidgets.QLabel(self.groupBox_3)
        self.label_17.setObjectName("label_17")
        self.gridLayout_8.addWidget(self.label_17, 0, 0, 1, 1)
        self.groupBox_14 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_14.setObjectName("groupBox_14")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_14)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_14)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout_7.addWidget(self.checkBox_5, 3, 0, 1, 1)
        self.checkBox_9 = QtWidgets.QCheckBox(self.groupBox_14)
        self.checkBox_9.setEnabled(True)
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout_7.addWidget(self.checkBox_9, 2, 2, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_14)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_7.addWidget(self.checkBox_3, 1, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_14)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_7.addWidget(self.pushButton_4, 4, 0, 1, 3)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_14)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_7.addWidget(self.checkBox_2, 0, 2, 1, 1)
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox_14)
        self.checkBox_7.setEnabled(True)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout_7.addWidget(self.checkBox_7, 3, 2, 1, 1)
        self.checkBox_8 = QtWidgets.QCheckBox(self.groupBox_14)
        self.checkBox_8.setEnabled(True)
        self.checkBox_8.setCheckable(True)
        self.checkBox_8.setChecked(False)
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout_7.addWidget(self.checkBox_8, 2, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_14)
        self.checkBox.setChecked(False)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_7.addWidget(self.checkBox, 0, 0, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_14)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_7.addWidget(self.checkBox_4, 1, 2, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_14, 0, 1, 3, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout_8.addWidget(self.textEdit_2, 1, 0, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout_8.addWidget(self.pushButton_20, 2, 0, 1, 1)
        self.gridLayout_11.addWidget(self.groupBox_3, 4, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setObjectName("label_18")
        self.gridLayout_13.addWidget(self.label_18, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_13.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setObjectName("label_19")
        self.gridLayout_13.addWidget(self.label_19, 1, 0, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setMinimum(-999999.0)
        self.doubleSpinBox.setMaximum(999999.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout_13.addWidget(self.doubleSpinBox, 1, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setObjectName("label_21")
        self.gridLayout_13.addWidget(self.label_21, 1, 2, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setObjectName("label_20")
        self.gridLayout_13.addWidget(self.label_20, 2, 0, 1, 1)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_2.setMinimum(-999999.0)
        self.doubleSpinBox_2.setProperty("value", 0.0)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.gridLayout_13.addWidget(self.doubleSpinBox_2, 2, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.groupBox)
        self.label_22.setObjectName("label_22")
        self.gridLayout_13.addWidget(self.label_22, 2, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_13.addWidget(self.pushButton_3, 3, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_13.addWidget(self.pushButton_2, 3, 1, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_13.addWidget(self.pushButton_15, 4, 0, 1, 2)
        self.gridLayout_11.addWidget(self.groupBox, 4, 0, 1, 2)
        self.pushButton_19 = QtWidgets.QPushButton(self.tab)
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout_11.addWidget(self.pushButton_19, 3, 2, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_11 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_11.setObjectName("groupBox_11")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_11)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_3.addWidget(self.pushButton_8)
        self.horizontalLayout_2.addWidget(self.groupBox_11)
        self.groupBox_12 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_12.setObjectName("groupBox_12")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_12)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_12)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_5.addWidget(self.textEdit, 1, 0, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.groupBox_12)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_5.addWidget(self.pushButton_16, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox_12)
        self.groupBox_13 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_13.setEnabled(True)
        self.groupBox_13.setObjectName("groupBox_13")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_13)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_13)
        self.pushButton_14.setEnabled(False)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_6.addWidget(self.pushButton_14, 3, 1, 1, 1)
        self.pushButton_31 = QtWidgets.QPushButton(self.groupBox_13)
        self.pushButton_31.setObjectName("pushButton_31")
        self.gridLayout_6.addWidget(self.pushButton_31, 7, 0, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_13)
        self.pushButton_11.setEnabled(False)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_6.addWidget(self.pushButton_11, 2, 0, 1, 1)
        self.pushButton_21 = QtWidgets.QPushButton(self.groupBox_13)
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout_6.addWidget(self.pushButton_21, 4, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_13)
        self.pushButton_9.setEnabled(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_6.addWidget(self.pushButton_9, 1, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.groupBox_13)
        self.label_24.setObjectName("label_24")
        self.gridLayout_6.addWidget(self.label_24, 5, 0, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox_13)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout_6.addWidget(self.checkBox_6, 0, 0, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_13)
        self.pushButton_10.setEnabled(False)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_6.addWidget(self.pushButton_10, 1, 1, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_13)
        self.pushButton_12.setEnabled(False)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_6.addWidget(self.pushButton_12, 2, 1, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_13)
        self.pushButton_13.setEnabled(False)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_6.addWidget(self.pushButton_13, 3, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.groupBox_13)
        self.label_25.setObjectName("label_25")
        self.gridLayout_6.addWidget(self.label_25, 6, 0, 1, 1)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.groupBox_13)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.gridLayout_6.addWidget(self.doubleSpinBox_3, 6, 1, 1, 1)
        self.gridLayout_6.setColumnStretch(0, 1)
        self.gridLayout_6.setColumnStretch(1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox_13)
        self.gridLayout_11.addWidget(self.groupBox_2, 5, 0, 1, 3)
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.label_27 = QtWidgets.QLabel(self.groupBox_9)
        self.label_27.setObjectName("label_27")
        self.gridLayout_14.addWidget(self.label_27, 0, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_9)
        self.label_3.setObjectName("label_3")
        self.gridLayout_14.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_9)
        self.label_2.setObjectName("label_2")
        self.gridLayout_14.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.groupBox_9)
        self.label_26.setObjectName("label_26")
        self.gridLayout_14.addWidget(self.label_26, 0, 2, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_9)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout_14.addWidget(self.comboBox_3, 0, 1, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.groupBox_9)
        self.label_28.setObjectName("label_28")
        self.gridLayout_14.addWidget(self.label_28, 2, 0, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.groupBox_9)
        self.label_41.setText("")
        self.label_41.setObjectName("label_41")
        self.gridLayout_14.addWidget(self.label_41, 2, 1, 1, 3)
        self.label_42 = QtWidgets.QLabel(self.groupBox_9)
        self.label_42.setText("")
        self.label_42.setObjectName("label_42")
        self.gridLayout_14.addWidget(self.label_42, 1, 1, 1, 3)
        self.gridLayout_11.addWidget(self.groupBox_9, 0, 0, 1, 3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_30 = QtWidgets.QLabel(self.tab_2)
        self.label_30.setObjectName("label_30")
        self.gridLayout_12.addWidget(self.label_30, 0, 0, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout_12.addWidget(self.pushButton_18, 0, 7, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_12.addWidget(self.label_5, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_12.addWidget(self.lineEdit_3, 1, 2, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_12.addWidget(self.label_6, 1, 4, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_12.addWidget(self.lineEdit_4, 1, 5, 1, 3)
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_12.addWidget(self.label_9, 2, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_12.addWidget(self.lineEdit_7, 2, 2, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_12.addWidget(self.label_7, 2, 4, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_12.addWidget(self.lineEdit_5, 2, 5, 1, 3)
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_12.addWidget(self.label_10, 3, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_12.addWidget(self.lineEdit_8, 3, 2, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_12.addWidget(self.label_8, 3, 4, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_12.addWidget(self.lineEdit_6, 3, 5, 1, 3)
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_12.addWidget(self.label_11, 4, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_12.addWidget(self.lineEdit_9, 4, 2, 1, 2)
        self.label_32 = QtWidgets.QLabel(self.tab_2)
        self.label_32.setObjectName("label_32")
        self.gridLayout_12.addWidget(self.label_32, 4, 4, 1, 1)
        self.lineEdit_19 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_19.setText("")
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.gridLayout_12.addWidget(self.lineEdit_19, 4, 5, 1, 3)
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_12.addWidget(self.label_12, 5, 0, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_12.addWidget(self.lineEdit_10, 5, 2, 1, 2)
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout_12.addWidget(self.label_13, 6, 0, 1, 2)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_12.addWidget(self.lineEdit_11, 6, 2, 1, 2)
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout_12.addWidget(self.label_14, 7, 0, 1, 2)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_12.addWidget(self.lineEdit_12, 7, 2, 1, 2)
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout_12.addWidget(self.label_15, 8, 0, 1, 2)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout_12.addWidget(self.lineEdit_13, 8, 2, 1, 2)
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_12.addWidget(self.label_16, 9, 0, 1, 2)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout_12.addWidget(self.lineEdit_14, 9, 2, 1, 2)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_12.addWidget(self.pushButton_5, 10, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_12.addWidget(self.pushButton_6, 10, 3, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.tab_2)
        self.label_31.setObjectName("label_31")
        self.gridLayout_12.addWidget(self.label_31, 0, 1, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_12.addWidget(self.pushButton_17, 0, 6, 1, 1)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_18.setText("")
        self.lineEdit_18.setFrame(True)
        self.lineEdit_18.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.gridLayout_12.addWidget(self.lineEdit_18, 0, 2, 1, 4)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_10.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 754, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu_2.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "凸轮形线分析"))
        self.tabWidget.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>形线分析器</p><p><br/></p></body></html>"))
        self.groupBox_4.setTitle(_translate("MainWindow", "串口连接"))
        self.lineEdit_16.setText(_translate("MainWindow", "115200"))
        self.label.setText(_translate("MainWindow", "串口号"))
        self.pushButton_22.setText(_translate("MainWindow", "连接"))
        self.lineEdit_2.setText(_translate("MainWindow", "COM3"))
        self.label_4.setText(_translate("MainWindow", "波特率"))
        self.pushButton_7.setText(_translate("MainWindow", "可用串口检测"))
        self.groupBox_5.setTitle(_translate("MainWindow", "数据显示"))
        self.pushButton_23.setText(_translate("MainWindow", "清零"))
        self.label_39.setText(_translate("MainWindow", "----"))
        self.pushButton_24.setText(_translate("MainWindow", "清零"))
        self.pushButton_26.setText(_translate("MainWindow", "清零"))
        self.label_37.setText(_translate("MainWindow", "----"))
        self.label_33.setText(_translate("MainWindow", "通道2"))
        self.label_34.setText(_translate("MainWindow", "通道3"))
        self.label_29.setText(_translate("MainWindow", "通道1"))
        self.label_38.setText(_translate("MainWindow", "----"))
        self.label_35.setText(_translate("MainWindow", "通道4"))
        self.pushButton_25.setText(_translate("MainWindow", "清零"))
        self.label_36.setText(_translate("MainWindow", "----"))
        self.checkBox_10.setText(_translate("MainWindow", "取反"))
        self.checkBox_11.setText(_translate("MainWindow", "取反"))
        self.checkBox_12.setText(_translate("MainWindow", "取反"))
        self.checkBox_13.setText(_translate("MainWindow", "取反"))
        self.groupBox_7.setTitle(_translate("MainWindow", "操作选项"))
        self.pushButton_27.setText(_translate("MainWindow", "开始记录"))
        self.pushButton_29.setText(_translate("MainWindow", "一键清零"))
        self.pushButton_30.setText(_translate("MainWindow", "打开保存文件夹"))
        self.pushButton_28.setText(_translate("MainWindow", "保存记录"))
        self.groupBox_6.setTitle(_translate("MainWindow", "文件保存设置"))
        self.label_40.setText(_translate("MainWindow", "预设保存总路径"))
        self.label_23.setText(_translate("MainWindow", "文件完整路径名"))
        self.lineEdit_17.setText(_translate("MainWindow", "D:\\CamshaftMeasure\\MeasureTest"))
        self.groupBox_8.setTitle(_translate("MainWindow", "提示"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "数据读取"))
        self.pushButton.setText(_translate("MainWindow", "从资源管理器打开文件"))
        self.groupBox_3.setTitle(_translate("MainWindow", "手动图形比对分析"))
        self.label_17.setText(_translate("MainWindow", "测量数据2（该数据仅用于作对比图形）"))
        self.groupBox_14.setTitle(_translate("MainWindow", "绘图选项"))
        self.checkBox_5.setText(_translate("MainWindow", "差值线1"))
        self.checkBox_9.setText(_translate("MainWindow", "测量进气形线2"))
        self.checkBox_3.setText(_translate("MainWindow", "测量进气形线1"))
        self.pushButton_4.setText(_translate("MainWindow", "绘图"))
        self.checkBox_2.setText(_translate("MainWindow", "设计排气形线"))
        self.checkBox_7.setText(_translate("MainWindow", "差值线2"))
        self.checkBox_8.setText(_translate("MainWindow", "测量进气形线2"))
        self.checkBox.setText(_translate("MainWindow", "设计进气形线"))
        self.checkBox_4.setText(_translate("MainWindow", "测量排气形线1"))
        self.pushButton_20.setText(_translate("MainWindow", "选择文件"))
        self.groupBox.setTitle(_translate("MainWindow", "手动数据分析"))
        self.label_18.setText(_translate("MainWindow", "数据编辑"))
        self.comboBox.setItemText(0, _translate("MainWindow", "进气线"))
        self.comboBox.setItemText(1, _translate("MainWindow", "排气线"))
        self.label_19.setText(_translate("MainWindow", "X向移动"))
        self.label_21.setText(_translate("MainWindow", "°"))
        self.label_20.setText(_translate("MainWindow", "Y向移动"))
        self.label_22.setText(_translate("MainWindow", "mm"))
        self.pushButton_3.setText(_translate("MainWindow", "撤销"))
        self.pushButton_2.setText(_translate("MainWindow", "修改"))
        self.pushButton_15.setText(_translate("MainWindow", "保存修改结果"))
        self.pushButton_19.setText(_translate("MainWindow", "读取最近保存的数据文件"))
        self.groupBox_2.setTitle(_translate("MainWindow", "自动分析"))
        self.groupBox_11.setTitle(_translate("MainWindow", "数据分析"))
        self.pushButton_8.setText(_translate("MainWindow", "一键分析"))
        self.groupBox_12.setTitle(_translate("MainWindow", "计算结果"))
        self.pushButton_16.setText(_translate("MainWindow", "导出结果"))
        self.groupBox_13.setTitle(_translate("MainWindow", "自动绘图"))
        self.pushButton_14.setText(_translate("MainWindow", "排气减压高度图像"))
        self.pushButton_31.setText(_translate("MainWindow", "极坐标绘图"))
        self.pushButton_11.setText(_translate("MainWindow", "进气升程跳动图像"))
        self.pushButton_21.setText(_translate("MainWindow", "正时点位置图像"))
        self.pushButton_9.setText(_translate("MainWindow", "进气基圆跳动图像"))
        self.label_24.setText(_translate("MainWindow", "极坐标作图"))
        self.checkBox_6.setText(_translate("MainWindow", "设计形线参照"))
        self.pushButton_10.setText(_translate("MainWindow", "排气基圆跳动图像"))
        self.pushButton_12.setText(_translate("MainWindow", "排气升程跳动图像"))
        self.pushButton_13.setText(_translate("MainWindow", "进气减压高度图像"))
        self.label_25.setText(_translate("MainWindow", "基本高度（mm）"))
        self.groupBox_9.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_27.setText(_translate("MainWindow", " "))
        self.label_3.setText(_translate("MainWindow", "数据1 最近保存的文件"))
        self.label_2.setText(_translate("MainWindow", "凸轮型号"))
        self.label_26.setText(_translate("MainWindow", " "))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "RV145"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "RV80S"))
        self.label_28.setText(_translate("MainWindow", "数据1 当前读取的文件"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "形线数据分析"))
        self.label_30.setText(_translate("MainWindow", "用户登录"))
        self.pushButton_18.setText(_translate("MainWindow", "注销"))
        self.label_5.setText(_translate("MainWindow", "编码器周期"))
        self.label_6.setText(_translate("MainWindow", "角度数据列名"))
        self.label_9.setText(_translate("MainWindow", "起始数据舍弃"))
        self.label_7.setText(_translate("MainWindow", "进气数据列名"))
        self.label_10.setText(_translate("MainWindow", "基圆范围"))
        self.label_8.setText(_translate("MainWindow", "排气数据列名"))
        self.label_11.setText(_translate("MainWindow", "升程范围"))
        self.label_32.setText(_translate("MainWindow", "减压数据列名"))
        self.label_12.setText(_translate("MainWindow", "减压范围"))
        self.label_13.setText(_translate("MainWindow", "正时点进气高度"))
        self.label_14.setText(_translate("MainWindow", "正时点排气高度"))
        self.label_15.setText(_translate("MainWindow", "编码器角度系数"))
        self.label_16.setText(_translate("MainWindow", "传感器高度系数"))
        self.pushButton_5.setText(_translate("MainWindow", "读取参数"))
        self.pushButton_6.setText(_translate("MainWindow", "保存参数"))
        self.label_31.setText(_translate("MainWindow", "密码"))
        self.pushButton_17.setText(_translate("MainWindow", "登录"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "默认参数设置"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "帮助"))
        self.action.setText(_translate("MainWindow", "数据分析"))
