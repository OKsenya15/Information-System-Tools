b = input('Введите строку: ')
b = b.lower() 
b = b.replace(' ','') 
if b == b[::-1]:
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")
    