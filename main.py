""" In order to protect the Employee Class from being directly instantiated, one can use the abc package to define
abstract classes and, consequently, abstract methods. Abstract methods are declared, but contains no implementation.
Abstract classes cannot be instantiated, and require subclasses to provide implementations for the abstract methods.
Source:https://www.python-course.eu/python3_abstract_classes.php
"""

from abc import ABC, abstractmethod


class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(ABC):
    def __init__(self, code, name, salary, department):
        self.code = code
        self.name = name
        self.salary = salary
        self.goal = True
        self.workload = 8
        self._departament = department

    @abstractmethod
    def calc_bonus(self):
        pass

    def get_hours(self):
        return self.workload

    def get_department(self):
        return self._departament.name

    def set_department(self, new_departament, new_code):
        self._departament.name = new_departament
        self._departament.code = new_code


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('managers', 1))

    def calc_bonus(self):
        if self.goal:
            return self.salary * 0.15


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('sellers', 2))
        self._sales = 0

    def calc_bonus(self):
        return self.get_sales() * 0.15

    def get_sales(self):
        return self._sales

    def put_sales(self, new_sale):
        self._sales += new_sale
