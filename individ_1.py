#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math


#   Создать класс Triangle для представления треугольника. Поля данных должны включать
#   углы и стороны. Требуется реализовать
#   операции: получения полей данных,
#   вычисления площади, вычисления периметра, вычисления высот, а также определения
#   вида треугольника (равносторонний, равнобедренный или прямоугольный).

class Triangle:

    def __init__(self, side=0):
        side = float(side)
        self.__first = side
        self.__second = side
        self.__third = side

    @property
    def first(self):
        return self.__first

    @property
    def second(self):
        return self.__second

    @property
    def third(self):
        return self.__third

    # Ввод сторон треугольника
    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = list(map(int, line.split()))
        if len(parts) != 3:
            print("Неверный размер списка", file=sys.stderr)
            exit(1)

        if parts[0] == 0 or parts[1] == 0 or parts[2] == 0:
            raise ValueError()

        if parts[0] < 1 or parts[1] < 1 or parts[2] < 1:
            raise ValueError()

        self.__first = abs(parts[0])
        self.__second = abs(parts[1])
        self.__third = abs(parts[2])

    # Вывести числа на экран
    def display(self):
        print(f"{self.__first}")

    # Вычисление периметра треугольника
    def add(self, rhs):
        if isinstance(rhs, Triangle):
            global perimeter
            perimeter = self.first + self.second + self.third
            print(f"Периметр треугольника равен: ")

            return Triangle(perimeter)
        else:
            raise ValueError()

    # Вычисление площади треугольника
    def sub(self, rhs):
        if isinstance(rhs, Triangle):
            p = perimeter / 2
            square = math.sqrt(p * (p - self.first) * (p - self.second) * (p - self.third))
            print(f"Площадь треугольника равна: ")

            return Triangle(square)
        else:
            raise ValueError()

    # Вычисление высоты проведенной к стороне A
    def height_one(self, rhs):
        if isinstance(rhs, Triangle):
            p = perimeter / 2
            h1 = 2 * math.sqrt(p * (p - self.first) * (p - self.second) * (p - self.third)) / self.first
            print(f"Высота  проведенная к стороне A равна: ")

            return Triangle(h1)
        else:
            raise ValueError()

    # Вычисление высоты проведенной к стороне B
    def height_two(self, rhs):
        if isinstance(rhs, Triangle):
            p = perimeter / 2
            h2 = 2 * math.sqrt(
                p * (p - self.first) * (p - self.second) * (p - self.third)) / self.second
            print(f"Высота  проведенная к стороне B равна: ")

            return Triangle(h2)
        else:
            raise ValueError()

    # Вычисление высоты проведенной к стороне C
    def height_three(self, rhs):
        if isinstance(rhs, Triangle):
            p = perimeter / 2
            h3 = 2 * math.sqrt(
                p * (p - self.first) * (p - self.second) * (p - self.third)) / self.third
            print(f"Высота  проведенная к стороне C равна: ")

            return Triangle(h3)
        else:
            raise ValueError()

    # Вычисление градусов углов
    def corner_one(self, rhs):
        if isinstance(rhs, Triangle):
            first_corner = math.acos(
                ((self.second ** 2) + (self.third ** 2) - (self.first ** 2)) / (2 * self.third * self.second))
            first_degrees = math.degrees(first_corner)

            second_corner = math.acos(
                ((self.first ** 2) + (self.second ** 2) - (self.third ** 2)) / (2 * self.first * self.second))
            second_degrees = math.degrees(second_corner)

            third_corner = math.acos(
                ((self.first ** 2) + (self.third ** 2) - (self.second ** 2)) / (2 * self.first * self.third))
            third_degrees = math.degrees(third_corner)

            print(f"Первый угол равен: {round(first_degrees)}")
            print(f"Первый угол равен: {round(second_degrees)}")
            print(f"Первый угол равен: {round(third_degrees)}")

            if first_degrees == 90 or second_degrees == 90 or third_degrees == 90:
                print("Треугольник прямоугольный")
            elif first_degrees == second_degrees or first_degrees == third_degrees or second_degrees == third_degrees:
                print("Треугольник равнобедренный")
            elif first_degrees == second_degrees == third_degrees:
                print("Треугольник равносторонний")
            else:
                print("Обычный треугольник")

            return Triangle()
        else:
            raise ValueError()


if __name__ == '__main__':
    r1 = Triangle()
    r1.read("Введите стороны треугольника в формате (a b c): ")

    # Вывод периметра треугольника
    r2 = r1.add(r1)
    r2.display()

    # Вывод площади треугольника
    r3 = r1.sub(r1)
    r3.display()

    # Вывод высоты треугольника к стороне A
    r4 = r1.height_one(r1)
    r4.display()

    # Вывод высоты треугольника к стороне B
    r5 = r1.height_two(r1)
    r5.display()

    # Вывод высоты треугольника к стороне C
    r6 = r1.height_three(r1)
    r6.display()

    # Вывод первого угла треугольника
    r7 = r1.corner_one(r1)
    r7.display()
