import asyncio
import signal
import sys
import os
import subprocess
import types
import json

from PySide6.QtCore import QFileInfo, QLibraryInfo, QLocale, QMimeData, QPoint, QSettings, QSize, QTranslator, QUrl, Qt
from PySide6.QtGui import QColorConstants, QDesktopServices, QDrag, QDragEnterEvent, QIcon, QAction, QCursor, QKeySequence, QPainter, QPixmap, QShortcut
from PySide6.QtWidgets import QFileIconProvider, QInputDialog, QMainWindow, QApplication, QDialog, QMenu, QFileDialog, QSizePolicy, QStyleFactory, QSystemTrayIcon, QTreeWidgetItem, QPushButton, QMessageBox, QLabel
import PySide6.QtAsyncio as QtAsyncio

import main_window
import settings_window

from palettes import palettes

class SettingsWindow(QDialog):
    def __init__(self):
        super(SettingsWindow, self).__init__()
        self.ui = settings_window.Ui_SettingsWindow()
        self.ui.setupUi(self)

        styles = QStyleFactory.keys()
        for i in range(len(styles)):
            styles[i] = styles[i].lower()
        self.ui.comboBox_style.addItems(styles)
        self.ui.comboBox_style.setCurrentText(app.style().name())

        palettes_list = palettes.keys()
        self.ui.comboBox_palette.addItems(palettes_list)
        self.ui.comboBox_palette.setCurrentText(
            settings.value('palette', 'System'))

        self.ui.buttonBox.accepted.connect(self.ok)

    def ok(self):
        app.setStyle(self.ui.comboBox_style.currentText())
        app.setPalette(palettes[self.ui.comboBox_palette.currentText()])

        settings.setValue('style', self.ui.comboBox_style.currentText())
        settings.setValue('palette', self.ui.comboBox_palette.currentText())


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = main_window.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.treeWidget_list.header().setSortIndicator(0, Qt.SortOrder.AscendingOrder)

        self.ui.button_search.clicked.connect(self.search)
        self.ui.lineEdit_search.editingFinished.connect(self.search)
        self.ui.button_link.clicked.connect(self.link)
        self.ui.button_create_link.clicked.connect(self.create_link)

        self.ui.action_settings.triggered.connect(self.open_settings_window)
        self.ui.action_exit.triggered.connect(self.close)
        self.ui.action_about.triggered.connect(lambda: QMessageBox.aboutQt(self))

        self.ui.treeWidget_list.customContextMenuRequested.connect(self.show_context_menu_tree_search)

        self.search()

        # self.shortcuts()

    def timer_update(self):
        pass

    def open_settings_window(self):
        open_win = SettingsWindow()
        open_win.exec()

    def search(self):
        text = self.ui.lineEdit_search.text()

        with open('list.json', 'r') as file:
            data: dict = json.load(file)
        print(data)

        self.ui.statusbar.showMessage('Поиск')

        self.ui.treeWidget_list.clear()
        
        for key, value in data.items():
            if key.lower().rfind(text.lower()) != -1:
                item = QTreeWidgetItem()
                item.setText(0, key)
                item.setText(1, value[0])
                self.ui.treeWidget_list.addTopLevelItem(item)

        self.ui.statusbar.showMessage('')
    
    def link(self, item: QTreeWidgetItem = None):
        if item is None or item == False:
            item = self.ui.treeWidget_list.currentItem()
        else:
            item = None

        if item is not None:
            protocol = self.ui.comboBox.currentText()
            if self.ui.checkBox_auto.isChecked():
                driver = 'everywhere'
            else:
                driver = item.text(1)
            command = f'lpadmin -p {item.text(0)} -v {protocol} -E -m {driver}'
            print(command)
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            OUT, _ = process.communicate()
            OUT = OUT.decode()

            print(OUT)

    def create_link(self, item: QTreeWidgetItem = None):
        if item is None or item == False:
            item = self.ui.treeWidget_list.currentItem()
        else:
            item = None

        if item is not None:
            print(item.text(0))

    def show_context_menu_tree_search(self, point):
        index = self.ui.treeWidget_list.indexAt(point)

        if not index.isValid():
            return

        item = self.ui.treeWidget_list.itemAt(point)

        menu = QMenu()

        action = QAction(self)
        action.setText('Подключить')
        action.setIcon(QIcon.fromTheme('system-file-manager'))
        action.triggered.connect(self.link)
        menu.addAction(action)

        action = QAction(self)
        action.setText('Создать ярлык')
        action.setIcon(QIcon.fromTheme('system-file-manager'))
        action.triggered.connect(self.create_link)
        menu.addAction(action)

        menu.exec(QCursor.pos())

if __name__ == '__main__':
    app = QApplication()
    settings = QSettings('Denis Mazur', 'P Explorer')
    app.setStyle(settings.value('style', ''))
    app.setPalette(palettes[settings.value('palette', 'System')])

    qt_translator = QTranslator()
    translator = QTranslator()

    qt_translator.load(f'qtbase_{QLocale.system().name()}.qm', QLibraryInfo.path(
        QLibraryInfo.LibraryPath.TranslationsPath))
    app.installTranslator(qt_translator)

    if translator.load(f'{os.path.dirname(__file__) + os.sep}translations{os.sep}{QLocale.system().language().name}.qm'):
        app.installTranslator(translator)


    window = MainWindow()
    window.show()

    sys.exit(QtAsyncio.run())
