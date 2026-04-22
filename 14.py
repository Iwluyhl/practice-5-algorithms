import random
from math import comb

# НАЧАЛО ЛОТЕРЕИ
print("=" * 60)
print("         ДОБРО ПОЖАЛОВАТЬ В ЛОТЕРЕЮ!")
print("=" * 60)
print("\nУгадайте 5 чисел от 1 до 42 и выигрывайте деньги!")
print()

# Программа загадывает 5 неповторяющихся чисел
winning_numbers = sorted(random.sample(range(1, 43), 5))

# Вводим числа от пользователя
print("Введите 5 различных чисел от 1 до 42")
print("(числа вводите через пробел или запятую)")
print()

user_input = input("Ваши числа: ").strip()

# Обработка ввода
try:
    # Заменяем запятые на пробелы и разбиваем
    user_input = user_input.replace(",", " ")
    user_numbers = list(map(int, user_input.split()))
    
    # Проверяем количество чисел
    if len(user_numbers) != 5:
        print(f"Ошибка! Вы ввели {len(user_numbers)} чисел, нужно 5!")
        exit()
    
    # Проверяем диапазон
    for num in user_numbers:
        if num < 1 or num > 42:
            print(f"Ошибка! Число {num} выходит за пределы 1-42!")
            exit()
    
    # Проверяем на повторения
    if len(set(user_numbers)) != 5:
        print("Ошибка! Числа должны быть разными!")
        exit()
    
    user_numbers = sorted(user_numbers)

except:
    print("Ошибка! Введите 5 целых чисел через пробел или запятую.")
    exit()

# РЕЗУЛЬТАТЫ
print("\n" + "=" * 60)
print("РЕЗУЛЬТАТЫ ЛОТЕРЕИ")
print("=" * 60)

print(f"\nВыигрышные числа: {winning_numbers}")
print(f"Ваши числа:       {user_numbers}")

# Находим совпадения
matches = len(set(winning_numbers) & set(user_numbers))

print(f"\nВы угадали: {matches} чисел из 5")

# Определяем приз
if matches == 5:
    prize = 50000
    result = "СУПЕР ПРИЗ!"
elif matches == 4:
    prize = 4000
    result = "Отличный результат!"
elif matches == 3:
    prize = 300
    result = "Неплохо!"
else:
    prize = 0
    result = "К сожалению, вы не выиграли."

print(f"Результат: {result}")
print(f"Приз: {prize} рублей")

print("\n" + "=" * 60)
print("ИНФОРМАЦИЯ О ЛОТЕРЕЕ")
print("=" * 60)

# Вычисляем вероятность
total_combinations = comb(42, 5)
print(f"\nВсего возможных комбинаций: {total_combinations:,}")
print(f"Вероятность угадать все 5 чисел: 1 из {total_combinations:,}")
print(f"Это примерно {1/total_combinations*100:.6f}% (0.000001%)")

print("\nВероятности по совпадениям:")
print(f"  3 совпадения: приз 300 рублей")
print(f"  4 совпадения: приз 4000 рублей")
print(f"  5 совпадений: приз 50000 рублей")

print("\n" + "=" * 60)
print("Спасибо за участие в лотерее!")
print("=" * 60)

