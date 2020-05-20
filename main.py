""" In order to protect the Employee Class from being directly instantiated, one can use the abc package to define
abstract classes and, consequently, abstract methods. Abstract methods are declared, but contains no implementation.
Abstract classes cannot be instantiated, and require subclasses to provide implementations for the abstract methods.
Source:https://www.python-course.eu/python3_abstract_classes.php
"""

from abc import ABC
from abc import abstractmethod


class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee:
    def __init__(self, code, name, salary):
        self.code = code
        self.name = name
        self.salary = salary

    workload = 8

    def calc_bonus(self):
        pass

    def get_hours(self):
        pass


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.departament = Department('managers', 1)

    def calc_bonus(self):
        return self.salary * 0.15


class Seller(Manager):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.departament = Department('sellers', 2)
        self.sales = 0

    def get_hours(self):
        return 6


dep = Department('Tecnologia', 10)
print(dep.code)
