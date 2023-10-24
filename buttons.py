from telebot import types

def more_buttons():
    buttons = types.ReplyKeyboardMarkup(raw_width=1)

    ask_about_Kaneki_Button = types.KeyboardButton('who is it Kaneki')
    ask_about_Kanekis_strngth_Button = types.KeyboardButton('tell more about his strenth')

    buttons.add(ask_about_Kaneki_Button,ask_about_Kanekis_strngth_Button)
    return buttons