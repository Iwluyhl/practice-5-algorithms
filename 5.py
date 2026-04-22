from unicodedata import digit

num = input("введите номер трамвайного билета: ")
if len(num) != 6:
    print("Номер должен содержать ровно 6 цифр")
else:
    d = [int(digit) for digit in num]

    sum_f = d[0] + d[1] + d[2]

    sum_l = d[3] + d[4] + d[5]

    if sum_l  ==  sum_f:
        print("билет счастливый")
    else:
        print("Билет не счастливый")