import pickle
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import os
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl

print(os.path.realpath(__file__))
dirname, filename = os.path.split(os.path.realpath(__file__))
print(dirname)
Form, Window = uic.loadUiType(dirname + "\\MyApp.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()


def save_to_file():
    global start_date, calc_date, description, dirname
    data_to_save = {"start": start_date, "end": calc_date, "desc": description}
    file1 = open(dirname + "\\config.txt", "wb")
    pickle.dump(data_to_save, file1)
    file1.close()


def save2_to_file():
    global start_date, calc_date, description, dirname
    data_to_save2 = {"start": start_date, "end": calc_date, "desc": description}
    file2 = open(dirname + "\\config2.txt", "wb")
    pickle.dump(data_to_save2, file2)
    file2.close()


def read_from_file():
    global start_date, calc_date, description, now_date, dirname
    try:
        file1 = open(dirname + "\\config.txt", "rb")
        data_to_load = pickle.load(file1)
        file1.close()
        start_date = data_to_load["start"]
        calc_date = data_to_load["end"]
        description = data_to_load["desc"]
        print(start_date.toString('dd-MM-yyyy'), calc_date.toString('dd-MM-yyyy'), description)
        form.calendarWidget_2.setSelectedDate(calc_date)
        form.dateEdit_2.setDate(calc_date)
        form.plainTextEdit_2.setPlainText(description)
        delta_days_left = start_date.daysTo(now_date)  # прошло дней
        delta_days_right = now_date.daysTo(calc_date)  # осталось дней
        days_total = start_date.daysTo(calc_date)  # всего дней
        print("$$$$: ", delta_days_left, delta_days_right, days_total)
        procent = (100 - ((delta_days_right - delta_days_left) // days_total)  * 100)
        print("%%%: ",  procent)
        form.progressBar.setValue(100 - procent)
    except:
        print("Не могу прочитать файл конфигурации (Может его нет )))!)")


def read2_from_file():
    global start_date, calc_date, description, now_date, dirname
    try:
        file2 = open(dirname + "\\config2.txt", "rb")
        data_to_load = pickle.load(file2)
        file2.close()
        start_date = data_to_load["start"]
        calc_date = data_to_load["end"]
        description = data_to_load["desc"]
        print(start_date.toString('dd-MM-yyyy'), calc_date.toString('dd-MM-yyyy'), description)
        form.calendarWidget.setSelectedDate(calc_date)
        form.dateEdit.setDate(calc_date)
        form.plainTextEdit.setPlainText(description)
        delta_days_left = start_date.daysTo(now_date)  # прошло дней
        delta_days_right = now_date.daysTo(calc_date)  # осталось дней
        days_total = start_date.daysTo(calc_date)  # всего дней
        print("$$$$: ", delta_days_left, delta_days_right, days_total)
        procent = ((delta_days_right - delta_days_left) // days_total)  * 100
        print(procent)
        form.progressBar.setValue(100 - procent)
    except:
        print("Не могу прочитать файл конфигурации 2 (Может его нет )))!)")


def on_click2():
    global calc_date, description, start_date
    start_date = now_date
    calc_date = form.calendarWidget.selectedDate()
    description = form.plainTextEdit.toPlainText()

    print("Clicked2!!!")
    save2_to_file()


def on_click():
    global calc_date, description, start_date
    start_date = now_date
    calc_date = form.calendarWidget_2.selectedDate()
    description = form.plainTextEdit_2.toPlainText()

    delta_days_left = start_date.daysTo(now_date)  # прошло дней
    delta_days_right = now_date.daysTo(calc_date)  # осталось дней
    days_total = start_date.daysTo(calc_date)  # всего дней
    print("$$$$: ", delta_days_left, delta_days_right, days_total)
    procent = int(delta_days_left * 100 / days_total)
    print(procent)
    form.progressBar.setProperty("value", procent)

    print("Clicked!!!")
    save_to_file()


def on_click2():
    global calc_date, description, start_date
    start_date = now_date
    calc_date = form.calendarWidget.selectedDate()
    description = form.plainTextEdit.toPlainText()

    print("Clicked!!!")
    save2_to_file()


def on_click_calendar():
    global start_date, calc_date
    form.dateEdit.setDate(form.calendarWidget.selectedDate())
    calc_date = form.calendarWidget.selectedDate()
    delta_days = start_date.daysTo(calc_date)
    print(delta_days)


def on_click_calendar2():
    global start_date, calc_date
    form.dateEdit_2.setDate(form.calendarWidget_2.selectedDate())
    calc_date = form.calendarWidget_2.selectedDate()
    delta_days = start_date.daysTo(calc_date)
    print(delta_days)
    form.label_11.setText("До наступления события осталось: %s дней!)" % delta_days)


def on_dateedit_change():
    global start_date, calc_date
    # print(form.dateEdit.dateTime().toString('dd-MM-yyyy'))
    form.calendarWidget.setSelectedDate(form.dateEdit.date())
    calc_date = form.dateEdit.date()
    delta_days = start_date.daysTo(calc_date)
    print(delta_days)


def on_dateedit_change2():
    global start_date, calc_date
    # print(form.dateEdit.dateTime().toString('dd-MM-yyyy'))
    form.calendarWidget_2.setSelectedDate(form.dateEdit_2.date())
    calc_date = form.dateEdit_2.date()
    delta_days = start_date.daysTo(calc_date)
    print(delta_days)
    form.label_11.setText("До наступления события осталось: %s дней!)" % delta_days)


def exit_btn():
    print("Кнопка выхода нажата.")
    exit()


form.pushButton_4.clicked.connect(on_click)
form.pushButton.clicked.connect(on_click2)
form.pushButton_2.clicked.connect(exit_btn)
form.pushButton_4.clicked.connect(read_from_file)
form.pushButton_4.clicked.connect(read2_from_file)


form.calendarWidget.clicked.connect(on_click_calendar)
form.dateEdit.dateChanged.connect(on_dateedit_change)
form.calendarWidget_2.clicked.connect(on_click_calendar2)
form.dateEdit_2.dateChanged.connect(on_dateedit_change2)



start_date = form.calendarWidget_2.selectedDate()
now_date = form.calendarWidget_2.selectedDate()
calc_date = form.calendarWidget_2.selectedDate()
description = form.plainTextEdit_2.toPlainText()

read_from_file()
read2_from_file()

media_player = QMediaPlayer()
url = QUrl.fromLocalFile("audio.wav.mp3")
content = QMediaContent(url)
media_player.setMedia(content)
media_player.play()

app.exec_()
