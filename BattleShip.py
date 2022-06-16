
class BoardOutException(Exception):     # Класс исключений для выстрела за пределы игрового поля (меньше 1 и более 6)
    pass

class StrValueException(Exception):    # Класс исключений для ошибки ввода строки вместо одного или двух чисел
    pass

class AmountValueException(Exception):  # Класс исключений для ошибки ввода пользователем координат менее или более двух
    pass

class Dot:                              # Класс точек, определяемый параметрами
    def __init__(self, x, y):           #
        self.x = x                      # координата по оси ОХ
        self.y = y                      # координата по оси OY

    def __eq__(self, other):                                # Метод проверки точки на равенство координат
        return self.x is other.x and self.y is other.y      # с координатами других точек (экземпляров класса)

class Ship:                             # Класс кораблей на игровом поле, описываемые параметрами:
    def __init__(self, length, x, y, direction):
        self.length = length                                # Длина корабля
        self.x = x                                          # Точка носа по оси ОХ
        self.y = y                                          # Точка носа по оси OY
        self.direction = direction                          # Направление. 1 - горизонтальное, 2 - вертикальное
        self.lives = length                                 # Количество жизней (изначально равно length)
                                        # Важное уточнение. От точки носа, построение корабля и для человека и для ИИ
                                        # осуществляется слева направо, если .direction == 1 и сверху вниз
                                        # если .direction == 2

    def dots(self):                     # Метод, который возвращает список точек корабля (список из списков [X, Y])
        position = [[self.x, self.y]]           # Список, с начальными координатами
        if self.length == 1:                    # Если корабль одинарной длины, возвращается список с одной парой XY
            return position
        else:                                   # Если корабль длиннее 1, то в зависимости от .direction по циклу
            if self.direction == 1:                 # добавляется единица к координате X или Y для следующей пары чисел
                for i in range(1,self.length):
                    position.append([self.x + i, self.y])
            else:
                for i in range(1,self.length):
                    position.append([self.x, self.y + i])
            return position

a = Ship(1, 2, 2, 1)

print(a.dots())
print("Количество жизней : ", a.lives)













