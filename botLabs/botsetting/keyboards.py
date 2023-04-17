from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

button_lab_1 = KeyboardButton('/lab1')
button_lab_2 = KeyboardButton('/lab2')
button_lab_3 = KeyboardButton('/lab3')
button_lab_5 = KeyboardButton('/lab5')
button_menu = KeyboardButton('/menu')
menu_kb = ReplyKeyboardMarkup().add(button_lab_1, button_lab_2, button_lab_3,  button_lab_5,
                                    button_menu)

lab_1_kb = ReplyKeyboardMarkup().add(KeyboardButton('2 5'), button_menu)

lab_2_kb = ReplyKeyboardMarkup().add(KeyboardButton('{"test":"1","test2":"2","test3":"3","test4":"4","test5":"5"}'),
                                     button_menu)

lab_3_kb = ReplyKeyboardMarkup().add(KeyboardButton('/menu'))


