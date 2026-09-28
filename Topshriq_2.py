class Employee:
    def __init__(self, name, salary, employee_id):
        self.name = name
        self._salary = salary
        self.__employee_id = employee_id

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, val):
        if val < 0:
            print("Salary 0 dan kichik bo'lishi mumkin emas!")
        else:
            self._salary = val

    def __str__(self):
        return f"Xodim: {self.name}, Maosh: {self.salary}"

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.__employee_id}')"

employee1 = Employee("Ali", 5000000, "EMP001")
employee2 = Employee("Vali", 6000000, "EMP002")
employee3 = Employee("Hasan", 7000000, "EMP003")

print(employee1)
print(employee2)
print(employee3)

print("Ali maoshi:", employee1.salary)

employee1.salary = 5500000
print("Yangi maosh:", employee1.salary)

employee2.salary = -1000

print(repr(employee1))
print(repr(employee2))
print(repr(employee3))

try:
    print(employee1.__employee_id)
except AttributeError:
    print("Private atributga to'g'ridan-to'g'ri murojaat qilib bo'lmaydi!")