# TODO импортировать необходимые молули
import csv
import json
# создаем переменные с отображением их путей
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:  #функция, которая выплняет действия конвертации файлов
    # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, 'r') as f:  # открываем содержимое  входяшего csv файла в режиме чтения используя имя f
        reader = csv.DictReader(f, delimiter=',')  #испоьзуем DictReader, чтобы преобразовать каждую строку в словарь
        data = list(reader)  # преобразуем полученные словари в список, который содержит словари таблицы файла csv

    ...  # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w', encoding="utf-8") as final:  # открываем содержимое выходящего .json файла в режиме записи, используя имя final
        json.dump(data, final, indent=4, ensure_ascii=False)  # создаем отступы с помощью indent=4, с помощью ensure_ascii=False сохраняем кириллицу


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
