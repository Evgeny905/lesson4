import time
from threading import Thread
from datetime import datetime
def wite_words(word_count, file_name):
    file = open(file_name, 'w')
    file.close()
    for i in range(1, word_count + 1):
        file_new = open(file_name, 'a')
        file_new.write((f'Какое-то слово № {i}\n'))
        file_new.close()
        time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

time_start_1 = datetime.now()

wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

time_end_1 = datetime.now()

time_1 = time_end_1 - time_start_1

print(f'Работа потоков{time_1}')

time_start_2 = datetime.now()

thr_first = Thread(target = wite_words, args = (10, 'example5.txt'))
thr_second = Thread(target = wite_words, args = (30, 'example6.txt'))
thr_third = Thread(target = wite_words, args = (200, 'example7.txt'))
thr_fourth = Thread(target = wite_words, args = (100, 'example8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()

time_end_2 = datetime.now()

time_2 = time_end_2 - time_start_2

print(f'Работа потоков{time_2}')