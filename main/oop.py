# no of employees - Class Variable -- can be accessed using ClassName.variable_name


class Employee:

    no_of_employees = 0
    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.no_of_employees += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

# pass is used to create an empty class


emp1 = Employee('Chinmay', 'V', 60000)
emp2 = Employee('Kshitij', 'V', 120000)

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
# print(emp1.email)
# print(emp2.email)

# print(emp1.fullname())
# print(emp2.fullname())


