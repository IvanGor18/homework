import os
import string
import csv
# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на
# печать построчно последние строки в количестве lines (на всякий случай проверим, что задано положительное 
# целое число). Протестируем функцию на файле article.txt со следующим содержимым:

# def read_last(lines, file):
    
    
#     all_lines = file.readlines()

#     last_lines = all_lines[-lines:]  
    
#     for line in last_lines:
#         print(line.strip())


# read_last(int(input("Кол-во строк: ")),open(r'article.txt', 'r'))

# Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите 
# на печать в терминал ее содержимое, как и
# всех подкаталогов при помощи функции print_docs(directory).

# import os

# def print_docs(directory):
#     for root, _, files in os.walk(directory):
#         print(f"{root}:")
#         for file in files:
#             print(f"\t{file}")

# directory_to_scan = "/home/"
# print_docs(directory_to_scan)


# Требуется реализовать функцию longest_words(file), которая выводит слово
# , имеющее максимальную длину (или список слов, если таковых несколько). 

# def longest_words(file_path):
#     longest_words_list = []
#     max_length = 0

#     with open(file_path, 'r', encoding='utf-8') as file:
#         for line in file:
#             words = line.split()
#             for word in words:
#                 if len(word) > max_length:
#                     max_length = len(word)
#                     longest_words_list.clear()
#                     longest_words_list.append(word)
#                 elif len(word) == max_length:
#                     longest_words_list.append(word)

#     return longest_words_list


# file_path = 'article.txt'
# result = longest_words(file_path)

# print("Самые длинные слова:", ', '.join(result))

# текстовый редактор

# filename = input("Введите имя файла: ")
# if not filename.endswith(".txt"):
#     filename += ".txt"
            
# if os.path.exists(filename):
#     print(f"Файл {filename} уже существует.")

    
# with open(filename, 'w', encoding="utf-8") as file:
#     print("Введите текст. Оставьте строку пустой для сохранения файла.")
#     while True:
#         line = input()
#         if line == "" or any(s in set(string.punctuation) for s in line[:1]):
#             break
#         file.write(line + "\n")


## csv 

# import time

# def create_csv_file():
#     file = open('rows_300.csv', mode='w', newline='')
        
#     file.write('№,second,microsecond\n')

#     for i in range(1, 301):
#         current_time = time.time()
#         second = int(current_time)
#         microsecond = int((current_time - second) * 1000000)
#         file.write(f"{i},{second},{microsecond}\n")
#         time.sleep(0.01) 

# create_csv_file()


# круги

from PIL import Image, ImageDraw
import random
import os

def circles_generator(num_of_circles=100000):
    dir = 'circles'
    if not os.path.exists(dir):
        os.makedirs(dir)


    size = (600,600)
    radius = 300

    for i in range(num_of_circles):

        img = Image.new('RGB', size, color=(255, 255, 255))  
        draw = ImageDraw.Draw(img)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = (r, g, b)


        x_center = y_center = size[0] // 2
        coords = [
            x_center - radius,
            y_center - radius,
            x_center + radius,
            y_center + radius
        ]
        draw.ellipse(coords, fill=color)


        filename = f"circle_{i+1}.jpg"
        path = os.path.join(dir, filename)
        img.save(path, format='JPEG')

    print(f"Создано и сохранено {num_of_circles} кругов в директории '{dir}'.")

circles_generator()