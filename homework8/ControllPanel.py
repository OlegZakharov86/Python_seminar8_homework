import InputData, WriteData, ReadData
from InputData import Enter_the_data
from WriteData import Write_the_data
from ReadData import Read_the_data

def Mode_selection():
    print("Введите число от 1 до 2, где:\n 1- ввод данных\n 2- просмотр данных ")
    number = input()
    while number.isdigit() and number in range(1, 3):
        if number == 1:
            Enter_the_data()
            Write_the_data()
        else:
            Read_the_data()

