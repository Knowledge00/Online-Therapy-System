from PyQt5 import QtCore, QtGui, QtWidgets
from subprocess import call
import matplotlib.pyplot as plt
import sqlite3
import sys
from datetime import date
name_of_program = sys.argv[0]
UID = sys.argv[1]
UID = int(UID)

class Ui_MindServe(object):
    def __init__(self):
        MindServe.setWindowTitle("MindServe - Symptom Tracker")
        MindServe.resize(1000, 650)
        self.centralwidget = QtWidgets.QWidget(MindServe)
        self.dial = QtWidgets.QDial(self.centralwidget)
        self.Save = QtWidgets.QPushButton(self.centralwidget)
        self.progress = QtWidgets.QPushButton(self.centralwidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.chat = QtWidgets.QPushButton(self.centralwidget)

    def Style(self):
        self.Save.setStyleSheet("background-color: white;"
                                "border-style: outset;"
                                "border-width: 2px;"
                                "border-radius: 30px;"
                                "border-color: black;"
                                "padding: 14px;")
        self.progress.setStyleSheet("background-color: white;\n"
                                    "border-style: outset;"
                                    "border-width: 2px;"
                                    "border-radius: 30px;"
                                    "border-color: black;"
                                    "padding: 14px;")
        self.chat.setStyleSheet("background-color: white;\n"
                                "border-style: outset;"
                                "border-width: 2px;"
                                "border-radius: 30px;"
                                "border-color: black;"
                                "padding: 14px;")

    def Tracker(self, MindServe):
        self.dial.setGeometry(QtCore.QRect(320, 300, 360, 295))
        self.dial.setStyleSheet("background-color: rgb(146, 101, 202)")
        self.dial.setMinimum(1)
        self.dial.setMaximum(10)
        self.value = self.dial.value()
        self.label.setGeometry(QtCore.QRect(0, 0, 1000, 650))
        self.label.setPixmap(QtGui.QPixmap("Symptom.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.Save.setGeometry(QtCore.QRect(791, 530, 171, 71))
        self.Save.setText("Save")
        self.Save.clicked.connect(self.SaveRating)
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(14)
        self.Save.setFont(font)
        self.Save.setIconSize(QtCore.QSize(20, 20))
        self.progress.setGeometry(QtCore.QRect(70, 445, 171, 81))
        self.progress.setText("View my progress")
        self.font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(12)
        self.progress.setFont(font)
        self.progress.setIconSize(QtCore.QSize(20, 20))
        self.progress.setObjectName("progress")
        self.progress.clicked.connect(self.ProgressView)
        self.chat.setGeometry(QtCore.QRect(70, 325, 171, 71))
        self.chat.setText("Chat")
        self.chat.clicked.connect(self.Chat_Clicked)
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(14)
        self.chat.setFont(font)
        self.chat.setIconSize(QtCore.QSize(20, 20))
        self.chat.setObjectName("chat")
        self.label.raise_()
        self.dial.raise_()
        self.Save.raise_()
        self.progress.raise_()
        self.chat.raise_()
        MindServe.setCentralWidget(self.centralwidget)

    def Chat_Clicked(self):
        call(["python", "Chat.py"]) #chat is on a seperate python file

    def ProgressView(self):
        self.data = sqlite3.connect('NEA.A.db')
        self.Collecting = self.data.execute('SELECT Rating, Date FROM SymptomT WHERE UserID = "%s"' %(UID))
        self.dates = []
        self.Ratings = []
        for t in self.Collecting:
                self.Ratings.append(t[0])
                self.dates.append(t[1])
        plt.plot(self.dates, self.Ratings)
        plt.title('MindServe - Your Tracker')
        plt.xlabel('Date')
        plt.ylabel('Rating')
        plt.show()

    def SaveRating(self):
        self.value = self.dial.value()
        self.today = date.today()
        TD = self.today.strftime("%d/%m/%Y")
        self.data = sqlite3.connect('NEA.A.db')
        self.Collecting = self.data.execute('''SELECT Date,UserID FROM SymptomT WHERE UserID = "%s" and Date = "%s"'''%(UID,TD))
        if self.Collecting.fetchone():
            self.data.execute('''UPDATE SymptomT SET Rating = "%s" WHERE UserID = "%s" and Date = "%s"'''%(self.value,UID,TD))
        else:
            self.data.execute('''INSERT INTO SymptomT VALUES(:UserID, :Date, :Rating)''',
                            {
                            "UserID": UID,
                            "Date": TD,
                            "Rating": self.value
                            }
                        )
        self.data.commit()
        self.data.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MindServe = QtWidgets.QMainWindow()
    Symptom = Ui_MindServe()
    Symptom.Tracker(MindServe)
    Symptom.Style()
    MindServe.show()
    sys.exit(app.exec_())
