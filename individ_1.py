#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


#   Создать класс Triangle для представления треугольника. Поля данных должны включать
#   углы и стороны. Требуется реализовать операции: получения полей данных,
#   вычисления площади, вычисления периметра, вычисления высот, а также определения
#   вида треугольника (равносторонний, равнобедренный или прямоугольный).

class Triangle:

    def __init__(self, first=1, second=1, third=1):
        self.first = int(first)
        self.second = int(second)
        self.third = int(third)

        self.__corner_one()

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
        self.perimeter = self.first + self.second + self.third
        self.p = self.perimeter / 2
        return self.perimeter

    # Вычисление площади треугольника
    def square(self):
        self.h = math.sqrt(self.p * (self.p - self.first) * (self.p - self.second) * (self.p - self.third))
        return self.h

    # Вычисление высоты проведенной к стороне A
    def height_one(self):
        return 2 * self.h / self.first

    # Вычисление высоты проведенной к стороне B
    def height_two(self):
        return 2 * self.h / self.second

    # Вычисление высоты проведенной к стороне C
    def height_three(self):
        return 2 * self.h / self.third

    # Вычисление градусов углов по формуле Герона
    def __corner_one(self):
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
            return print("Треугольник прямоугольный")
        elif self.f_d == self.s_d or self.f_d == self.th_d or self.s_d == self.th_d:
            return print("Треугольник равнобедренный")
        elif self.f_d == self.s_d == self.th_d:
            return print("Треугольник равносторонний")
        else:
            return print("Обычный треугольник")


if __name__ == '__main__':
    r1 = Triangle()
    r1.read()
    print(f"Периметр треугольника равен: {r1.per()}")
    print(f"Площадь треугольника равна: {r1.square()}")
    print(f"Первая высота треугольника равна: {r1.height_one()}")
    print(f"Вторая высота треугольника равна:{r1.height_two()}")
    print(f"Третья высота треугольника равна:{r1.height_three()}")



