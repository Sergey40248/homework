#  Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, 
# является ли этот день выходным.
# Пример:

#- 6 -> да
#- 7 -> да
#- 1 -> нет

a = int(input('Введите цифру дня недели: '))
if a < 1 or a > 7:
    print(f'Цифра {a} не является днем недели')
elif a == 6 or a == 7:
    print(f'цифра {a} является  выходным днем')
else:
    print(f'Цифра {a} не выходной')
    
