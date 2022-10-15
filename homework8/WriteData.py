import InputData
from InputData import Enter_the_data

def Write_the_data():
    employee_file = open("Employees.txt", "a")
    employee_file.write(Enter_the_data())
    employee_file.close
