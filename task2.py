
#Напишите программу, которая принимает на вход координаты точки (X и Y),
#  причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
#  в которой находится эта точка (или на какой оси она находится).

#Пример:
#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3

x = int(input('enter X  '))
y = int(input('enter Y  '))


if x > 0 and y > 0:

    print(f'Введенные кординаты {x, y} принадлежат 1 четверти ')

elif x > 0 and y < 0:

    print(f'Введенные кординаты {x, y} принадлежат 4 Четверти')

elif x < 0 and y > 0:

    print(f'Введенные кординаты {x, y} принадлежат 2 Четверти')

elif x < 0 and y < 0:

    print(f'Введенные кординаты {x, y} принадлежат 3 Четверти')


elif x == 0 and y > 0:
    print(f'Введенные кординаты {x, y},точка лежит на оси y между 1 и 2 четвертью')

elif x == 0 and y < 0:
    print(f'Введенные кординаты {x, y},точка лежит на оси y между 3 и 4 четвертью')

elif y == 0 and x > 0:
    print(f'Введенные кординаты {x, y},точка лежит на оси y между 1 и 4 четвертью')

elif y == 0 and x > 0:
    print(f'Введенные кординаты {x, y},точка лежит на оси y между 1 и 2 четвертью')

else:

    print(f' Вы ввели {x, y} не выполнено условие задачи X ≠ 0 и Y ≠ 0')
    
