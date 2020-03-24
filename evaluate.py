# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluate.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from score import Ui_Dialog as Score
import sqlite3
data = sqlite3.connect("database.db")
datacur = data.cursor()


class Ui_evaluate_team(object):
    def __init__(self):
        self.score_Window = QtWidgets.QMainWindow()
        self.score_screen = Score()
        self.score_screen.setupUi(self.score_Window)

    def setupUi(self, evaluate_team):
        evaluate_team.setObjectName("evaluate_team")
        evaluate_team.resize(609, 472)
        self.label = QtWidgets.QLabel(evaluate_team)
        self.label.setGeometry(QtCore.QRect(200, 10, 391, 51))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(69)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.teamdrop = QtWidgets.QComboBox(evaluate_team)
        self.teamdrop.setGeometry(QtCore.QRect(90, 70, 151, 31))
        self.teamdrop.setCurrentText("")
        self.teamdrop.setObjectName("teamdrop")
        self.matchdrop = QtWidgets.QComboBox(evaluate_team)
        self.matchdrop.setEnabled(True)
        self.matchdrop.setGeometry(QtCore.QRect(350, 70, 151, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.matchdrop.setFont(font)
        self.matchdrop.setObjectName("matchdrop")
        self.matchdrop.addItem("")
        self.matchdrop.addItem("")
        self.line = QtWidgets.QFrame(evaluate_team)
        self.line.setGeometry(QtCore.QRect(40, 95, 551, 41))
        self.line.setStyleSheet("color: rgb(0, 0, 0);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(evaluate_team)
        self.label_2.setGeometry(QtCore.QRect(130, 130, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(evaluate_team)
        self.label_3.setGeometry(QtCore.QRect(400, 130, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Calculate = QtWidgets.QPushButton(evaluate_team)
        self.Calculate.setEnabled(True)
        self.Calculate.setGeometry(QtCore.QRect(240, 410, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(69)
        self.Calculate.setFont(font)
        self.Calculate.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Calculate.setAutoDefault(False)
        self.Calculate.setObjectName("Calculate")
        self.playerlist = QtWidgets.QListWidget(evaluate_team)
        self.playerlist.setGeometry(QtCore.QRect(50, 160, 221, 241))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(69)
        self.playerlist.setFont(font)
        self.playerlist.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.playerlist.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.playerlist.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.playerlist.setObjectName("playerlist")
        self.pointlist = QtWidgets.QListWidget(evaluate_team)
        self.pointlist.setGeometry(QtCore.QRect(320, 160, 211, 241))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(69)
        self.pointlist.setFont(font)
        self.pointlist.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.pointlist.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.pointlist.setObjectName("pointlist")

        self.retranslateUi(evaluate_team)
        QtCore.QMetaObject.connectSlotsByName(evaluate_team)

        self.Calculate.clicked.connect(self.final_score)
        selected_team = self.teamdrop.currentText()

        self.changedname(selected_team)

        self.teamdrop.currentTextChanged.connect(self.changedname)

    def retranslateUi(self, evaluate_team):
        _translate = QtCore.QCoreApplication.translate
        evaluate_team.setWindowTitle(_translate("evaluate_team", "Dialog"))
        self.label.setText(_translate("evaluate_team", "Evaluate Scores"))
        self.matchdrop.setItemText(0, _translate("evaluate_team", "select match"))
        self.matchdrop.setItemText(1, _translate("evaluate_team", "Match1"))
        self.label_2.setText(_translate("evaluate_team", "Players"))
        self.label_3.setText(_translate("evaluate_team", "Points"))
        self.Calculate.setStatusTip(_translate("evaluate_team", "calculating score"))
        self.Calculate.setText(_translate("evaluate_team", "Calculate"))
        self.Calculate.setShortcut(_translate("evaluate_team", "Return"))

        getTeamNames = datacur.execute("SELECT  DISTINCT name from teams;")
        teams = getTeamNames.fetchall()
        for team in teams:
            self.teamdrop.addItem(team[0])


    def changedname(self, t):
        self.playerlist.clear()
        self.pointlist.clear()
        getPlayer = datacur.execute("SELECT players from teams WHERE name='" + t + "';")
        players = getPlayer.fetchall()
        for player in players:
            self.playerlist.addItem(player[0])
        getPlayerVal = datacur.execute("SELECT value from teams WHERE name='" + t + "';")
        values = getPlayerVal.fetchall()
        for value in values:
            self.pointlist.addItem(str(value[0]))


    def final_score(self):
        total_score = 0
        getVal = datacur.execute("SELECT value from teams WHERE name='" + self.teamdrop.currentText() + "';")
        values = getVal.fetchall()
        for value in values:
            total_score += value[0]
        self.score_screen.finalscore.setText(str(total_score))
        self.score_Window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    evaluate_team = QtWidgets.QDialog()
    ui = Ui_evaluate_team()
    ui.setupUi(evaluate_team)
    evaluate_team.show()
    sys.exit(app.exec_())
