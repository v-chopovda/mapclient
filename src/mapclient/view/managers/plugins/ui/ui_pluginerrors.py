# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pluginerrors.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QDialog,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_PluginErrors(object):
    def setupUi(self, PluginErrors):
        if not PluginErrors.objectName():
            PluginErrors.setObjectName(u"PluginErrors")
        PluginErrors.resize(351, 319)
        icon = QIcon()
        icon.addFile(u":/mapclient/images/icon-app.png", QSize(), QIcon.Normal, QIcon.Off)
        PluginErrors.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(PluginErrors)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(PluginErrors)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.listWidget = QListWidget(PluginErrors)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.listWidget.setTextElideMode(Qt.ElideMiddle)

        self.verticalLayout.addWidget(self.listWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.hideCheckBox = QCheckBox(PluginErrors)
        self.hideCheckBox.setObjectName(u"hideCheckBox")

        self.horizontalLayout.addWidget(self.hideCheckBox)

        self.horizontalSpacer = QSpacerItem(288, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ignoreButton = QPushButton(PluginErrors)
        self.ignoreButton.setObjectName(u"ignoreButton")

        self.horizontalLayout.addWidget(self.ignoreButton)

        self.pushButton = QPushButton(PluginErrors)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(PluginErrors)
        self.pushButton.clicked.connect(PluginErrors.close)

        QMetaObject.connectSlotsByName(PluginErrors)
    # setupUi

    def retranslateUi(self, PluginErrors):
        PluginErrors.setWindowTitle(QCoreApplication.translate("PluginErrors", u"Plugin Errors", None))
        self.label.setText("")
        self.hideCheckBox.setText(QCoreApplication.translate("PluginErrors", u"Don't show me this again", None))
        self.ignoreButton.setText(QCoreApplication.translate("PluginErrors", u"Ignore", None))
        self.pushButton.setText(QCoreApplication.translate("PluginErrors", u"OK", None))
    # retranslateUi

