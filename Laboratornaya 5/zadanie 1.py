str = input("Введите строку: ") #Команда ввода с клавиатуры.
if str == str[::-1]: #выбираем эелементы строки в обратном порядке, начиная с последнего и заканчивая первым символом.
    print("Да, это палиндром") #Если строка и её перевёрнутый вариант совпадают, то программа выводит сообщение «Да, это палиндром».
else:
    print("Нет, это не палиндром") #При других условиях выводится «Нет, это не палиндром».