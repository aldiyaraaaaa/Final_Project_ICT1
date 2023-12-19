from tkinter import *
import random

root = Tk()
root.title('Игра в угадайку чисел')
root.geometry('1000x1000')
root.resizable(height=False, width=False)
root['bg'] = 'black'

подсказки_легкий = ["Попробуй число между 1 и 5", "Это число находится в диапазоне от 1 до 12", "Как насчет числа 3?"]
подсказки_средний = ["Это число больше или равно 15", "Число нечетное", "Мы выбрали число от 1 до 31"]

def начать_игру(диапазон, макс_попыток, подсказки):
    global загаданное_число, оставшиеся_попытки
    загаданное_число = random.randint(1, диапазон)
    оставшиеся_попытки = макс_попыток
    случайная_подсказка = random.choice(подсказки)
    label.config(text=f'{случайная_подсказка} (осталось попыток: {оставшиеся_попытки})', fg='white')
    entry.config(state='normal')
    кнопка_проверки.config(state='normal')

def проверить_число():
    global оставшиеся_попытки
    попытка = entry.get()

    try:
        попытка = int(попытка)
    except ValueError:
        label.config(text='Пожалуйста, введите число', fg='red')
        return

    оставшиеся_попытки -= 1

    if попытка == загаданное_число:
        label.config(text=f'Поздравляю! Ты угадал число {загаданное_число}', fg='green')
        entry.config(state='disabled')
        кнопка_проверки.config(state='disabled')
    elif оставшиеся_попытки == 0:
        label.config(text=f'Игра окончена. Загаданное число было {загаданное_число}', fg='red')
        entry.config(state='disabled')
        кнопка_проверки.config(state='disabled')
    else:
        подсказка = "больше" if попытка < загаданное_число else "меньше"
    label.config(text=f'Попробуй еще раз. Загаданное число {подсказка} чем {попытка}. (осталось попыток: {оставшиеся_попытки})', fg='red')
label = Label(root, text='Добро пожаловать в игру!', font='Arial 15', bg='black', fg='white')
label.pack()
entry = Entry(root, font='Arial 15', state='disabled')
entry.pack(pady=10)
кнопка_легкий = Button(root, text="Легкий уровень (1-12)", command=lambda: начать_игру(12, 4, подсказки_легкий), font='Arial 15')
кнопка_легкий.pack()
кнопка_средний = Button(root, text="Средний уровень (1-31)", command=lambda: начать_игру(31, 6, подсказки_средний), font='Arial 15')
кнопка_средний.pack()
кнопка_проверки = Button(root, text="Проверить", command=проверить_число, font='Arial 15', state='disabled')
кнопка_проверки.pack()
root.mainloop()
