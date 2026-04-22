h = int(input("введите ваш рост в см: "))
w = float(input("введите вес в кг: "))

iw = h- 110

difference = w - iw

if difference > 0:
    print(f"Вам нужно сбросить {difference:.1f} кг.")
elif difference < 0:
    print(f"Вам нужно набрать {abs(difference):.1f} кг.")
else:
    print("Ваш вес идеальный!")

