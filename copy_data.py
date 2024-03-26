from return_data_file import data_file

def copy_row():
    print("Выберите файл ОТКУДА скопировать:")
    data, nf = data_file()
    count_rows = len(data)
    if count_rows == 0:
        print("Файл пустой!")
    else:
        number_row = int(input(f"Введите номер строки которую Вы хотите скопировать"
                               f"от 1 до {count_rows}: "))
        while number_row < 1 or number_row > count_rows:
            number_row = int(input(f"Ошибка!"
                                   f"Введите номер строки "
                                   f"от 1 до {count_rows}: "))
        row_to_copy = data[number_row - 1].split(";")
        print("Выберите файл КУДА скопировать:")
        data2, nf2 =  data_file()
        with open(f'db/data_{nf2}.txt', 'a', encoding='utf-8') as file:
            file.write(f'{number_row};{row_to_copy[1]};'
                   f'{row_to_copy[2]};{row_to_copy[3]};{row_to_copy[4]}\n')
        print("Данные успешно скопированы!")

copy_row()      