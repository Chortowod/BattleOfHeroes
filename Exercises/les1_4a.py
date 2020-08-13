# 1. С клавиатуры в одной строке вводится произвольное количество вещественных чисел. 
# Запишите их в файл, расположив каждое число на отдельной строке. 
# Затем загрузите список чисел из этого файла и вычислите их сумму и максимум 
# и допишите результаты в файл.

userinp = input("Введите числа")
clist = userinp.split()

myfile = open("myfile.txt", 'w') # Открывает файл (создает/очищает)
for val in clist:
    myfile.write(val + "\n")
myfile.close()

fs = open("myfile.txt").read() # Прочитать файл целиком в строку
clist2 = userinp.split()
map_object = map(int, clist2)
list_int = list(map_object)

myfile = open("myfile.txt", 'a') # Открывает файл (добавляет)
myfile.write("Sum = " + str(sum(list_int)) + " | Max = " + str(max(list_int)))
myfile.close()

# 2. В файле записано стихотворение. Выведите его на экран, а также укажите, каких слов 
# в нем больше: начинающихся на гласную или на согласную букву (регистр не учитывается).

fs = open("stih.txt", encoding="utf-8").read() # Прочитать файл целиком в строку
print(fs)
clist3 = fs.split()
vow_count = 0
cons_count = 0
glasn = ["а", "А", "я", "Я", "о", "О", "ё", "Ё", "у", "У", "ю", "Ю", "ы", "Ы", "и", "И", "о", "О", "е", "Е"]
for val in clist3:
    check = False
    for glas in glasn:
        if val[0] == glas:
            vow_count +=1
            check = True
            break
    if not check: cons_count += 1
    
print("Гласных букв:", vow_count)
print("Согласных букв:", cons_count)

# 3. Информация о занятости мест в зрительном зале кинотеатра хранится в текстовом файле
# Напишите программу, которая позволит пользователю увидеть количество свободных мест, 
# а также, введя номер ряда и места, получить информацию - свободно оно или нет

F = open('movie.txt')           # Открыть файл 
empty = 0
movie = []
line = F.readline()             # Прочитать одну строку
while (line):                   
    line.rstrip()               # Удалить символ конца строки
    parts = line.split()
    temprow = []
    for val in parts:
        temprow.append(val)
        if val == "0": empty +=1
    movie.append(temprow)
    line = F.readline()

def is_seat_free_print(row, seat, movie):
    if movie[row - 1][seat - 1] == "0":
        print("Ряд %d, место %d свободно" % (row, seat))
    else:
        print("Ряд %d, место %d занято" % (row, seat))

print("Пустых мест: %d" % empty)
is_seat_free_print(2, 4, movie)    

