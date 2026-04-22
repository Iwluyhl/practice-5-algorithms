number = input("введите число: ")

try:
    num = float(number)

    if num  % 1 != 0 :
        print("число имеет вещественную часть")
    else:
        print("Чсило неимеет вещественной части")
except ValueError:
    print("ошибка! введено не число!")
