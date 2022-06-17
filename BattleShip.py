
class BoardOutException(Exception):     # Класс исключений для выстрела за пределы игрового поля (координата меньше 1 и более 6)
    def __str__(self):                  # Специальный метод строкового представления, чтобы избежать ссылки на ячейку памяти
        return "Вы пытаетесь выстрелить за пределы игрового поля! Повторите выстрел."

class DotRepeatException(Exception):    # Класс исключений для повторного выстрела по ранее "обстреляной" клетке
    def __str__(self):                  # Специальный метод строкового представления
        return "В эту клетку раньше уже стреляли! Повторите выстрел."

class AmountValueException(Exception):  # Класс исключений для ошибки ввода пользователем координат менее или более двух
    pass

class Dot:                              # Класс точек, определяемый параметрами
    def __init__(self, x, y):           #
        self.x = x                      # координата по оси ОХ
        self.y = y                      # координата по оси OY

    def __eq__(self, other):                                # Метод проверки точки на равенство координат
        return self.x is other.x and self.y is other.y      # с координатами других точек (экземпляров класса)

    #def __str__(self):                      # Специальный метод строкового представления объекта, чтобы избежать
     #   return f"Dot ({self.x}, {self.y})"  # вид "ссылка на ячейку памяти" при вызове объекта

    def __repr__(self):                     # Специальный метод представления, используется, в том числе
        return f"Dot ({self.x}, {self.y})"   # для вывода объектов в контейнере, типа списка


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
    @property
    def dots(self):                     # Метод, который возвращает список точек корабля (список из списков [X, Y])
        position = []                   # Пустой список, для координат корабля
        position.append(Dot(self.x, self.y))
        if self.length == 1:                    # Если корабль одинарной длины, возвращается список с одной парой XY
            return position
        else:                                   # Если корабль длиннее 1, то в зависимости от .direction по циклу
            if self.direction == 1:             # добавляется единица к координате X или Y для следующей пары чисел
                for i in range(1,self.length):
                    position.append(Dot(self.x + 1, self.y))
            else:
                for i in range(1,self.length):
                    position.append(Dot(self.x, self.y + 1))
            return position

    def shooten(self, shot):                    # Метод проверки попадания "выстрела" (точки) в корабль (в одну из
        return shot in self.dots                # точек, занятых кораблем)


a = Ship(2, 2, 2, 2)
print(a.shooten(Dot(2,2)))







