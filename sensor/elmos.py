from GUI.Ui_MplMainWindow import Ui_MainWindow
import json

# the parameters in combobox
Athval1=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21",
        "22","23","24","25","26","27","28","29","30","31"]
Athval2=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21",
        "22","23","24","25","26","27","28","29","30","31"]
Athval3=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21",
        "22","23","24","25","26","27","28","29","30","31"]
Athval4=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21",
        "22","23","24","25","26","27","28","29","30","31"]
Athval5=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21",
        "22","23","24","25","26","27","28","29","30","31"]
Athval6=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21",
        "22","23","24","25","26","27","28","29","30","31"]
Athval7=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21",
        "22","23","24","25","26","27","28","29","30","31"]
Athval8=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21",
        "22","23","24","25","26","27","28","29","30","31"]
Athval9=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21",
        "22","23","24","25","26","27","28","29","30","31"]
Athval10=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21",
        "22","23","24","25","26","27","28","29","30","31"]

Athpos1=["1","2","3","4","5"]
Athpos2=["1","2","3","4","5"]
Athpos3=["1","2","3","4","5"]
Athpos4=["1","2","3","4","5"]
Athpos5=["1","2","3","4","5"]
Athpos6=["1","2","3","4","5"]
Athpos7=["1","2","3","4","5"]
Athpos8=["1","2","3","4","5"]
Athpos9=["1","2","3","4","5"]
Athpos10=["1","2","3","4","5"]

Bthval1=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21",
        "22","23","24","25","26","27","28","29","30","31"]
Bthval2=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21",
        "22","23","24","25","26","27","28","29","30","31"]
Bthval3=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21",
        "22","23","24","25","26","27","28","29","30","31"]
Bthval4=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21",
        "22","23","24","25","26","27","28","29","30","31"]
Bthval5=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21",
        "22","23","24","25","26","27","28","29","30","31"]
Bthval6=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21",
        "22","23","24","25","26","27","28","29","30","31"]
Bthval7=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21",
        "22","23","24","25","26","27","28","29","30","31"]
Bthval8=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21",
        "22","23","24","25","26","27","28","29","30","31"]
Bthval9=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21",
        "22","23","24","25","26","27","28","29","30","31"]
Bthval10=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21",
        "22","23","24","25","26","27","28","29","30","31"]

Bthpos1=["1","2","3","4","5"]
Bthpos2=["1","2","3","4","5"]
Bthpos3=["1","2","3","4","5"]
Bthpos4=["1","2","3","4","5"]
Bthpos5=["1","2","3","4","5"]
Bthpos6=["1","2","3","4","5"]
Bthpos7=["1","2","3","4","5"]
Bthpos8=["1","2","3","4","5"]
Bthpos9=["1","2","3","4","5"]
Bthpos10=["1","2","3","4","5"]

NPULSES_A=["4","8","12","16","20","24","28","32"]
NPULSES_B=["4","8","12","16","20","24","28","32"]
NPULSES_C=["4","8","12","16","20","24","28","32"]

TMEAS_A=["8.75","11.66","14.58","17.49","20.41","23.32","29.15","34.98"]
TMEAS_B=["8.75","11.66","14.58","17.49","20.41","23.32","29.15","34.98"]
TMEAS_C=["8.75","11.66","14.58","17.49","20.41","23.32","29.15","34.98"]

THSEL_A=["ThresA","ThresB"]
THSEL_B=["ThresA","ThresB"]
THSEL_C=["ThresA","ThresB"]

STC_POS0=["256","512","1024","2048","4096"]
STC_POS1=["256","512","1024","2048","4096"]
STC_POS2=["256","512","1024","2048","4096"]
STC_POS3=["256","512","1024","2048","4096"]
STC_POS4=["256","512","1024","2048","4096"]

S_DAMP=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]
TSENS_Trim=["-1.56","-3.12","-4.68","-6.24","0","1.56","3.12","4.68"]

class elmos():
    def __init__(self, windows, send_EL, cache_data_path):
        """ set GUI for elmos sensor

        Args:
            windows (_type_): the main gui object
            send_EL (_type_): the serial port sending function
        """
        self.windows = windows
        self.send_EL = send_EL
        self.cache_data_path = cache_data_path
        self.elmos_initinalization()

        # data load fron json file
        self.data_loader()
    
    def data_loader(self):
        with open(self.cache_data_path, 'r') as f:
            data = json.load(f)

            if "TOF_Comp" in data:
                self.windows.el_tofcomp.setText(data["TOF_Comp"])

            if "Athval1" in data:
                self.windows.el_Athval1.setCurrentIndex(
                    Athval1.index(data["Athval1"]))
            if "Athval2" in data:
                self.windows.el_Athval2.setCurrentIndex(
                    Athval2.index(data["Athval2"]))
            if "Athval3" in data:
                self.windows.el_Athval3.setCurrentIndex(
                    Athval3.index(data["Athval3"]))
            if "Athval4" in data:
                self.windows.el_Athval4.setCurrentIndex(
                    Athval4.index(data["Athval4"]))
            if "Athval5" in data:
                self.windows.el_Athval5.setCurrentIndex(
                    Athval5.index(data["Athval5"]))
            if "Athval6" in data:
                self.windows.el_Athval6.setCurrentIndex(
                    Athval6.index(data["Athval6"]))
            if "Athval7" in data:
                self.windows.el_Athval7.setCurrentIndex(
                    Athval7.index(data["Athval7"]))
            if "Athval8" in data:
                self.windows.el_Athval8.setCurrentIndex(
                    Athval8.index(data["Athval8"]))
            if "Athval9" in data:
                self.windows.el_Athval9.setCurrentIndex(
                    Athval9.index(data["Athval9"]))
            if "Athval10" in data:
                self.windows.el_Athval10.setCurrentIndex(
                    Athval10.index(data["Athval10"]))

            if "Athpos1" in data:
                self.windows.el_Athpos1.setCurrentIndex(
                    Athpos1.index(data["Athpos1"]))
            if "Athpos2" in data:
                self.windows.el_Athpos2.setCurrentIndex(
                    Athpos2.index(data["Athpos2"]))
            if "Athpos3" in data:
                self.windows.el_Athpos3.setCurrentIndex(
                    Athpos3.index(data["Athpos3"]))
            if "Athpos4" in data:
                self.windows.el_Athpos4.setCurrentIndex(
                    Athpos4.index(data["Athpos4"]))
            if "Athpos5" in data:
                self.windows.el_Athpos5.setCurrentIndex(
                    Athpos5.index(data["Athpos5"]))
            if "Athpos6" in data:
                self.windows.el_Athpos6.setCurrentIndex(
                    Athpos6.index(data["Athpos6"]))
            if "Athpos7" in data:
                self.windows.el_Athpos7.setCurrentIndex(
                    Athpos7.index(data["Athpos7"]))
            if "Athpos8" in data:
                self.windows.el_Athpos8.setCurrentIndex(
                    Athpos8.index(data["Athpos8"]))
            if "Athpos9" in data:
                self.windows.el_Athpos9.setCurrentIndex(
                    Athpos9.index(data["Athpos9"]))
            if "Athpos10" in data:
                self.windows.el_Athpos10.setCurrentIndex(
                    Athpos10.index(data["Athpos10"]))

            if "Bthval1" in data:
                self.windows.el_Bthval1.setCurrentIndex(
                    Bthval1.index(data["Bthval1"]))
            if "Bthval2" in data:
                self.windows.el_Bthval2.setCurrentIndex(
                    Bthval2.index(data["Bthval2"]))
            if "Bthval3" in data:
                self.windows.el_Bthval3.setCurrentIndex(
                    Bthval3.index(data["Bthval3"]))
            if "Bthval4" in data:
                self.windows.el_Bthval4.setCurrentIndex(
                    Bthval4.index(data["Bthval4"]))
            if "Bthval5" in data:
                self.windows.el_Bthval5.setCurrentIndex(
                    Bthval5.index(data["Bthval5"]))
            if "Bthval6" in data:
                self.windows.el_Bthval6.setCurrentIndex(
                    Bthval6.index(data["Bthval6"]))
            if "Bthval7" in data:
                self.windows.el_Bthval7.setCurrentIndex(
                    Bthval7.index(data["Bthval7"]))
            if "Bthval8" in data:
                self.windows.el_Bthval8.setCurrentIndex(
                    Bthval8.index(data["Bthval8"]))
            if "Bthval9" in data:
                self.windows.el_Bthval9.setCurrentIndex(
                    Bthval9.index(data["Bthval9"]))
            if "Bthval10" in data:
                self.windows.el_Bthval10.setCurrentIndex(
                    Bthval10.index(data["Bthval10"]))

            if "Bthpos1" in data:
                self.windows.el_Bthpos1.setCurrentIndex(
                    Bthpos1.index(data["Bthpos1"]))
            if "Bthpos2" in data:
                self.windows.el_Bthpos2.setCurrentIndex(
                    Bthpos2.index(data["Bthpos2"]))
            if "Bthpos3" in data:
                self.windows.el_Bthpos3.setCurrentIndex(
                    Bthpos3.index(data["Bthpos3"]))
            if "Bthpos4" in data:
                self.windows.el_Bthpos4.setCurrentIndex(
                    Bthpos4.index(data["Bthpos4"]))
            if "Bthpos5" in data:
                self.windows.el_Bthpos5.setCurrentIndex(
                    Bthpos5.index(data["Bthpos5"]))
            if "Bthpos6" in data:
                self.windows.el_Bthpos6.setCurrentIndex(
                    Bthpos6.index(data["Bthpos6"]))
            if "Bthpos7" in data:
                self.windows.el_Bthpos7.setCurrentIndex(
                    Bthpos7.index(data["Bthpos7"]))
            if "Bthpos8" in data:
                self.windows.el_Bthpos8.setCurrentIndex(
                    Bthpos8.index(data["Bthpos8"]))
            if "Bthpos9" in data:
                self.windows.el_Bthpos9.setCurrentIndex(
                    Bthpos9.index(data["Bthpos9"]))
            if "Bthpos10" in data:
                self.windows.el_Bthpos10.setCurrentIndex(
                    Bthpos10.index(data["Bthpos10"]))

            if "NPULSES_A" in data:
                self.windows.el_npulsesa.setCurrentIndex(
                    NPULSES_A.index(data["NPULSES_A"]))
            if "TMEAS_A" in data:
                self.windows.el_tmeasa.setCurrentIndex(
                    TMEAS_A.index(data["TMEAS_A"]))
            if "THSEL_A" in data:
                self.windows.el_thsela.setCurrentIndex(
                    THSEL_A.index(data["THSEL_A"]))

            if "NPULSES_B" in data:
                self.windows.el_npulsesb.setCurrentIndex(
                    NPULSES_B.index(data["NPULSES_B"]))
            if "TMEAS_B" in data:
                self.windows.el_tmeasb.setCurrentIndex(
                    TMEAS_B.index(data["TMEAS_B"]))
            if "THSEL_B" in data:
                self.windows.el_thselb.setCurrentIndex(
                    THSEL_B.index(data["THSEL_B"]))

            if "NPULSES_C" in data:
                self.windows.el_npulsesc.setCurrentIndex(
                    NPULSES_C.index(data["NPULSES_C"]))
            if "TMEAS_C" in data:
                self.windows.el_tmeasc.setCurrentIndex(
                    TMEAS_C.index(data["TMEAS_C"]))
            if "THSEL_C" in data:
                self.windows.el_thselc.setCurrentIndex(
                    THSEL_C.index(data["THSEL_C"]))

            if "STC_POS0" in data:
                self.windows.el_stcpos0.setCurrentIndex(
                    STC_POS0.index(data["STC_POS0"]))
            if "STC_POS1" in data:
                self.windows.el_stcpos1.setCurrentIndex(
                    STC_POS1.index(data["STC_POS1"]))
            if "STC_POS2" in data:
                self.windows.el_stcpos2.setCurrentIndex(
                    STC_POS2.index(data["STC_POS2"]))
            if "STC_POS3" in data:
                self.windows.el_stcpos3.setCurrentIndex(
                    STC_POS3.index(data["STC_POS3"]))
            if "STC_POS4" in data:
                self.windows.el_stcpos4.setCurrentIndex(
                    STC_POS4.index(data["STC_POS4"]))

            if "S_DAMP" in data:
                self.windows.el_sdamp.setCurrentIndex(
                    S_DAMP.index(data["S_DAMP"]))
            if "TSENS_Trim" in data:
                self.windows.el_tsenstrim.setCurrentIndex(
                    TSENS_Trim.index(data["TSENS_Trim"]))

            if "STC_GAIN0" in data:
                self.windows.el_stcgain0.setText(data["STC_GAIN0"])
            if "STC_GAIN1" in data:
                self.windows.el_stcgain1.setText(data["STC_GAIN1"])
            if "STC_GAIN2" in data:
                self.windows.el_stcgain2.setText(data["STC_GAIN2"])
            if "STC_GAIN3" in data:
                self.windows.el_stcgain3.setText(data["STC_GAIN3"])
            if "STC_GAIN4" in data:
                self.windows.el_stcgain4.setText(data["STC_GAIN4"])
            
            if "ECHO_DEB" in data:
                self.windows.el_echodeb.setText(data["ECHO_DEB"])
            if "RT_CFG" in data:
                self.windows.el_rtcfg.setText(data["RT_CFG"])
            if "NFTG" in data:
                self.windows.el_nftg.setText(data["NFTG"])
            if "FTC" in data:
                self.windows.el_ftc.setText(data["FTC"])
            if "EPD" in data:
                self.windows.el_epd.setText(data["EPD"])
            if "APD" in data:
                self.windows.el_apd.setText(data["APD"])
            if "FILTER_CFG" in data:
                self.windows.el_filtercfg.setText(data["FILTER_CFG"])
            if "ATG_CFG" in data:
                self.windows.el_atgcfg.setText(data["ATG_CFG"])
            if "ATG_TAU" in data:
                self.windows.el_atgtau.setText(data["ATG_TAU"])
            if "ATG_ALPHA" in data:
                self.windows.el_atgalpha.setText(data["ATG_ALPHA"])
            if "NSUPP_CFG" in data:
                self.windows.el_nsuppcfg.setText(data["NSUPP_CFG"])
            if "NOISE_CFG" in data:
                self.windows.el_noisecfg.setText(data["NOISE_CFG"])
            if "SCALE_REC" in data:
                self.windows.el_scalerec.setText(data["SCALE_REC"])
            if "STATUS_CFG" in data:
                self.windows.el_statuscfg.setText(data["STATUS_CFG"])

            if "CUSTOMER" in data:
                self.windows.el_customer.setText(data["CUSTOMER"])
            if "F_DR" in data:
                self.windows.el_fdr.setText(data["F_DR"])
            if "V_DRV" in data:
                self.windows.el_vdrv.setText(data["V_DRV"])
            if "G_ANA" in data:
                self.windows.el_gana.setText(data["G_ANA"])
            if "G_DIG" in data:
                self.windows.el_gdig.setText(data["G_DIG"])
            if "NFD_TOFF" in data:
                self.windows.el_nfdtoff.setText(data["NFD_TOFF"])
            if "NFD_THRES" in data:
                self.windows.el_nfdthres.setText(data["NFD_THRES"])
            if "NFD_WIN" in data:
                self.windows.el_nfdwin.setText(data["NFD_WIN"])
            if "OSC_TRIM" in data:
                self.windows.el_osctrim.setText(data["OSC_TRIM"])

    def elmos_initinalization(self):
        self.windows.el_tofcomp.setPlaceholderText("0")
        self.elmos_threshold_initinalization()
        self.profile_initinalization()
        self.sensitivity_initialization()
        self.measurement_initialization()
        self.EFROM_initialization()
        self.windows.el_completesetup.clicked.connect(self.send_EL)


    def elmos_threshold_initinalization(self):
        self.windows.el_Athval1.setCurrentIndex(31)
        self.windows.el_Athval1.addItems(Athval1)
        self.windows.el_Athval2.setCurrentIndex(15)
        self.windows.el_Athval2.addItems(Athval2)
        self.windows.el_Athval3.setCurrentIndex(15)
        self.windows.el_Athval3.addItems(Athval3)
        self.windows.el_Athval4.setCurrentIndex(15)
        self.windows.el_Athval4.addItems(Athval4)
        self.windows.el_Athval5.setCurrentIndex(15)
        self.windows.el_Athval5.addItems(Athval5)
        self.windows.el_Athval6.setCurrentIndex(15)
        self.windows.el_Athval6.addItems(Athval6)
        self.windows.el_Athval7.setCurrentIndex(15)
        self.windows.el_Athval7.addItems(Athval7)
        self.windows.el_Athval8.setCurrentIndex(15)
        self.windows.el_Athval8.addItems(Athval8)
        self.windows.el_Athval9.setCurrentIndex(15)
        self.windows.el_Athval9.addItems(Athval9)
        self.windows.el_Athval10.setCurrentIndex(0)
        self.windows.el_Athval10.addItems(Athval10)
        self.windows.el_Athpos1.setCurrentIndex(0)
        self.windows.el_Athpos1.addItems(Athpos1)
        self.windows.el_Athpos2.setCurrentIndex(1)
        self.windows.el_Athpos2.addItems(Athpos2)
        self.windows.el_Athpos3.setCurrentIndex(1)
        self.windows.el_Athpos3.addItems(Athpos3)
        self.windows.el_Athpos4.setCurrentIndex(1)
        self.windows.el_Athpos4.addItems(Athpos4)
        self.windows.el_Athpos5.setCurrentIndex(3)
        self.windows.el_Athpos5.addItems(Athpos5)
        self.windows.el_Athpos6.setCurrentIndex(3)
        self.windows.el_Athpos6.addItems(Athpos6)
        self.windows.el_Athpos7.setCurrentIndex(3)
        self.windows.el_Athpos7.addItems(Athpos7)
        self.windows.el_Athpos8.setCurrentIndex(4)
        self.windows.el_Athpos8.addItems(Athpos8)
        self.windows.el_Athpos9.setCurrentIndex(4)
        self.windows.el_Athpos9.addItems(Athpos9)
        self.windows.el_Athpos10.setCurrentIndex(4)
        self.windows.el_Athpos10.addItems(Athpos10)

        self.windows.el_Bthval1.setCurrentIndex(31)
        self.windows.el_Bthval1.addItems(Bthval1)
        self.windows.el_Bthval2.setCurrentIndex(10)
        self.windows.el_Bthval2.addItems(Bthval2)
        self.windows.el_Bthval3.setCurrentIndex(10)
        self.windows.el_Bthval3.addItems(Bthval3)
        self.windows.el_Bthval4.setCurrentIndex(10)
        self.windows.el_Bthval4.addItems(Bthval4)
        self.windows.el_Bthval5.setCurrentIndex(10)
        self.windows.el_Bthval5.addItems(Bthval5)
        self.windows.el_Bthval6.setCurrentIndex(10)
        self.windows.el_Bthval6.addItems(Bthval6)
        self.windows.el_Bthval7.setCurrentIndex(15)
        self.windows.el_Bthval7.addItems(Bthval7)
        self.windows.el_Bthval8.setCurrentIndex(31)
        self.windows.el_Bthval8.addItems(Bthval8)
        self.windows.el_Bthval9.setCurrentIndex(31)
        self.windows.el_Bthval9.addItems(Bthval9)
        self.windows.el_Bthval10.setCurrentIndex(31)
        self.windows.el_Bthval10.addItems(Bthval10)
        self.windows.el_Bthpos1.setCurrentIndex(0)
        self.windows.el_Bthpos1.addItems(Bthpos1)
        self.windows.el_Bthpos2.setCurrentIndex(1)
        self.windows.el_Bthpos2.addItems(Bthpos2)
        self.windows.el_Bthpos3.setCurrentIndex(1)
        self.windows.el_Bthpos3.addItems(Bthpos3)
        self.windows.el_Bthpos4.setCurrentIndex(1)
        self.windows.el_Bthpos4.addItems(Bthpos4)
        self.windows.el_Bthpos5.setCurrentIndex(3)
        self.windows.el_Bthpos5.addItems(Bthpos5)
        self.windows.el_Bthpos6.setCurrentIndex(3)
        self.windows.el_Bthpos6.addItems(Bthpos6)
        self.windows.el_Bthpos7.setCurrentIndex(3)
        self.windows.el_Bthpos7.addItems(Bthpos7)
        self.windows.el_Bthpos8.setCurrentIndex(4)
        self.windows.el_Bthpos8.addItems(Bthpos8)
        self.windows.el_Bthpos9.setCurrentIndex(4)
        self.windows.el_Bthpos9.addItems(Bthpos9)
        self.windows.el_Bthpos10.setCurrentIndex(4)
        self.windows.el_Bthpos10.addItems(Bthpos10)

    def profile_initinalization(self):
        self.windows.el_npulsesa.setCurrentIndex(3)
        self.windows.el_npulsesa.addItems(NPULSES_A)
        self.windows.el_tmeasa.setCurrentIndex(0)
        self.windows.el_tmeasa.addItems(TMEAS_A)
        self.windows.el_thsela.setCurrentIndex(0)
        self.windows.el_thsela.addItems(THSEL_A)

        self.windows.el_npulsesb.setCurrentIndex(0)
        self.windows.el_npulsesb.addItems(NPULSES_B)
        self.windows.el_tmeasb.setCurrentIndex(0)
        self.windows.el_tmeasb.addItems(TMEAS_B)
        self.windows.el_thselb.setCurrentIndex(0)
        self.windows.el_thselb.addItems(THSEL_B)

        self.windows.el_npulsesc.setCurrentIndex(5)
        self.windows.el_npulsesc.addItems(NPULSES_C)
        self.windows.el_tmeasc.setCurrentIndex(0)
        self.windows.el_tmeasc.addItems(TMEAS_C)
        self.windows.el_thselc.setCurrentIndex(0)
        self.windows.el_thselc.addItems(THSEL_C)

    def sensitivity_initialization(self):
        self.windows.el_stcpos0.setCurrentIndex(0)
        self.windows.el_stcpos0.addItems(STC_POS0)
        self.windows.el_stcpos1.setCurrentIndex(0)
        self.windows.el_stcpos1.addItems(STC_POS0)
        self.windows.el_stcpos2.setCurrentIndex(0)
        self.windows.el_stcpos2.addItems(STC_POS0)
        self.windows.el_stcpos3.setCurrentIndex(0)
        self.windows.el_stcpos3.addItems(STC_POS0)
        self.windows.el_stcpos4.setCurrentIndex(0)
        self.windows.el_stcpos4.addItems(STC_POS0)

        self.windows.el_stcgain0.setPlaceholderText("0")
        self.windows.el_stcgain1.setPlaceholderText("8")
        self.windows.el_stcgain2.setPlaceholderText("8")
        self.windows.el_stcgain3.setPlaceholderText("8")
        self.windows.el_stcgain4.setPlaceholderText("7")

    def measurement_initialization(self):
        self.windows.el_echodeb.setPlaceholderText("0")
        self.windows.el_rtcfg.setPlaceholderText("0")
        self.windows.el_nftg.setPlaceholderText("1")
        self.windows.el_ftc.setPlaceholderText("0")
        self.windows.el_epd.setPlaceholderText("1")
        self.windows.el_apd.setPlaceholderText("0")
        self.windows.el_filtercfg.setPlaceholderText("0")
        self.windows.el_atgcfg.setPlaceholderText("1")
        self.windows.el_atgtau.setPlaceholderText("0")
        self.windows.el_atgalpha.setPlaceholderText("1")
        self.windows.el_nsuppcfg.setPlaceholderText("0")
        self.windows.el_noisecfg.setPlaceholderText("1")
        self.windows.el_scalerec.setPlaceholderText("0")
        self.windows.el_statuscfg.setPlaceholderText("1")

    def EFROM_initialization(self):
        self.windows.el_customer.setPlaceholderText("0")
        self.windows.el_fdr.setPlaceholderText("61")
        self.windows.el_vdrv.setPlaceholderText("7")
        self.windows.el_gana.setPlaceholderText("4")
        self.windows.el_gdig.setPlaceholderText("0")
        self.windows.el_nfdtoff.setPlaceholderText("4")
        self.windows.el_nfdthres.setPlaceholderText("4")
        self.windows.el_nfdwin.setPlaceholderText("2")
        self.windows.el_osctrim.setPlaceholderText("0")
        self.windows.el_sdamp.setCurrentIndex(0)
        self.windows.el_sdamp.addItems(S_DAMP)
        self.windows.el_tsenstrim.setCurrentIndex(0)
        self.windows.el_tsenstrim.addItems(TSENS_Trim)
        
        
