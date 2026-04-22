day = int(input("Введите номер дня недели (1–7): "))

if day == 1:
    print("Понедельник")
elif day == 2:
    print("Вторник")
elif day == 3:
    print("Среда")
elif day == 4:
    print("Четверг")
elif day == 5:
    print("Пятница")
elif day == 6:
    print("Суббота")
elif day == 7:
    print("Воскресенье")
else:
    print("Ошибка: введите число от 1 до 7!")