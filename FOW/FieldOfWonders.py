import pandas as pd
import random as rnd
import tkinter as tk
from tkinter import messagebox
global main_window
main_window = tk.Tk()


def window():
    list_of_challengers = pd.read_excel('./challengers.xls', engine='openpyxl')
    names_list = list_of_challengers['Участники'].tolist()
    sales_list = list_of_challengers['Услуги'].tolist()
    main_window.title('Поле Чудес!')
    main_window.resizable(width=False, height=False)
    main_window.iconbitmap('./logo.ico')
    frame_names = tk.Frame(master=main_window)
    for i in range(0, len(names_list)+1):
        for j in range(2):
            if i == 0 and j == 0:
                tk.Label(
                    master=frame_names,
                    text='Участники',
                    font=('Arial', 15, 'bold'),
                    relief='ridge',
                    width=20
                ).grid(row=0, column=0)
            if i == 0 and j == 1:
                tk.Label(
                    master=frame_names,
                    text='Услуги',
                    font=('Arial', 15, 'bold'),
                    relief='ridge',
                    width=8
                ).grid(row=0, column=1)
            if i > 0 and j == 0:
                tk.Label(
                    master=frame_names,
                    text=names_list[i-1],
                    relief='ridge',
                    width=40
                ).grid(row=i, column=0)
            if i > 0 and j == 1:
                tk.Label(
                    master=frame_names,
                    text=sales_list[i-1],
                    relief='ridge',
                    width=16
                ).grid(row=i, column=1)
    frame_names.grid(row=0, column=0)
    frame_btn = tk.Frame(master=main_window, padx=2, pady=2)
    lotery = tk.Button(
        text='Выбрать Победителя!',
        font=('Arial', 15, 'bold'),
        width=27,
        height=2,
        master=frame_btn,
        command=lambda: calculate(names_list, sales_list)
    )
    lotery.grid(columnspan=2)
    frame_btn.grid(columnspan=2)
    main_window.mainloop()


def core(names_list, sales_list):
    temp = []
    for i in range(len(names_list)):
        for j in range(int(sales_list[i])):
            temp.append(names_list[i])
    lucky_number = rnd.randint(0, len(temp)-1)
    for k in range(0, len(names_list)):
        if temp[lucky_number] == names_list[k]:
            if 4 < sales_list[k]:
                return 'Наш Великий Победитель, ' + str(temp[lucky_number]) + ', оказал ' + str(sales_list[k]) + \
                       ' услуг и победил с шансом ' + str(round(sales_list[k] / len(temp) * 100, 2)) + '%!'
            if 1 < sales_list[k] < 5:
                return 'Наш Великий Победитель, ' + str(temp[lucky_number]) + ', оказал ' + str(sales_list[k]) + \
                       ' услуги и победил с шансом ' + str(round(sales_list[k] / len(temp) * 100, 2)) + '%!'
            if sales_list[k] == 1:
                return 'Наш Великий Победитель, ' + str(temp[lucky_number]) + ', оказал ' + str(sales_list[k]) + \
                       ' услугу и победил с шансом ' + str(round(sales_list[k] / len(temp) * 100, 2)) + '%!'


def calculate(names_list, sales_list):
    messagebox.showinfo(
        'Спасибо Деду За Победу!',
        core(names_list, sales_list)
    )
    main_window.quit()


window()
