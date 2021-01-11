# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать базовый класс Car (машина), характеризуемый торговой маркой (строка), числом
# цилиндров, мощностью. Определить методы переназначения и изменения мощности.
# Создать производный класс Lorry (грузовик), характеризуемый также грузоподъемностью
# кузова. Определить функции переназначения марки и изменения грузоподъемности


class Car:

    def __init__(self, name='', cylind='0', power='0'):
        self.__name = str(name)
        self.__cylind = int(cylind)
        self.__power = int(power)

    @property
    def name(self):
        return self.__name

    @property
    def cylind(self):
        return self.__cylind

    @property
    def power(self):
        return self.__power

    def read(self):
        power = input('Введите новую мощность: ')

        self.__name = str(self.name)
        self.__cylind = int(self.cylind)
        self.__power = int(power)

    def display(self):
        print(
            f"Торговая марка: {self.__name}\n"
            f"Число цилиндров: {self.__cylind}\n"
            f"Мощность: {self.__power}\n"
        )

    def power_edit(self, new):
        if isinstance(new, Car):
            power = new.power

            return Car(name=self.__name, cylind=self.__cylind, power=power)
        else:
            raise ValueError()


class Lorry:

    def __init__(self, stamp='', weight='0'):
        self.__stamp = str(stamp)
        self.__weight = int(weight)

    @property
    def stamp(self):
        return self.__stamp

    @property
    def weight(self):
        return self.__weight

    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = list(map(str, line.split(',', maxsplit=5)))

        self.__stamp = parts[0]
        self.__weight = parts[1]

    def display(self):
        print(
            f"Марка грузовика: {self.__stamp}\n"
            f"Грузоподъемность: {self.__weight}\n"
        )

    def stamp_edit(self, new):
        if isinstance(new, Lorry):
            stamp = new.stamp

            return Lorry(stamp=stamp, weight=self.__weight)
        else:
            raise ValueError()

    def weight_edit(self, new):
        if isinstance(new, Lorry):
            weight = new.weight

            return Lorry(stamp=self.__stamp, weight=weight)
        else:
            raise ValueError()


if __name__ == '__main__':
    a1 = Car("Ford", 12, 160)
    a1.display()

    a2 = Car()
    a2.read()

    a3 = a1.power_edit(a2)
    a3.display()

    b1 = Lorry("Man", 1000)
    b1.display()

    b2 = Lorry()
    b2.read("Введите новую марку и грузоподъемность грузовика")
    b2.display()

    b3 = b2.stamp_edit(b1)

    b4 = b2.weight_edit(b1)

