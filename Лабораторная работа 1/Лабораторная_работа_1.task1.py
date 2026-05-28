numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

count_of_numbers = len(numbers)     # расчет количества всех элементов
numbers_1 = numbers[0:4]     # Создем срез от 0 элемента списка до 4 элемента не включительно
sum_of_numbers_1 = sum(numbers_1)    # считаем ср. ариф. среза 1
numbers_2 = numbers[5:]     # Создем срез от 5 элемента списка до последнего элемента
sum_of_numbers_2 = sum(numbers_2)       # считаем ср. ариф. среза 2
average_of_numbers = (sum_of_numbers_1 + sum_of_numbers_2)/count_of_numbers     # считаем среднее арифметическое
numbers[4] = average_of_numbers      # заменяем 4 элемент на полученное среднее арифметическое
print("Измененный список:",numbers)
