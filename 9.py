def is_leap_year(year: int) -> bool:
    """Проверка високосного года по правилам Григорианского календаря."""
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def days_in_month(month: int, year: int) -> int:
    """Возвращает количество дней в указанном месяце."""
    if month == 2:
        return 29 if is_leap_year(year) else 28

    # месяцы с 31 днём
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31

    # месяцы с 30 днями
    if month in (4, 6, 9, 11):
        return 30

    return -1  # некорректный месяц


def is_valid_date(day: int, month: int, year: int) -> bool:
    """Проверка корректности введённой даты."""
    if year <= 0:
        return False
    if month < 1 or month > 12:
        return False

    dim = days_in_month(month, year)
    if dim == -1:
        return False

    return 1 <= day <= dim


def next_day(day: int, month: int, year: int):
    """Возвращает дату следующего дня."""
    dim = days_in_month(month, year)

    if day < dim:
        return day + 1, month, year

    # если день последний в месяце
    if month < 12:
        return 1, month + 1, year

    # если 31 декабря
    return 1, 1, year + 1


# --- Основная программа ---
day = int(input("Введите день: "))
month = int(input("Введите месяц: "))
year = int(input("Введите год: "))

if not is_valid_date(day, month, year):
    print("Некорректная дата!")
else:
    nd, nm, ny = next_day(day, month, year)
    print(f"Следующий день: {nd:02d}.{nm:02d}.{ny}")
