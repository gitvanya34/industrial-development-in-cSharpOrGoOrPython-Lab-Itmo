from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

button_lab_1 = KeyboardButton('/lab1')
button_lab_2 = KeyboardButton('/lab2')
button_lab_3 = KeyboardButton('/lab3')
button_lab_4 = KeyboardButton('/lab4')
button_lab_5 = KeyboardButton('/lab5')
button_lab_6 = KeyboardButton('/lab6')

menu_kb = ReplyKeyboardMarkup().add(button_lab_1, button_lab_2, button_lab_3, button_lab_4, button_lab_5, button_lab_6)

lab_1_kb = ReplyKeyboardMarkup().add(KeyboardButton('2 5'), KeyboardButton('/menu'))


