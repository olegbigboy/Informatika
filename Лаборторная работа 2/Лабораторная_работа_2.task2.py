salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0  # подушкка безопастности, которая изначально равна 0
spend_at_moment = spend  # расходы в данный момент

for month in range (months):  # перечисляем все 10 месяцев
    nygda = spend_at_moment - salary  # сколько нехватает денег, чтобы выйти в ноль в месяц
    money_capital += nygda  # прибавляем нехватку к капиталу
    spend_at_moment *= (1 + increase)  # считаем затраты после повыщение цен каждый месяц
money_capital = round(money_capital)  # округляем капитал
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
