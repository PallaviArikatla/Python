class Employee:
    empCount = 0
    sum = 0
    avg = 0

    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department
        Employee.empCount += 1
        Employee.avgSal(salary)

    def avgSal(salary):
        Employee.sum += salary
        Employee.avg = Employee.sum / Employee.empCount


class permanentEmployee(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary, department)


emp = Employee("nancy", 5000, "Development")
emp = Employee("mike", 6000, "IT")
full = permanentEmployee("elle", 8000,"Code")
print(full.name)
print("Average Salary:",Employee.avg)
print("Employee COunt:",Employee.empCount)