import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import os
import tkinter
from tkinter import *
print('cookie_browser(2023)-----bata0.4')


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # 搞一個 QTabWidget
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        self.setWindowTitle('cookie browser')
        

           #讓分頁可以關掉
        self.tabs.setTabsClosable(True)
        #設定怎麼關掉法
        self.tabs.tabCloseRequested.connect(self.close_current_tab)
        #搞個圖標
        self.setWindowIcon(QIcon('cookie.ico'))
	
	
        



        self.showMaximized()

        self.home_url = "https://www.bing.com/browserextension/minecraft?origin=ext&pc=U585&FORM=U585DF#"

        # 搞一個新選項卡並將他設置為home選項卡
        self.add_new_tab(self.home_url, "主頁")

        # 搞個導航工具欄
        navbar = QToolBar()
        self.addToolBar(navbar)
        #搞一堆按鈕
        back_btn = QAction(QIcon('back.svg'),'', self)
        back_btn.triggered.connect(self.tabs.currentWidget().back)
        navbar.addAction(back_btn)

        forward_btn = QAction(QIcon('forward.svg'),'', self)
        forward_btn.triggered.connect(self.tabs.currentWidget().forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction(QIcon('reload.svg'),'', self)
        reload_btn.triggered.connect(self.tabs.currentWidget().reload)
        navbar.addAction(reload_btn)

        home_btn = QAction(QIcon('home.png'),'', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        new_tab_btn = QAction(QIcon('add.svg'),'', self)
        new_tab_btn.triggered.connect(self.add_new_tab)
        navbar.addAction(new_tab_btn)

        
        


        

        # 搞一個搜索欄
        self.search_bar = QLineEdit()
        self.search_bar.returnPressed.connect(self.search)
        navbar.addWidget(self.search_bar)

         # 搞個導航工具欄
        never = QToolBar()
        self.addToolBar(never)

        google_btn = QAction(QIcon('google.png'),'', self)
        google_btn.triggered.connect(self.google_home_one)
        never.addAction(google_btn)

        bing_btn = QAction(QIcon('bing.jpg'),'', self)
        bing_btn.triggered.connect(self.bing_home_two)
        never.addAction(bing_btn)

        newstool_btn = QAction(QIcon('news.png'),'', self)
        newstool_btn.triggered.connect(self.newstool_btn)
        never.addAction(newstool_btn)



    def google_home_one(self):
        self.home_url = "https://www.google.com.tw"
    def bing_home_two(self):
        self.home_url = "https://www.bing.com/browserextension/minecraft?origin=ext&pc=U585&FORM=U585DF#"
    def newstool_btn(self):
        print('1')
    def add_new_tab(self, url=None, title="新分頁"):
        browser = QWebEngineView()

        #搞一個url
        if url:
            browser.setUrl(QUrl(url))

        # 創建一個新選項卡並將瀏覽器設置為其小部件
        tab_index = self.tabs.addTab(browser, title)

        # 搞一個新分頁
        self.tabs.setCurrentIndex(tab_index)

        #更新搜尋欄
        browser.urlChanged.connect(self.update_url)
        
    def search(self):
        url = self.search_bar.text()
        current_tab = self.tabs.currentWidget()
        current_tab.setUrl(QUrl(f"https://google.com.tw/search?q={url}"))
    

    def navigate_home(self):
        self.tabs.currentWidget().setUrl(QUrl(self.home_url))

    def update_url(self, q):
        self.search_bar.setText(q.toString())
        #讓分頁關掉成為可能
    def close_current_tab(self, i):
	    if self.tabs.count() < 2:
		    return
	    self.tabs.removeTab(i)

   

    


app = QApplication(sys.argv)
QApplication.setApplicationName('cookie browser 0.4bata')
window = MainWindow()
app.exec_()

