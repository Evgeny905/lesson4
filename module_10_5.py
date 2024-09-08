import datetime
import multiprocessing


def read_info(name):
    all_data = []
    file = open(name, 'r')
    line = '0'
    while line != '':
        line = file.readline()
        all_data.append(line)
    file.close()


# Линейный вызов
start = datetime.datetime.now()

filenames = [f'./file {number}.txt' for number in range(1, 5)]
for name in filenames:
    read_info(name)

end = datetime.datetime.now()

print(end - start)
# Время выполнения 0:00:05.353258


"""
# Многопроцессный

start = datetime.datetime.now()

if __name__ == "__mane__":
    with multiprocessing.Pool(processes=2) as pool:
        filenames = [f'./file {number}.txt' for number in range(1, 5)]
        pool.map(read_info, filenames)
end = datetime.datetime.now()
print(end - start)

# Время 0:00:00.000004
"""


"""
# Создание файлов

filenames = [f'./file {number}.txt' for number in range(1, 5)]
for name in filenames:
    file = open(name, 'w')
    file.write(f'Я {name}, у меня записаны строки\n')
    file.close()
    for i in range(10_000_000):
        file = open(name, 'a')
        file.write(f'Я строка {i} в {name}\n')
        file.close()
"""