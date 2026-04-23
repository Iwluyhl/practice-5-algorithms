# игра "Однорукий бандит"
import random
balance = 5000
bet_cost = 100

print(f"Добро пожаловать в 'Однорукий бандит'!")
print(f"Ваш начальный капитал: {balance} руб. Стоимость игры: {bet_cost} руб.")



while balance >= bet_cost:
    # ОДИН ЕДИНСТВЕННЫЙ ВВОД
    # Если нажать просто Enter, переменная 'cmd' будет пустой строкой ""
    cmd = input(f"\nБаланс: {balance} | Нажмите [Enter] для игры или [q] для выхода: ")

    # Проверяем, не ввел ли пользователь символ выхода
    if cmd.lower() == 'q':
        print("Игра завершена. Ваш итог:", balance)
        break # Выходим из цикла
    balance -= bet_cost
    a, b, c = random.randint(0, 7), random.randint(0, 7), random.randint(0, 7)
    print(f"Крутим барабаны... Результат: [ {a} | {b} | {c} ]")

    print(f"результат {a} {b} {c} ")

    if a == 7 and b == 7 and c == 7:
        print("!!!ДЖЕКПОТ!!! Вы выйграли 100000 руб! Игра окончена.")
        balance += 1000000
        is_running = False

    elif a == 6 and b == 6 and c == 6:
        print("Штраф! Вы потеряли 1000 руб")
        balance -= 1000
    elif a == 5 and b == 5 and c == 5:
       print("Три пятерки! вы выйграли 5000 руб!")
       balance += 5000
    elif a == 5 and b == 5:
       print("Две пятерки! Вы выйграли 500 руб!")
       balance += 500
    elif a == 5:
        print("Одна пятерка! Вы выйграли 100 руб!")
        balance += 100
    elif a == b == c:
        print("Три в ряд! Вы выйграли 2000 руб!")
        balance += 2000
    elif a == 7 and b == 7:
        print("Две семерки! Вы выйграли 1000 руб!")
        balance += 1000
    elif a == 7:
        print("Одна семерка! Вы выйграли 500 руб!")
        balance += 200

    else:
        print("Увы, ничего не вышло. Попробуйте снова!")
    print(f"Ваш текущий баланс: {balance} руб.")

    if (balance == 0):
        print("У вас закончились деньги. Игра окончена.")
        break
