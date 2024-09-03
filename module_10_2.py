from threading import Thread
import time
class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.warrior = 100
        self.day = 0
    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.warrior > 0:
            time.sleep(1)
            self.day += 1
            self.warrior -= self.power
            print(f'{self.name} сражается {self.day} день (дня)..., осталось {self.warrior} воинов')
        print(f'{self.name} одержал победу спустя {self.day} дней (дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')