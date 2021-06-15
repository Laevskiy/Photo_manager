import tkinter as tk
from tkinter import ttk
import pandas as pd

win = tk.Tk()
win.geometry(f"285x525+800+150")
win.config(bg="#1faee9")
win.resizable(False,False)
win.title("PHOTO MANAGER")
# Создаем кнопки - баттоны
mounth= ("ЯНВАРЬ","ФЕВРАЛЬ","МАРТ","АПРЕЛЬ","МАЙ","ИЮНЬ","ИЮЛЬ","АВГУСТ","СЕНТЯБРЬ","ОКТЯБРЬ","НОЯБРЬ","ДЕКАБРЬ")
mounth_add_number = {"ЯНВАРЬ": 0.01,
                     "ФЕВРАЛЬ":0.02,
                     "МАРТ":0.03,
                     "АПРЕЛЬ":0.04,
                     "МАЙ":0.05,
                     "ИЮНЬ":0.06,
                     "ИЮЛЬ":0.07,
                     "АВГУСТ":0.08,
                     "СЕНТЯБРЬ":0.09,
                     "ОКТЯБРЬ":0.10,
                     "НОЯБРЬ":0.11,
                     "ДЕКАБРЬ":0.12}
day_w = tk.Entry(win)
# Блок переменых функции перезапись
city_w_l = tk.Entry(win)
name_w_l = tk.Entry(win)
cost_w_l = tk.Entry(win)
tel_w_l = tk.Entry(win)
# Блок переменых функции запись
city_w_l_2 = tk.Entry(win)
name_w_l_2 = tk.Entry(win)
cost_w_l_2 = tk.Entry(win)
tel_w_l_2 = tk.Entry(win)
combo = ttk.Combobox(win, values=mounth)
# Функция принимающая ввод даты

def close_windows():
    win.destroy()

def izmen_tabl_2():
    print("Я в функции изменения таблицы 2")
    btn_zapis["state"] = tk.DISABLED
    btn_zapis["text"] = "ДАТА ЗАПИСАННА!"
    btn1["state"] = tk.NORMAL
    btn_zapis["bg"] = "green"
    days_001 = pd.read_excel('./Свадебные даты 2021.xlsx')
    new_data = [city_w_l_2.get(), cost_w_l_2.get(),name_w_l_2.get(), tel_w_l_2.get()]
    days_001[vvod] = new_data
    days_002 = pd.DataFrame(days_001)
    days_002.to_excel('./Свадебные даты 2021.xlsx')
def izmen_tabl():
    btn_perezapis["state"] = tk.DISABLED
    btn_perezapis["text"] = "ДАТА ЗАПИСАННА!"
    btn_perezapis["bg"]= "green"
    btn1["state"] = tk.NORMAL
    days_001 = pd.read_excel('./Свадебные даты 2021.xlsx')
    days_003 = days_001.copy()
    days_003.loc[0, vvod] = city_w_l.get()
    days_003.loc[1, vvod] = cost_w_l.get()
    days_003.loc[2, vvod] = name_w_l.get()
    days_003.loc[3, vvod] = tel_w_l.get()
    days_003.to_excel('./Свадебные даты 2021.xlsx')
def zapise():
    btn_zapis["state"] = tk.NORMAL
    btn_zapis["text"] = "ЗАПИСАТЬ"
    btn_perezapis["bg"] = "red"
    btn_YES_2["state"] = tk.DISABLED
    btn_NO_2["state"] = tk.DISABLED
    city_w.grid(row=10, column=0, stick="wesn", padx=4, pady=4)
    name_w.grid(row=11, column=0, stick="wesn", padx=4, pady=4)
    cost_w.grid(row=12, column=0, stick="wesn", padx=4, pady=4)
    tel_w.grid(row=13, column=0, stick="wesn", padx=4, pady=4)
    city_w_l_2.grid(row=10, column=1, stick="wesn", padx=4, pady=4)
    name_w_l_2.grid(row=11, column=1, stick="wesn", padx=4, pady=4)
    cost_w_l_2.grid(row=12, column=1, stick="wesn", padx=4, pady=4)
    tel_w_l_2.grid(row=13, column=1, stick="wesn", padx=4, pady=4)
    btn_zapis.grid(row=14, column=0,columnspan=2, stick="wesn", padx=4, pady=4)

def perezapise():
    btn_perezapis["state"] = tk.NORMAL
    btn_perezapis["text"] = "ПЕРЕЗАПИСАТЬ!"
    btn_perezapis["bg"] = "red"
    btn_YES["state"] = tk.DISABLED
    btn_NO["state"] = tk.DISABLED
    global vvod
    city_w_l.grid(row=10, column=1, stick="wesn", padx=4, pady=4)
    name_w_l.grid(row=11, column=1, stick="wesn", padx=4, pady=4)
    cost_w_l.grid(row=12, column=1, stick="wesn", padx=4, pady=4)
    tel_w_l.grid(row=13, column=1, stick="wesn", padx=4, pady=4)
    city_w.grid(row=10, column=0, stick="wesn", padx=4, pady=4)
    name_w.grid(row=11, column=0, stick="wesn", padx=4, pady=4)
    cost_w.grid(row=12, column=0, stick="wesn", padx=4, pady=4)
    tel_w.grid(row=13, column=0, stick="wesn", padx=4, pady=4)

    btn_perezapis.grid(row=14, column=0,columnspan=2, stick="wesn", padx=4, pady=4)


def getting_vvod():
    btn_YES["state"] = tk.NORMAL
    btn_NO["state"] = tk.NORMAL
    btn_YES_2["state"] = tk.NORMAL
    btn_NO_2["state"] = tk.NORMAL
    btn1["state"] = tk.DISABLED
    global vvod
    vvod = int(day_w.get())+float(mounth_add_number[combo.get()])

    days_001 = pd.read_excel('./Свадебные даты 2021.xlsx')
    days = []
    for i in days_001.keys():
        days.append(i)

    if vvod in days:
        city = days_001[vvod][0]
        cost = days_001[vvod][1]
        DONT_FREE = tk.Label(win, text="ДАТА УЖЕ ЗАБРОНИРОВАННА!",
                         bg="RED",
                         fg="WHITE",
                         font=("Arial", 12, "bold"),
                         padx=5,
                         pady=5,
                         anchor="sw",
                         # Устанавливаем границы ЛАЙБЛА
                         relief=tk.RAISED,
                         bd=3,
                         ).grid(row=5, column=0,columnspan=2, stick="wesn", padx=4, pady=4)
        city_DONT_FREE = tk.Label(win, text=f"В городе : {city}",
                             # определяем фон
                             bg="GREEN",
                             # Определяем цвет букв
                             fg="WHITE",
                             # Меняем шрифт
                             font=("Arial", 10, "bold"),
                             # Меняем отступы надписи внутри лайбла
                             padx=5,
                             pady=5,
                             # Меняем размер лейбла
                             # width = 10,
                             # height = 2,
                             # Меняем расположение надписи внутри лайбла(s,e,w)
                             anchor="sw",
                             # Устанавливаем границы ЛАЙБЛА
                             relief=tk.RAISED,
                             bd=3,
                             ).grid(row=6, column=0, columnspan=2, stick="wesn", padx=4, pady=4)
        cost_DONT_FREE = tk.Label(win, text=f"ПО ЦЕНЕ : {cost}",
                                  # определяем фон
                                  bg="GREEN",
                                  # Определяем цвет букв
                                  fg="WHITE",
                                  # Меняем шрифт
                                  font=("Arial", 12, "bold"),
                                  # Меняем отступы надписи внутри лайбла
                                  padx=5,
                                  pady=5,
                                  # Меняем размер лейбла
                                  # width = 10,
                                  # height = 2,
                                  # Меняем расположение надписи внутри лайбла(s,e,w)
                                  anchor="sw",
                                  # Устанавливаем границы ЛАЙБЛА
                                  relief=tk.RAISED,
                                  bd=3,
                                  ).grid(row=7, column=0, columnspan=2, stick="wesn", padx=4, pady=4)
        perezapis = tk.Label(win, text="Хотите перезаписать эту дату?",
                         # определяем фон
                         bg="BLACK",
                         # Определяем цвет букв
                         fg="WHITE",
                         # Меняем шрифт
                         font=("Arial", 10, "bold"),
                         # Меняем отступы надписи внутри лайбла
                         padx=5,
                         pady=5,
                         # Меняем размер лейбла
                         # width = 10,
                         # height = 2,
                         # Меняем расположение надписи внутри лайбла(s,e,w)
                         anchor="sw",
                         # Устанавливаем границы ЛАЙБЛА
                         relief=tk.RAISED,
                         bd=3,
                         ).grid(row=8, column=0, columnspan=2, stick="wesn", padx=4, pady=4)
        btn_NO .grid(row=9, column=1, stick="wesn", padx=4, pady=4)
        btn_YES .grid(row=9, column=0, stick="wesn", padx=4, pady=4)

    else:
        FREE = tk.Label(win, text="ДАТА СВОБОДНА",
                             # определяем фон
                             bg="RED",
                             # Определяем цвет букв
                             fg="WHITE",
                             # Меняем шрифт
                             font=("Arial", 12, "bold"),
                             # Меняем отступы надписи внутри лайбла
                             padx=5,
                             pady=5,
                             anchor="sw",
                             # Устанавливаем границы ЛАЙБЛА
                             relief=tk.RAISED,
                             bd=3,
                             ).grid(row=5, column=0, columnspan=2, stick="wesn", padx=4, pady=4)
        zapis = tk.Label(win, text="Хотите записать эту дату?",
                             # определяем фон
                             bg="BLACK",
                             # Определяем цвет букв
                             fg="WHITE",
                             # Меняем шрифт
                             font=("Arial", 10, "bold"),
                             # Меняем отступы надписи внутри лайбла
                             padx=5,
                             pady=5,
                             # Меняем размер лейбла
                             # width = 10,
                             # height = 2,
                             # Меняем расположение надписи внутри лайбла(s,e,w)
                             anchor="sw",
                             # Устанавливаем границы ЛАЙБЛА
                             relief=tk.RAISED,
                             bd=3,
                             ).grid(row=8, column=0, columnspan=2, stick="wesn", padx=4, pady=4)
        btn_NO_2 .grid(row=9, column=1, stick="wesn", padx=4, pady=4)
        btn_YES_2 .grid(row=9, column=0, stick="wesn", padx=4, pady=4)

# Выводим в баттоне знечение по умолчанию ЯНВАРЬ
city_w = tk.Label(win, text="Введите город:",
                bg="BLACK",
                fg="WHITE",
                font=("Arial", 8, "bold"),
                padx=5,
                pady=5,
                anchor="sw",
                relief=tk.RAISED,
                bd=3,
                )
name_w = tk.Label(win, text="Введите имя:",
                      bg="BLACK",
                      fg="WHITE",
                      font=("Arial", 8, "bold"),
                      padx=5,
                      pady=5,
                      anchor="sw",
                      relief=tk.RAISED,
                      bd=3,
                      )
cost_w = tk.Label(win, text="Введите стоймость:",
                      bg="BLACK",
                      fg="WHITE",
                      font=("Arial", 8, "bold"),
                      padx=5,
                      pady=5,
                      anchor="sw",
                      relief=tk.RAISED,
                      bd=3,
                      )
tel_w = tk.Label(win, text="Введите тел :",
                      bg="BLACK",
                      fg="WHITE",
                      font=("Arial", 8, "bold"),
                      padx=5,
                      pady=5,
                      anchor="sw",
                      relief=tk.RAISED,
                      bd=3,
                      )
btn_NO_2 = tk.Button(win, text="НЕТ",
                           font=("Arial", 13),
                           bg="#ff0000",
                           bd=3,
                           fg="black",
                           # вызываем функцию когда кнопка нажата
                           command=close_windows,
                           state=tk.NORMAL
                           )
btn_YES_2 = tk.Button(win, text="ДА",
                            font=("Arial", 13),
                            bg="#ff0000",
                            bd=3,
                            fg="black",
                            # вызываем функцию когда кнопка нажата
                            command=zapise,
                            state=tk.NORMAL
                            )
btn_perezapis = tk.Button(win, text="ПЕРЕЗАПИСАТЬ",
                        font=("Arial", 13),
                        bg="#ff0000",
                        bd=3,
                        fg="white",
                        # вызываем функцию когда кнопка нажата
                        command= izmen_tabl,
                        state=tk.NORMAL
                        )
btn_zapis = tk.Button(win, text="ЗАПИСАТЬ",
                        font=("Arial", 13),
                        bg="#ff0000",
                        bd=3,
                        fg="white",
                        # вызываем функцию когда кнопка нажата
                        command= izmen_tabl_2,
                        state=tk.NORMAL
                        )
level = tk.Label(win, text="Выберете дату и месяц",
                # определяем фон
                bg="BLACK",
                # Определяем цвет букв
                fg="WHITE",
                # Меняем шрифт
                font=("Arial", 15, "bold"),
                # Меняем отступы надписи внутри лайбла
                padx=5,
                pady=5,
                # Меняем размер лейбла
                # width = 10,
                # height = 2,
                # Меняем расположение надписи внутри лайбла(s,e,w)
                anchor="sw",
                # Устанавливаем границы ЛАЙБЛА
                relief=tk.RAISED,
                bd=3,
                )
btn1 = tk.Button(win, text="ПРОВЕРИТЬ ДАТУ",
                 font=("Arial", 13),
                 bg="#17806d",
                 bd=3,
                 fg="white",
                 # вызываем функцию когда кнопка нажата
                 command= getting_vvod,
                 state=tk.NORMAL
                 )
btn_NO = tk.Button(win, text="НЕТ",
                 font=("Arial", 13),
                 bg="#ff0000",
                 bd=3,
                 fg="white",
                 # вызываем функцию когда кнопка нажата
                 command= close_windows,
                 state=tk.NORMAL
                 )
btn_YES = tk.Button(win, text="ДА",
                 font=("Arial", 13),
                 bg="#ff0000",
                 bd=3,
                 fg="white",
                 # вызываем функцию когда кнопка нажата
                 command=perezapise,
                 state=tk.NORMAL
                 )
combo.current(0)
win.grid_columnconfigure(0, minsize=60)
win.grid_rowconfigure(0, minsize=40)
win.grid_columnconfigure(1, minsize=20)


combo.grid(row=2, column=1, stick="wesn", padx=4, pady=4)
level.grid(row=0, column=0, columnspan=2, stick="wesn", padx=4, pady=4)
day_w.grid(row=2, column=0,stick="wesn", padx=4, pady=4)
btn1.grid(row=3, column=0,columnspan=2, stick="wesn", padx=4, pady=4)
win.mainloop()

