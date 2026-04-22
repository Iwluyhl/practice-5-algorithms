gender = input("ведите пол(муж/жен): ").lower()
age = int(input("введите возраст: "))
if gender not in ['муж', 'жен']:
    print("Ошибка: введите 'муж' для мужского пола или 'жен' для женского.")
else:
    if (gender == 'м' and age >= 65) or (gender == 'ж' and age >= 60):
        print("Пора на пенсию!")
    else:
        print("Ещё не пора на пенсию.")
