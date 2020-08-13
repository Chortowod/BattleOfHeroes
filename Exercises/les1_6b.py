# необходимо установить модуль: pip install pyinputplus
import os
import csv
import logging
import pyinputplus as pyip
from datetime import datetime as dt

# список имен файлов
list_cvs_names = ["bikes1.csv", "bikes2.csv", "bikes3.csv", "bikes4.csv", "bikes5.csv"]

# время; инициализация логирования; имя файла
timestring = dt.now().strftime("%d.%m.%Y_%H.%M.%S")
logfile = 'copy_to_flat_' + timestring + '.log'
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s_%(levelname)s: %(message)s',
                    handlers=[logging.FileHandler(logfile, 'w', 'utf-8')])
filename = "[" + timestring + "] " + "flat_file.csv"
header = ["Type", "Color", "Price"]

# создаем файл
with open(filename, "w", encoding="utf-8", newline="") as fh:
    writer = csv.writer(fh, quoting=csv.QUOTE_ALL)

    # вписываем заранее известные колонки (либо можем вытащить из файла, но код будет длиннее)
    writer.writerow(header)

    for value in list_cvs_names:
        # пробуем открыть файл из списка
        try:
            with open(value, "r", encoding="utf-8") as fh2:
                reader = csv.reader(fh2)
                # проверяем, совпадает ли заголовок с исходным
                if next(reader) != header:
                    logging.warning("Файл с именем " + value + " имеет неверные заголовки!")
                    continue
                rows = list(reader)
                for row in rows:
                    writer.writerow(row)
            os.remove(value)
            logging.info("Файл с именем " + value + " скопирован и удален.")
        except FileNotFoundError:
            logging.warning("Файл с именем " + value + " не найден!")
print("Копирование завершено")
print("Отчет в файле " + logfile)
print("Результат в файле " + filename)
print("Хотите отсортировать полученный файл? y/n")
# ждем ответа пользователя (y/n)
response = pyip.inputYesNo()
if (response == "yes"):
    with open(filename, 'r', newline='') as f_input:
        csv_input = csv.DictReader(f_input)
        data = sorted(csv_input, key=lambda row: (row['Type'], row['Color']))

    with open(filename, 'w', newline='') as f_output:    
        csv_output = csv.DictWriter(f_output, fieldnames=csv_input.fieldnames)
        csv_output.writeheader()
        csv_output.writerows(data)
    print("Файл успешно отсортирован")
