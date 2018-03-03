# Python Object-Oriented Programming
# https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc

class Employee():

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() ==6:  # 使用weekday method, 如果是5或者6就是周末，就不是workday
            return False
        return True


class Developer(Employee):

    def __init__(self, first, last, pay, prog_lang):
        super(Developer, self).__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super(Manager, self).__init__(first, last, pay)
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

    def print_emp(self):
        for emp in self.employees:
            print(emp.fullname())


dev_1 = Developer('Co', 'Sch', 80000, 'Python')
dev_2= Developer('C', 'S', 30000, 'Java')


# # print(dev_1.prog_lang)
# # print(dev_1.email)
#
# mrg_1 = Manager('Te', 'Us', 90000, [dev_1, dev_2])
# mrg_1.print_emp()

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

import datetime  # 导入Python中日期模块
my_data = datetime.date(2018, 2, 26)  # 传入一个日期，这个日期是星期一是workday

print(dev_1.is_workday(my_data))
# print(emp_2.fullname())
#
# print(emp_1)
# print(emp_2)
#
# print(emp_1.email)
# print(emp_2.email)

# 以上输出结果：
# <__main__.Employee object at 0x00000202B0497B00>
# <__main__.Employee object at 0x00000202B0497B38>
# Corey.Schafer@company.com
# Test.User@company.com
