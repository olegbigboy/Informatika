list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
middle_index = len(list_players) // 2    # мы посчитали количество всех игроком и целочисленно разделили на 2

first_team = list_players[:middle_index]      # в первую команду мы относим игроков от начала до 3 не включительно
second_team = list_players[middle_index:]     # во вторую команду мы относим игроков от 3 и до конца

print(first_team)
print(second_team)
