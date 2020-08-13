def avg(a, b):
    """
    Вернуть среднее геометрическое чисел 'a' и 'b'.
        Параметры:
            - a, b (int или float).
        Результат:
            - float.
    """
    
    try:
        result = (a * b) ** 0.5
        if a < 0 or b < 0:
            raise Exception('Cреднее геометрическое определено только для положительных чисел')
    except TypeError as er:
        print('Внимание! ', type(er), er)
    else:
         result
a = float(input("a = "))
b = float(input("b = "))
c = avg(a, b)
#print("Среднее геометрическое = {:.2f}".format(c))
print(c)