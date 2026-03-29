from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, 
    QWidget, 
    QPushButton, 
    QLabel, 
    QVBoxLayout, 
    QHBoxLayout, 
    QMessageBox, 
    QRadioButton,
    QGroupBox,
    QButtonGroup)

from random import shuffle
import sys

class Question():
    def __init__(self, question, rightAns, wrongAns1, wrongAns2, wrongAns3):
        self.question = question
        self.rightAns = rightAns
        self.wrongAns1 = wrongAns1
        self.wrongAns2 = wrongAns2
        self.wrongAns3 = wrongAns3

q1 = Question('Что такое PEP 8?', 'рекомендации по написанию кода', 'вывод hello world', 'вывод рандомного числа', 'input(Введите имя)')
q2 = Question('Может ли быть индекс списка отрицательным?', 'да', 'нет', 'нет верного ответа', 'не знаю')
q3 = Question('Что значит конструкция pass?', 'пустой оператор/затычка', 'вывод hello', 'рандомное число', 'не знаю')
q4 = Question('Как просмотреть методы объекта?', 'dir()', 'list()', 'нет верного ответа', 'не знаю')
q5 = Question('Python полностью поддерживает ООП?', 'да', 'нет', 'нет верного ответа', 'не знаю')
q6 = Question('Зачем в Python используется ключевое слово self?', 'обращения к текущему объекту класса', 'просто чтобы было', 'нет верного ответа', 'не знаю')
q7 = Question('Что может быть ключом в словаре', 'любой неизменяемый объект', 'все что хочу', 'нет верного ответа', 'не знаю')
q8 = Question('Для чего используется функция __init__?', 'Функция __init__ является конструктором класса', 'что-то связано с классом', 'нет верного ответа', 'не знаю')
q9 = Question('Какой функции нет в Python?', 'output', 'input', 'print', 'len')
question_list = list()
question_list.append(q1)
question_list.append(q2)
question_list.append(q3)
question_list.append(q4)
question_list.append(q5)
question_list.append(q6)
question_list.append(q7)
question_list.append(q8)
question_list.append(q9)
question_list
shuffle(question_list)




# глобальные переменные
font_size = 16
question_counter = 0
n = len(question_list)
right = 0
wrong = 0
total = 0

def ask(q):
    global answers, question
    shuffle(answers)
    question.setText(q.question)
    answers[0].setText(q.rightAns)
    answers[1].setText(q.wrongAns1)
    answers[2].setText(q.wrongAns2)
    answers[3].setText(q.wrongAns3)

def check_answer():
    global answers, res_label, right_ans, right, wrong, total
    if answers[0].isChecked():
        total += 1
        right += 1
        res_label.setText('правильно 🎉🎉🎉')
        right_ans.setText(f'Правильный ответ: {answers[0].text()}\nПравильно: {right}\nНеправильно: {wrong}\nСтатистика: {round(right/total*100, 2)}%')
    else:
        total += 1
        wrong += 1
        res_label.setText('неправильно 😢😢😢')
        right_ans.setText(f'Правильный ответ: {answers[0].text()}\nПравильно: {right}\nНеправильно: {wrong}\nСтатистика: {round(right/total*100, 2)}%')


def btn_click():
    global question_counter
    if btn.text() == 'Ответить':
        if rbtn1.isChecked() or rbtn2.isChecked() or rbtn3.isChecked() or rbtn4.isChecked():
            check_answer()
            RadioGroupBox.hide()
            AnsGroupBox.show()
            if question_counter == n:
                btn.setText('Завершить')
            else:
                btn.setText('Далее')
        else:
            pass
    elif btn.text() == 'Далее':
        if question_counter < n:
            ask(question_list[question_counter])
            question_counter += 1
            uncheck()
            AnsGroupBox.hide()
            RadioGroupBox.show()
            btn.setText('Ответить')
        else:
            pass
    elif btn.text() == 'Завершить':
        sys.exit()

def uncheck():
    btn_group.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    btn_group.setExclusive(True)

app = QApplication([])
desktop = app.desktop() # данные монитора
main_win = QWidget()
main_win.setStyleSheet("background-image: url(bgi.jpg)")
main_win.resize(int(desktop.width() * 0.65), int(desktop.height() * 0.65)) # рассчет размера
main_win.setWindowTitle('MemoryCard')

question = QLabel('Какой национальности не существует?')
question.setStyleSheet(f"font-size: {font_size}pt;")
btn = QPushButton('Ответить')
btn.setStyleSheet(f"font-size: {font_size}pt;")

RadioGroupBox = QGroupBox('варианты ответов')
RadioGroupBox.setStyleSheet(f"font-size: {font_size}pt;")
btn_group = QButtonGroup()
rbtn1 = QRadioButton('Энцы')
rbtn1.setStyleSheet(f"font-size: {font_size}pt;")
rbtn2 = QRadioButton('Смурфы')
rbtn2.setStyleSheet(f"font-size: {font_size}pt;")
rbtn3 = QRadioButton('Чулымцы')
rbtn3.setStyleSheet(f"font-size: {font_size}pt;")
rbtn4 = QRadioButton('Алеуты')
rbtn4.setStyleSheet(f"font-size: {font_size}pt;")
btn_group.addButton(rbtn1)
btn_group.addButton(rbtn2)
btn_group.addButton(rbtn3)
btn_group.addButton(rbtn4)

answers = [rbtn1, rbtn2, rbtn3, rbtn4]

main_line = QVBoxLayout()
line1 = QHBoxLayout()
line2 = QVBoxLayout()
line3 = QVBoxLayout()
line2.addWidget(rbtn1, alignment=Qt.AlignLeft)
line2.addWidget(rbtn2, alignment=Qt.AlignLeft)
line3.addWidget(rbtn3, alignment=Qt.AlignLeft)
line3.addWidget(rbtn4, alignment=Qt.AlignLeft)
line1.addLayout(line2)
line1.addLayout(line3)
RadioGroupBox.setLayout(line1)

AnsGroupBox = QGroupBox('результат теста')
AnsGroupBox.setStyleSheet(f"font-size: {font_size}pt;")
res_label = QLabel('правильно/неправильно')
res_label.setStyleSheet(f"font-size: {font_size}pt;")
right_ans = QLabel('правильный ответ')
right_ans.setStyleSheet(f"font-size: {font_size}pt;")
line = QVBoxLayout()
res_line = QHBoxLayout()
right_ans_line = QHBoxLayout()
res_line.addWidget(res_label, alignment=Qt.AlignLeft)
right_ans_line.addWidget(right_ans, alignment=Qt.AlignCenter)
line.addLayout(res_line)
line.addLayout(right_ans_line)
AnsGroupBox.setLayout(line)
AnsGroupBox.hide()

main_line.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
main_line.addWidget(RadioGroupBox)
main_line.addWidget(AnsGroupBox)
main_line.addWidget(btn, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
main_win.setLayout(main_line)

ask(question_list[question_counter])
question_counter += 1
btn.clicked.connect(btn_click)

main_win.show()
app.exec_()
