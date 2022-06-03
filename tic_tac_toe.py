spisok_unikum = []          # Создать список для записи двузначных чисел, кодирующих ячейки по двум индексам, для проверки
                            # попытки повторной записи в ячейку

s_0 = ['-','-','-']         # Объявление трех списков по три элемента. Это строки с элементами столбца.
s_1 = ['-','-','-']         # Впоследствии дефисы в списках будут меняться на знаки X и 0
s_2 = ['-','-','-']

def print_matrix_ttt():                 # Функция для печати матрицы игрового поля из строк s_1, s_2, s_3 с тем,
    print('\t\t','0'," ",'1'," ",'2')                       # что в них записано на момент вызова функции
    print('\t0\t', s_0[0], " ", s_0[1], " ", s_0[2])
    print('\t1\t', s_1[0], " ", s_1[1], " ", s_1[2])
    print('\t2\t', s_2[0], " ", s_2[1], " ", s_2[2])

def any_line():    # функция проверки победы, т.е. наличия трех знаков (отличных от дефиса) в строке, в столбце или по диагонали
    if s_0[0] == s_1[1] and s_1[1] == s_2[2] and s_0[0] != '-':    # Диагональ от 0-0 к 2-2
        return True
    elif s_0[2] == s_1[1] and s_1[1]== s_2[0] and s_2[0] != '-':  # Диагональ от 0-2 к 2-0
        return True
    elif s_0[0] == s_0[1] and s_0[1] == s_0[2] and s_0[0] != '-':  # Верхняя строка
        return True
    elif s_1[0] == s_1[1] and s_1[1] == s_1[2] and s_1[0] != '-':  # Вторая строка сверху
        return True
    elif s_2[0] == s_2[1] and s_2[1] == s_2[2] and s_2[0] != '-':  # Нижняя строка
        return True
    elif s_0[0] == s_1[0] and s_1[0] == s_2[0] and s_0[0] != '-':  # Левый столбец
        return True
    elif s_0[1] == s_1[1] and s_1[1] == s_2[1] and s_0[1] != '-':  # Средний столбец
        return True
    elif s_0[2] == s_1[2] and s_1[2] == s_2[2] and s_0[2] != '-':  # Правый столбец
        return True
    else:
        return False

print("      ", "Игроки! Пора начинать Батл!")          # Начальное приветствие
print("  ", "Играйте честно! Да Пребудет с Вами СИЛА!") # и печать пустого игрового поля
print("Первый Игрок начинает ходить с крестика. Поехали!")
print()
print_matrix_ttt()
print()

for i in range(1,6):    # Цикл для организации ходов, один ход, ввод через пробел пары символов х о.
                        # При ничьей максимум пять циклов ходов. Второй игрок не участвует в пятом цикле

    while True:         # Первый игрок вводит пару координат для Х. Проверка диапазона координат и проверка того, что ячейка не занята
        step_game_1 = input("Первый Игрок - ввести через пробел номер строки и столбца (каждый от 0 до 2): ")
        step_game_1 = list(map(int, step_game_1.split()))
        if len(step_game_1) == 2:
            if step_game_1 not in spisok_unikum:
                if 0 <= step_game_1[0] <=2 and 0 <= step_game_1[1] <= 2:
                    spisok_unikum.append(step_game_1)       # В список номеров занятых ячеек добавляет новая занятая ячейка -
                    break                                   # в виде вложенного списка
                else:
                    print("\n"," -!!!---!!!- > ", "Минимум одно число выходит за диапазон от 0 до 2. Будьте внимательны!","\n")
            else:
                print("\n"," -!!!---!!!- > ", "Эта позиция в игровом поле уже занята. Выберите другую.","\n")
        else:
            print("\n"," -!!!---!!!- > ", "Введено меньше или больше двух чисел, что неверно.","\n")

    if step_game_1[0] == 0:
        s_0[step_game_1[1]] = 'x'
    elif step_game_1[0] == 1:
        s_1[step_game_1[1]] = 'x'
    else:
        s_2[step_game_1[1]] = 'x'
    print()
    print_matrix_ttt()
    print()
    if any_line():
        print("Игра завершена!", "\n")
        print("Поздравляю Вас - Первый Игрок! Вы - Победитель!!!","\n")
        print("Второму Игроку повезет в другой раз.")
        break

    if i < 5:
        while True:         # Второй игрок вводит пару координат для O. Проверка диапазона координат
            step_game_2 = input("Второй Игрок - ввести через пробел номер строки и столбца (каждый от 0 до 2): ")
            step_game_2 = list(map(int, step_game_2.split()))
            if len(step_game_2) == 2:
                if step_game_2 not in spisok_unikum:
                    if 0 <= step_game_2[0] <= 2 and 0 <= step_game_2[1] <= 2:
                        spisok_unikum.append(step_game_2)  # Добавление в список Уникум занятой позиции в Матрице
                        break
                    else:
                        print("\n"," -!!!---!!!- > ", "Минимум одно число выходит за диапазон от 0 до 2. Будьте внимательны!","\n")
                else:
                    print("\n"," -!!!---!!!- > ", "Эта позиция в игровом поле уже занята. Выберите другую.","\n")
            else:
                print("\n"," -!!!---!!!- > ", "Введено меньше или больше двух чисел, что неверно.","\n")

        if step_game_2[0] == 0:
            s_0[step_game_2[1]] = 'o'
        elif step_game_2[0] == 1:
            s_1[step_game_2[1]] = 'o'
        else:
            s_2[step_game_2[1]] = 'o'

        print_matrix_ttt()
        print()
        if any_line():
            print("Игра завершена!", "\n")
            print("Поздравляю Вас - Второй Игрок! Вы - Победитель!!!", "\n")
            print("Первому Игроку повезет в другой раз.")
            break

    else:
        print("Увы! Ничья. Ну ничего, кому-то повезет в следующий раз!")











