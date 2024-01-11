##Задание 1-2
print('Hello world')

##Задание3
a = 3
print(type (a+1))
a = 3.5
print(type (a+1))
a = ‘qwerty’
print(type (a))
a = True
print(type (a))
a = 123
print(type (a+1))

##Задание4
b = 5.7
print(int(b))
c = -5.7
print(int(c))
e = 3**39 - int(float(3**39))
print(int(e))

##Задание 5
print("Привет! Давай знакомиться, как тебя зовут?")
user_name = input()
print("Я очень рад, " + user_name + ":)")

##Задание6
x = int(input())
y = int(input())
m = sum(x * 60 + y for m in range(2))
print("Путь доктора общий", sum)

##Задание 7
a = False
b = True
c = False
print (not a or b and c)
print (not (a or b) and c) 


##Задание 8
a = int(input('Год рождения: '))
    if a < 1900 or a > 3000:  
        print('Год не входит в выборку.')
    elif a % 4 != 0 or a % 100 == 0:  
        print('Обычный год :(')
    else:
        print('С днём рождения!:)')

##Задание 9
number = 0
while number < 20:
   number += 1
   if number % 2 == 1:
      continue
   print(number, end=' ')   

##Задание 10
   sum = 0;
   x = int(input())
   sum += x;
while x != 0:
   x = int(input())
   sum += x;
print ("Итог:",sum)

##Задание 11
x = int(input('Количество коллег в клинике: '))
    y = int(input('Количество коллег в поликлинике: '))
    a = 2
    while a % y != 0 or a % x != 0:  
        a += 1
    print('Нужно кусков: ',a)

##Задание 12
for i in range(0, 20, 2):
   print (i)

##Задание 13
    a = int(input('Введите значение 1: '))
    b = int(input('Введите значение 2: '))
    c = int(input('Введите значение 3: '))
    d = int(input('Введите значение 4: '))
   print('', end='\t')  
    for j in range(c, d + 1): 
        print(j, end='\t')
    print()  
    for i in range(a, b + 1):  
        print(i, end='\t')
        for j in range(c, d + 1):
            print(i * j, end='\t')  
    print()
      #Задача 14
    n = int(input('Введите значение матрицы: '))
    a = [[0] * n for i in range(n)]
    count = 0
    for i in range(n):   
        count += 1
        a[0][i] = count
    j = 0
    i = n-1
    n -= 1  
    while len(a)**2 != count:  
        for k in range(n):  
            j += 1
            count += 1
            a[j][i] = count
        for k in range(n):  
            i -= 1
            count += 1
            a[j][i] = count
        for k in range(n-1):  
            j -= 1
            count += 1
            a[j][i] = count
        for k in range(n-1): 
            i += 1
            count += 1
            a[j][i] = count
        n -= 2    
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' ')
        print()

#Задача 15
    import time
    from tkinter import messagebox

    while True: 
        time.sleep(10) 
        if __name__ == '__main__':
            messagebox.showinfo('Useful Python', 'Вы долго смотрели в монитор, теперь посмотрите в окно.')

#Задача 16
import time
from tkinter import *

def main_window(): 
    global window
    window= Tk() 
    window.title('Будильник') 
    window.geometry('400x200') 
    lbl = Label(window, text='Вы долго смотрели в монитор,\n теперь посмотрите в окно.', 
                font=('Arial Bold', 14))
    lbl.grid(column=0, row=0)

    btn1 = Button(window, text='Перезапустить', command=clicked1)
    btn2 = Button(window, text='Выход', command=clicked2)

    btn1.grid(column=0, row=1)
    btn2.grid(column=1, row=1)
    window.mainloop()  

def clicked1(): 
    window.destroy()
    time.sleep(10)
    main_window()

def clicked2():
    quit()

if __name__ == '__main__': 
    main_window()

   