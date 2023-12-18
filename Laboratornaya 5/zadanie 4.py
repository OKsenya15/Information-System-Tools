import pymysql # Привязка к pymysql, чтобы python и mysql были совместимы.

connect = pymysql.connect( # Сведения для подключения mysql.
    host='localhost',
    port=3306,
    user='root',
    password='pass',
    database='my_db'
)

cur = connect.cursor() # Это место, где будут сохраняться результаты запроса.
year= int(input('Введите год: ')) # Запрос года.
s = year 
cur.execute(' select first_name,last_name,date_of_birth from user where year(date_of_birth) = %s',s) # Команда выполняет указанный запрос в БД. Запуск цикла.
for rec in cur:
    print(rec[0],rec[1],rec[2]) # Параметры запроса (Имя, фамилия, год рождения)