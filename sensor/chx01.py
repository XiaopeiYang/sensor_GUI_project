from GUI.Ui_MplMainWindow import Ui_MainWindow
import json

# the parameters in combobox
sensorType = ["GH101_GPR", "CHR101_SR_GPR", "CH201_GPRMT"]
ch_Mode = ["TX_RX", "FREERUN", "RX_ONLY", "MODE_IDLE"]
ch_fsr = ["1000", "2000", "3000", "4000", "5000"]
ch_sampingRate = ["5", "10", "15", "25", "30"]

class chx01():
    def __init__(self, windows, send_CH, chx01_range_listener, cache_data_path):
        """ set GUI for chx01 sensor

        Args:
            windows (_type_): the main gui object
            send_CH (_type_): the serial port sending function
        """
        self.windows = windows
        self.send_CH = send_CH
        self.chx01_range_listener = chx01_range_listener
        self.cache_data_path = cache_data_path
        self.chx01_initinalization()

        # data load fron json file
        self.data_loader()

    def data_loader(self):
        with open(self.cache_data_path, 'r') as f:
            data = json.load(f)
            if "sensorType" in data:
                self.windows.ch_sensorType.setCurrentIndex(
                    sensorType.index(data["sensorType"]))
            if "ch_Mode" in data:
                self.windows.ch_Mode.setCurrentIndex(
                    ch_Mode.index(data["ch_Mode"]))
            if "ch_fsr" in data:
                self.windows.ch_fsr.setCurrentIndex(
                    ch_fsr.index(data["ch_fsr"]))
            if "ch_sampingRate" in data:
                self.windows.ch_sampingRate.setCurrentIndex(
                    ch_sampingRate.index(data["ch_sampingRate"]))

            if "ch_range1" in data:
                self.windows.ch_range1.setText(data["ch_range1"])
                self.windows.ch_threshold1.setText(str(int(data["ch_range1"])*14))
            if "ch_range2" in data:
                self.windows.ch_range2.setText(data["ch_range2"])
                self.windows.ch_threshold2.setText(
                    str(int(data["ch_range2"])*14))
            if "ch_range3" in data:
                self.windows.ch_range3.setText(data["ch_range3"])
                self.windows.ch_threshold3.setText(
                    str(int(data["ch_range3"])*14))
            if "ch_range4" in data:
                self.windows.ch_range4.setText(data["ch_range4"])
                self.windows.ch_threshold4.setText(
                    str(int(data["ch_range4"])*14))
            if "ch_range5" in data:
                self.windows.ch_range5.setText(data["ch_range5"])
                self.windows.ch_threshold5.setText(
                    str(int(data["ch_range5"])*14))
            if "ch_range6" in data:
                self.windows.ch_range6.setText(data["ch_range6"])
                self.windows.ch_threshold6.setText(
                    str(int(data["ch_range6"])*14))

            if "ch_amplitude1" in data:
                self.windows.ch_amplitude1.setText(data["ch_amplitude1"])
            if "ch_amplitude2" in data:
                self.windows.ch_amplitude2.setText(data["ch_amplitude2"])
            if "ch_amplitude3" in data:
                self.windows.ch_amplitude3.setText(data["ch_amplitude3"])
            if "ch_amplitude4" in data:
                self.windows.ch_amplitude4.setText(data["ch_amplitude4"])
            if "ch_amplitude4" in data:
                self.windows.ch_amplitude4.setText(data["ch_amplitude4"])
            if "ch_amplitude5" in data:
                self.windows.ch_amplitude5.setText(data["ch_amplitude5"])
            if "ch_amplitude6" in data:
                self.windows.ch_amplitude6.setText(data["ch_amplitude6"])
    
    def chx01_initinalization(self):
        """Settings for the parameters frame
        """
        self.windows.ch_sensorType.setCurrentIndex(0)
        self.windows.ch_sensorType.addItems(sensorType)

        self.windows.ch_Mode.setCurrentIndex(0)
        self.windows.ch_Mode.addItems(ch_Mode)

        self.windows.ch_fsr.setCurrentIndex(0)
        self.windows.ch_fsr.addItems(ch_fsr)

        self.windows.ch_sampingRate.setCurrentIndex(0)
        self.windows.ch_sampingRate.addItems(ch_sampingRate)
        self.threshold_initinalization()
        self.amplitude_initinalization()
        self.windows.completeSetup.clicked.connect(self.send_CH)

    def threshold_initinalization(self):
        self.windows.ch_threshold1.editingFinished.connect(lambda: self.chx01_range_listener(1))
        self.windows.ch_threshold1.setPlaceholderText("364")
        self.windows.ch_range1.setReadOnly(True)
        self.windows.ch_threshold2.editingFinished.connect(lambda: self.chx01_range_listener(2))
        self.windows.ch_threshold2.setPlaceholderText("546")
        self.windows.ch_range2.setReadOnly(True)
        self.windows.ch_threshold3.editingFinished.connect(
            lambda: self.chx01_range_listener(3))
        self.windows.ch_threshold3.setPlaceholderText("784")
        self.windows.ch_range3.setReadOnly(True)
        self.windows.ch_threshold4.editingFinished.connect(
            lambda: self.chx01_range_listener(4))
        self.windows.ch_threshold4.setPlaceholderText("1106")
        self.windows.ch_range4.setReadOnly(True)
        self.windows.ch_threshold5.editingFinished.connect(
            lambda: self.chx01_range_listener(5))
        self.windows.ch_threshold5.setPlaceholderText("1246")
        self.windows.ch_range5.setReadOnly(True)
        self.windows.ch_threshold6.editingFinished.connect(
            lambda: self.chx01_range_listener(6))
        self.windows.ch_threshold6.setPlaceholderText("6300")
        self.windows.ch_range6.setReadOnly(True)

    def amplitude_initinalization(self):
        self.windows.ch_amplitude1.setPlaceholderText("5000")
        self.windows.ch_amplitude2.setPlaceholderText("2000")
        self.windows.ch_amplitude3.setPlaceholderText("800")
        self.windows.ch_amplitude4.setPlaceholderText("400")
        self.windows.ch_amplitude5.setPlaceholderText("250")
        self.windows.ch_amplitude6.setPlaceholderText("175")

