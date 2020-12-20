#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


#   Создать класс Triad (тройка чисел); определить методы изменения полей и вычисления
#   суммы чисел. Определить производный класс Triangle с полями-сторонами. Определить
#   методы вычисления углов и площади треугольника.

class Triad:

    def __init__(self, first=0, second=0, third=0, summa=0):
        self.first = int(first)
        self.second = int(second)
        self.third = int(third)

        self.sum()

    # Ввод тройки чисел
    def read(self):
        first = input('Введите первое число: ')
        second = input('Введите второе число: ')
        third = input('Введите третье число: ')

        self.first = int(first)
        self.second = int(second)
        self.third = int(third)

        self.sum()

    # Вычисление суммы чисел
    def sum(self):
        self.summa = self.first + self.second + self.third

    # NEW - вывести числа на экран
    def display(self):
        print(f"Сумма чисел равна: {self.summa}")


class Triangle(Triad):
    def __init__(self, side_one=0, side_two=0, side_three=0):
        super(Triangle, self).__init__()
        self.side_one = int(side_one)
        self.side_two = int(side_two)
        self.side_three = int(side_three)

    def read(self):
        side_one = input('Введите первую сторону треугольника: ')
        side_two = input('Введите вторую сторону треугольника: ')
        side_three = input('Введите третью сторону треугольника: ')

        self.side_one = int(side_one)
        self.side_two = int(side_two)
        self.side_three = int(side_three)

        self.add()
        self.square()
        self.corner_one()

    def add(self):
        global perimeter
        perimeter = self.side_one + self.side_two + self.side_three

    # Вычисление площади треугольника по формуле Герона
    def square(self):
        p = perimeter / 2
        s = math.sqrt(p * (p - self.side_one) * (p - self.side_two) * (p - self.side_three))
        print(f"Площадь треугольника равна: {s}")

    # Вычисление градусов углов в треугольнике
    def corner_one(self):
        first_corner = math.acos(
            ((self.side_two ** 2) + (self.side_three ** 2) - (self.side_one ** 2)) / (
                        2 * self.side_three * self.side_two))
        self.first_degrees = math.degrees(first_corner)

        second_corner = math.acos(
            ((self.side_one ** 2) + (self.side_two ** 2) - (self.side_three ** 2)) / (
                        2 * self.side_one * self.side_two))
        self.second_degrees = math.degrees(second_corner)

        third_corner = math.acos(
            ((self.side_one ** 2) + (self.side_three ** 2) - (self.side_two ** 2)) / (
                        2 * self.side_one * self.side_three))
        self.third_degrees = math.degrees(third_corner)

    # Вывести значения на экран
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

