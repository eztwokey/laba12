#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать класс Fraction для работы с дробными числами. Число должно быть представлено
# двумя целочисленными полями: целая часть и дробная часть. Реализовать арифметические
# операции сложения, вычитания, умножения и операции сравнения.

class Fraction:

    def __init__(self, whole='0', fractional='1'):
        whole = int(whole)
        fractional = int(fractional)

        self.__whole = abs(whole)
        self.__fractional = abs(fractional)

    @property
    def whole(self):
        return self.__whole

    @property
    def fractional(self):
        return self.__fractional

    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = list(map(int, line.split('/', maxsplit=1)))

        if parts[1] == 0:
            raise ValueError()

        self.__whole = abs(parts[0])
        self.__fractional = abs(parts[1])

    def display(self):
        print(f"{self.__whole}/{self.__fractional}")

    def add(self, rhs):
        if isinstance(rhs, Fraction):
            whole = self.whole * rhs.fractional + \
                self.fractional * rhs.whole
            fractional = self.fractional * rhs.fractional

            return Fraction(whole, fractional)
        else:
            raise ValueError()

    def sub(self, rhs):
        if isinstance(rhs, Fraction):
            whole = self.whole * rhs.fractional - \
                self.fractional * rhs.whole
            fractional = self.fractional * rhs.fractional

            return Fraction(whole, fractional)
        else:
            raise ValueError()

    def mul(self, rhs):
        if isinstance(rhs, Fraction):
            whole = self.whole * rhs.whole
            fractional = self.fractional * rhs.fractional

            return Fraction(whole, fractional)
        else:
            raise ValueError()

    def equals(self, rhs):
        if isinstance(rhs, Fraction):
            return (self.whole == rhs.whole) and \
                   (self.fractional == rhs.fractional)
        else:
            return False

    def greater(self, rhs):
        if isinstance(rhs, Fraction):
            v1 = self.whole / self.__fractional
            v2 = rhs.whole / rhs.fractional

            return v1 > v2
        else:
            return False

    def less(self, rhs):
        if isinstance(rhs, Fraction):
            v1 = self.whole / self.__fractional
            v2 = rhs.whole / rhs.fractional

            return v1 < v2
        else:
            return False


if __name__ == '__main__':
    r1 = Fraction(5, 6)
    r1.display()

    r2 = Fraction()
    r2.read("Введите дробь:")
    r2.display()

    r3 = r2.add(r1)
    r3.display()

    r4 = r2.sub(r1)
    r4.display()

    r5 = r2.mul(r1)
    r5.display()
