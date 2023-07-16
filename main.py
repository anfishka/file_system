# 1) Создать текстовый файлик с именем принятым с клавы
# 2) Создать текстовый файлик с именем принятым с клавы и 10 случайными числами через запятую
# 3) Считать файл чисел и вывести их сумму
# 4) Создать приложение телефонной книги с хранением фио контакта и множества его номеров телефонаt_hi(name):

def createFile():
    invalid_charachters = ['/', '\\', '*', '<', '>', '|', '?', ':', '"', "'", '!', '%', " "]

    while True:
        name_of_file = input("Enter name of file without spacing! By default your file has .txt format, that`s why enter just name of file! Don't use these symbols: /, \\, *, <, >, |, ?, :, \", \', !, %\n-> ")
        if len(name_of_file) > 0:
            splitted_name_of_file = list(name_of_file)

            is_valid = True
            for l in splitted_name_of_file:
                if l in invalid_charachters:
                    is_valid = False
                    break

            if is_valid:
                print(name_of_file)
                return name_of_file
                break
            else:
                print("Invalid name! Please try again")
        else:
            print("Invalid name! Please try again")



if __name__ == '__main__':
    txt_file = createFile() + '.txt'
