string1 = input("Введите строку 1: ")
string2 = input("Введите строку 2: ")
int1 = int(input("Введите число 1: "))
int2 = int(input("Введите число 2: "))

print(string1+string2)
print("sum: ", int1+int2)
print("mult: ", int1*int2)

print(len(string1), len(string2))

print(type(string1), type(string2), type(int1), type(int2))

print(int1 > int2)

dictMy = {"FirstName": "", "LastName": ""}
dictMy["FirstName"] = input('Введите имя: ')
dictMy["LastName"] = input('Введите фамилию: ')
print(dictMy.keys())
print(dictMy.values())
