# 1. Определите максимальное и минимальное значения из двух различных целых чисел
# ?????

# 2. Дано натуральное число. Определите сумму и количество его цифр
from random import randint
from random import uniform as rnd

n1 = randint(100, 999999)

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10 # деление без остатка после запятой
    return s
print(n1)
print(sum_digits(n1))

# 3. Вывести в строку 10 первых натуральных чисел, оканчивающихся на цифру k, 
# кратных числу s и находящихся в интервале, левая граница которого равна start

start = randint(1, 1000)
k = randint(0, 9)
s = randint(1, 20)

print("start:", start, "k:", k, "s:", s)

def find_10(start, k, s):
    cnt = 0
    s_point = start
    while cnt<15:
        if (s_point > 1000000):
            print("Нет чисел, подходящих условию")
            return
        if (s_point % s == 0 and s_point % 10 == k):
            print(s_point)
            cnt+=1
        s_point+=1

find_10(start, k, s)

# 4.	Для введенных с клавиатуры положительных целых чисел a и b (a≤b) определите 
# (отрезок поиска включает сами числа a. и b, при выводе вещественных результатов 
# оставьте два знака после запятой):
#   a.	сумму всех целых чисел от a до b;
#   b.	произведение всех целых чисел от a до b;
#   c.	среднее арифметическое всех целых чисел от a до b;
#   d.	среднее геометрическое нечетных чисел от a до b.
from math import sqrt

while True:
    a = int(input("Введите a: "))
    b = int(input("Введите b (больше a): "))
    if b > a:
        break
    print("Неправильно ввели, попробуйте еще раз.")

sum = 0
mult = 1
count = b - a + 1
while a <= b:
    sum += a
    mult *= a
    a+=1
print("Сумма:", sum, "Произведение:", mult, "Среднее арифметическое:", sum / count)
print("Среднее геометрическое:", round(mult**(1/count), 2))

# 5. Предложение, введенное с клавиатуры, содержит слова из гласных и согласных букв кириллицы 
# (регистр может быть различный), а также пробелы. Определите количество гласных и 
# согласных букв в предложении. Для пропуска пробелов используйте оператор continue

p = input("Введите предложение: ")
vow = 0
cons = 0
spaces = 0
russian = 0
for ch in p:
    print(ord(ch))
    if (ch == " "):
        spaces += 1
        continue
    if (ord(ch) >= 1040 and ord(ch) <= 1103):
        russian += 1
        continue
    if (ch == 'a' or ch == 'A' or ch == 'e' or ch == 'E' or ch == 'i' or ch =='I' or ch =='o' or ch =='O' or ch =='u' or ch =='U'):
        vow += 1
    else:
        cons += 1
print("Согласных:", vow, "Гласных:", cons, "Пробелов:", spaces, "Русских:", russian)

# 6. Дано n вещественных чисел. Определите, является ли последовательность 
# упорядоченной по возрастанию. В случае отрицательного ответа выведите 
# порядковый номер числа, нарушающего такую упорядоченность.

conseq = [1.1, 2.2, 3.334, 5.5, 5.52, 44, 222.112]
conseq2 = [1.1, 2.2, 3.1, 3.11, 5.52, 44, 222.112]
conseq3 = [1.1, 2.2, 3.1, 3.01, 5.52, 44, 222.112]

def find_traitror(conseq):
    n = len(conseq)
    cnt = 0
    while cnt < n - 1:
        if (conseq[cnt] > conseq[cnt+1]):
            print("Номер предателя:", cnt+1, "Значение:", conseq[cnt+1])
            return
        cnt+=1
    print("Предателей нет. Последовательность прекрасна.")

find_traitror(conseq)
find_traitror(conseq2)
find_traitror(conseq3)

# 7. Дано предложение. Выведите его на экран, удалив из него все слова, 
# содержащие произвольную букву (вводится с клавиатуры). 
# Рекомендация: строковые методы str.split() и str.join() могут оказаться полезными.

cons = input("Введите предложение: ")
letter = input("Введите букву для удаления: ")

def delete_letter(cons, letter):
    clist = cons.split()
    listnew = []
    for value in clist:
        if (letter not in value):
            listnew.append(value)
    print(" ".join(listnew))

delete_letter(cons, letter)

# 8. Напишите программу, которая позволит пользователю увидеть количество свободных мест, 
# а также, введя номер ряда и места, получить информацию - свободно оно или нет. 
# Данные о занятости мест вводятся с клавиатуры (набор из 0 и 1 для каждого ряда).

seats = [
    [0, 1, 0, 0 , 1],
    [1, 1, 1, 0, 1, 0, 1],
    [0, 1, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1]
]

print(seats)

def isfree(seats):
    free = 0
    for value in seats:
        for seat in value:
            if seat == 0:
                free += 1
    return free

print(isfree(seats))

def isseatfree(row, seat, seats):
    if seats[row - 1][seat - 1] == 0:
        return True
    else:
        return False

print(isseatfree(2, 3, seats))