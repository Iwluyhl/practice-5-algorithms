import math

# Ввод данных
n = int(input("Количество кур (N): "))
m = float(input("Цена за одну курицу (M): "))
x = float(input("Яиц в неделю с одной курицы (X): "))
z_with_nds = float(input("Цена за десяток яиц с учетом НДС (Z): "))

NDS_RATE = 0.10  # 10% НДС на продукты питания

total_costs = n * m

# 2. Доходы

z_clean = z_with_nds / (1 + NDS_RATE)

price_per_egg_clean = z_clean / 10

eggs_per_day = (n * x) / 7

daily_revenue = eggs_per_day * price_per_egg_clean

# 3. Окупаемость
if daily_revenue > 0:
    days = total_costs / daily_revenue
    print(f"Цена за 1 яйцо без НДС: {price_per_egg_clean:.2f} руб.")
    print(f"Куры окупятся через {math.ceil(days)} дн.")
else:
    print("Дохода нет.")