# import os
# print('dir', os.getcwd())
# dir = 'Oop1'
# if not os.path.isdir(dir):
#     os.mkdir(dir)
# else:
#     print('такая папка уже есть')

# os.chdir('Oop1')
# print('dir', os.getcwd())
# os.chdir('..')
# print('dir', os.getcwd())

# os.makedirs('f1/f2/f3/f4')

# file = open('text.txt', 'a')
# file.write('1234567890\nqwerty')

# os.rename('text.txt', 'wen_text.txt')

# os.replace('nem_text.txt', '../Oop1/new.txt')
# os.replace('../Oop1/new.txt', '../OopClasses/wen_text.txt')

import os
# os.mkdir('folder')

# if not os.path.isdir('folder'):
    # os.mkdir('folder')
# os.chdir('folder')
# os.chdir('...')
# os.makedirs('floder1/floder2/floder3')
# print(os.getcwd())
# text_file = open('text.txt', 'w')
# text_file.write('9876543210')
# os.rename('text.txt', 'renamed-text.txt')
# os.replace('renamed-text.txt', 'folder/renamed-text.txt')
# os.remove("folder/renamed-text.txt")
# os.rmdir('folder')
# os.removedirs('floder1/floder2/floder3')
# open('text.txt', 'w').write('9876543234567')
# print(os.stat('text.txt'))
# print('Размер файла', os.stat('text.txt').st_size)
# print('Время доступа', os.stat('text.txt').st_atime)
# print('Время последнего изменения', os.stat('text.txt').st_mtime)
# print('Время создания файла', os.stat('text.txt').st_ctime)

# file = open('folder/article.txt', 'a')
# # file.write('\nqwertynoqwerty')
#
# # os.rename('text.txt', 'new_text.txt')
# # os.replace('./folder/new.txt', '../new_text.txt')
# # os.remove('folder')
# # for path, dirs, files in os.walk('../venv'):
# #     for dir in dirs:
# #         print(os.path.join(path, dir))
# #     for file in files:
# #         print(os.path.join(path, file))
#
# # os.rmdir('folder')
# # print(os.stat('files.py').st_size)
# with open('.folder'):
#     pass


##############################
#1111111111111111111111111111#
##############################


# def read_end(lines, file):
#     if not isinstance(lines, int) or lines <= 0:
#         raise ValueError('Количество строк не может быть отрицательным')
#
#     try:
#         with open(file, 'r', encoding='utf-8') as f:
#             content = f.readlines()
#
#
#             for line in content[-lines:]:
#                 print(line.strip())
#     except FileNotFoundError:
#         print(f"Фаила с именем \"'{file}'\" не существует")
#
# read_end(2, 'article.txt')

#####################
#2222222222222222222#
#####################


# def print_reps(directory):
#     for dirpath, dirnames, filenames in os.walk(directory):
#         print(f"Папка: {dirpath}")
#         if dirnames:
#             print("Подпапки:")
#             for dirname in dirnames:
#                 print(f" - {dirname}")
#         if filenames:
#             print("Файлы:")
#             for filename in filenames:
#                 print(f" - {filename}")
#         print()
#
# print_reps('./venv/Lib')


#########
#3333333#
#########

# def longest_word(file):
#     with open(file, encoding='utf-8') as f:
#         listF = f.readlines()
#     maxL = 0
#     listMax = []
#     sepList = ',.;:-—!?'
#     clearLs = []
#     for sent in listF:
#         st = ''
#         for w in sent:
#             if w not in sepList:
#                 st += w
#         clearLs.append(st)
#     for sent in clearLs:
#         listSt = sent.split()
#         for item in listSt:
#             if maxL < len(item):
#                 maxL = len(item)
#                 listMax = []
#             if len(item) == maxL:
#                 listMax.append(item)
#     print(listMax)
#
#
# longest_word('./poem.txt')

############
#4444444444#
############

# def latin_text(file):
#     with open(file, 'r') as f:
#         text = f.read()
#
#     letter_count = sum(1 for char in text if char.isalpha())
#     word_count = len(text.split())
#     line_count = text.count('\n') + 1
#
#     print("Input file contains:")
#     print(f"{letter_count} letters")
#     print(f"{word_count} words")
#     print(f"{line_count} lines")
#
# latin_text('./file.txt')

