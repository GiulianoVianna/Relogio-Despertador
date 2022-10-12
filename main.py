import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import  QTimer, QTime
from PyQt5.uic import loadUi
from playsound import playsound

### Classe tela - form ui com timer
class tela(QMainWindow):
    def __init__(self):
        super(tela, self).__init__()
        loadUi('relogio.ui', self)
        timer = QTimer(self)
        timer.timeout.connect(self.lcd_time)
        timer.start(1000)
        self.bt_parar.clicked.connect(self.parar)

    ### Função lcd_time - Atualiza display e define horário do despertador
    def lcd_time(self):
        tempo_corrente = QTime.currentTime()
        display = tempo_corrente.toString('hh:mm:ss')
        self.lcdNumber.display(display)

        temp_horas = tempo_corrente.toString('hh:mm')
        horas = self.cb_horas.currentText() + ":" + self.cb_minutos.currentText()
        
        if horas == temp_horas:
            playsound("sino.mp3")

    ### Função parar - Reseta horário do despertador   
    def parar(self):
        if self.cb_horas.currentText() + ":" + self.cb_minutos.currentText() == "00:00":
            item1 = "01"
            self.cb_horas.setCurrentText(item1)
            self.cb_minutos.setCurrentText(item1) 
        else:
            item2 = "00"
            self.cb_horas.setCurrentText(item2)
            self.cb_minutos.setCurrentText(item2)    


app = QApplication(sys.argv)
main = tela()
main.show()
sys.exit(app.exec_())
