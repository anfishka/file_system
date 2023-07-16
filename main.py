# 1) Создать текстовый файлик с именем принятым с клавы
# 2) Создать текстовый файлик с именем принятым с клавы и 10 случайными числами через запятую
# 3) Считать файл чисел и вывести их сумму
# 4) Создать приложение телефонной книги с хранением фио контакта и множества его номеров телефонаt_hi(name):


import random

def nameFile():
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

def randNums(amount):
    nums = []
    for i in range(amount):
        num = random.randint(1,100)
        nums.append(num)
    return nums

def sumNums(nums):
    splitted_str = nums.split(",")
    sum = 0
    for i in splitted_str:
        sum += int(i)
    return str(sum)

def createFile():
    if __name__ == '__main__':
        txt_file = nameFile() + '.txt'
        file = open(txt_file, 'a')
        file.close()
        print(f"File has been successfully created with name : {txt_file}")

def createFileWithNums():
    if __name__ == '__main__':
        txt_file = nameFile() + '.txt'
        file = open(txt_file, 'w')
        nums = ",".join(map(str, randNums(10)))
        file.write(nums)
        file.close()
        print(f"File has been successfully created with the name {txt_file} and it contains : {nums}")

def readFileAndSumNums(name_of_file):
    if __name__ == '__main__':
        file = open(name_of_file, 'r')
        content = file.read()
        result = sumNums(content)
        file.close()
        print(f"Sum of {content} is {result}")


#
# createFile()
# createFileWithNums()
readFileAndSumNums("nnnm.txt")



