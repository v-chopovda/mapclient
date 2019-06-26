# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/mapclient/view/dialogs/log/qt/loginformation.ui',
# licensing of 'src/mapclient/view/dialogs/log/qt/loginformation.ui' applies.
#
# Created: Wed Jun 26 16:08:18 2019
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_LogInformation(object):
    def setupUi(self, LogInformation):
        LogInformation.setObjectName("LogInformation")
        LogInformation.resize(645, 534)
        LogInformation.setMinimumSize(QtCore.QSize(600, 450))
        LogInformation.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gridLayout_2 = QtWidgets.QGridLayout(LogInformation)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.history = QtWidgets.QLabel(LogInformation)
        self.history.setObjectName("history")
        self.gridLayout.addWidget(self.history, 0, 0, 1, 1)
        self.information_table = QtWidgets.QTableWidget(LogInformation)
        self.information_table.setEnabled(True)
        self.information_table.setMouseTracking(False)
        self.information_table.setAutoFillBackground(False)
        self.information_table.setInputMethodHints(QtCore.Qt.ImhNone)
        self.information_table.setFrameShadow(QtWidgets.QFrame.Raised)
        self.information_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.information_table.setTabKeyNavigation(False)
        self.information_table.setProperty("showDropIndicator", False)
        self.information_table.setDragDropOverwriteMode(False)
        self.information_table.setAlternatingRowColors(False)
        self.information_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.information_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.information_table.setShowGrid(False)
        self.information_table.setGridStyle(QtCore.Qt.NoPen)
        self.information_table.setCornerButtonEnabled(False)
        self.information_table.setRowCount(0)
        self.information_table.setColumnCount(5)
        self.information_table.setObjectName("information_table")
        self.information_table.setColumnCount(5)
        self.information_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.information_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.information_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.information_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.information_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.information_table.setHorizontalHeaderItem(4, item)
        self.information_table.horizontalHeader().setVisible(True)
        self.information_table.horizontalHeader().setCascadingSectionResizes(True)
        self.information_table.horizontalHeader().setDefaultSectionSize(75)
        self.information_table.horizontalHeader().setHighlightSections(True)
        self.information_table.horizontalHeader().setMinimumSectionSize(75)
        self.information_table.horizontalHeader().setSortIndicatorShown(True)
        self.information_table.horizontalHeader().setStretchLastSection(True)
        self.information_table.verticalHeader().setVisible(False)
        self.information_table.verticalHeader().setDefaultSectionSize(20)
        self.information_table.verticalHeader().setHighlightSections(False)
        self.information_table.verticalHeader().setMinimumSectionSize(15)
        self.gridLayout.addWidget(self.information_table, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.loadButton = QtWidgets.QPushButton(LogInformation)
        self.loadButton.setObjectName("loadButton")
        self.horizontalLayout.addWidget(self.loadButton)
        self.detailsButton = QtWidgets.QPushButton(LogInformation)
        self.detailsButton.setObjectName("detailsButton")
        self.horizontalLayout.addWidget(self.detailsButton)
        spacerItem = QtWidgets.QSpacerItem(328, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.closeWindowButton = QtWidgets.QPushButton(LogInformation)
        self.closeWindowButton.setObjectName("closeWindowButton")
        self.horizontalLayout.addWidget(self.closeWindowButton)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(LogInformation)
        QtCore.QObject.connect(self.closeWindowButton, QtCore.SIGNAL("clicked()"), LogInformation.close)
        QtCore.QMetaObject.connectSlotsByName(LogInformation)

    def retranslateUi(self, LogInformation):
        LogInformation.setWindowTitle(QtWidgets.QApplication.translate("LogInformation", "Logged Information", None, -1))
        self.history.setText(QtWidgets.QApplication.translate("LogInformation", "History:", None, -1))
        self.information_table.setSortingEnabled(True)
        self.information_table.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("LogInformation", "Date", None, -1))
        self.information_table.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("LogInformation", "Time", None, -1))
        self.information_table.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("LogInformation", "Location", None, -1))
        self.information_table.horizontalHeaderItem(3).setText(QtWidgets.QApplication.translate("LogInformation", "Level", None, -1))
        self.information_table.horizontalHeaderItem(4).setText(QtWidgets.QApplication.translate("LogInformation", "Description", None, -1))
        self.loadButton.setText(QtWidgets.QApplication.translate("LogInformation", "Load", None, -1))
        self.detailsButton.setText(QtWidgets.QApplication.translate("LogInformation", "Details", None, -1))
        self.closeWindowButton.setText(QtWidgets.QApplication.translate("LogInformation", "Close", None, -1))

