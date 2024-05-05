import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import os
import tkinter
from tkinter import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://news.google.com/home?hl=zh-TW&gl=TW&ceid=TW:zh-Hant'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('上一頁', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('下一頁', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('重新載入', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        google_btn = QAction('google新聞', self)
        google_btn.triggered.connect(self.google)
        navbar.addAction(google_btn)

        microsoft_btn = QAction('microsoft新聞', self)
        microsoft_btn.triggered.connect(self.microsoft)
        navbar.addAction(microsoft_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def google(self):
        self.browser.setUrl(QUrl('https://news.google.com/home?hl=zh-TW&gl=TW&ceid=TW:zh-Hant'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def microsoft(self):
        self.browser.setUrl(QUrl('https://www.msn.com/zh-tw/'))

    def update_url(self, q):
        self.url_bar.setText(q.toString())
        
    
app = QApplication(sys.argv)
QApplication.setApplicationName('新聞')
window = MainWindow()
app.exec_()
