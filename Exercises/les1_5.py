# 1. Дан список температурных изменений в течение дня (целые числа). 
# Известно, что измеряющее устройство иногда сбоит и записывает отсутствие температуры 
# (значение None). Выведите среднюю температуру за наблюдаемый промежуток времени, 
# предварительно очистив список от неопределенных значений. 
# Гарантируется, что хотя бы одно определенное значение в списке есть.

temp_list = [19, 22, 24, 29, 33, 34, 33, None, 25, None, 20, 18, 17]
def show_median(temp_list):
    """
    Принимает список температурных значений.
    Возвращает средний показатель температуры.
    """
    sum = 0
    cnt = 0
    for value in temp_list:
        if value != None:
            sum += value
            cnt += 1
    return round(sum / cnt, 2)

result = show_median(temp_list)
print(show_median.__doc__)
print("Средняя температура за сутки: %d" % result)

# 2. Напишите функцию, которая принимает неограниченное количество числовых аргументов 
# и возвращает кортеж из двух списков: отрицательных значений (отсортирован по убыванию);  
# неотрицательных значений (отсортирован по возрастанию).

def sort_pos_neg(*args):
    """
    Принимает неограниченное количество числовых аргументов.
    Возвращает кортеж из двух списков: 
        - отрицательных значений (отсортирован по убыванию);
        - неотрицательных значений (отсортирован по возрастанию).
    """
    positive = []
    negative = []
    for arg in args:
        if arg < 0:
            negative.append(arg)
        else:
            positive.append(arg)
    positive.sort()
    negative.sort(reverse = True)
    return (positive, negative)

result = sort_pos_neg(5, 3, -2, 15, 33, -22, 44, -22, 22, 0, 77, 543, -223)
print(sort_pos_neg.__doc__)
print(result)

# 3. Составьте две функции для возведения числа в степень: 
# один из вариантов реализуйте в рекурсивном стиле.

def my_pow(numb, pow):
    """
    Принимает два числовых значения: число, возводимое в степень, и степень.
    Возвращает число, возведенное в указанную степень.
    """
    check = False
    if pow == 0:
        return 1
    if pow == 1:
        return numb
    if pow < 0:
        # если степень оказалась отрицательной, то превращаем ее в положительную
        pow *= -1
        check = True
    result = numb
    for x in range(pow - 1):
        result *= numb
    if check:
        # единицу делим на полученный результат (т.е. 5**-2 = 1 / 5**2)
        return 1 / result
    else:
        return result

def my_pow_rec(numb, pow):
    """
    Принимает два числовых значения: число, возводимое в степень, и степень.
    Возвращает число, возведенное в указанную степень.
    (рекурсивный вариант)
    """
    check = False
    if pow < 0:
        pow *= -1
        check = True
    if pow == 0:
        return 1
    if pow >= 1 and not check:
        return numb * my_pow_rec(numb, pow - 1)
    if pow >= 1 and check:
        return 1 / (numb * my_pow_rec(numb, pow - 1))

result = my_pow(3, 4)
result2 = my_pow_rec(3, 4)

print(my_pow.__doc__)
print(result)
print(my_pow_rec.__doc__)
print(result2)