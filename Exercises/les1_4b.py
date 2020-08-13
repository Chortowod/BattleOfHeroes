import pandas as pd

filename = "orderdata_sample.csv"

# Записываем содержимое файла в датафрейм
df = pd.read_csv(filename)

# Записываем в переменную новую колонку, окгругляя значения до 2 после запятой
sum_column = round(df["Quantity"] * df["Price"] + df["Freight"], 2)

# Добавляем колонку в датафрейм
df["Total"] = sum_column

# Конвертируем датафрейм обратно в файл
df.to_csv(r'new_orderdata_sample.csv', index = False, header=True)