import sys
import json
import csv
from unittest import case
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from GUI.Ui_MplMainWindow import Ui_MainWindow
# from Ui_MplMainWindow import Ui_MainWindow
import serial
import serial.tools.list_ports
import datetime
from matplotlib.dates import date2num
from sensor.chx01 import chx01
from GUI.Ui_elmos import Ui_elmos
from GUI.Ui_chx01 import Ui_chx01
from GUI.Ui_vl53 import Ui_vl53xxxx

from database.database import Database

import tkinter as tk
from tkinter import filedialog

from sensor.elmos import elmos


Num_points_A_curve = 5
class Code_MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,  main_window):
        """GUI Operation

        Args:
            main_window (_type_): the sys window
        """

        super(Code_MainWindow, self).__init__()
        self.setupUi(main_window)
        self.setWindowIcon(QIcon('GUI/res/uni.png'))

        self.serialPort_initinalization()
        self.refreshbutton.clicked.connect(self.refresh)

        # open ELMOS Threshold setting subwindow
        self.actionCHX01.triggered.connect(
            lambda: self.switch_to_subwindows(0))
        self.actionELMOS_E524_33.triggered.connect(
            lambda: self.switch_to_subwindows(1))
        self.actionVL53xxxx.triggered.connect(
            lambda: self.switch_to_subwindows(2))

        # Timer for receiving data on time period
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.recv)
        self.timer_send = QTimer(self)
        self.timer_send.timeout.connect(self.shot_operation)

        # trigger the data receiveing
        self.buttonread.clicked.connect(self.buttonRead)
        self.buttonshot.clicked.connect(self.shot_operation)

        # showring widgets
        self.table_initinalization()

        # initialize database
        self.db = Database()

        # initialize distance checkbox
        self.uspa = False
        self.x_distance.setChecked(True)
        self.x_distance.toggled.connect(lambda: self.btnstate(self.x_distance))

        # initialize time checkbox
        self.x_time.toggled.connect(lambda: self.btnstate(self.x_time))

        # initialize measurement data download button
        self.savetabledata.clicked.connect(self.downloadtabledata)
        self.savecanvasdata.clicked.connect(self.downloadcanvasdata) 

        #initialize measurement data import button
        self.importcanvasdata.clicked.connect(self.importcanvas_operation)

    def shot_operation(self):
        # if self.uspa :
        if self.x_time.isChecked():
                self.send("Time")
        elif self.x_distance.isChecked():
                self.send("Distance")
        

    def btnstate(self, btn):
        if btn.text() == "Distance":
            if btn.isChecked() == True:
                
                results = self.db.read_uspadistance_db(
                )[-Num_points_A_curve:]

                self.mplUspa.updatedata([i[1] for i in results], [i[3] for i in results], [
                                        i[4] for i in results], [i[5] for i in results], xlabel="Distance (mm)")
        if btn.text() == "Time":
            if btn.isChecked() == True:
                
                results = self.db.read_uspatime_db()[-Num_points_A_curve:]

                self.mplUspa.updatedata([i[1] for i in results], [i[3] for i in results], [
                                        i[4] for i in results], [i[5] for i in results], xlabel="Time (μs)")

    def buttonRead(self):
        if self.buttonread.text() == "READ":
            if self.ser:
                self.buttonread.setText("STOP")
                self.timer_send.start(1000)
            else:
                QMessageBox.critical(self, 'pycom', 'Please open the port')
        else:
            self.buttonread.setText("READ")
            self.timer_send.stop()

    def serialPort_initinalization(self):
        """global variable
        """
        self.btn_sta = True  # Open the serial port button status indicator

        # serial port invalid
        self.ser = None
        self.send_num = 0
        self.receive_num = 0

        # serial port initialization
        self.cmbBaudRate = '115200'
        self.cmbDataLen = '8'
        self.cmbStopBit = "1"
        self.cmbCheckBit = "NONE"

        # Check the valid com port
        self.refresh()
        # Open and close the serial port button
        self.butOpenPort.clicked.connect(self.open_close)

    def table_initinalization(self):
        self.dataTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.dataTable.setColumnCount(3)
        self.dataTable.setColumnWidth(0, 200)
        self.dataTable.setColumnWidth(1, 100)
        self.dataTable.setColumnWidth(2, 100)

        self.dataTable.setHorizontalHeaderLabels(
            ['Timestamp', 'Range(mm)', 'Amplitude'])

    def dataTable_insert(self, timestamp_, range_, amp_):
        """insert new row into the table

        Args:
            timestamp (_type_): the timestamp of the sensor value
            range (_type_): the value of range
            amp (_type_): the value of amplitude
        """
        rowsNum = self.dataTable.rowCount()
        self.dataTable.setRowCount(rowsNum + 1)

        range = QTableWidgetItem(range_)
        range.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        amp = QTableWidgetItem(amp_)
        amp.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        timestamp = QTableWidgetItem(timestamp_)
        timestamp.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        self.dataTable.setItem(rowsNum, 0, timestamp)
        self.dataTable.setItem(rowsNum, 1, range)
        self.dataTable.setItem(rowsNum, 2, amp)

    def refresh(self):
        """find the list of valid port, description : USB Serial Device
        """
        plist = list(serial.tools.list_ports.comports())

        if len(plist) <= 0:
            print("No used com!")

        else:
            # clear the port list
            self.portlist.clear()

            for i in range(0, len(plist)):
                if "USB Serial Device" in plist[i].description:
                    plist_0 = list(plist[i])
                    self.portlist.addItem(
                        str(plist_0[0])+"  (USB Serial Device)")

    def switch_to_subwindows(self, index):
        if index == 0:
            self.chile_Win = CHX01_Setting_window(self.send)
            self.chile_Win.show()
        elif index == 1:
            # not ready yet
            self.chile_Win = elmos_Setting_window(self.send)
            self.chile_Win.show()
        elif index == 2:
            # not ready yet
            self.chile_Win = vl53_Setting_window()
            self.chile_Win.show()
        # self.chile_Win.exec_()

    def downloadtabledata(self):

        name = QFileDialog.getSaveFileName(self, 'Save data "level and amplitude"')
        
        with open(name[0]+".csv", 'w', newline='') as csv_file: 
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(self.db.read_rangeamp_db())
            
    def downloadcanvasdata(self):
        name = QFileDialog.getSaveFileName(self, 'Save data "threshold, "')
        #delete the default first row(0,0,0,0,0,0) in the database
        if self.x_time.isChecked():
            self.db.delete_uspatime_t_db(str(0))
        elif self.x_distance.isChecked():
            self.db.delete_uspadistance_t_db(str(0))        

        with open(name[0]+".csv", 'w', newline='') as csv_file: 
            csv_writer = csv.writer(csv_file)
            #if time x_axis is selected
            if self.x_time.isChecked():            
                csv_writer.writerows(self.db.read_uspatime_db())
            #if distance x_axis is selected
            elif self.x_distance.isChecked():
                csv_writer.writerows(self.db.read_uspadistance_db())   

    def choosefile(self):
        """Opens the Select Folder dialog"""
        root = tk.Tk()
        root.withdraw()
        Filepath = filedialog.askopenfilename() #get selected file
        print(Filepath)
        return Filepath
    
    
    def importcanvas_operation(self):

        if self.x_distance.isChecked():
            if self.db.read_uspadistance_db():
                self.db.delete_uspadistance_db()
                
                QMessageBox.information(self, 'Info', 'previous data is cleared')                
                #read the selected file
                csvfilepath=self.choosefile()

                with open(csvfilepath,'r') as fin: # `with` statement available in 2.5+
                    # csv.DictReader uses first line in file for column headings by default
                    dr = csv.reader(fin) # comma is default delimiter
                    #insert data from csv file   
                    for row in dr:
                        self.db.insert_uspadistance_db(row[0],row[1],row[2],row[3],row[4],row[5])
                                                       
                #show the last data set of this database  
                results = self.db.read_uspadistance_db(                    
                )[-Num_points_A_curve:]
                self.mplUspa.updatedata([i[1] for i in results], [i[3] for i in results], [
                                        i[4] for i in results], [i[5] for i in results], xlabel="Distance (mm)")
            else:
                #read the selected file
                csvfilepath=self.choosefile()
                      
                with open(csvfilepath,'r') as fin: # `with` statement available in 2.5+
                    # csv.DictReader uses first line in file for column headings by default
                    dr = csv.reader(fin) # comma is default delimiter
                    #insert data from csv file               
                    for row in dr:
                        self.db.insert_uspadistance_db(row[0],row[1],row[2],row[3],row[4],row[5])
                        
               # show the last data set of this database                         
                results = self.db.read_uspadistance_db(
                )[-Num_points_A_curve:]
                self.mplUspa.updatedata([i[1] for i in results], [i[3] for i in results], [
                                        i[4] for i in results], [i[5] for i in results], xlabel="Distance (mm)")

        elif self.x_time.isChecked():
            if self.db.read_uspatime_db():
                self.db.delete_uspatime_db()
                QMessageBox.information(self, 'Info', 'previous data is cleared')
            
                #read the selected file
                csvfilepath=self.choosefile()

                with open(csvfilepath,'r') as fin: # `with` statement available in 2.5+
                    # csv.DictReader uses first line in file for column headings by default
                    dr = csv.reader(fin) # comma is default delimiter
                    #insert data from csv file   
                    for row in dr:
                        self.db.insert_uspatime_db(row[0],row[1],row[2],row[3],row[4],row[5])

                #show the last data set of this database  
                results = self.db.read_uspatime_db()[-Num_points_A_curve:]

                self.mplUspa.updatedata([i[1] for i in results], [i[3] for i in results], [
                                        i[4] for i in results], [i[5] for i in results], xlabel="Time (μs)")
            else:
                #read the selected file
                csvfilepath=self.choosefile()
                      
                with open(csvfilepath,'r') as fin: # `with` statement available in 2.5+
                    # csv.DictReader uses first line in file for column headings by default
                    dr = csv.reader(fin) # comma is default delimiter
                    #insert data from csv file               
                    for row in dr:
                        self.db.insert_uspatime_db(row[0],row[1],row[2],row[3],row[4],row[5])

                # show the last data set of this database                         
                results = self.db.read_uspatime_db()[-Num_points_A_curve:]

                self.mplUspa.updatedata([i[1] for i in results], [i[3] for i in results], [
                                        i[4] for i in results], [i[5] for i in results], xlabel="Time (μs)")

    

    def recv(self):
        """handle the received data

        Returns:
            _type_: _description_
        """
        try:
            num = self.ser.inWaiting()
        except:

            # self.timer_send.stop()
            self.timer.stop()
            # error
            self.ser.close()
            self.ser = None

            # change the openning state
            self.butOpenPort.setChecked(False)
            self.butOpenPort.setText("open serial")
            print('serial error!')
            return None
        if (num > 0):
            # Sometimes there will be one less character read, and you have to read it a second time, so read one more: range,amp
            data = self.ser.read(num)
            # byte to string
            readBuffer = bytes.decode(data, encoding="utf8", errors='ignore')
            splitted = readBuffer.split(',')

            # showing into the table and store in the database
            stamp = str(datetime.datetime.now().strftime(
                '%Y-%m-%d %H:%M:%S'))
            # if splitted[0] == 'rangeAmp':
            if splitted[0] == 'T':
                 # split the data
                databuffer = readBuffer.split('t')
                # print the range amp data into the table, database
                splitted_table = databuffer[0].split(',')
                self.db.insert_rangeamp_db(stamp, splitted_table[1], splitted_table[2])
                self.dataTable_insert(stamp,  splitted_table[1], splitted_table[2])

                # print the uspatime data into the table, database
                timestamp = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S") # current date and time

                for i in databuffer[1:]:                    

                    splitted_canvas = i.split(',')
                    if self.db.read_uspatime_db():
                        self.db.insert_uspatime_db(self.db.read_uspatime_lastid_db()+1,int(splitted_canvas[1]), timestamp,
                         int(splitted_canvas[2]), int(splitted_canvas[3]), int(splitted_canvas[4]))
                    else:
                        self.db.insert_uspatime_db(0,int(splitted_canvas[1]), timestamp,
                         int(splitted_canvas[2]), int(splitted_canvas[3]), int(splitted_canvas[4]))
                         

                results = self.db.read_uspatime_db(
                )[-Num_points_A_curve:]

                self.mplUspa.updatedata([i[1] for i in results], [i[3] for i in results], [
                                        i[4] for i in results], [i[5] for i in results], xlabel="Time (mm)")
                
                
            elif splitted[0] == 'D':
                # split the data
                databuffer = readBuffer.split('d')
                # print the range amp data into the table, database
                splitted_table = databuffer[0].split(',')
                self.db.insert_rangeamp_db(stamp, splitted_table[1], splitted_table[2])
                self.dataTable_insert(stamp, splitted_table[1], splitted_table[2])

                # print the uspatime data into the table, database
                timestamp = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S") # current date and time
               
                for i in databuffer[1:]:                    

                    splitted_canvas = i.split(',')
                    if self.db.read_uspadistance_db():
                        self.db.insert_uspadistance_db(self.db.read_uspadistance_lastid_db()+1,int(splitted_canvas[1]), timestamp,
                         int(splitted_canvas[2]), int(splitted_canvas[3]), int(splitted_canvas[4]))
                    else:
                        self.db.insert_uspadistance_db(0,int(splitted_canvas[1]), timestamp,
                         int(splitted_canvas[2]), int(splitted_canvas[3]), int(splitted_canvas[4]))

                results = self.db.read_uspadistance_db(
                )[-Num_points_A_curve:]

                self.mplUspa.updatedata([i[1] for i in results], [i[3] for i in results], [
                                        i[4] for i in results], [i[5] for i in results], xlabel="Distance (mm)")

                

            elif splitted[0] == 'elmos':
                #print the command data into the resultdisplay of ELMOSsetting_window
                databuffer = readBuffer.split(',')
                self.chile_Win.reload_buffer(databuffer[1])

            ##############################################################################
            num = len(data)

            self.receive_num = self.receive_num + num
            dis = 'send' + '{:d}'.format(self.send_num) + \
                '  receive:' + '{:d}'.format(self.receive_num)
            self.statusbar.showMessage(dis)

        else:
            pass

    def send(self, input_s):
        """Serial port send data processing

        Returns:
            _type_: _description_
        """
        if self.ser:
            if input_s != "":

                input_s = input_s + '\r\n'
                input_s = input_s.encode('utf-8')

                try:
                    num = self.ser.write(input_s)
                except:

                    # self.timer_send.stop()
                    self.timer.stop()
                    # error
                    self.ser.close()
                    self.ser = None

                    # change the opening state
                    self.butOpenPort.setChecked(False)
                    self.butOpenPort.setText("Open serial")
                    print('serial error send!')
                    return None

                self.send_num = self.send_num + num
                dis = 'Send' + \
                    '{:d}'.format(self.send_num) + '  receive:' + \
                    '{:d}'.format(self.receive_num)
                self.statusbar.showMessage(dis)
                print('send test!')
            else:
                print('none data input!')

        else:
            # stop the sending timer
            # self.timer_send.stop()
            QMessageBox.critical(self, 'Send failed', 'Please open the port')

    def open_close(self):
        """Open port

        Returns:
            _type_: _description_
        """

        if self.btn_sta == True:
            try:
                # paremeters assigned 'COM13',115200
                # print(int(self.cmbBaudRate.currentText()))
                self.ser = serial.Serial(
                    self.portlist.currentText().split(" ")[0], int(self.cmbBaudRate), timeout=0.1)
            except:
                QMessageBox.critical(
                    self, 'pycom', 'No serial port is available or the current serial port is occupied')
                return None
            # Character interval timeout time setting
            self.ser.interCharTimeout = 0.001

            # 1ms Test cycle
            self.timer.start(2)
            self.butOpenPort.setText("close serial")
            self.btn_sta = False
            print('open!')
        else:
            # Turn off the timer and stop reading and receiving data
            # self.timer_send.stop()
            self.timer.stop()
            # time.sleep(0.5)
            try:
                # Turn off serial port
                self.ser.close()
            except:
                QMessageBox.critical(
                    self, 'pycom', 'Failed to close the serial port')
                return None

            self.ser = None

            self.butOpenPort.setText("open serial")
            self.btn_sta = True
            print('close!')

    def releasePlot(self):

        self.mplCanvas.releasePlot()


class CHX01_Setting_window(QWidget, Ui_chx01):
    """chx01 window operations

    Args:
        QWidget (_type_): pyqt5 class
        Ui_chx01 (_type_): form .py class
    """

    def __init__(self, send):
        super(CHX01_Setting_window, self).__init__()
        self.setupUi(self)
        self.send = send
        self.cache_data_path = "database/cache/chx01.json"

        self.download_chx01_settings.clicked.connect(self.downloadSettings_CH)

        chx01(self, self.send_CH, self.chx01_range_listener, self.cache_data_path)

    def downloadSettings_CH(self):
        name = QFileDialog.getSaveFileName(self, 'Save Sensor Configurations')

        # convert json object to csv file
        with open(self.cache_data_path, encoding='utf8') as json_file:
            ls = json.load(json_file)
            data = [list(ls.keys())]

            data.append([ls[item] for item in ls])

            with open(name[0]+".csv", 'w', newline='') as out_file:
                # out_file.write(json.dumps(self.packageUp()))
                for line in data:

                    out_file.write(",".join(line) + "\n")

        # QMessageBox.information(self, 'Info', 'Download successful')

    def chx01_range_listener(self, number):
        if number == 1:
            if self.ch_threshold1.text().isnumeric():
                self.ch_range1.setText(
                    str(round(int(self.ch_threshold1.text())/14)))
        elif number == 2:
            if self.ch_threshold2.text().isnumeric():
                self.ch_range2.setText(
                    str(round(int(self.ch_threshold2.text())/14)))
        elif number == 3:
            if self.ch_threshold3.text().isnumeric():
                self.ch_range3.setText(
                    str(round(int(self.ch_threshold3.text())/14)))
        elif number == 4:
            if self.ch_threshold4.text().isnumeric():
                self.ch_range4.setText(
                    str(round(int(self.ch_threshold4.text())/14)))
        elif number == 5:
            if self.ch_threshold5.text().isnumeric():
                self.ch_range5.setText(
                    str(round(int(self.ch_threshold5.text())/14)))
        elif number == 6:
            if self.ch_threshold6.text().isnumeric():
                self.ch_range6.setText(
                    str(round(int(self.ch_threshold6.text())/14)))

    def send_CH(self):

        input_s = json.dumps(self.packageUp())
        # save data to josn file
        f2 = open(self.cache_data_path, 'w')
        f2.write(input_s)
        f2.close()

        self.send(input_s)

    def packageUp(self):
        """package the data into a python dictionary

        Returns:
            _type_: _description_
        """
        # get sensortype
        send_data = {}
        if self.ch_sensorType.currentText():
            send_data["sensorType"] = self.ch_sensorType.currentText()
        # get chmode
        if self.ch_Mode.currentText():
            send_data["ch_Mode"] = self.ch_Mode.currentText()
        # get fsr
        if self.ch_fsr.currentText():
            send_data["ch_fsr"] = self.ch_fsr.currentText()
        # get samping Rate
        if self.ch_sampingRate.currentText():
            send_data["ch_sampingRate"] = self.ch_sampingRate.currentText()

        # get ranges
        if self.ch_range1.text():
            send_data["ch_range1"] = self.ch_range1.text()
        if self.ch_range2.text():
            send_data["ch_range2"] = self.ch_range2.text()
        if self.ch_range3.text():
            send_data["ch_range3"] = self.ch_range3.text()
        if self.ch_range4.text():
            send_data["ch_range4"] = self.ch_range4.text()
        if self.ch_range5.text():
            send_data["ch_range5"] = self.ch_range5.text()
        if self.ch_range6.text():
            send_data["ch_range6"] = self.ch_range6.text()

        # get amplitudes
        if self.ch_amplitude1.text():
            send_data["ch_amplitude1"] = self.ch_amplitude1.text()
        if self.ch_amplitude2.text():
            send_data["ch_amplitude2"] = self.ch_amplitude2.text()
        if self.ch_amplitude3.text():
            send_data["ch_amplitude3"] = self.ch_amplitude3.text()
        if self.ch_amplitude4.text():
            send_data["ch_amplitude4"] = self.ch_amplitude4.text()
        if self.ch_amplitude5.text():
            send_data["ch_amplitude5"] = self.ch_amplitude5.text()
        if self.ch_amplitude6.text():
            send_data["ch_amplitude6"] = self.ch_amplitude6.text()

        return send_data


class elmos_Setting_window(QWidget, Ui_elmos):
    """elmos window operations

    Args:
        QWidget (_type_): pyqt5 class
        Ui_elmos (_type_): form .py class
    """

    def __init__(self, send):
        super(elmos_Setting_window, self).__init__()
        self.setupUi(self)
        self.send = send
        self.cache_data_path = "database/cache/elmos.json"

        self.download_elmos_settings.clicked.connect(self.downloadSettings_EL)
        # self.el_completesetup.clicked.connect(self.send_EL)
        elmos(self, self.send_EL, self.cache_data_path)
        self.el_active.clicked.connect(self.active_EL)

    def reload_buffer(self, readBuffer):
        if readBuffer:
            self.el_resultdisplay.setText(readBuffer)

    def downloadSettings_EL(self):
        name = QFileDialog.getSaveFileName(self, 'Save Sensor Configurations')

        # convert json object to csv file
        with open(self.cache_data_path, encoding='utf8') as json_file:
            ls = json.load(json_file)
            data = [list(ls.keys())]

            data.append([ls[item] for item in ls])

            with open(name[0]+".csv", 'w', newline='') as out_file:
                # out_file.write(json.dumps(self.packageUp()))
                for line in data:

                    out_file.write(",".join(line) + "\n")

        # QMessageBox.information(self, 'Info', 'Download successful')

    def send_EL(self):

        input_s = json.dumps(self.packageUp())
        # save data to josn file
        f2 = open(self.cache_data_path, 'w')
        f2.write(input_s)
        f2.close()
        self.send(input_s)

    def packageUp(self):
        """package the data into a python dictionary

        Returns:
            _type_: _description_
        """
        # get sensortype
        send_data = {}
        
        if self.el_tofcomp.text():
            send_data["TOF_Comp"] = self.el_tofcomp.text()

        if self.el_Athval1.currentText():
            send_data["Athval1"] = self.el_Athval1.currentText()
        if self.el_Athval2.currentText():
            send_data["Athval2"] = self.el_Athval2.currentText()
        if self.el_Athval3.currentText():
            send_data["Athval3"] = self.el_Athval3.currentText()
        if self.el_Athval4.currentText():
            send_data["Athval4"] = self.el_Athval4.currentText()
        if self.el_Athval5.currentText():
            send_data["Athval5"] = self.el_Athval5.currentText()
        if self.el_Athval6.currentText():
            send_data["Athval6"] = self.el_Athval6.currentText()
        if self.el_Athval7.currentText():
            send_data["Athval7"] = self.el_Athval7.currentText()
        if self.el_Athval8.currentText():
            send_data["Athval8"] = self.el_Athval8.currentText()
        if self.el_Athval9.currentText():
            send_data["Athval9"] = self.el_Athval9.currentText()
        if self.el_Athval10.currentText():
            send_data["Athval10"] = self.el_Athval10.currentText()

        if self.el_Athpos1.currentText():
            send_data["Athpos1"] = self.el_Athpos1.currentText()
        if self.el_Athpos2.currentText():
            send_data["Athpos2"] = self.el_Athpos2.currentText()
        if self.el_Athpos3.currentText():
            send_data["Athpos3"] = self.el_Athpos3.currentText()
        if self.el_Athpos4.currentText():
            send_data["Athpos4"] = self.el_Athpos4.currentText()
        if self.el_Athpos5.currentText():
            send_data["Athpos5"] = self.el_Athpos5.currentText()
        if self.el_Athpos6.currentText():
            send_data["Athpos6"] = self.el_Athpos6.currentText()
        if self.el_Athpos7.currentText():
            send_data["Athpos7"] = self.el_Athpos7.currentText()
        if self.el_Athpos8.currentText():
            send_data["Athpos8"] = self.el_Athpos8.currentText()
        if self.el_Athpos9.currentText():
            send_data["Athpos9"] = self.el_Athpos9.currentText()
        if self.el_Athpos10.currentText():
            send_data["Athpos10"] = self.el_Athpos10.currentText()

        if self.el_Bthval1.currentText():
            send_data["Bthval1"] = self.el_Bthval1.currentText()
        if self.el_Bthval2.currentText():
            send_data["Bthval2"] = self.el_Bthval2.currentText()
        if self.el_Bthval3.currentText():
            send_data["Bthval3"] = self.el_Bthval3.currentText()
        if self.el_Bthval4.currentText():
            send_data["Bthval4"] = self.el_Bthval4.currentText()
        if self.el_Bthval5.currentText():
            send_data["Bthval5"] = self.el_Bthval5.currentText()
        if self.el_Bthval6.currentText():
            send_data["Bthval6"] = self.el_Bthval6.currentText()
        if self.el_Bthval7.currentText():
            send_data["Bthval7"] = self.el_Bthval7.currentText()
        if self.el_Bthval8.currentText():
            send_data["Bthval8"] = self.el_Bthval8.currentText()
        if self.el_Bthval9.currentText():
            send_data["Bthval9"] = self.el_Bthval9.currentText()
        if self.el_Bthval10.currentText():
            send_data["Bthval10"] = self.el_Bthval10.currentText()

        if self.el_Bthpos1.currentText():
            send_data["Bthpos1"] = self.el_Bthpos1.currentText()
        if self.el_Bthpos2.currentText():
            send_data["Bthpos2"] = self.el_Bthpos2.currentText()
        if self.el_Bthpos3.currentText():
            send_data["Bthpos3"] = self.el_Bthpos3.currentText()
        if self.el_Bthpos4.currentText():
            send_data["Bthpos4"] = self.el_Bthpos4.currentText()
        if self.el_Bthpos5.currentText():
            send_data["Bthpos5"] = self.el_Bthpos5.currentText()
        if self.el_Bthpos6.currentText():
            send_data["Bthpos6"] = self.el_Bthpos6.currentText()
        if self.el_Bthpos7.currentText():
            send_data["Bthpos7"] = self.el_Bthpos7.currentText()
        if self.el_Bthpos8.currentText():
            send_data["Bthpos8"] = self.el_Bthpos8.currentText()
        if self.el_Bthpos9.currentText():
            send_data["Bthpos9"] = self.el_Bthpos9.currentText()
        if self.el_Bthpos10.currentText():
            send_data["Bthpos10"] = self.el_Bthpos10.currentText()

        if self.el_npulsesa.currentText():
            send_data["NPULSES_A"] = self.el_npulsesa.currentText()
        if self.el_tmeasa.currentText():
            send_data["TMEAS_A"] = self.el_tmeasa.currentText()
        if self.el_thsela.currentText():
            send_data["THSEL_A"] = self.el_thsela.currentText()

        if self.el_npulsesb.currentText():
            send_data["NPULSES_B"] = self.el_npulsesb.currentText()
        if self.el_tmeasb.currentText():
            send_data["TMEAS_B"] = self.el_tmeasb.currentText()
        if self.el_thselb.currentText():
            send_data["THSEL_B"] = self.el_thselb.currentText()

        if self.el_npulsesc.currentText():
            send_data["NPULSES_C"] = self.el_npulsesc.currentText()
        if self.el_tmeasc.currentText():
            send_data["TMEAS_C"] = self.el_tmeasc.currentText()
        if self.el_thselc.currentText():
            send_data["THSEL_C"] = self.el_thselc.currentText()

        if self.el_stcpos0.currentText():
            send_data["STC_POS0"] = self.el_stcpos0.currentText()
        if self.el_stcpos1.currentText():
            send_data["STC_POS1"] = self.el_stcpos1.currentText()
        if self.el_stcpos2.currentText():
            send_data["STC_POS2"] = self.el_stcpos2.currentText()
        if self.el_stcpos3.currentText():
            send_data["STC_POS3"] = self.el_stcpos3.currentText()
        if self.el_stcpos4.currentText():
            send_data["STC_POS4"] = self.el_stcpos4.currentText()

        if self.el_stcgain0.text():
            send_data["STC_GAIN0"] = self.el_stcgain0.text()
        if self.el_stcgain1.text():
            send_data["STC_GAIN1"] = self.el_stcgain1.text()
        if self.el_stcgain2.text():
            send_data["STC_GAIN2"] = self.el_stcgain2.text()
        if self.el_stcgain3.text():
            send_data["STC_GAIN3"] = self.el_stcgain3.text()
        if self.el_stcgain4.text():
            send_data["STC_GAIN4"] = self.el_stcgain4.text()

        if self.el_echodeb.text():
            send_data["ECHO_DEB"] = self.el_echodeb.text()
        if self.el_rtcfg.text():
            send_data["RT_CFG"] = self.el_rtcfg.text()
        if self.el_nftg.text():
            send_data["NFTG"] = self.el_nftg.text()
        if self.el_ftc.text():
            send_data["FTC"] = self.el_ftc.text()
        if self.el_epd.text():
            send_data["EPD"] = self.el_epd.text()
        if self.el_echodeb.text():
            send_data["APD"] = self.el_apd.text()
        if self.el_apd.text():
            send_data["FILTER_CFG"] = self.el_filtercfg.text()
        if self.el_filtercfg.text():
            send_data["ATG_CFG"] = self.el_atgcfg.text()
        if self.el_atgcfg.text():
            send_data["ATG_TAU"] = self.el_atgtau.text()
        if self.el_atgtau.text():
            send_data["ATG_ALPHA"] = self.el_atgalpha.text()
        if self.el_atgalpha.text():
            send_data["NSUPP_CFG"] = self.el_nsuppcfg.text()
        if self.el_nsuppcfg.text():
            send_data["NOISE_CFG"] = self.el_noisecfg.text()
        if self.el_noisecfg.text():
            send_data["SCALE_REC"] = self.el_scalerec.text()
        if self.el_statuscfg.text():
            send_data["STATUS_CFG"] = self.el_statuscfg.text()

        if self.el_customer.text():
            send_data["CUSTOMER"] = self.el_customer.text()
        if self.el_sdamp.currentText():
            send_data["S_DAMP"] = self.el_sdamp.currentText()
        if self.el_fdr.text():
            send_data["F_DR"] = self.el_fdr.text()
        if self.el_vdrv.text():
            send_data["V_DRV"] = self.el_vdrv.text()
        if self.el_gana.text():
            send_data["G_ANA"] = self.el_gana.text()
        if self.el_gdig.text():
            send_data["G_DIG"] = self.el_gdig.text()
        if self.el_nfdtoff.text():
            send_data["NFD_TOFF"] = self.el_nfdtoff.text()
        if self.el_nfdthres.text():
            send_data["NFD_THRES"] = self.el_nfdthres.text()
        if self.el_nfdwin.text():
            send_data["NFD_WIN"] = self.el_nfdwin.text()
        if self.el_osctrim.text():
            send_data["OSC_TRIM"] = self.el_osctrim.text()
        if self.el_tsenstrim.currentText():
            send_data["TSENS_Trim"] = self.el_tsenstrim.currentText()
      
        return send_data

    def active_EL(self):
        input_s = self.el_command.currentText()
        self.send(input_s)


class vl53_Setting_window(QWidget, Ui_vl53xxxx):
    """vl53 window operations

    Args:
        QWidget (_type_): pyqt5 class
        Ui_vl53xxxx (_type_): form .py class
    """

    def __init__(self):
        super(vl53_Setting_window, self).__init__()
        self.setupUi(self)
        self.cache_data_path = "database/cache/vl53.json"


if __name__ == "__main__":
    app = QApplication(sys.argv)  # initialize application
    MainWindow = QMainWindow()  # Create main window
    main_ui = Code_MainWindow(MainWindow)  # Create UI window
    MainWindow.show()  # present window
    # It returns 0 after the message loop ends, and then calls sys.exit (0) to
    # exit the program
    sys.exit(app.exec_())
