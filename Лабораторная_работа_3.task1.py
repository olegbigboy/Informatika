def find_index ( item_lists , item):  # функция для поиска индекса в каком-то списке таворов
    for I in range(len(item_lists)):  # делаем перебор составляющих этого списка вместе с индексами
        if item_lists[I] == item:  # функция, если нашли нужный товар из списка то
            return I  # получаем индекс этого товара
    return None  # если не смогли его найти, получаем нон

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index (items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
