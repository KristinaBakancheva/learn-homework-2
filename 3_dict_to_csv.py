"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

def main():
    dict_people = [
        {'name': 'Alex', 'age': 14, 'job': 'School', "family_size": "small"}, 
        {'name': 'Jasica', 'age': 35, 'job': 'Teacher', "family_size": "large"}, 
        {'name': 'Stive', 'age': 20, 'job': 'Student', "family_size": "medium"},
        {'name': 'Stacy', 'age': 2, 'job': 'baby', "family_size": "big"}
    ]
    
    with open("new.csv", "w", encoding = "utf-8") as n:
        field = ["name", "age", "job", "family_size"]
        writer = csv.DictWriter(n, field, delimiter = ";")
        writer.writeheader()
        for el in dict_people:
            writer.writerow(el)


if __name__ == "__main__":
    main()
