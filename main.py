import os
import numpy as np


class Field:
    # инициализует поле 10х15 клеток, расставляет по координатам юниты
    def __init__(self, arr_of_chars):
        self.cs = arr_of_chars
        self.arr = np.zeros((10, 15))
        for i in self.cs:
            self.arr[i.y][i.x] = i.name

    # выводит на экран поле в виде таблицы NxM
    def Show(self):
        for i in range(self.arr.shape[0]):
            for j in range(self.arr.shape[1]):
                print(round(self.arr[i, j], None), end='')
            print('')

    # перемещает юнит под индексом cid в направлении dc
    def Move(self, cid, dc):
        x = self.cs[cid].x
        y = self.cs[cid].y
        if dc == 'w':  # проверка движения вверх
            if y == 0:
                return  # если край карты
            if y != 0:
                if self.arr[y - 1][x] != 0:  # если занятая клетка
                    return
        if dc == 'a':  # проверка движения влево
            if x == 0:
                return
            if x != 0:
                if self.arr[y][x - 1] != 0:
                    return
        if dc == 's':  # проверка движения вниз
            if y == self.arr.shape[0] - 1:
                return
            if y < self.arr.shape[0] - 1:
                if self.arr[y + 1][x] != 0:
                    return
        if dc == 'd':  # проверка движения вправо
            if x == self.arr.shape[1] - 1:
                return
            if x < self.arr.shape[1] - 1:
                if self.arr[y][x + 1] != 0:
                    return

        # перемещение
        if dc == 'w':
            self.arr[y - 1, x] = self.arr[y, x]  # занимается соседняя клетка названием
            self.arr[y, x] = 0  # прежняя зануляется
        elif dc == 's':
            self.arr[y + 1, x] = self.arr[y, x]
            self.arr[y, x] = 0
        elif dc == 'a':
            self.arr[y, x - 1] = self.arr[y, x]
            self.arr[y, x] = 0
        elif dc == 'd':
            self.arr[y, x + 1] = self.arr[y, x]
            self.arr[y, x] = 0
        self.cs[cid].Move(dc)  # обновляются координаты у юнитов


class Character:
    # инициализация юнита, задаются координаты, имя
    def __init__(self, nm, y_arr, x_arr):
        self.name = nm
        self.x = x_arr
        self.y = y_arr

    # перемещение (обновление координат на 1)
    def Move(self, dc):
        if dc == 'w':
            self.y -= 1
        if dc == 's':
            self.y += 1
        if dc == 'a':
            self.x -= 1
        if dc == 'd':
            self.x += 1


p1 = Character(1, 2, 2)
p2 = Character(2, 2, 12)
p3 = Character(3, 7, 2)
p4 = Character(4, 7, 12)
chars = [p1, p2, p3, p4]
for i in range(0, len(chars)):
    for j in range(i + 1, len(chars)):
        if chars[i].x == chars[j].x and chars[i].y == chars[j].y:
            print("ERROR")
            exit()
field = Field(chars)
counter = 0

while True:
    field.Show()
    cid = counter % len(chars)
    print("Goes", cid + 1, "\nEnter WASD direction: ", end='')
    dc = input()
    field.Move(cid, dc)
    counter += 1
    os.system('cls')