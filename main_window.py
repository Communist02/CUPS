# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 800)
        MainWindow.setWindowTitle(u"P Explorer")
        icon = QIcon(QIcon.fromTheme(u"printer"))
        MainWindow.setWindowIcon(icon)
        self.action_new_remote = QAction(MainWindow)
        self.action_new_remote.setObjectName(u"action_new_remote")
        icon1 = QIcon(QIcon.fromTheme(u"system-file-manager"))
        self.action_new_remote.setIcon(icon1)
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        icon2 = QIcon(QIcon.fromTheme(u"application-exit"))
        self.action_exit.setIcon(icon2)
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        icon3 = QIcon(QIcon.fromTheme(u"help-about"))
        self.action_about.setIcon(icon3)
        self.action_list_remotes = QAction(MainWindow)
        self.action_list_remotes.setObjectName(u"action_list_remotes")
        self.action_list_remotes.setCheckable(True)
        self.action_list_remotes.setChecked(True)
        self.action_new_serve = QAction(MainWindow)
        self.action_new_serve.setObjectName(u"action_new_serve")
        icon4 = QIcon(QIcon.fromTheme(u"applications-internet"))
        self.action_new_serve.setIcon(icon4)
        self.action_settings = QAction(MainWindow)
        self.action_settings.setObjectName(u"action_settings")
        icon5 = QIcon(QIcon.fromTheme(u"applications-development"))
        self.action_settings.setIcon(icon5)
        self.action_show_tasks = QAction(MainWindow)
        self.action_show_tasks.setObjectName(u"action_show_tasks")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setDocumentMode(True)
        self.printers_search = QWidget()
        self.printers_search.setObjectName(u"printers_search")
        self.verticalLayout_4 = QVBoxLayout(self.printers_search)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lineEdit_search = QLineEdit(self.printers_search)
        self.lineEdit_search.setObjectName(u"lineEdit_search")

        self.horizontalLayout_5.addWidget(self.lineEdit_search)

        self.comboBox_search_mode = QComboBox(self.printers_search)
        self.comboBox_search_mode.addItem("")
        self.comboBox_search_mode.addItem("")
        self.comboBox_search_mode.addItem("")
        self.comboBox_search_mode.setObjectName(u"comboBox_search_mode")

        self.horizontalLayout_5.addWidget(self.comboBox_search_mode)

        self.pushButton_search = QPushButton(self.printers_search)
        self.pushButton_search.setObjectName(u"pushButton_search")

        self.horizontalLayout_5.addWidget(self.pushButton_search)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboBox_protocol = QComboBox(self.printers_search)
        self.comboBox_protocol.setObjectName(u"comboBox_protocol")
        self.comboBox_protocol.setEditable(True)

        self.horizontalLayout.addWidget(self.comboBox_protocol)

        self.lineEdit_uri = QLineEdit(self.printers_search)
        self.lineEdit_uri.setObjectName(u"lineEdit_uri")

        self.horizontalLayout.addWidget(self.lineEdit_uri)

        self.checkBox_auto = QCheckBox(self.printers_search)
        self.checkBox_auto.setObjectName(u"checkBox_auto")

        self.horizontalLayout.addWidget(self.checkBox_auto)

        self.pushButton_create_link = QPushButton(self.printers_search)
        self.pushButton_create_link.setObjectName(u"pushButton_create_link")

        self.horizontalLayout.addWidget(self.pushButton_create_link)

        self.pushButton_link = QPushButton(self.printers_search)
        self.pushButton_link.setObjectName(u"pushButton_link")

        self.horizontalLayout.addWidget(self.pushButton_link)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.treeWidget_list = QTreeWidget(self.printers_search)
        self.treeWidget_list.setObjectName(u"treeWidget_list")
        self.treeWidget_list.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.treeWidget_list.setRootIsDecorated(False)
        self.treeWidget_list.setSortingEnabled(True)

        self.verticalLayout_4.addWidget(self.treeWidget_list)

        self.tabWidget.addTab(self.printers_search, icon, "")
        self.tab_add = QWidget()
        self.tab_add.setObjectName(u"tab_add")
        self.verticalLayout_2 = QVBoxLayout(self.tab_add)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.tab_add)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.lineEdit_add_name = QLineEdit(self.tab_add)
        self.lineEdit_add_name.setObjectName(u"lineEdit_add_name")

        self.verticalLayout_3.addWidget(self.lineEdit_add_name)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.tab_add)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_6.addWidget(self.label_3)

        self.lineEdit_desc = QLineEdit(self.tab_add)
        self.lineEdit_desc.setObjectName(u"lineEdit_desc")

        self.verticalLayout_6.addWidget(self.lineEdit_desc)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.comboBox_add_protocol = QComboBox(self.tab_add)
        self.comboBox_add_protocol.setObjectName(u"comboBox_add_protocol")
        self.comboBox_add_protocol.setEditable(True)

        self.horizontalLayout_2.addWidget(self.comboBox_add_protocol)

        self.lineEdit_add_uri = QLineEdit(self.tab_add)
        self.lineEdit_add_uri.setObjectName(u"lineEdit_add_uri")

        self.horizontalLayout_2.addWidget(self.lineEdit_add_uri)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.tab_add)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.comboBox_add_driver = QComboBox(self.tab_add)
        self.comboBox_add_driver.setObjectName(u"comboBox_add_driver")
        self.comboBox_add_driver.setEditable(True)

        self.horizontalLayout_4.addWidget(self.comboBox_add_driver)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.pushButton_add = QPushButton(self.tab_add)
        self.pushButton_add.setObjectName(u"pushButton_add")

        self.verticalLayout_2.addWidget(self.pushButton_add)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        icon6 = QIcon(QIcon.fromTheme(u"list-add"))
        self.tabWidget.addTab(self.tab_add, icon6, "")
        self.tab_drivers = QWidget()
        self.tab_drivers.setObjectName(u"tab_drivers")
        self.verticalLayout_5 = QVBoxLayout(self.tab_drivers)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_drivers_update = QPushButton(self.tab_drivers)
        self.pushButton_drivers_update.setObjectName(u"pushButton_drivers_update")

        self.horizontalLayout_6.addWidget(self.pushButton_drivers_update)

        self.lineEdit_drivers_search = QLineEdit(self.tab_drivers)
        self.lineEdit_drivers_search.setObjectName(u"lineEdit_drivers_search")

        self.horizontalLayout_6.addWidget(self.lineEdit_drivers_search)

        self.pushButton_drivers_search = QPushButton(self.tab_drivers)
        self.pushButton_drivers_search.setObjectName(u"pushButton_drivers_search")

        self.horizontalLayout_6.addWidget(self.pushButton_drivers_search)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.treeWidget_drivers = QTreeWidget(self.tab_drivers)
        self.treeWidget_drivers.setObjectName(u"treeWidget_drivers")
        self.treeWidget_drivers.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.treeWidget_drivers.setRootIsDecorated(False)
        self.treeWidget_drivers.setSortingEnabled(True)

        self.verticalLayout_5.addWidget(self.treeWidget_drivers)

        self.tabWidget.addTab(self.tab_drivers, icon5, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 33))
        self.menuClient = QMenu(self.menubar)
        self.menuClient.setObjectName(u"menuClient")
        self.menuOther = QMenu(self.menubar)
        self.menuOther.setObjectName(u"menuOther")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setSizeGripEnabled(False)
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuClient.menuAction())
        self.menubar.addAction(self.menuOther.menuAction())
        self.menuClient.addAction(self.action_settings)
        self.menuClient.addSeparator()
        self.menuClient.addAction(self.action_exit)
        self.menuOther.addAction(self.action_about)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.action_new_remote.setText(QCoreApplication.translate("MainWindow", u"New remote", None))
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.action_list_remotes.setText(QCoreApplication.translate("MainWindow", u"List remotes", None))
        self.action_new_serve.setText(QCoreApplication.translate("MainWindow", u"New serve", None))
        self.action_settings.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.action_show_tasks.setText(QCoreApplication.translate("MainWindow", u"Show tasks", None))
        self.lineEdit_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.comboBox_search_mode.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u0432\u0441\u0435", None))
        self.comboBox_search_mode.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043b\u044c\u043a\u043e, \u0433\u0434\u0435 \u0435\u0441\u0442\u044c URI", None))
        self.comboBox_search_mode.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043b\u044c\u043a\u043e, \u0433\u0434\u0435 \u043d\u0435\u0442 URI", None))

        self.pushButton_search.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
#if QT_CONFIG(tooltip)
        self.comboBox_protocol.setToolTip(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u043f\u0440\u043e\u0442\u043e\u043a\u043e\u043b\u0430", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_uri.setPlaceholderText(QCoreApplication.translate("MainWindow", u"URI", None))
#if QT_CONFIG(tooltip)
        self.checkBox_auto.setToolTip(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043f\u043e\u0434\u0431\u043e\u0440 \u0434\u0440\u0430\u0439\u0432\u0435\u0440\u0430", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_auto.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0434\u0440\u0430\u0439\u0432\u0435\u0440", None))
        self.pushButton_create_link.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u044f\u0440\u043b\u044b\u043a", None))
        self.pushButton_link.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c", None))
        ___qtreewidgetitem = self.treeWidget_list.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"URI", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"\u0414\u0440\u0430\u0439\u0432\u0435\u0440", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.printers_search), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043d\u0442\u0435\u0440\u044b", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.comboBox_add_protocol.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0442\u043e\u043a\u043e\u043b", None))
        self.lineEdit_add_uri.setPlaceholderText(QCoreApplication.translate("MainWindow", u"URI", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0440\u0430\u0439\u0432\u0435\u0440", None))
        self.pushButton_add.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_add), QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_drivers_update.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.lineEdit_drivers_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.pushButton_drivers_search.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        ___qtreewidgetitem1 = self.treeWidget_drivers.headerItem()
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"\u0414\u0440\u0430\u0439\u0432\u0435\u0440", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0435\u043b\u044c", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_drivers), QCoreApplication.translate("MainWindow", u"\u0414\u0440\u0430\u0439\u0432\u0435\u0440\u044b", None))
        self.menuClient.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.menuOther.setTitle(QCoreApplication.translate("MainWindow", u"\u0414\u0440\u0443\u0433\u043e\u0435", None))
        pass
    # retranslateUi

