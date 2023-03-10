# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?


# Пусть Петя сделал x журавликов,
# тогда Сережа сделал x журавликов,
# а Катя сделала (x+x)*2 журавликов.
# Все вместе они сделали x+x+(x+x)*2=6x журавликов.
# Отсюда уравнение: 6x=S

# Примеры:
# 6 -> 1 4 1
# 24 -> 4 16 4 
# 60 -> 10 40 10

# также можно использовать x = float(S/6) вместо int, 
# тогда данные будут точнее с дробными числами, но вывод не красивый получается(

S = int(input("Введите кольчество журавликов - "))
x = int(S/6)
y = (x + x) * 2
print('Петя сделал', x, 'журавликов, ','Катя сделала', y, 'журавликов, ', 'Серёжа сделал', x, 'журавликов')