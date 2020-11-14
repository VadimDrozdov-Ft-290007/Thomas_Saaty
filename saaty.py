# -*- coding: utf-8 -*-

# Функция вывода двумерного массива
def printMatrix (matrix):
   for row in matrix:
      for x in row:
          print("{:8}".format(x), end = "")
      print()

print('Добро пожаловать в программу, реализующую метод анализа иерархий Томаса Саати для одного уровня!')

while True:

    # Проверка ввода правильного числа
    try:
        count = int(input('Введите количество критериев: '))
    except ValueError:
        print('Введён неправильный символ!')
    if count > 0: break
    print('Введите положительное число!')

# Создание макета матрицы
criteria = [[0] * (count+1) for i in range(count+1)]

criteria[0][0] = 'Критерии'

# Ввод номеров критериев
for j in range(count):
    criteria[0][j+1] = j+1
for i in range(count):
    criteria[i+1][0] = i+1

print('\nВ методе Саати для оценки относительной важности критериев рекомендуется специальная шкала от 1 до 9, в которой компонентам равной важности ставится в соответствие единица, при умеренном превосходстве — 3, при существенном превосходстве — 5, значительном превосходстве — 7 и очень сильном превосходстве — 9. Значения 2, 4, 6, 8 используются как промежуточные между двумя соседними компонентами.\n')

# Заполнение матрицы коэффициентами попарного сравнения
for i in range(count):
    for j in range(count):
        while True:
            if i+1 != j+1:
                print('Относительная важность критерия №', i+1, ' по отношению к критерию №', j+1, ': ', sep='', end='')

                # Проверка правильности ввода числа
                try:
                    criteria[i+1][j+1] = float(input())
                    if criteria[i+1][j+1] > 0 and criteria[i+1][j+1] <= 9:
                        criteria[i+1][j+1] = round(criteria[i+1][j+1], 3)
                        break
                    print('Вы ввели неверное число. Попробуйте ещё раз.')

                except ValueError:
                    print('Введён неправильный символ!')

            else:
                criteria[i+1][j+1] = 1.0
                break
print()
printMatrix(criteria)

# Подсчёт сумм
summ = []
s = 0
S = 0
for i in range(count):
    for j in range(count):
        s += criteria[i+1][j+1]
    summ.append(s)
    s = 0

for i in summ:
    S += i

# Расчёт весовых коэффициентов
k = []
for i in summ:
    k.append(round(i/S, 2))

print('\nВесовые коэффициенты критериев:')
for i in range(count):
    print('Критерий №', i+1, ': ', k[i], sep='')
