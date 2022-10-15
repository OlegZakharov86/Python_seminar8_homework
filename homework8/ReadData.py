def Read_the_data():
    employee_file = open("Employees.txt", "r")
    print(employee_file.readlines())
    employee_file.close