# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'usb_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QHeaderView, QLineEdit, QPushButton,
    QSizePolicy, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_USBWindow(object):
    def setupUi(self, USBWindow):
        if not USBWindow.objectName():
            USBWindow.setObjectName(u"USBWindow")
        USBWindow.resize(1040, 717)
        icon = QIcon(QIcon.fromTheme(u"printer"))
        USBWindow.setWindowIcon(icon)
        self.verticalLayout_2 = QVBoxLayout(USBWindow)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_linked_update = QPushButton(USBWindow)
        self.pushButton_linked_update.setObjectName(u"pushButton_linked_update")

        self.horizontalLayout_7.addWidget(self.pushButton_linked_update)

        self.lineEdit_linked_search = QLineEdit(USBWindow)
        self.lineEdit_linked_search.setObjectName(u"lineEdit_linked_search")

        self.horizontalLayout_7.addWidget(self.lineEdit_linked_search)

        self.pushButton_linked_search = QPushButton(USBWindow)
        self.pushButton_linked_search.setObjectName(u"pushButton_linked_search")

        self.horizontalLayout_7.addWidget(self.pushButton_linked_search)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.treeWidget_linked = QTreeWidget(USBWindow)
        self.treeWidget_linked.setObjectName(u"treeWidget_linked")
        self.treeWidget_linked.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.treeWidget_linked.setRootIsDecorated(False)
        self.treeWidget_linked.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.treeWidget_linked)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.buttonBox = QDialogButtonBox(USBWindow)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(USBWindow)
        self.buttonBox.accepted.connect(USBWindow.accept)
        self.buttonBox.rejected.connect(USBWindow.reject)

        QMetaObject.connectSlotsByName(USBWindow)
    # setupUi

    def retranslateUi(self, USBWindow):
        USBWindow.setWindowTitle(QCoreApplication.translate("USBWindow", u"USB \u043f\u0440\u0438\u043d\u0442\u0435\u0440\u044b", None))
        self.pushButton_linked_update.setText(QCoreApplication.translate("USBWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.lineEdit_linked_search.setPlaceholderText(QCoreApplication.translate("USBWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.pushButton_linked_search.setText(QCoreApplication.translate("USBWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        ___qtreewidgetitem = self.treeWidget_linked.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("USBWindow", u"URI", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("USBWindow", u"\u041c\u043e\u0434\u0435\u043b\u044c", None));
    # retranslateUi

