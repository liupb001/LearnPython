# Python Object-Oriented Programming
# https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        self.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


# 创建 Developer之类，继承Employee类
class Developer(Employee):
    raise_amount = 1.10  # 把Developer的raise_amount设置为1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  # 这个初始化就是把父类的__init__初始化复制到这里
        # Employee.__init__(self, first, last, pay)  # 这个初始化和super初始化一样，但一般用在多继承时
        self.prog_lang = prog_lang


# 创建 Manager类，继承Employee类
class Manager(Employee):

    # 注意我们这里的employees=None，而不是可变的空列表和空元组，这很重要
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)  # 这个初始化就是把父类的__init__初始化复制到这里
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'User', 60000, 'Java')

print(dev_1.email)

# mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
#
# print(isinstance(mgr_1, Manager))  # 输出 True
# print(isinstance(mgr_1, Developer))  # 输出 False
# print(issubclass(Manager, Employee))  # 输出 True
# print(issubclass(Manager, Developer))  # 输出 False
