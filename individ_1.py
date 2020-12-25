#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


#   Создать класс Triangle для представления треугольника. Поля данных должны включать
#   углы и стороны. Требуется реализовать операции: получения полей данных,
#   вычисления площади, вычисления периметра, вычисления высот, а также определения
#   вида треугольника (равносторонний, равнобедренный или прямоугольный).

class Triangle:

    def __init__(self, first=0, second=0, third=0):
        self.first = int(first)
        self.second = int(second)
        self.third = int(third)

        self.per()

    # Ввод сторон треугольника
    def read(self):
        first = input('Введите первую сторону треугольника: ')
        second = input('Введите вторую сторону треугольника: ')
        third = input('Введите третью сторону треугольника: ')

        self.first = int(first)
        self.second = int(second)
        self.third = int(third)

    # Вычисление периметра треугольника
    def per(self):
        return self.first + self.second + self.third

    # Вычисление площади треугольника
    def square(self):
        self.perimeter = self.first + self.second + self.third
        p = self.perimeter / 2
        return math.sqrt(p * (p - self.first) * (p - self.second) * (p - self.third))

    # Вычисление высоты проведенной к стороне A
    def height_one(self):
        p = self.perimeter / 2
        return 2 * math.sqrt(p * (p - self.first) * (p - self.second) * (p - self.third)) / self.first

    # Вычисление высоты проведенной к стороне B
    def height_two(self):
        p = self.perimeter / 2
        return 2 * math.sqrt(p * (p - self.first) * (p - self.second) * (p - self.third)) / self.second

    # Вычисление высоты проведенной к стороне C
    def height_three(self):
        p = self.perimeter / 2
        return 2 * math.sqrt(p * (p - self.first) * (p - self.second) * (p - self.third)) / self.third

    # Вычисление градусов углов по формуле Герона
    def corner_one(self):
        a = self.first
        b = self.second
        c = self.third
        first_corner = math.acos(((b ** 2) + (c ** 2) - (a ** 2)) / (2 * c * b))
        self.f_d = math.degrees(first_corner)

        second_corner = math.acos(((a ** 2) + (b ** 2) - (c ** 2)) / (2 * a * b))
        self.s_d = math.degrees(second_corner)

        third_corner = math.acos(((a ** 2) + (c ** 2) - (b ** 2)) / (2 * a * c))
        self.th_d = math.degrees(third_corner)

        if self.f_d == 90 or self.s_d == 90 or self.th_d == 90:
            print("Треугольник прямоугольный")
        elif self.f_d == self.s_d or self.f_d == self.th_d or self.s_d == self.th_d:
            print("Треугольник равнобедренный")
        elif  self.f_d == self.s_d == self.th_d:
            print("Треугольник равносторонний")
        else:
            print("Обычный треугольник")


if __name__ == '__main__':
    r1 = Triangle()
    r1.read()

    print(r1.per())
    print(r1.square())
    print(r1.height_one())
    print(r1.height_two())
    print(r1.height_three())
    


