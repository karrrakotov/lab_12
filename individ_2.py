#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


#   Создать класс Triad (тройка чисел); определить методы изменения полей и вычисления
#   суммы чисел. Определить производный класс Triangle с полями-сторонами. Определить
#   методы вычисления углов и площади треугольника.

class Triad:

    def __init__(self, first=0, second=0, third=0):
        self.first = float(first)
        self.second = float(second)
        self.third = float(third)

        self.sum()

    # Ввод тройки чисел
    def read(self):
        first = input('Введите первое число: ')
        second = input('Введите второе число: ')
        third = input('Введите третье число: ')

        self.first = float(first)
        self.second = float(second)
        self.third = float(third)

        self.sum()

    # Вычисление суммы чисел
    def sum(self):
        self.summa = self.first + self.second + self.third

    # Вывод суммы на экран
    def display(self):
        print(f"Сумма чисел равна: {self.summa}")


# Создание нового класса
class Triangle(Triad):
    def __init__(self, side_one=0, side_two=0, side_three=0):
        super(Triangle, self).__init__()
        self.side_one = float(side_one)
        self.side_two = float(side_two)
        self.side_three = float(side_three)

    # Ввод сторон треугольника
    def read(self):
        side_one = input('Введите первую сторону треугольника: ')
        side_two = input('Введите вторую сторону треугольника: ')
        side_three = input('Введите третью сторону треугольника: ')

        self.side_one = float(side_one)
        self.side_two = float(side_two)
        self.side_three = float(side_three)

        self.add()
        self.square()
        self.corner_one()

    # Вычисление периметра треугольника
    def add(self):
        self.perimeter = self.side_one + self.side_two + self.side_three

    # Вычисление площади треугольника по формуле Герона
    def square(self):
        p = self.perimeter / 2
        s = math.sqrt(p * (p - self.side_one) * (p - self.side_two) * (p - self.side_three))
        print(f"Площадь треугольника равна: {s}")

    # Вычисление градусов углов в треугольнике
    def corner_one(self):
        a = self.side_one
        b = self.side_two
        c = self.side_three
        first_corner = math.acos(((b ** 2) + (c ** 2) - (a ** 2)) / (2 * c * b))
        self.first_degrees = math.degrees(first_corner)

        second_corner = math.acos(((a ** 2) + (b ** 2) - (c ** 2)) / (2 * a * b))
        self.second_degrees = math.degrees(second_corner)

        third_corner = math.acos(((a ** 2) + (c ** 2) - (b ** 2)) / (2 * a * c))
        self.third_degrees = math.degrees(third_corner)

    # Вывод значений
    def display(self):
        print(f"Первый угол в треугольнике равен: {self.first_degrees}")
        print(f"Второй угол в треугольнике равен: {self.second_degrees}")
        print(f"Третий угол в треугольнике равен: {self.third_degrees}")


if __name__ == '__main__':
    r1 = Triad()
    r1.read()
    r1.display()

    r2 = Triangle()
    r2.read()
    r2.display()

