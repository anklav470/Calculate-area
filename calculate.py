import math


def circle_area(radius):
    return math.pi * radius ** 2


def triangle_area(side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))


def is_right_triangle(side1, side2, side3):
    sides = [side1, side2, side3]
    sides.sort()
    return 'Да' if sides[0] + sides[1] == sides[2] ** 2 else 'Нет'


# Запрос радиуса круга или сторон треугольника у пользователя
input_data = input("Введите радиус круга или стороны треугольника через пробел: ")

# Проверка на ввод радиуса круга
try:
    circle_radius = float(input_data)
    print("Площадь круга:", circle_area(circle_radius))
except ValueError:
    # Если введены стороны треугольника
    sides = input_data.split()
    if len(sides) != 3:
        print("Неверное количество сторон треугольника")
    else:
        try:
            side1, side2, side3 = float(sides[0]), float(sides[1]), float(sides[2])
            print("Площадь треугольника:", triangle_area(side1, side2, side3))
            print("Является ли треугольник прямоугольным:", is_right_triangle(side1, side2, side3))
        except ValueError:
            print("Некорректные значения сторон треугольника")
