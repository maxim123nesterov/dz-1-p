# Задача 2: Найдите сумму цифр трехзначного числа.
# Примеры:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

x = int(input('Введите трёхзначное число - '))
# n = x // 100
# b = (x % 100) / 10
# m = x % 10
# sum = n + int(b) + m
sum = (x // 100) + ((x % 100) / 10) + (x % 10)
print(int(sum))