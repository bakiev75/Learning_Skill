
class BoardOutException(Exception):     # Класс исключений для выстрела за пределы игрового поля (координата меньше 1 и более 6)
    def __str__(self):                  # Специальный метод строкового представления, чтобы избежать ссылки на ячейку памяти
        return "Вы пытаетесь выстрелить за пределы игрового поля! Повторите выстрел."

class DotRepeatException(Exception):    # Класс исключений для повторного выстрела по ранее "обстреляной" клетке
    def __str__(self):                  # Специальный метод строкового представления
        return "В эту клетку раньше уже стреляли! Повторите выстрел."

# class AmountValueException(Exception):  # Класс исключений для ошибки ввода пользователем координат менее или более двух
   # pass

class BoardWrongShipException(Exception):   # Исключение, которое не будет выводить сообщение об ошибке
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


class Board:                                    # Класс игрового поля
    def __init__(self, hid=False, size=6):
        self.size = size                        # Атрибут размера стороны поля, по умолчанию 6
        self.hid = hid                          # Атрибут,"скрывающий" корабли от вывода на консоль

        self.count = 0                          # Количество пораженных кораблей

        self.field = [["O"] * size for _ in range(size)]    # Генератор списка. Формирует поле из нулей в
                                                            # виде списка списков
        self.busy = []                          # Список занятых точек, занятых кораблями, либо куда уже стреляли
        self.ships = []                         # Список кораблей. Создается при генерировании кораблей на доске

    def __str__(self):                          # Функция формирования специальной строки res, в которой хранится
        res = ""                                # вид доски, которую видит игрок, со всеми атрибутами (разделители,
        res += "  | 1 | 2 | 3 | 4 | 5 | 6 |"    # номера строк и столбцов, специальные символы переноса строки)
        for i, row in enumerate(self.field):
            res += f"\n{i + 1} | " + " | ".join(row) + " |"

        if self.hid:                            # Замена в строке res символов, если атрибут hid равен True
            res = res.replace("■", "O")
        return res

    def out(self, d):                           # Метод определяет, находится ли точка в пределах игрового поля
        return not ((0 <= d.x < self.size) and (0 <= d.y < self.size))  #

    def contour(self, ship, verb=False):        # Метод контура, для получения списка точек вокруг корабля
        near = [                                # Стандартный набор относительных сдвигов от каждой точки
            (-1, -1), (-1, 0), (-1, 1),         # корабля, во все стороны
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for d in ship.dots:                             # цикл перебора точек корабля
            for dx, dy in near:                         # из списка near извлекаются пары координат
                cur = Dot(d.x + dx, d.y + dy)           # и прибавляются к рассматриваемой точке корабля, сдвигая точку
                if not (self.out(cur)) and cur not in self.busy:    # Проверка двух условий
                    if verb:                            # Проверка параметра verd, который определяет
                        self.field[cur.x][cur.y] = "."  # печать точки на поле, только в процессе игры!
                    self.busy.append(cur)               # Добавление новой точки (контурной) в список занятых точек

    def add_ship(self, ship):                           # Метод обавления корабля на доску
        for d in ship.dots:                                # Для точек корабля по циклу
            if self.out(d) or d in self.busy:              # Условие, что точка корабля внутри игр.поля и не в списке Busy
                raise BoardWrongShipException()            # Если условие True, выбрасывается исключение, без сообщения
        for d in ship.dots:
            self.field[d.x][d.y] = "■"
            self.busy.append(d)

        self.ships.append(ship)
        self.contour(ship)






