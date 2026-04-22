import random

# Получаем температуру от пользователя
print("=== ПРОГНОЗ ПОГОДЫ ===\n")

try:
    temp = int(input("Введите температуру за окном (°C): "))
except:
    print("Ошибка! Введите целое число.")
    exit()

# АНАЛИЗ ТЕКУЩЕЙ ТЕМПЕРАТУРЫ
print("\nТекущая погода:")

# Определяем описание температуры
if temp <= -30:
    condition = "Сильный мороз! Одевайтесь теплее!"
elif temp <= -10:
    condition = "Холодно! Мороз."
elif temp < 0:
    condition = "Холодно."
elif temp < 10:
    condition = "Холодновато, но терпимо."
elif temp < 15:
    condition = "Прохладно."
elif temp < 20:
    condition = "Тепло."
elif temp < 25:
    condition = "Теплая и приятная погода."
elif temp < 30:
    condition = "Жарко."
else:
    condition = "Очень жарко!"

print(f"Температура: {temp}°C")
print(f"Состояние: {condition}")

# ГЕНЕРИРУЕМ ПРОГНОЗ НА ЗАВТРА
print("\n" + "-" * 40)
print("Прогноз на завтра:")
print("-" * 40)

# Случайная температура на завтра (±5 градусов от сегодня)
tomorrow_temp = temp + random.randint(-5, 5)
print(f"Температура: {tomorrow_temp}°C")

# Случайная скорость ветра (от 0 до 25 м/с)
wind_speed = random.randint(0, 25)
if wind_speed == 0:
    wind_desc = "Ветра нет"
elif wind_speed <= 3:
    wind_desc = "Слабый ветер"
elif wind_speed <= 10:
    wind_desc = "Умеренный ветер"
elif wind_speed <= 20:
    wind_desc = "Сильный ветер"
else:
    wind_desc = "Очень сильный ветер"

print(f"Ветер: {wind_speed} м/с ({wind_desc})")

# Случайные осадки
rain_chance = random.randint(0, 100)
if rain_chance < 20:
    precipitation = "Осадков не ожидается"
elif rain_chance < 50:
    precipitation = "Возможны лёгкие осадки"
elif rain_chance < 80:
    precipitation = "Ожидаются осадки"
else:
    precipitation = "Сильные осадки"

print(f"Осадки: {rain_chance}% вероятность - {precipitation}")

# Температура воды в Чёрном море (примерно от 6 до 27 градусов)
if tomorrow_temp <= 0:
    water_temp = random.randint(6, 8)
elif tomorrow_temp <= 10:
    water_temp = random.randint(8, 10)
elif tomorrow_temp <= 20:
    water_temp = random.randint(12, 18)
else:
    water_temp = random.randint(20, 27)

print(f"Температура воды в Чёрном море: {water_temp}°C")

print("-" * 40)
print("Спасибо за использование прогноза!")

