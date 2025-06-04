import sys
import os
import subprocess
import json

from PySide6.QtCore import QLibraryInfo, QLocale, QSettings, QTranslator, Qt
from PySide6.QtGui import QAction, QCursor, QGuiApplication
from PySide6.QtWidgets import QMainWindow, QApplication, QDialog, QMenu, QStyleFactory, QTreeWidgetItem, QMessageBox

import main_window
import settings_window
import usb_window

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


class USBWindow(QDialog):
    def __init__(self):
        super(USBWindow, self).__init__()
        self.ui = usb_window.Ui_USBWindow()
        self.ui.setupUi(self)

        self.ui.treeWidget_linked.header().resizeSection(0, 500)

        self.ui.lineEdit_linked_search.editingFinished.connect(
            self.linked_search)
        self.ui.pushButton_linked_update.clicked.connect(self.linked_update)
        self.ui.treeWidget_linked.customContextMenuRequested.connect(
            self.show_context_menu_linked)

        self.ui.buttonBox.accepted.connect(self.ok)

        self.linked_search()

    def ok(self):
        item = self.ui.treeWidget_linked.currentItem()
        if item is not None:
            window.ui.lineEdit_add_uri.setText(item.text(1))
            window.ui.comboBox_add_protocol.setCurrentText(' ')

    def linked_search(self):
        text = self.ui.lineEdit_linked_search.text()
        try:
            with open(os.path.dirname(__file__) + os.sep + 'config/linked.json', 'r') as file:
                data: dict = json.load(file)
        except json.decoder.JSONDecodeError and FileNotFoundError:
            data: dict = {}

        self.ui.treeWidget_linked.clear()

        for key, value in data.items():
            if value.lower().rfind(text.lower()) != -1:
                item = QTreeWidgetItem()
                item.setText(1, key)
                item.setText(0, value)
                self.ui.treeWidget_linked.addTopLevelItem(item)

    def linked_update(self):
        command = 'lpinfo -v | grep usb:'
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        OUT, _ = process.communicate()
        OUT = OUT.decode()

        print(OUT)

        list_out = OUT.split('\n')
        data: dict = {}

        for s in list_out:
            uri = s[s.find(' '):]
            model = ''
            if uri != '':
                data[uri] = model

        with open(os.path.dirname(__file__) + os.sep + 'config/linked.json', 'w') as file:
            file.write(json.dumps(data, sort_keys=True))

        self.linked_search()

    def show_context_menu_linked(self, point):
        index = self.ui.treeWidget_linked.indexAt(point)

        if not index.isValid():
            return

        item = self.ui.treeWidget_linked.itemAt(point)

        menu = QMenu()

        def copy(text: str):
            clipboard = QGuiApplication.clipboard()
            clipboard.setText(text)

        action = QAction(self)
        action.setText('Копировать URI')
        action.triggered.connect(lambda: copy(item.text(1)))
        menu.addAction(action)

        menu.exec(QCursor.pos())


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = main_window.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.treeWidget_drivers.header().resizeSection(0, 500)
        self.ui.treeWidget_linked_all.header().resizeSection(0, 500)
        self.ui.treeWidget_scan.header().resizeSection(0, 500)
        self.ui.treeWidget_list.header().resizeSection(0, 500)

        self.ui.treeWidget_list.header().setSortIndicator(0, Qt.SortOrder.AscendingOrder)
        self.ui.treeWidget_drivers.header().setSortIndicator(
            0, Qt.SortOrder.AscendingOrder)
        self.ui.treeWidget_linked_all.header().setSortIndicator(
            0, Qt.SortOrder.AscendingOrder)
        self.ui.treeWidget_scan.header().setSortIndicator(0, Qt.SortOrder.AscendingOrder)

        self.ui.pushButton_search.clicked.connect(self.search)
        self.ui.lineEdit_search.editingFinished.connect(self.search)
        self.ui.lineEdit_drivers_search.editingFinished.connect(
            self.drivers_search)
        self.ui.lineEdit_scan_search.editingFinished.connect(self.scan_search)
        self.ui.pushButton_link.clicked.connect(self.link)
        self.ui.pushButton_add_and_link.clicked.connect(self.add_and_link)
        self.ui.pushButton_drivers_update.clicked.connect(self.drivers_update)
        self.ui.pushButton_drivers_search.clicked.connect(self.drivers_search)
        self.ui.pushButton_scan_search.clicked.connect(self.scan_search)
        self.ui.pushButton_scan_update.clicked.connect(self.scan_update)
        self.ui.pushButton_linked_all_update.clicked.connect(
            self.linked_all_update)
        self.ui.pushButton_scan_create_link.clicked.connect(self.create_link)
        self.ui.pushButton_linked_all_search.clicked.connect(
            self.linked_all_search)
        self.ui.toolButton_select_usb.clicked.connect(self.open_usb_window)

        self.ui.action_settings.triggered.connect(self.open_settings_window)
        self.ui.action_exit.triggered.connect(self.close)
        self.ui.action_about.triggered.connect(
            lambda: QMessageBox.aboutQt(self))

        self.ui.treeWidget_list.customContextMenuRequested.connect(
            self.show_context_menu_tree_search)
        self.ui.treeWidget_drivers.customContextMenuRequested.connect(
            self.show_context_menu_drivers)
        self.ui.treeWidget_scan.customContextMenuRequested.connect(
            self.show_context_menu_tree_scan)
        self.ui.treeWidget_linked_all.customContextMenuRequested.connect(
            self.show_context_menu_tree_linked_all)

        self.ui.treeWidget_drivers.itemSelectionChanged.connect(
            self.select_driver)
        
        self.ui.checkBox_auto.hide()

        self.search()
        self.drivers_search()
        self.scan_search()
        self.update_protocols()
        self.linked_all_update()
        self.linked_all_search()

    def open_settings_window(self):
        open_win = SettingsWindow()
        open_win.exec()

    def open_usb_window(self):
        open_win = USBWindow()
        open_win.exec()

    def select_driver(self):
        item = self.ui.treeWidget_drivers.currentItem()
        if item is not None:
            self.ui.lineEdit_add_name.setText(item.text(0).replace(' ', '_'))
            self.ui.lineEdit_desc.setText(item.text(0))
            self.ui.comboBox_add_driver.setCurrentText(item.text(1))

    def update_protocols(self):
        self.ui.comboBox_protocol.clear()
        self.ui.comboBox_add_protocol.clear()
        with open(os.path.dirname(__file__) + os.sep + 'config/protocols.txt', 'r') as file:
            for line in file:
                self.ui.comboBox_protocol.addItem(line.strip())
                self.ui.comboBox_add_protocol.addItem(line.strip())

    def search(self):
        text = self.ui.lineEdit_search.text()
        try:
            with open(os.path.dirname(__file__) + os.sep + 'config/list.json', 'r') as file:
                data: dict = json.load(file)
        except FileNotFoundError:
            data: dict = {}
            with open(os.path.dirname(__file__) + os.sep + 'config/list.json', 'w') as file:
                file.write(json.dumps(data))

        self.ui.statusbar.showMessage('Поиск')

        self.ui.treeWidget_list.clear()

        for key, value in data.items():
            if key.lower().rfind(text.lower()) != -1:
                if self.ui.comboBox_search_mode.currentIndex() == 0 or self.ui.comboBox_search_mode.currentIndex() == 1 and value.get('uri', '') != '' or self.ui.comboBox_search_mode.currentIndex() == 2 and value.get('uri', '') == '':
                    item = QTreeWidgetItem()
                    item.setText(0, key)
                    item.setText(1, value['driver'])
                    item.setText(2, value.get('uri', ''))
                    self.ui.treeWidget_list.addTopLevelItem(item)

        self.ui.statusbar.showMessage('')

    def drivers_search(self):
        text = self.ui.lineEdit_drivers_search.text()
        try:
            with open(os.path.dirname(__file__) + os.sep + 'config/drivers.json', 'r') as file:
                data: dict = json.load(file)
        except json.decoder.JSONDecodeError and FileNotFoundError:
            data: dict = {}

        self.ui.treeWidget_drivers.clear()
        self.ui.comboBox_add_driver.clear()

        for key, value in data.items():
            if value.lower().rfind(text.lower()) != -1:
                item = QTreeWidgetItem()
                item.setText(1, key)
                item.setText(0, value)
                self.ui.treeWidget_drivers.addTopLevelItem(item)
                self.ui.comboBox_add_driver.addItem(key)

    def linked_all_search(self):
        text = self.ui.lineEdit_linked_all_search.text()
        try:
            with open(os.path.dirname(__file__) + os.sep + 'config/linked_all.json', 'r') as file:
                data: dict = json.load(file)
        except json.decoder.JSONDecodeError and FileNotFoundError:
            data: dict = {}

        self.ui.treeWidget_linked_all.clear()

        for key, value in data.items():
            if value.lower().rfind(text.lower()) != -1:
                item = QTreeWidgetItem()
                item.setText(0, key)
                item.setText(1, value)
                self.ui.treeWidget_linked_all.addTopLevelItem(item)

    def scan_search(self):
        text = self.ui.lineEdit_scan_search.text()
        try:
            with open(os.path.dirname(__file__) + os.sep + 'config/scan.json', 'r') as file:
                data: dict = json.load(file)
        except json.decoder.JSONDecodeError and FileNotFoundError:
            data: dict = {}

        self.ui.treeWidget_scan.clear()

        for key, value in data.items():
            if value.lower().rfind(text.lower()) != -1:
                item = QTreeWidgetItem()
                item.setText(1, key)
                item.setText(0, value)
                self.ui.treeWidget_scan.addTopLevelItem(item)

    def scan_update(self):
        command = 'scanimage -L'

        self.ui.statusbar.showMessage('Обновление списка сканеров')

        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        OUT, _ = process.communicate()
        OUT = OUT.decode()

        print(OUT)

        list_out = OUT.split('\n')
        data: dict = {}

        for s in list_out:
            if s.find('No scanners were identified') != -1:
                break
            addr = s[s.find('device')+8:s.find("' is a")]
            model = s[s.find('is a')+5:]
            if addr != '':
                data[addr] = model

        with open(os.path.dirname(__file__) + os.sep + 'config/scan.json', 'w') as file:
            file.write(json.dumps(data, sort_keys=True))

        self.ui.statusbar.showMessage('Обновление списка сканеров завершено')

        self.scan_search()

    def linked_all_update(self):
        command = 'lpstat -v'

        self.ui.statusbar.showMessage(
            'Обновление списка подключенных принтеров')

        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        OUT, _ = process.communicate()
        OUT = OUT.decode()

        print(OUT)

        list_out = OUT.split('\n')
        data: dict = {}

        for s in list_out:
            name = s[s.find('для') + 3:s.find(':')]
            uri = s[s.find(':')+1:]
            if uri != '':
                data[name] = uri

        with open(os.path.dirname(__file__) + os.sep + 'config/linked_all.json', 'w') as file:
            file.write(json.dumps(data, sort_keys=True))

        self.ui.statusbar.showMessage('')

        self.linked_all_search()

    def drivers_update(self):
        command = 'lpinfo -m'

        self.ui.statusbar.showMessage('Обновление списка драйверов')

        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        OUT, _ = process.communicate()
        OUT = OUT.decode()

        print(OUT)

        list_drivers = OUT.split('\n')
        drivers: dict = {}

        for s in list_drivers:
            driver = s[:s.find(' ')]
            model = s[s.find(' ')+1:]
            if driver != '':
                drivers[driver] = model

        with open(os.path.dirname(__file__) + os.sep + 'config/drivers.json', 'w') as file:
            file.write(json.dumps(drivers, sort_keys=True))

        self.ui.statusbar.showMessage('Обновление списка драйверов завершено')

        self.drivers_search()

    def add_printer(self):
        name = self.ui.lineEdit_add_name.text().strip()
        desc = self.ui.lineEdit_desc.text().strip()
        uri = self.ui.comboBox_add_protocol.currentText(
        ) + self.ui.lineEdit_add_uri.text().strip()
        driver = self.ui.comboBox_add_driver.currentText().strip()

        self.ui.statusbar.showMessage('')

        with open(os.path.dirname(__file__) + os.sep + 'config/list.json', 'r') as file:
            data: dict = json.load(file)

        data[name] = {'name': name, 'desc': desc, 'uri': uri, 'driver': driver}

        with open(os.path.dirname(__file__) + os.sep + 'config/list.json', 'w') as file:
            file.write(json.dumps(data, sort_keys=True))

        self.search()

        self.ui.statusbar.showMessage('Добавлен принтер ' + name)

    def link(self, item: QTreeWidgetItem = None):
        if item is None or item == False:
            item = self.ui.treeWidget_list.currentItem()
        else:
            item = None

        if item is not None:
            protocol = self.ui.comboBox_protocol.currentText()
            if self.ui.checkBox_auto.isChecked():
                driver = 'everywhere'
            else:
                driver = item.text(1)

            if driver != '':
                driver = f'-m "{driver}"'

            uri = f'{protocol}{self.ui.lineEdit_uri.text()}'
            if item.text(2) != '':
                uri = item.text(2)

            command = f'lpadmin -p "{item.text(0)}" -v {uri} -E {driver}'
            print(command)
            process = subprocess.Popen(
                command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            OUT, ERR = process.communicate()
            OUT = OUT.decode()
            ERR = ERR.decode()

            print(OUT)
            print(ERR)

            # command = f'lpoptions -d "{item.text(0)}"'
            # print(command)
            # process = subprocess.Popen(
            #     command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            # OUT, ERR = process.communicate()
            # OUT = OUT.decode()
            # ERR = ERR.decode()

            # print(OUT)
            # print(ERR)

    def add_and_link(self):
        self.add_printer()
        name = self.ui.lineEdit_add_name.text().strip()
        desc = self.ui.lineEdit_desc.text().strip()
        uri = self.ui.comboBox_add_protocol.currentText(
        ) + self.ui.lineEdit_add_uri.text().strip()
        driver = self.ui.comboBox_add_driver.currentText().strip()
        command = f'lpadmin -p "{name}" -v {uri} -E -m {driver}'
        print(command)

        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        OUT, ERR = process.communicate()
        OUT = OUT.decode()
        ERR = ERR.decode()

        self.linked_all_update()

        print(OUT)
        print(ERR)

    def create_link(self, item: QTreeWidgetItem = None):
        if item is None or item == False:
            item = self.ui.treeWidget_scan.currentItem()
        else:
            item = None

        username = os.getenv('SUDO_USER') or os.getenv('USER')
        if username:
            desktop_path = os.path.join('/home', username, 'Desktop')
        else:
            desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

        if item is not None:
            s = '[Desktop Entry]\n'
            s += f'Name={item.text(0)}\n'
            s += 'Type=Application\n'
            s += 'NoDisplay=false\n'
            s += 'Hidden=false\n'
            s += 'StartupNotify=false\n'
            s += 'Version=1.0.0\n'
            s += f'Exec=simple-scan {item.text(1)}\n'
            s += 'Terminal=False\n'
            s += 'Categories=Graphics;Scanning\n'
            s += 'Icon=org.gnome.SimpleScan\n'

            with open(desktop_path + f'/{item.text(0)}.desktop', 'w') as file:
                file.write(s)

    def delete_printer_config(self, name: str):
        with open(os.path.dirname(__file__) + os.sep + 'config/list.json', 'r') as file:
            data: dict = json.load(file)

        data.pop(name)

        with open(os.path.dirname(__file__) + os.sep + 'config/list.json', 'w') as file:
            file.write(json.dumps(data, sort_keys=True))

        self.search()

    def show_context_menu_tree_search(self, point):
        index = self.ui.treeWidget_list.indexAt(point)

        if not index.isValid():
            return

        item = self.ui.treeWidget_list.itemAt(point)

        menu = QMenu()

        action = QAction(self)
        action.setText('Подключить')
        action.triggered.connect(self.link)
        menu.addAction(action)

        action = QAction(self)
        action.setText('Создать ярлык')
        action.triggered.connect(self.create_link)
        menu.addAction(action)

        menu.addSeparator()

        action = QAction(self)
        action.setText('Удалить')
        action.triggered.connect(
            lambda: self.delete_printer_config(item.text(0)))
        menu.addAction(action)

        menu.exec(QCursor.pos())

    def show_context_menu_tree_scan(self, point):
        index = self.ui.treeWidget_scan.indexAt(point)

        if not index.isValid():
            return

        def copy(text: str):
            clipboard = QGuiApplication.clipboard()
            clipboard.setText(text)

        item = self.ui.treeWidget_scan.itemAt(point)

        menu = QMenu()

        action = QAction(self)
        action.setText('Создать ярлык')
        action.triggered.connect(self.create_link)
        menu.addAction(action)

        action = QAction(self)
        action.setText('Копировать URI')
        action.triggered.connect(lambda: copy(item.text(1)))
        menu.addAction(action)

        action = QAction(self)
        action.setText('Копировать модель')
        action.triggered.connect(lambda: copy(item.text(0)))
        menu.addAction(action)

        menu.exec(QCursor.pos())

    def show_context_menu_drivers(self, point):
        index = self.ui.treeWidget_drivers.indexAt(point)

        if not index.isValid():
            return

        item = self.ui.treeWidget_drivers.itemAt(point)

        menu = QMenu()

        def copy(text: str):
            clipboard = QGuiApplication.clipboard()
            clipboard.setText(text)

        action = QAction(self)
        action.setText('Копировать драйвер')
        action.triggered.connect(lambda: copy(item.text(1)))
        menu.addAction(action)

        action = QAction(self)
        action.setText('Копировать модель')
        action.triggered.connect(lambda: copy(item.text(0)))
        menu.addAction(action)

        menu.exec(QCursor.pos())

    def delete_printer(self, name: str):
        command = f'lpadmin -x {name}'
        print(command)

        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        OUT, ERR = process.communicate()
        OUT = OUT.decode()
        ERR = ERR.decode()

        print(OUT)
        print(ERR)
        self.linked_all_update()

    def show_context_menu_tree_linked_all(self, point):
        index = self.ui.treeWidget_linked_all.indexAt(point)

        if not index.isValid():
            return

        item = self.ui.treeWidget_linked_all.itemAt(point)

        menu = QMenu()

        def copy(text: str):
            clipboard = QGuiApplication.clipboard()
            clipboard.setText(text)

        action = QAction(self)
        action.setText('Копировать URI')
        action.triggered.connect(lambda: copy(item.text(1)))
        menu.addAction(action)

        action = QAction(self)
        action.setText('Копировать имя')
        action.triggered.connect(lambda: copy(item.text(0)))
        menu.addAction(action)

        action = QAction(self)
        action.setText('Удалить')
        action.triggered.connect(lambda: self.delete_printer(item.text(0)))
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

    sys.exit(app.exec())
