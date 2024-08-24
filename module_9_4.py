first = 'Мама мыла раму'
second = 'Рамена мало было'

lambda_def = list(map(lambda x, y: x == y, first, second))
print(lambda_def)

def get_advanced_writer(file_name):
    my_file = open(file_name, 'w')
    my_file.write('')
    my_file.close()
    def write_everything(*data_set):
        for line in data_set:
            my_file = open(file_name, 'a')
            my_file.write(str(line))
            my_file.write('\n')
            my_file.close()
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

import random
class MysticBall:
    def __init__(self, *words):
        self.words = words
    def __call__(self):
        win = random.choice(self.words)
        return win

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())