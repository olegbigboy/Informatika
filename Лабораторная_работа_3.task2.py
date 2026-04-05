def find_common_participants(group_1, group_2, separator=','):  # создаем функцию для нахождения общих участников из групп

    list_participants1 = group_1.split(separator)  # делаем разделение строк группы 1
    list_participants2 = group_2.split(separator)  # делаем разделение строк группы 2


    list_participants = []  # создаем список (пустой), в который потом запишем общих участников


    for participant in list_participants1:  # выполняем перебор участников группы 1
        if participant in list_participants2 and participant not in list_participants:  # функция, если участник упоминаетсяя в списке
            # группы 2 и этого участника нет в 'пустом' списке
            list_participants.append(participant)  # пополняем пустой список этим участником


    list_participants.sort()  #  сортируем список в алфавитном порядке


    return list_participants  # возвращаем пустой список, с общими участниками


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group,participants_second_group, separator='|')  # проверили работу функциии с другим аргументом
print(f"Общие участники: {result}")
