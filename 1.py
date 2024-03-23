numbers = [3, 14,27, 33, 45]
user_number = int(input("Введите число: "))
if user_number in numbers:
    print(f"Поздравляю, вы угадали число! Исходный список: {numbers}. Число пользователя: {user_number}.")
else:
    print(f"Нет такого числа! Исходный список: {numbers}. Число пользователя: {user_number}.")