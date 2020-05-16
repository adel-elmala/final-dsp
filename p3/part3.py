#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 19:41:34 2020

@author: yossef
"""

from PyQt5 import QtWidgets
from design import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
import sys


from playsound import playsound
import numpy as np
from scipy.io import wavfile

#import stdarray


class ApplicationWindow(QtWidgets.QMainWindow):
    sampleRate = 44100
    length = 1
    
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

   
    def Csound(self):
        self.frequency=430.81
        self.PianoSound(self.frequency)

    def Dsound(self):
        self.frequency=546.83
        self.PianoSound(self.frequency)

    def Esound(self):
        self.frequency=664.81
        self.PianoSound(self.frequency)

    def Fsound(self):
        self.frequency=694.61
        self.PianoSound(self.frequency)

    def Gsound(self):
        self.frequency=736
        self.PianoSound(self.frequency)

    def Asound(self):
        self.frequency=780
        self.PianoSound(self.frequency)

    def Bsound(self):
        self.frequency=846.93
        self.PianoSound(self.frequency)
    def C1sound(self):
        self.frequency=891.63
        self.PianoSound(self.frequency)
    def D1sound(self):
        self.frequency=953.66
        self.PianoSound(self.frequency)
    def E1sound(self):
        self.frequency=1000.63
        self.PianoSound(self.frequency)
    def F1sound(self):
        self.frequency=1049.23
        self.PianoSound(self.frequency)
    def G1sound(self):
        self.frequency=1100
        self.PianoSound(self.frequency)
    def A1sound(self):
        self.frequency=1160
        self.PianoSound(self.frequency)
    def B1sound(self):
        self.frequency=1233.88
        self.PianoSound(self.frequency)


    def PianoSound(self,frequency):
        time = np.linspace(0, self.length, self.sampleRate * self.length)  
        Y = np.sin(2 * np.pi * self.frequency * time) * np.exp(-0.0004 * 2 * np.pi * self.frequency * time)
        Y += np.sin(2 * 2 * np.pi * self.frequency * time) * np.exp(-0.0004 * 2 * np.pi * self.frequency * time) / 2
        Y += np.sin(3 * 2 * np.pi * self.frequency * time) * np.exp(-0.0004 * 2 * np.pi * self.frequency * time) / 4
        Y += np.sin(4 * 2 * np.pi * self.frequency * time) * np.exp(-0.0004 * 2 * np.pi * self.frequency * time) / 8
        Y += np.sin(5 * 2 * np.pi * self.frequency * time) * np.exp(-0.0004 * 2 * np.pi * self.frequency * time) / 16
        Y += np.sin(6 * 2 * np.pi * self.frequency * time) * np.exp(-0.0004 * 2 * np.pi * self.frequency * time) / 32
        Y += Y * Y * Y
        Y *= 1 + 16 * time * np.exp(-6 * time)
        
        wavfile.write('Piano.wav', self.sampleRate, Y)
        playsound('Piano.wav')
    def Eguitar(self):
        self.frequency=329.63
        self.GuitarSound(self.frequency)
    def Bguitar(self):
        self.frequency=246.94
        self.GuitarSound(self.frequency)
    def Gguitar(self):
        self.frequency=196
        self.GuitarSound(self.frequency)
    def Dguitar(self):
        self.frequency=146.83
        self.GuitarSound(self.frequency)
    def Aguitar(self):
        self.frequency=110
        self.GuitarSound(self.frequency)
    def E2guitar(self):
        self.frequency=82.41
        self.GuitarSound(self.frequency)
    
    def GuitarSound(self,frequency):
        samples = []
        current_sample = 0
        previous_value = 0
        
        wavetable_size = self.sampleRate// int(self.frequency)
        wavetable = (2 * np.random.randint(0, 2, wavetable_size) - 1).astype(np.float)
        n_samples=self.sampleRate*2
        while len(samples) < n_samples:
            wavetable[current_sample] = 0.5 * (wavetable[current_sample] + previous_value)
            samples.append(wavetable[current_sample])
            previous_value = samples[-1]
            current_sample += 1
            current_sample = current_sample % wavetable.size
        data=np.array(samples)
        wavfile.write('guitar.wav', self.sampleRate, data)
        playsound('guitar.wav')

            





            
def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()

    application.ui.Eg.clicked.connect(application.Eguitar)
    application.ui.Bg.clicked.connect(application.Bguitar)
    application.ui.Gg.clicked.connect(application.Gguitar)
    application.ui.Dg.clicked.connect(application.Dguitar)
    application.ui.Ag.clicked.connect(application.Aguitar)
    application.ui.Eg_2.clicked.connect(application.E2guitar)
 
    
    application.ui.C.clicked.connect(application.Csound)
    application.ui.D.clicked.connect(application.Dsound)    
    application.ui.E.clicked.connect(application.Esound)
    application.ui.F.clicked.connect(application.Fsound)
    application.ui.G.clicked.connect(application.Gsound)
    application.ui.A.clicked.connect(application.Asound)
    application.ui.B.clicked.connect(application.Bsound)
    application.ui.C1.clicked.connect(application.C1sound)
    application.ui.D1.clicked.connect(application.D1sound)    
    application.ui.E1.clicked.connect(application.E1sound)
    application.ui.F1.clicked.connect(application.F1sound)
    application.ui.G1.clicked.connect(application.G1sound)
    application.ui.A1.clicked.connect(application.A1sound)
    application.ui.B1.clicked.connect(application.B1sound)




    application.show()
    app.exec_()


if __name__ == "__main__":
    main()