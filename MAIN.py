import sys
import typing 
import PyQt5 
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QScrollArea,  QMainWindow, QWidget, QGraphicsView, QGraphicsScene, QFileDialog, QMessageBox, QGraphicsTextItem, QComboBox, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon, QPalette, QColor, QPainter, QImage, QPainter
from PyQt5.QtCore import Qt, pyqtSignal
from scipy import interpolate
import os
import re 
import glob
import math
from scipy import constants as con
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTableWidget, QLabel
from PyQt5.QtCore import pyqtSlot
import fitz 
from PyQt5.QtGui import QPixmap 
from pdf2image import convert_from_path
import subprocess
import pickle
from PyQt5.QtWidgets import QTextEdit
import numpy

class color(QWidget):                                  
    def __init__(self, Color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)












class ClickableTextItem(QGraphicsTextItem):
    def __init__(self, text):
        super(ClickableTextItem, self).__init__(text)

    def mousePressEvent(self, event):
        color = self.defaultTextColor()
        if color == QColor("red"):
            self.setSelected(not self.isSelected())
        else:
            self.setSelected(True)

        color = QColor("red") if self.isSelected() else QColor("black")
        self.setDefaultTextColor(color)

       
        scene = self.scene()
        if scene:
            for item in scene.selectedItems():
                item.setSelected(self.isSelected())








class my_window(QMainWindow):                           
    def __init__(self):
        super(my_window, self).__init__()
        self.setGeometry(0 ,0 ,1920 ,1080 )
        self.setWindowTitle("TriMEph")
        self.setToolTip("TriMEph")
        self.setWindowIcon(QIcon("Logo.jpg"))
        
        
        
        self.initUI()
        

        self.file_positions = {}

        
        self.loaded_files1 = []     
        self.loaded_files2 = []     
        self.loaded_files3 = []     
        self.loaded_files4 = []     

        self.loaded_files5 = []    

        self.text_item1 = []
        self.text_item2 = []
        self.text_item3 = []
        self.text_item4 = []
        
        
        
        self.files_to_delete = [] 

        self.ev_vol_list = [] 

        self.temp_list = []  
        self.volume_list = []

        self.real_temp = [] 
    
        self.outfile = [] 
        self.outfile_names = [] 


        self.mx = []  
        self.my = []
        self.mz = [] 

        self.data_list = []

        self.result = []

        self.count = []

        self.mx2 = []
        self.my2 = []
        self.mz2 = []        
        
        self.mx1 = [] 
        self.my1 = []
        self.mz1 = []



        self.factor_list = []

        self.generated_graphs_factor = [] 
        self.generated_graphs_mi1 = [] 
       
        self.atom_names = []
        self.atom_numbers = []
        self.atom_masses = []
        self.Er_const_list = []
    
        self.sing_temperature = []

        self.sing_mx = []
        self.sing_my = []
        self.sing_mz = []
        


        self.y_axis = []
        self.x_axis = []

     

        self.factor_stored_kwargs_f = {}
        self.mx1_stored_kwargs = {}
        self.my1_stored_kwargs = {}
        self.mz1_stored_kwargs = {}

        self.xAxis = []
        self.yAxis = [] 
        
        self.i = 1
        

        sys.excepthook = self.exception_hook

        
    def initUI(self):
        

       
        
        self.scroll = QScrollArea()          
        self.widget = QWidget() 
        self.widget.resize(1920, 1080) 
        self.scroll.setWidget(self.widget)


        pixmap = QPixmap("C:/Users/filip/Desktop/AV Fyzika program/pozadie.png")  
        
        background_label = QLabel(self.widget)
        background_label.setPixmap(pixmap)
        background_label.setGeometry(0, 0, self.width(), self.height())

        self.btn_documentation = QtWidgets.QPushButton(self.widget)
        self.btn_documentation.setText("?")
        self.btn_documentation.move(10,10)
        self.btn_documentation.setStyleSheet("font-size: 40px")
        self.btn_documentation.resize(160,75)
        self.btn_documentation.clicked.connect(self.open_documentation)

        self.txt_updload_files = QtWidgets.QLabel(self.widget)
        self.txt_updload_files.setText("Please Upload Following Data:")
        self.txt_updload_files.move(180,20)
        self.txt_updload_files.setStyleSheet("font-size: 16px")
        


       
       
        self.txt_name = QtWidgets.QLabel(self.widget) 
        self.txt_name.setText("Phonopy.yaml file:")
        self.txt_name.move(180, 55)
        self.txt_name.setStyleSheet("font-size: 15px")
        
        self.btn_name = QtWidgets.QPushButton(self.widget)
        self.btn_name.setText("Upload")
        self.btn_name.resize(100,30)
        self.btn_name.move(370, 50)
        self.btn_name.setStyleSheet("background-color: lightgreen; border: 1px solid black; font-size: 16px;")
        self.btn_name.clicked.connect(self.openFileDialog1)


        self.graphics_load1 = QGraphicsView(self.widget)
        self.graphics_load1.move(180,90)
        self.graphics_load1.resize(400,200)
        
        self.btn_1delete = QtWidgets.QPushButton(self.widget)
        self.btn_1delete.setText("Delete")
        self.btn_1delete.move(480, 50)
        self.btn_1delete.resize(100,30)
        self.btn_1delete.setStyleSheet("background-color: red; border: 1px solid black; font-size: 16px;")
        self.btn_1delete.clicked.connect(self.DeleteLoadedFiles1)




        self.txt_2name = QtWidgets.QLabel(self.widget)
        self.txt_2name.setText("Thermal Displacements Files:")
        self.txt_2name.move(180, 305)
        self.txt_2name.setStyleSheet("font-size: 15px")  


        self.btn_2name = QtWidgets.QPushButton(self.widget)
        self.btn_2name.setText("Upload")
        self.btn_2name.move(370, 300)
        self.btn_2name.resize(100,30)
        self.btn_2name.setStyleSheet("background-color: lightgreen; border: 1px solid black; font-size: 16px;")
        self.btn_2name.clicked.connect(self.openFileDialog2)
        

        self.graphics_load2 = QGraphicsView(self.widget)
        self.graphics_load2.move(180,340)
        self.graphics_load2.resize(400,200)

        self.btn_2delete = QtWidgets.QPushButton(self.widget)
        self.btn_2delete.setText("Delete")
        self.btn_2delete.move(480, 300)
        self.btn_2delete.resize(100,30)
        self.btn_2delete.setStyleSheet("background-color: red; border: 1px solid black; font-size: 16px;")
        self.btn_2delete.clicked.connect(self.DeleteLoadedFiles2)



        self.txt_3name = QtWidgets.QLabel(self.widget)
        self.txt_3name.setText("Volume - Temperature File:")
        self.txt_3name.move(180, 555)
        self.txt_3name.setStyleSheet("font-size: 15px")

        self.btn_3name = QtWidgets.QPushButton(self.widget)
        self.btn_3name.setText("Upload")
        self.btn_3name.move(370, 550)
        self.btn_3name.resize(100,30)
        self.btn_3name.setStyleSheet("background-color: lightgreen; border: 1px solid black; font-size: 16px;")
        self.btn_3name.clicked.connect(self.openFileDialog3)

        self.graphics_load3 = QGraphicsView(self.widget)
        self.graphics_load3.move(180, 590)
        self.graphics_load3.resize(400,200)

        self.btn_3delete = QtWidgets.QPushButton(self.widget)
        self.btn_3delete.setText("Delete")
        self.btn_3delete.move(480, 550)
        self.btn_3delete.resize(100,30)
        self.btn_3delete.setStyleSheet("background-color: red; border: 1px solid black; font-size: 16px;")
        self.btn_3delete.clicked.connect(self.DeleteLoadedFiles3)




        self.txt_4name = QtWidgets.QLabel(self.widget)
        self.txt_4name.setText("e-V File:")
        self.txt_4name.move(180, 805)
        self.txt_4name.setStyleSheet("font-size: 15px")

        self.btn_4name = QtWidgets.QPushButton(self.widget)
        self.btn_4name.setText("Upload")
        self.btn_4name.move(370, 800)
        self.btn_4name.resize(100,30)
        self.btn_4name.setStyleSheet("background-color: lightgreen; border: 1px solid black; font-size: 16px;")
        self.btn_4name.clicked.connect(self.openFileDialog4)

        self.graphics_load4 = QGraphicsView(self.widget)
        self.graphics_load4.move(180, 840)
        self.graphics_load4.resize(400,150)

        self.btn_4delete = QtWidgets.QPushButton(self.widget)
        self.btn_4delete.setText("Delete")
        self.btn_4delete.move(480, 800)
        self.btn_4delete.resize(100,30)
        self.btn_4delete.setStyleSheet("background-color: red; border: 1px solid black; font-size: 16px;")
        self.btn_4delete.clicked.connect(self.DeleteLoadedFiles4)
        





        self.btn_process = QtWidgets.QPushButton(self.widget)
        self.btn_process.setText("Process")
        self.btn_process.move( 1600 , 600)
        self.btn_process.resize(100,50)
        self.btn_process.clicked.connect(self.PROCESSING)

        self.btn_save = QtWidgets.QPushButton(self.widget)
        self.btn_save.setText("Save Graph")
        self.btn_save.move( 1600 , 660)
        self.btn_save.resize(100,50)
        self.btn_save.clicked.connect(self.saveDisplayedFigure)

        self.btn_savetex = QtWidgets.QPushButton(self.widget)
        self.btn_savetex.setText("Save Tex.")
        self.btn_savetex.move(1600, 720 )
        self.btn_savetex.resize( 100, 50)
        self.btn_savetex.clicked.connect(self.Save_file)

        self.btn_Ploting = QtWidgets.QPushButton(self.widget)
        self.btn_Ploting.setText("Graph")
        self.btn_Ploting.move(1000, 600)
        self.btn_Ploting.resize(100,50)
        self.btn_Ploting.clicked.connect(self.Ploting)

        self.btn_Expdata = QtWidgets.QPushButton(self.widget)
        self.btn_Expdata.setText("Input\nExperimental\nData")
        self.btn_Expdata.setStyleSheet("text-align: center;")
        self.btn_Expdata.move( 1120 , 600)
        self.btn_Expdata.resize(100,50)
        self.btn_Expdata.clicked.connect(self.openFileDialog5)
        
        self.btn_ClearExpdata = QtWidgets.QPushButton(self.widget)
        self.btn_ClearExpdata.setText("Clear\nExperimental\nData")
        self.btn_ClearExpdata.setStyleSheet("text-align: center;")
        self.btn_ClearExpdata.move( 1240 , 600)
        self.btn_ClearExpdata.resize(100,50)
        self.btn_ClearExpdata.clicked.connect(self.ClearingExpData)
        
        
        self.graphics_graph = QGraphicsView(self.widget)
        self.graphics_graph.move(1000,80)
        self.graphics_graph.resize(700,500)
        self.graphics_graph.setInteractive(True)
        
        
        
        
        
        
        
        
        
        
        
        
        self.Box = QComboBox(self.widget)
        self.Box.move(1000, 50)
        self.Box.addItem(f"Atom Probability {1}")
        self.Box.addItem(f"Atom MSD {1}")
        
 
        self.ChooseWhich = QComboBox(self.widget)
        self.ChooseWhich.move(1140, 50)
        self.ChooseWhich.addItem("Factor")
        self.ChooseWhich.addItem("x^2")
        self.ChooseWhich.addItem("y^2")
        self.ChooseWhich.addItem("z^2")

        
        self.box_colors = QComboBox(self.widget)
        self.box_colors.move(1210, 50)
        self.box_colors.addItem('Colors')
        self.box_colors.addItem('Black')
        self.box_colors.addItem('Red')
        self.box_colors.addItem('Green')
        self.box_colors.addItem('Blue')
        self.box_colors.addItem('Yellow')
        self.box_colors.addItem('Orange')
        self.box_colors.addItem('Purple')

        self.box_linestyle = QComboBox(self.widget)
        self.box_linestyle.move(1290,50)
        self.box_linestyle.addItem('Linestyle')
        self.box_linestyle.addItem('solid')
        self.box_linestyle.addItem('dashed')
        self.box_linestyle.addItem('dashdot')
        self.box_linestyle.addItem('dotted')
        
        
        
        
        self.box_linewidth = QComboBox(self.widget)
        self.box_linewidth.move(1375,50)
        self.box_linewidth.addItem('Linewidth')
        self.box_linewidth.addItem('1')
        self.box_linewidth.addItem('2')
        self.box_linewidth.addItem('3')
        self.box_linewidth.addItem('4')
        self.box_linewidth.addItem('5')
        self.box_linewidth.addItem('6')
        self.box_linewidth.addItem('7')
        self.box_linewidth.addItem('8')
        self.box_linewidth.addItem('9')
        self.box_linewidth.addItem('10')
        self.box_linewidth.addItem('11')
        self.box_linewidth.addItem('12')


        self.box_markers = QComboBox(self.widget)
        self.box_markers.move(1465, 50 )
        self.box_markers.addItem('Markers')
        self.box_markers.addItem('none')
        self.box_markers.addItem('Circle')
        self.box_markers.addItem('Square')
        self.box_markers.addItem('Triangle')

        self.box_resolution = QComboBox(self.widget)
        self.box_resolution.move(1548, 50 )
        self.box_resolution.addItem('Resolution')
        self.box_resolution.addItem('720x480')
        self.box_resolution.addItem('1280x720')
        self.box_resolution.addItem('1920x1080 ')





        
        self.scene_load1 = None
        self.scene_load2 = None
        self.scene_load3 = None
        self.scene_load4 = None

        self.graphics_graph.setScene(QGraphicsScene())

        
        
        
        
        self.setCentralWidget(self.scroll)

    def printlists(self):
        print(self.x_axis, self.y_axis)

    

    def open_documentation(self):
        pdf_file_path = "C:/Users/filip/Desktop/AV Fyzika program/Praktikum_5_oprava.pdf"  
        
        try:
            os.startfile(pdf_file_path)
        except Exception as e:
            print("Error:", e)
        
  
    
    
    def GenerateComboBox(self):
        self.Box.clear()
        n = self.atom_numbers[-1]
        for i in range(1, n  +1):
            self.Box.addItem(f"Atom Probability {i}")
            self.Box.addItem(f"Atom MSD {i}")
        self.Box.currentIndexChanged.connect(self.Choosing)
    
    def combo_box_selection_changed(self, index):
        self.display_figure(index)
  


    def openFileDialog1(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_names, _ = QFileDialog.getOpenFileNames(self, "Select Files for Upload", "", "All Files (*);;Text Files (*.txt)", options=options)
        

        
        double_files = []
        total_width = 0
        file_pos = 0
        
        if file_names:
            for file_name in file_names:
                if file_name not in self.loaded_files1: 
                    self.loaded_files1.append(file_name)
                    self.displayFileName(file_name, self.graphics_load1, file_pos)
                    file_pos += 20
                    for item in self.scene_load1.items():
                        if isinstance(item, QGraphicsTextItem):
                            item.setPos(0, file_pos)
                            file_pos += 20
                            for index, item in enumerate(self.scene_load1.items()):   
                                if isinstance(item, QGraphicsTextItem):
                                    item.setPos(0, index*20)
                        for item in self.scene_load1.items():
                            if isinstance(item, QGraphicsTextItem):
                                total_width += item.boundingRect().width()
                
                else: 
                    double_files.append(file_name)
                          
            
            
            if len(double_files) == 1:
                    QMessageBox.information(self, "File Already Loaded", f"The file '{double_files[0]}' is already loaded.")
            elif len(double_files) > 1:
                QMessageBox.information(
                    self, "Files Already Loaded", f"The following files are already loaded:\n{', '.join(double_files)}"
                    )             
            

            visible_horizontal = (self.graphics_load1.viewport().width() - self.graphics_load1.contentsMargins().left() - self.graphics_load1.contentsMargins().right()) // total_width
            visible_vertical = (self.graphics_load1.viewport().height() - self.graphics_load1.contentsMargins().top() - self.graphics_load1.contentsMargins().bottom())//10
            
            
            if len(self.loaded_files1) <= visible_vertical:
                self.graphics_load1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)   
            else:
                self.graphics_load1.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            if len(self.loaded_files1) <= visible_horizontal:
                self.graphics_load1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)   
            else:
                self.graphics_load1.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            
            self.graphics_load1.update()

        else:
            QMessageBox.information(self, "No Files Selected", "No files were selected.")

    def openFileDialog2(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_names, _ = QFileDialog.getOpenFileNames(self, "Select Files for Upload", "", "All Files (*);;Text Files (*.txt)", options=options)
        

        double_files = []
        total_width = 0
        file_pos = 0
        
        if file_names:
            for file_name in file_names:
                if file_name not in self.loaded_files2:  
                    self.loaded_files2.append(file_name)
                    self.displayFileName(file_name, self.graphics_load2, file_pos)
                    file_pos += 20
                    for item in self.scene_load2.items():
                        if isinstance(item, QGraphicsTextItem):
                            item.setPos(0, file_pos)
                            file_pos += 20
                            for index, item in enumerate(self.scene_load2.items()):     
                                if isinstance(item, QGraphicsTextItem):
                                    item.setPos(0, index*20)
                        for item in self.scene_load2.items():
                            if isinstance(item, QGraphicsTextItem):
                                total_width += item.boundingRect().width()
                
                else: 
                    double_files.append(file_name)
                          
            
            
            if len(double_files) == 1:
                    QMessageBox.information(self, "File Already Loaded", f"The file '{double_files[0]}' is already loaded.")
            elif len(double_files) > 1:
                QMessageBox.information(
                    self, "Files Already Loaded", f"The following files are already loaded:\n{', '.join(double_files)}"
                    )             
            

            visible_horizontal = (self.graphics_load2.viewport().width() - self.graphics_load2.contentsMargins().left() - self.graphics_load2.contentsMargins().right()) // total_width
            visible_vertical = (self.graphics_load2.viewport().height() - self.graphics_load2.contentsMargins().top() - self.graphics_load2.contentsMargins().bottom())//20
            
            
            if len(self.loaded_files2) <= visible_vertical:
                self.graphics_load2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)   
            else:
                self.graphics_load2.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            if len(self.loaded_files2) <= visible_horizontal:
                self.graphics_load2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)   
            else:
                self.graphics_load2.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            
            self.graphics_load2.update()

        else:
            QMessageBox.information(self, "No Files Selected", "No files were selected.")


    def openFileDialog3(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_names, _ = QFileDialog.getOpenFileNames(self, "Select Files for Upload", "", "All Files (*);;Text Files (*.txt)", options=options)
        

        
        double_files = []
        total_width = 0
        file_pos = 0
        
        if file_names:
            for file_name in file_names:
                if file_name not in self.loaded_files3:  
                    self.loaded_files3.append(file_name)
                    self.displayFileName(file_name, self.graphics_load3, file_pos)
                    file_pos += 20
                    for item in self.scene_load3.items():
                        if isinstance(item, QGraphicsTextItem):
                            item.setPos(0, file_pos)
                            file_pos += 20
                            for index, item in enumerate(self.scene_load3.items()):     
                                if isinstance(item, QGraphicsTextItem):
                                    item.setPos(0, index*20)
                        for item in self.scene_load3.items():
                            if isinstance(item, QGraphicsTextItem):
                                total_width += item.boundingRect().width()
                
                else: 
                    double_files.append(file_name)
                          
            
            
            if len(double_files) == 1:
                    QMessageBox.information(self, "File Already Loaded", f"The file '{double_files[0]}' is already loaded.")
            elif len(double_files) > 1:
                QMessageBox.information(
                    self, "Files Already Loaded", f"The following files are already loaded:\n{', '.join(double_files)}"
                    )             
            

            visible_horizontal = (self.graphics_load3.viewport().width() - self.graphics_load3.contentsMargins().left() - self.graphics_load3.contentsMargins().right()) // total_width
            visible_vertical = (self.graphics_load3.viewport().height() - self.graphics_load3.contentsMargins().top() - self.graphics_load3.contentsMargins().bottom())//20
            
            
            if len(self.loaded_files3) <= visible_vertical:
                self.graphics_load3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)   
            else:
                self.graphics_load3.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            if len(self.loaded_files3) <= visible_horizontal:
                self.graphics_load3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)   
            else:
                self.graphics_load3.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            
            self.graphics_load3.update()

        else:
            QMessageBox.information(self, "No Files Selected", "No files were selected.")

    def openFileDialog4(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_names, _ = QFileDialog.getOpenFileNames(self, "Select Files for Upload", "", "All Files (*);;Text Files (*.txt)", options=options)
        

        
        double_files = []
        total_width = 0
        file_pos = 0
        
        if file_names:
            for file_name in file_names:
                if file_name not in self.loaded_files4:  
                    self.loaded_files4.append(file_name)
                    self.displayFileName(file_name, self.graphics_load4, file_pos)
                    file_pos += 20
                    for item in self.scene_load4.items():
                        if isinstance(item, QGraphicsTextItem):
                            item.setPos(0, file_pos)
                            file_pos += 20
                            for index, item in enumerate(self.scene_load4.items()):    
                                if isinstance(item, QGraphicsTextItem):
                                    item.setPos(0, index*20)
                        for item in self.scene_load4.items():
                            if isinstance(item, QGraphicsTextItem):
                                total_width += item.boundingRect().width()
                
                else: 
                    double_files.append(file_name)
                          
            
            
            if len(double_files) == 1:
                    QMessageBox.information(self, "File Already Loaded", f"The file '{double_files[0]}' is already loaded.")
            elif len(double_files) > 1:
                QMessageBox.information(
                    self, "Files Already Loaded", f"The following files are already loaded:\n{', '.join(double_files)}"
                    )             
            

            visible_horizontal = (self.graphics_load4.viewport().width() - self.graphics_load4.contentsMargins().left() - self.graphics_load4.contentsMargins().right()) // total_width
            visible_vertical = (self.graphics_load4.viewport().height() - self.graphics_load4.contentsMargins().top() - self.graphics_load4.contentsMargins().bottom())//20
            
            
            if len(self.loaded_files4) <= visible_vertical:
                self.graphics_load4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)   
            else:
                self.graphics_load4.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            if len(self.loaded_files4) <= visible_horizontal:
                self.graphics_load4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)   
            else:
                self.graphics_load4.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            
            self.graphics_load4.update()

        else:
            QMessageBox.information(self, "No Files Selected", "No files were selected.")


    def openFileDialog5(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_names, _ = QFileDialog.getOpenFileNames(self, "Select Files for Upload", "", "All Files (*);;Text Files (*.txt)", options=options)
        double_files = []

   
        if file_names:
            for file_name in file_names:
                if len(self.loaded_files5) == 0:
                    if file_name not in self.loaded_files5:  
                        self.loaded_files5.append(file_name)
                    else:
                        double_files.append(file_name)
                elif len(self.loaded_files5) == 1:
                    QMessageBox.information(self,"File Already Loaded", f"The file '{self.loaded_files5[0]}' is loaded. Clear experimental data for further use.")
                else:
                    self.loaded_files5.clear()
        
        
        
        if len(double_files) == 1:
            QMessageBox.information(self, "File Already Loaded", f"The file '{double_files[0]}' is loaded. Can not load the same file twice.")
        elif len(double_files) > 1:
            return
        self.OpenExperimentalData()
    
    def OpenExperimentalData(self):
        for file_name in self.loaded_files5:
            with open(file_name, 'r') as data:        
                for line in data:
                    p = line.split()
                    self.xAxis.append(float(p[0]))
                    self.yAxis.append(float(p[1]))
        print(self.xAxis)
        print(self.yAxis)

    def ClearingExpData(self):
        self.loaded_files5.clear()
        self.xAxis.clear()
        self.yAxis.clear()

        
    def displayMatplotlibFigure(self, figure):
    
        self.graphics_graph.scene().clear()

        
        canvas = FigureCanvas(figure)

        
        scene = QGraphicsScene()
        scene.addWidget(canvas)

        
        self.graphics_graph.setScene(scene)

        
        self.graphics_graph.show()








    def displayFileName(self, file_name, graphics_view, file_pos):
        if graphics_view == self.graphics_load1 and self.scene_load1 is None:
            self.scene_load1 = QGraphicsScene()
            self.graphics_load1.setScene(self.scene_load1)

        if graphics_view == self.graphics_load2 and self.scene_load2 is None:
            self.scene_load2 = QGraphicsScene()
            self.graphics_load2.setScene(self.scene_load2)

        if graphics_view == self.graphics_load3 and self.scene_load3 is None:
            self.scene_load3 = QGraphicsScene()
            self.graphics_load3.setScene(self.scene_load3)

        if graphics_view == self.graphics_load4 and self.scene_load4 is None:
            self.scene_load4 = QGraphicsScene()
            self.graphics_load4.setScene(self.scene_load4)

        scene = graphics_view.scene()

        graphics_view.setInteractive(True)
        graphics_view.setScene(scene)
        
        
        
        text_item = ClickableTextItem(file_name)
      
        if graphics_view == self.graphics_load1 and text_item not in self.text_item1:
            self.text_item1.append(text_item)
            scene.addItem(text_item)

            index = scene.items().index(text_item)
            text_item.setPos(0, index + file_pos)  

            text_item.setFlag(QGraphicsTextItem.ItemIsSelectable, True)
            text_item.setFlag(QGraphicsTextItem.ItemIsFocusable, True)
            text_item.setAcceptHoverEvents(True)

        if graphics_view == self.graphics_load2 and text_item not in self.text_item2:
            self.text_item2.append(text_item)
            scene.addItem(text_item)

            index = scene.items().index(text_item)
            text_item.setPos(0, index + file_pos) 

            text_item.setFlag(QGraphicsTextItem.ItemIsSelectable, True)
            text_item.setFlag(QGraphicsTextItem.ItemIsFocusable, True)
            text_item.setAcceptHoverEvents(True)
        
        if graphics_view == self.graphics_load3 and text_item not in self.text_item3:
            self.text_item3.append(text_item)
            scene.addItem(text_item)
            
            index = scene.items().index(text_item)
            text_item.setPos(0, index + file_pos) 

            text_item.setFlag(QGraphicsTextItem.ItemIsSelectable, True)
            text_item.setFlag(QGraphicsTextItem.ItemIsFocusable, True)
            text_item.setAcceptHoverEvents(True)
        
        if graphics_view == self.graphics_load4 and text_item not in self.text_item4:
            self.text_item4.append(text_item)
            scene.addItem(text_item)

            index = scene.items().index(text_item)
            text_item.setPos(0, index + file_pos)  
            text_item.setFlag(QGraphicsTextItem.ItemIsSelectable, True)
            text_item.setFlag(QGraphicsTextItem.ItemIsFocusable, True)
            text_item.setAcceptHoverEvents(True)





        if graphics_view == self.graphics_load1:
            self.text_item1.append(text_item)



        if graphics_view == self.graphics_load2:
            self.text_item2.append(text_item)


        if graphics_view == self.graphics_load3:
            self.text_item3.append(text_item)


        if graphics_view == self.graphics_load4:
            self.text_item4.append(text_item)
        
    
    
    
    
    def DeleteLoadedFiles1(self):
        if not self.loaded_files1:
            QMessageBox.information(self, "No Files Loaded", "No files have been loaded yet.")
            return
        reply = QMessageBox.question(self, "Delete Files", "Are you sure you want to delete the selected files?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            selected_items = self.scene_load1.selectedItems()
            total_width = 0

            if selected_items:
                file_pos = 0
                for item in selected_items:     
                    file_name = item.toPlainText()
                    self.loaded_files1.remove(file_name)
                    self.text_item1.remove(item)

                    self.scene_load1.removeItem(item)
                    
                file_pos = 0
                for item in self.scene_load1.items(): 
                    if isinstance(item, QGraphicsTextItem):
                        item.setPos(0, file_pos)
                        file_pos += 20
                        total_width += item.boundingRect().width()
                        self.scene_load1.setSceneRect(self.scene_load1.itemsBoundingRect())
                QMessageBox.information(
                    self, "Files Deleted", "Selected files have been deleted."
                )

            else:
                self.scene_load1.clear()
                self.loaded_files1.clear()
                QMessageBox.information(
                    self, "Files Deleted", "All files have been deleted."
                )
                self.loaded_files1.sort()
                
        
        visible_horizontal = 0
        if total_width != 0:
            visible_horizontal = (self.graphics_load1.viewport().width() - self.graphics_load1.contentsMargins().left() - self.graphics_load1.contentsMargins().right()) // total_width
        else:
            visible_horizontal = (self.graphics_load1.viewport().width() - self.graphics_load1.contentsMargins().left() - self.graphics_load1.contentsMargins().right())//1
            
            
            visible_vertical = (self.graphics_load1.viewport().height() - self.graphics_load1.contentsMargins().top() - self.graphics_load1.contentsMargins().bottom())//20
            
            
            if len(self.loaded_files1) <= visible_vertical:
                self.graphics_load1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)   
            else:
                self.graphics_load1.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            if len(self.loaded_files1) <= visible_horizontal:
                self.graphics_load1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)   
            else:
                self.graphics_load1.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            
            self.graphics_load1.update()          
    
    
    def DeleteLoadedFiles2(self):
        if not self.loaded_files2:
            QMessageBox.information(self, "No Files Loaded", "No files have been loaded yet.")
            return
        reply = QMessageBox.question(self, "Delete Files", "Are you sure you want to delete the selected files?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            selected_items = self.scene_load2.selectedItems()
            total_width = 0

            if selected_items:
                file_pos = 0
                for item in selected_items:    
                    file_name = item.toPlainText()
                    self.loaded_files2.remove(file_name)
                    self.text_item2.remove(item)

                    self.scene_load2.removeItem(item)
                    
                file_pos = 0
                for item in self.scene_load2.items(): 
                    if isinstance(item, QGraphicsTextItem):
                        item.setPos(0, file_pos)
                        file_pos += 20
                        total_width += item.boundingRect().width()
                        self.scene_load2.setSceneRect(self.scene_load2.itemsBoundingRect())
                QMessageBox.information(

                    self, "Files Deleted", "Selected files have been deleted."
                )

            else:
                self.scene_load2.clear()
                self.loaded_files2.clear()
                QMessageBox.information(
                    self, "Files Deleted", "All files have been deleted."
                )
                self.loaded_files2.sort()
        
        visible_horizontal = 0
        if total_width != 0:
            visible_horizontal = (self.graphics_load2.viewport().width() - self.graphics_load2.contentsMargins().left() - self.graphics_load2.contentsMargins().right()) // total_width
        else:
            visible_horizontal = (self.graphics_load2.viewport().width() - self.graphics_load2.contentsMargins().left() - self.graphics_load2.contentsMargins().right())//1
            
            
            visible_vertical = (self.graphics_load2.viewport().height() - self.graphics_load2.contentsMargins().top() - self.graphics_load2.contentsMargins().bottom())//20
            
            
            if len(self.loaded_files2) <= visible_vertical:
                self.graphics_load2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)   
            else:
                self.graphics_load2.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            if len(self.loaded_files2) <= visible_horizontal:
                self.graphics_load2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)   
            else:
                self.graphics_load2.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            
            self.graphics_load2.update()         

    
    
    def DeleteLoadedFiles3(self):
        if not self.loaded_files3:
            QMessageBox.information(self, "No Files Loaded", "No files have been loaded yet.")
            return
        reply = QMessageBox.question(self, "Delete Files", "Are you sure you want to delete the selected files?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            selected_items = self.scene_load3.selectedItems()
            total_width = 0 
            
            if selected_items:
                file_pos = 0
                for item in selected_items:    
                    file_name = item.toPlainText()
                    self.loaded_files3.remove(file_name)
                    self.text_item3.remove(item)

                    self.scene_load3.removeItem(item)
                    
                file_pos = 0
                for item in self.scene_load3.items():
                    if isinstance(item, QGraphicsTextItem):
                        item.setPos(0, file_pos)
                        file_pos += 20
                        total_width += item.boundingRect().width()
                        self.scene_load3.setSceneRect(self.scene_load3.itemsBoundingRect())
                QMessageBox.information(
                    self, "Files Deleted", "Selected files have been deleted."
                )

            else:
                self.scene_load3.clear()
                self.loaded_files3.clear()
                QMessageBox.information(
                    self, "Files Deleted", "All files have been deleted."
                )
                self.loaded_files3.sort()
                
        visible_horizontal = 0
        if total_width != 0:
            visible_horizontal = (self.graphics_load3.viewport().width() - self.graphics_load3.contentsMargins().left() - self.graphics_load3.contentsMargins().right()) // total_width
        else:
            visible_horizontal = (self.graphics_load3.viewport().width() - self.graphics_load3.contentsMargins().left() - self.graphics_load3.contentsMargins().right())//1
            
            
            visible_vertical = (self.graphics_load3.viewport().height() - self.graphics_load3.contentsMargins().top() - self.graphics_load3.contentsMargins().bottom())//20
            
            
            if len(self.loaded_files3) <= visible_vertical:
                self.graphics_load3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)   
            else:
                self.graphics_load3.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            if len(self.loaded_files3) <= visible_horizontal:
                self.graphics_load3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)   
            else:
                self.graphics_load3.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            
            self.graphics_load3.update()         




    def DeleteLoadedFiles4(self):

        
        if not self.loaded_files4:
            QMessageBox.information(self, "No Files Loaded", "No files have been loaded yet.")
            return
        reply = QMessageBox.question(self, "Delete Files", "Are you sure you want to delete the selected files?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            selected_items = self.scene_load4.selectedItems()
            total_width = 0 
            
            
            
            if selected_items:
                file_pos = 0
                for item in selected_items:     
                    file_name = item.toPlainText()
                    self.loaded_files4.remove(file_name)
                    self.text_item4.remove(item)

                    self.scene_load4.removeItem(item)
                    
                file_pos = 0
                for item in self.scene_load4.items():
                    if isinstance(item, QGraphicsTextItem):
                        item.setPos(0, file_pos)
                        file_pos += 20    
                        total_width += item.boundingRect().width()
                        self.scene_load4.setSceneRect(self.scene_load4.itemsBoundingRect())
                QMessageBox.information(
                    self, "Files Deleted", "Selected files have been deleted."
                )
            
            else:
                self.scene_load4.clear()
                self.loaded_files4.clear()
                QMessageBox.information(
                    self, "Files Deleted", "All files have been deleted."
                )
                self.loaded_files4.sort()
               
            visible_horizontal = 0
        if total_width != 0:
            visible_horizontal = (self.graphics_load4.viewport().width() - self.graphics_load4.contentsMargins().left() - self.graphics_load4.contentsMargins().right()) // total_width
        else:
            visible_horizontal = (self.graphics_load4.viewport().width() - self.graphics_load4.contentsMargins().left() - self.graphics_load4.contentsMargins().right())//1
            
            
            visible_vertical = (self.graphics_load4.viewport().height() - self.graphics_load4.contentsMargins().top() - self.graphics_load4.contentsMargins().bottom())//20
            
            
            if len(self.loaded_files4) <= visible_vertical:
                self.graphics_load4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)   
            else:
                self.graphics_load4.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            if len(self.loaded_files4) <= visible_horizontal:
                self.graphics_load4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)   
            else:
                self.graphics_load4.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            
            self.graphics_load4.update()


    def saveDisplayedFigure(self):
       
        current_figure = self.graphics_graph.scene().items()[0].widget().figure

    
        file_dialog = QtWidgets.QFileDialog(self)
        file_dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
        file_dialog.setNameFilter("PNG Files (*.png);;All Files (*)")
        if file_dialog.exec_():
            selected_file = file_dialog.selectedFiles()[0]
            current_figure.savefig(selected_file, format='png')


    def ev_volume(self):            
        if not self.loaded_files4:
            return                         
        file_name = self.loaded_files4[0] 
        with open(file_name, 'r') as data:
            for line in data:
                p = line.split()
                self.ev_vol_list.append(float(p[0]))

        


    def temp_vol(self):
        if not self.loaded_files3:
            return
        for file_names in self.loaded_files3:
            with open(file_names, 'r') as data:
                for line in data:
                    p = line.split()
                    self.temp_list.append(float(p[0]))
                    self.volume_list.append(float(p[1]))
        
    def real_temperature(self):
        if not self.loaded_files3:
            return
        self.real_temp = [0] * len(self.ev_vol_list)
        interpol = interpolate.interp1d(self.volume_list, self.temp_list, kind = "linear")
        for n in range(0,len(self.ev_vol_list)):
            self.real_temp[n] = interpol(self.ev_vol_list[n])




    def Cleaning(self):
            if not self.loaded_files4 and not self.loaded_files3:
                for  file_name in self.loaded_files2: 
                    infile = file_name
                    outfile = "cleaned"  + ".txt"
                    paths_outfile = os.path.abspath(outfile)
                    with open(infile) as fin, open(outfile, "w+") as fout:
                        lines = fin.readlines()
                        for i in range(len(lines)):     
                            if lines[i][0:5] == "  - [":
                                fout.writelines(lines[i][7:40] + "\n")
                    
                    self.outfile.append(paths_outfile)
                    self.outfile_names.append(paths_outfile)


            else:    
                for  file_name in self.loaded_files2: 
                    infile = file_name
                    outfile = "cleaned_" + file_name.split("yaml-")[1] + ".txt"
                    paths_outfile = os.path.abspath(outfile)
                    with open(infile) as fin, open(outfile, "w+") as fout:
                        lines = fin.readlines()
                        for i in range(len(lines)):     
                            if lines[i][0:5] == "  - [":
                                fout.writelines(lines[i][7:40] + "\n")
                    
                    self.outfile.append(paths_outfile)
                    self.outfile_names.append(paths_outfile)
                self.outfile.sort(key=self.get_sort_key)


    
    def get_sort_key(self, filename):
        match = re.search(r'cleaned_(-?\d+)', filename)
        if match:
            return int(match.group(1))
        return 0

    
    




        
        


    def DeletingCleanedFiles(self):
        if not self.outfile:
            return

 

        for file_names in self.files_to_delete:
            os.remove(file_names)
        
        self.outfile.clear()
    
    def Msd(self):
        for file_names in self.outfile:
            mx = [] 
            my = []
            mz = []
            
            with open(file_names, 'r') as data:
                for line in data:
                    p = line.split(",")
                    mx.append(float(p[0]))
                    my.append(float(p[1]))
                    mz.append(float(p[2]))
                    
            self.data_list.append([mx, my, mz]) 
             

    
    def Msd_interpol(self):
        natom = len(self.atom_masses)
        t = [float(np_scalar) for np_scalar in self.real_temp]
        i = 1
        for i in range(1 ,int(len(self.atom_masses)+1)):
            mx2 = []
            mz2 = []
            my2 = []
            
            for n in range(0, len(self.real_temp), 1):
                t_0 = math.trunc(t[n] / 10)*natom + i - 1 
                t_1 = t_0 + natom
                
                interpolx = [self.data_list[n][0][t_0], self.data_list[n][0][t_1]]
                interpoly = [self.data_list[n][1][t_0], self.data_list[n][1][t_1]]
                interpolz = [self.data_list[n][2][t_0], self.data_list[n][2][t_1]]

                boundary_temp = [math.trunc(t[n]/10)*10, math.trunc(t[n]/10)*10 + 10]

                fx = interpolate.interp1d(boundary_temp, interpolx, kind="linear")
                x = fx(t[n])

                fy = interpolate.interp1d(boundary_temp, interpoly, kind="linear")
                y = fy(t[n])

                fz = interpolate.interp1d(boundary_temp, interpolz, kind="linear")
                z = fz(t[n])
                mx2.append(x)
                my2.append(y)
                mz2.append(z)
            
            self.mx1.append(mx2)
            self.mz1.append(mz2)
            self.my1.append(my2)
       
      
        
    def count_values_smaller_than_first(self):
        first_vol = self.volume_list[0]
        count = 0

        for value in self.ev_vol_list:
            if value < first_vol:
                count += 1
     
        self.count.append(count)   

    
    def Removing(self):
        
        self.ev_vol_list = self.ev_vol_list[int(self.count[0]):]   
        self.outfile = self.outfile[int(self.count[0]):]

    
    def Mfactor(self):
        if not self.loaded_files3 and not self.loaded_files4:
            
            for i in range(1,int(len(self.atom_masses)+1)):
                atomic_number = self.atom_masses[int(i-1)]
                Er = self.Er_const_list[int(i-1)] * con.eV

                m = atomic_number * con.atomic_mass
                Eg_squared = 2 * m * con.c * con.c * Er
                d1 = Eg_squared / (con.c * con.hbar * con.c * con.hbar)
                factor_list = [] 
                for u in range(0, len(self.sing_temperature)):
                    f = math.exp(-(self.mx1[int(i-1)][u] + 0.5 * (self.mz1[int(i-1)][u] - self.mx1[int(i-1)][u] + self.mz1[int(i-1)][u] - self.my1[int(i-1)][u])) * d1 * 1.0e-20)
                    if f == 1:
                        factor_list.append(0)    
                    else:
                        factor_list.append(f)
                self.factor_list.append(factor_list)
        
        else:
            i = 1
            for i in range(1,int(len(self.atom_masses)+1)):
                atomic_number = self.atom_masses[int(i-1)]
                Er = self.Er_const_list[int(i-1)] * con.eV

                m = atomic_number * con.atomic_mass
                Eg_squared = 2 * m * con.c * con.c * Er
                d1 = Eg_squared / (con.c * con.hbar * con.c * con.hbar)
                factor_list = []  
                for u in range(0, len(self.real_temp)):
                    f = math.exp(-(self.mx1[int(i-1)][u] + 0.5 * (self.mz1[int(i-1)][u] - self.mx1[int(i-1)][u]+ self.mz1[int(i-1)][u] - self.my1[int(i-1)][u] )) * d1 * 1.0e-20)
                    factor_list.append(f)
                self.factor_list.append(factor_list)  
          
    def get_atom_info(self):
        for file_name in self.loaded_files1:
            with open(file_name, "r") as file:
                content = file.read()

            start_index = content.find("primitive_cell:")
            end_index = content.find("reciprocal_lattice:")
            segment = content[start_index:end_index]

            atom_info = re.findall(r"symbol: (\w+) # (\d+)\s+coordinates: .*?\n\s+mass: ([\d.]+)", segment, re.DOTALL)

        

            for symbol, atom_number, mass in atom_info:
                self.atom_names.append(symbol)
                self.atom_numbers.clear()
                self.atom_numbers.append(int(atom_number))
                self.atom_masses.append(float(mass))


    def map_names_to_numbers(self):
        elements = {"Fe": 1.95883310e-03,
        "I": 3.218e-03,
        "Sn": 2.57423e-3,
        "Sb": 6.122e-03,
        "Ir": 1.9094e-02}
        for name in self.atom_names:
            if name in elements:
                self.Er_const_list.append(elements[name])
            else:
                self.Er_const_list.append((0))




     
    def extract_temperatures(self):
        for file_names in self.loaded_files2:
            with open(file_names, 'r') as file:
                    for line in file:
                        
                        match = re.search(r'temperature:\s+([\d.]+)', line)
                        if match:
                          
                            temperature = float(match.group(1))
                            self.sing_temperature.append(temperature)
        
    
   

   
   
   
    def sing_Msd_interpol(self):
        natom = len(self.atom_masses)
        t = [float(np_scalar) for np_scalar in self.sing_temperature]
        
        for i in range(0 ,int(len(self.atom_masses))):
            mx2 = []
            mz2 = []
            my2 = []
            
            for n in range(0, len(self.sing_temperature)):
                t_0 = math.trunc(t[n] / 10)*natom + i
                
                mx2.append(self.data_list[0][0][t_0])
                my2.append(self.data_list[0][1][t_0])
                mz2.append(self.data_list[0][2][t_0])
            
            self.mx1.append(mx2)
            self.mz1.append(mz2)
            self.my1.append(my2)
   
   
   
  
   
   
   
   
    def get_selected_resolution(self):
        selected_resolution_index = self.box_resolution.currentIndex()
        selected_resolution = self.box_resolution.itemText(selected_resolution_index)
        
        if selected_resolution == 'Resolution':
            return {'figsize': (6.4, 3.8), 'dpi': 100}
        elif selected_resolution == '720x480':
            return {'figsize': (7.2, 4.8), 'dpi': 100}
        elif selected_resolution == '1280x720':
            return {'figsize': (12.8, 7.2), 'dpi': 100}
        else:
            return {'figsize': (19.2, 10.8), 'dpi': 100}
    
    
    
    
    def get_selected_color(self):
        selected_color_index = self.box_colors.currentIndex()
        selected_color = self.box_colors.itemText(selected_color_index)
        
        if selected_color != 'Colors':
            return {'color': selected_color}
        else:
            return {'color': 'black'}
    
    
    def get_linestyle(self):
        selected_linestyle_index = self.box_linestyle.currentIndex()
        selected_linestyle = self.box_linestyle.itemText(selected_linestyle_index)

        if selected_linestyle != 'Linestyle':
            return {'linestyle' : selected_linestyle}
        else:     
            return {'linestyle' : 'solid'}
    
    def get_markers(self):
        selected_markers_index = self.box_markers.currentIndex()
        selected_markers = self.box_markers.itemText(selected_markers_index)

        if selected_markers == 'Circle':
            return {'marker' : 'o' }
        elif selected_markers == 'Triangle':
            return {'marker' : '^' }
        elif selected_markers == 'Square':
            return {'marker' : 's' }   
        else:
            return {'marker' : None }
        
    def get_linewidth(self):
        selected_width_index = self.box_linewidth.currentIndex()
        selected_width = self.box_linewidth.itemText(selected_width_index)

        if selected_width != 'Linewidth':
            selected_width_converted = float(selected_width)
            return {'linewidth' : selected_width_converted}
        else:     
            return {'linewidth' : 1.0}
    
        
    
    
    
    def generate_graph(self):
        if not self.loaded_files5:
            if not self.loaded_files3 and not self.loaded_files4:    
                selected_ChooseWhich_index = self.ChooseWhich.currentIndex()
                selected_ChooseWhich = self.ChooseWhich.itemText(selected_ChooseWhich_index)

                resolution_settings = self.get_selected_resolution()
                if selected_ChooseWhich == 'Factor':
                    self.factor_stored_kwargs_f.clear()
                    self.factor_stored_kwargs_f.update(**self.get_selected_color(), **self.get_linestyle(), **self.get_markers(), **self.get_linewidth())
                elif selected_ChooseWhich == 'x^2':
                    self.mx1_stored_kwargs.clear()
                    self.mx1_stored_kwargs.update(**self.get_selected_color(), **self.get_linestyle(), **self.get_markers(), **self.get_linewidth())
                elif selected_ChooseWhich == 'y^2':
                    self.my1_stored_kwargs.clear()
                    self.my1_stored_kwargs.update(**self.get_selected_color(), **self.get_linestyle(), **self.get_markers(), **self.get_linewidth())
                elif selected_ChooseWhich == 'z^2':
                    self.mz1_stored_kwargs.clear()
                    self.mz1_stored_kwargs.update(**self.get_selected_color(), **self.get_linestyle(), **self.get_markers(), **self.get_linewidth())
                else:
                    return
                i= 1
                for i in range(1,len(self.atom_masses)+1):
                    fig1, ax = plt.subplots(figsize=resolution_settings['figsize'], dpi=resolution_settings['dpi'])  
                    ax.plot(self.sing_temperature, self.factor_list[int(i-1)], **self.factor_stored_kwargs_f)
                    ax.set_xlabel('T[K]')  
                    ax.set_ylabel('f') 
                    ax.set_title(f'Mossbauser factor for {self.atom_names[int(i-1)]}')  
                    ax.grid(False)  
                    ax.legend(['Factor'])
                    self.generated_graphs_factor.append(fig1)
                    
                    
                    fig2, ax = plt.subplots(figsize=resolution_settings['figsize'], dpi=resolution_settings['dpi'])
                    ax.plot(self.sing_temperature, self.mx1[int(i-1)], **self.mx1_stored_kwargs )
                    ax.plot(self.sing_temperature, self.mz1[int(i-1)], **self.mz1_stored_kwargs )
                    ax.plot(self.sing_temperature, self.my1[int(i-1)], **self.my1_stored_kwargs )
                    ax.set_xlabel('T[K]')  
                    ax.set_ylabel('MSD')  
                    ax.set_title(f'MSD for {self.atom_names[int(i-1)]}')  
                    ax.grid(False)  
                    ax.legend(['MSD of X','MSD of Z','MSD of Y'])
                    self.generated_graphs_mi1.append(fig2)
                
           
                
                
                selected_ChooseWhich_index = self.ChooseWhich.currentIndex()
                selected_ChooseWhich = self.ChooseWhich.itemText(selected_ChooseWhich_index)
            
            
            
            
            
            else:
                selected_ChooseWhich_index = self.ChooseWhich.currentIndex()
                selected_ChooseWhich = self.ChooseWhich.itemText(selected_ChooseWhich_index)

                resolution_settings = self.get_selected_resolution()
                if selected_ChooseWhich == 'Factor':
                    self.factor_stored_kwargs_f.clear()
                    self.factor_stored_kwargs_f.update(**self.get_selected_color(), **self.get_linestyle(), **self.get_markers(), **self.get_linewidth())
                elif selected_ChooseWhich == 'x^2':
                    self.mx1_stored_kwargs.clear()
                    self.mx1_stored_kwargs.update(**self.get_selected_color(), **self.get_linestyle(), **self.get_markers(), **self.get_linewidth())
                elif selected_ChooseWhich == 'y^2':
                    self.my1_stored_kwargs.clear()
                    self.my1_stored_kwargs.update(**self.get_selected_color(), **self.get_linestyle(), **self.get_markers(), **self.get_linewidth())
                elif selected_ChooseWhich == 'z^2':
                    self.mz1_stored_kwargs.clear()
                    self.mz1_stored_kwargs.update(**self.get_selected_color(), **self.get_linestyle(), **self.get_markers(), **self.get_linewidth())
                else:
                    return
                i= 1
                for i in range(1,len(self.atom_masses)+1):
                    fig1, ax = plt.subplots(figsize=resolution_settings['figsize'], dpi=resolution_settings['dpi'])  
                    ax.plot(self.real_temp, self.factor_list[int(i-1)], **self.factor_stored_kwargs_f)
                    ax.set_xlabel('T[K]') 
                    ax.set_ylabel('f') 
                    ax.set_title(f'Mossbauser factor for {self.atom_names[int(i-1)]}') 
                    ax.grid(False)
                    ax.legend(['Factor']) 
                    self.generated_graphs_factor.append(fig1)
                    
                    
                    fig2, ax = plt.subplots(figsize=resolution_settings['figsize'], dpi=resolution_settings['dpi'])
                    ax.plot(self.real_temp, self.mx1[int(i-1)], **self.mx1_stored_kwargs )
                    ax.plot(self.real_temp, self.mz1[int(i-1)], **self.mz1_stored_kwargs )
                    ax.plot(self.real_temp, self.my1[int(i-1)], **self.my1_stored_kwargs )
                    ax.set_xlabel('T[K]')  
                    ax.set_ylabel('MSD') 
                    ax.set_title(f'MSD for {self.atom_names[int(i-1)]}')  
                    ax.grid(False)  
                    ax.legend(['MSD of X','MSD of Z','MSD of Y'])
                    self.generated_graphs_mi1.append(fig2)
                
   
                
                
                selected_ChooseWhich_index = self.ChooseWhich.currentIndex()
                selected_ChooseWhich = self.ChooseWhich.itemText(selected_ChooseWhich_index)
        else:
            if not self.loaded_files3 and not self.loaded_files4:    
                selected_ChooseWhich_index = self.ChooseWhich.currentIndex()
                selected_ChooseWhich = self.ChooseWhich.itemText(selected_ChooseWhich_index)

                resolution_settings = self.get_selected_resolution()
                if selected_ChooseWhich == 'Factor':
                    self.factor_stored_kwargs_f.clear()
                    self.factor_stored_kwargs_f.update(**self.get_selected_color(), **self.get_linestyle(), **self.get_markers(), **self.get_linewidth())
                elif selected_ChooseWhich == 'x^2':
                    self.mx1_stored_kwargs.clear()
                    self.mx1_stored_kwargs.update(**self.get_selected_color(), **self.get_linestyle(), **self.get_markers(), **self.get_linewidth())
                elif selected_ChooseWhich == 'y^2':
                    self.my1_stored_kwargs.clear()
                    self.my1_stored_kwargs.update(**self.get_selected_color(), **self.get_linestyle(), **self.get_markers(), **self.get_linewidth())
                elif selected_ChooseWhich == 'z^2':
                    self.mz1_stored_kwargs.clear()
                    self.mz1_stored_kwargs.update(**self.get_selected_color(), **self.get_linestyle(), **self.get_markers(), **self.get_linewidth())
                else:
                    return
                i= 1
                for i in range(1,len(self.atom_masses)+1):
                    fig1, ax = plt.subplots(figsize=resolution_settings['figsize'], dpi=resolution_settings['dpi'])  
                    ax.plot(self.sing_temperature, self.factor_list[int(i-1)], **self.factor_stored_kwargs_f)  
                    ax.plot(self.xAxis, self.yAxis, marker='+', linestyle='None', markersize=10, color='b', label='Experimental results')
                    ax.set_xlabel('T[K]') 
                    ax.set_ylabel('f') 
                    ax.set_title(f'Mossbauser factor for {self.atom_names[int(i-1)]}')  
                    ax.grid(False)  
                    ax.legend(['Factor'])
                    self.generated_graphs_factor.append(fig1)
                    
                    
                    fig2, ax = plt.subplots(figsize=resolution_settings['figsize'], dpi=resolution_settings['dpi'])
                    ax.plot(self.sing_temperature, self.mx1[int(i-1)], **self.mx1_stored_kwargs )
                    ax.plot(self.sing_temperature, self.mz1[int(i-1)], **self.mz1_stored_kwargs )
                    ax.plot(self.sing_temperature, self.my1[int(i-1)], **self.my1_stored_kwargs )
                    ax.set_xlabel('T[K]')
                    ax.set_ylabel('MSD') 
                    ax.set_title(f'MSD for {self.atom_names[int(i-1)]}')  
                    ax.grid(False)  
                    ax.legend(['MSD of X','MSD of Z','MSD of Y'])
                    self.generated_graphs_mi1.append(fig2)
                
             
                
                
                selected_ChooseWhich_index = self.ChooseWhich.currentIndex()
                selected_ChooseWhich = self.ChooseWhich.itemText(selected_ChooseWhich_index)
            
            
            
            
            
            else:
                selected_ChooseWhich_index = self.ChooseWhich.currentIndex()
                selected_ChooseWhich = self.ChooseWhich.itemText(selected_ChooseWhich_index)

                resolution_settings = self.get_selected_resolution()
                if selected_ChooseWhich == 'Factor':
                    self.factor_stored_kwargs_f.clear()
                    self.factor_stored_kwargs_f.update(**self.get_selected_color(), **self.get_linestyle(), **self.get_markers(), **self.get_linewidth())
                elif selected_ChooseWhich == 'x^2':
                    self.mx1_stored_kwargs.clear()
                    self.mx1_stored_kwargs.update(**self.get_selected_color(), **self.get_linestyle(), **self.get_markers(), **self.get_linewidth())
                elif selected_ChooseWhich == 'y^2':
                    self.my1_stored_kwargs.clear()
                    self.my1_stored_kwargs.update(**self.get_selected_color(), **self.get_linestyle(), **self.get_markers(), **self.get_linewidth())
                elif selected_ChooseWhich == 'z^2':
                    self.mz1_stored_kwargs.clear()
                    self.mz1_stored_kwargs.update(**self.get_selected_color(), **self.get_linestyle(), **self.get_markers(), **self.get_linewidth())
                else:
                    return
                i= 1
                for i in range(1,len(self.atom_masses)+1):
                    fig1, ax = plt.subplots(figsize=resolution_settings['figsize'], dpi=resolution_settings['dpi'])  
                    ax.plot(self.real_temp, self.factor_list[int(i-1)], **self.factor_stored_kwargs_f)
                    ax.plot(self.xAxis, self.yAxis, marker='+', linestyle='None', markersize=10, color='b', label='Experimental results')
                    ax.set_xlabel('T[K]') 
                    ax.set_ylabel('f') 
                    ax.set_title(f'Mossbauser factor for {self.atom_names[int(i-1)]}') 
                    ax.grid(False) 
                    ax.legend(['Factor']) 
                    self.generated_graphs_factor.append(fig1)
                    
                    
                    fig2, ax = plt.subplots(figsize=resolution_settings['figsize'], dpi=resolution_settings['dpi'])
                    ax.plot(self.real_temp, self.mx1[int(i-1)], **self.mx1_stored_kwargs )
                    ax.plot(self.real_temp, self.mz1[int(i-1)], **self.mz1_stored_kwargs )
                    ax.plot(self.real_temp, self.my1[int(i-1)], **self.my1_stored_kwargs )
                    ax.set_xlabel('T[K]') 
                    ax.set_ylabel('MSD')  
                    ax.set_title(f'MSD for {self.atom_names[int(i-1)]}')  
                    ax.grid(False) 
                    ax.legend(['MSD of X','MSD of Z','MSD of Y'])
                    self.generated_graphs_mi1.append(fig2)
                
              
                
                
                selected_ChooseWhich_index = self.ChooseWhich.currentIndex()
                selected_ChooseWhich = self.ChooseWhich.itemText(selected_ChooseWhich_index)
        

        
    
    
    
    
    
    
     
    def Choosing(self, index):
        selected_text = self.Box.currentText()

        if "Atom Probability" in selected_text:
            atom_type = "Atom Probability"
        elif "Atom MSD" in selected_text:
            atom_type = "Atom MSD"
        else:
            atom_type = None
        
        if atom_type:
            selected_value = int(selected_text[-2:])
            self.i = selected_value
            if atom_type == "Atom Probability":
                self.handleAtomProbability(selected_value)
            elif atom_type == "Atom MSD":
                self.handleAtomMSD(selected_value)
        
    def handleAtomProbability(self, value):
        if 1 <= value <= len(self.generated_graphs_factor):
            self.displayMatplotlibFigure(self.generated_graphs_factor[int(value)-1])
        else:
            return

    def handleAtomMSD(self, value):
        if 1 <= value <= len(self.generated_graphs_mi1):       

                self.displayMatplotlibFigure(self.generated_graphs_mi1[int(value)-1])
        else:
            return
    
    
    def Ploting(self):
        self.generated_graphs_mi1.clear()
        self.generated_graphs_factor.clear()
        self.generate_graph()
        self.Choosing(self.i)

    

    

    
    def copyfiles(self):
        self.files_to_delete = self.outfile.copy()         
    
    
    
    
    def Save_file(self):

        if not self.loaded_files3 and not self.loaded_files4:
            temperature = self.sing_temperature
        else:
            temperature = self.real_temp
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)", options=options)
        i = 0 
        if file_path:
            with open(file_path, 'w') as file:
                for i in range(len(temperature) ):
                    temperature_str = f"{temperature[i]:0.10f}"
                    mx1_str = f"{self.mx1[int(self.i -1)][i]:0.10f}"
                    my1_str = f"{self.my1[int(self.i -1)][i]:0.10f}"
                    mz1_str = f"{self.mz1[int(self.i -1)][i]:0.10f}"
                    factor_str = f"{self.factor_list[int(self.i -1)][i]:0.10f}"
                    file.write(f"{temperature_str}\t{mx1_str}\t{my1_str}\t{mz1_str}\t{factor_str}\n")


    
    
    def PROCESSING(self):
        if not self.loaded_files3 and not self.loaded_files4:   
            self.Er_const_list.clear() 
            self.real_temp.clear()
            self.data_list.clear()
            self.result.clear()
            self.outfile.clear()
            self.mx1.clear()
            self.my1.clear()
            self.mz1.clear()
            self.mx.clear()
            self.my.clear()
            self.mz.clear()
            self.ev_vol_list.clear()
            self.factor_list.clear()
            self.mx2.clear()
            self.my2.clear()
            self.mz2.clear()
            self.atom_masses.clear()
            self.atom_names.clear()
            self.atom_numbers.clear()
            self.count.clear() 
            self.sing_temperature.clear()
            
            self.get_atom_info()
            self.map_names_to_numbers()
            self.extract_temperatures()
            self.Cleaning()
            self.copyfiles()
            self.Msd()
            self.sing_Msd_interpol()
            self.GenerateComboBox()
            self.Mfactor()
            self.DeletingCleanedFiles()

        else:   
            self.Er_const_list.clear() 
            self.real_temp.clear()
            self.data_list.clear()
            self.result.clear()
            self.outfile.clear()
            self.mx1.clear()
            self.my1.clear()
            self.mz1.clear()
            self.mx.clear()
            self.my.clear()
            self.mz.clear()
            self.ev_vol_list.clear()
            self.factor_list.clear()
            self.mx2.clear()
            self.my2.clear()
            self.mz2.clear()
            self.atom_masses.clear()
            self.atom_names.clear()
            self.atom_numbers.clear()
            self.count.clear()
            
            self.get_atom_info()
            self.map_names_to_numbers()
            self.ev_volume()
            self.temp_vol()
            self.Cleaning()
            self.copyfiles()
            self.count_values_smaller_than_first()
            self.Removing()
            self.real_temperature()
            self.Msd()
            self.Msd_interpol()
            self.GenerateComboBox()
            self.Mfactor()
            self.DeletingCleanedFiles()
    
    
    
    def exception_hook(self, exctype, value, traceback):
        error_message = f"An error occurred: {exctype.__name__}: {value}"
        QMessageBox.critical(self, "Error", error_message, QMessageBox.Ok)


    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Close Window", "Are you sure you want to close the window?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
            self.DeletingCleanedFiles()
        else:
            event.ignore()




def window ():
    app = QApplication(sys.argv)
    win = my_window()
    app.setWindowIcon(QIcon("Logo.jpg"))
        

    win.show()

    sys.exit(app.exec_())



window()