import numpy as np

intList = [33, 25, 22, 66, 112, 44, 12, 550, 230, 15]
npArray = np.array([33, 25, 22, 66, 112, 44, 12, 550, 230, 15])

intList.append(9)
intList.append(10)
npArray = np.append(npArray, [9,10])
print("Список после добавления элемента: ", intList)
print("Массив после добавления элемента: ", npArray)

npArray[::-1].sort()
intList.sort(reverse=True)

print("Список после сортировки элементов: ", intList)
print("Массив после сортировки элементов: ", npArray)

intList = [val*2 for val in intList]
npArray*=2

print("Список после умножения элементов: ", intList)
print("Массив после умножения элементов: ", npArray)

print("Первые три элемента списка: ", intList[0:3])
print("Первые три элемента массива: ", npArray[0:3])

print("Доступных атрибутов для списка: ", len(dir(intList)))
print("Доступных атрибутов для массива: ", len(dir(npArray)))