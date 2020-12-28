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

    # Ввод тройки чисел
    def read(self):
        first = input('Введите первое число: ')
        second = input('Введите второе число: ')
        third = input('Введите третье число: ')

        self.first = float(first)
        self.second = float(second)
        self.third = float(third)

    # Вычисление суммы чисел
    def sum(self):
        return self.first + self.second + self.third


# Создание нового класса
class Triangle(Triad):
    def __init__(self, side_one=0, side_two=0, side_three=0):
        super(Triangle, self).__init__()
        self.side_one = float(side_one)
        self.side_two = float(side_two)
        self.side_three = float(side_three)
        self.per()
        self.__corner_one()

    # Ввод сторон треугольника
    def read(self):
        side_one = input('Введите первую сторону треугольника: ')
        side_two = input('Введите вторую сторону треугольника: ')
        side_three = input('Введите третью сторону треугольника: ')

        self.side_one = float(side_one)
        self.side_two = float(side_two)
        self.side_three = float(side_three)

    # Вычисление периметра треугольника
    def per(self):
        return self.side_one + self.side_two + self.side_three

    # Вычисление площади треугольника
    def square(self):
        p = (self.side_one + self.side_two + self.side_three) / 2
        return math.sqrt(p * (p - self.side_one) * (p - self.side_two) * (p - self.side_three))

    # Вычисление градусов углов в треугольнике
    def __corner_one(self):
        a = self.side_one
        b = self.side_two
        c = self.side_three

        first_corner = math.acos(((b ** 2) + (c ** 2) - (a ** 2)) / (2 * c * b))
        self.f_d = math.degrees(first_corner)

        second_corner = math.acos(((a ** 2) + (b ** 2) - (c ** 2)) / (2 * a * b))
        self.s_d = math.degrees(second_corner)

        third_corner = math.acos(((a ** 2) + (c ** 2) - (b ** 2)) / (2 * a * c))
        self.th_d = math.degrees(third_corner)

        if self.f_d == 90 or self.s_d == 90 or self.th_d == 90:
            return print("Треугольник прямоугольный")
        elif self.f_d == self.s_d or self.f_d == self.th_d or self.s_d == self.th_d:
            return print("Треугольник равнобедренный")
        elif self.f_d == self.s_d == self.th_d:
            return print("Треугольник равносторонний")
        else:
            return print("Обычный треугольник")


if __name__ == '__main__':
    r1 = Triad()
    r1.read()
    print(r1.sum())

    r2 = Triangle()
    r2.read()
    print(r2.square())
