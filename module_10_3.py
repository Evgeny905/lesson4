from threading import Thread, Lock
import time
import random
class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()
    def deposit(self):
        a = 0
        while a < 100:
            a += 1
            self.kesh_plus = random.randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            else:
                self.balance += self.kesh_plus
                print(f'Пополнение: {self.kesh_plus}. Баланс: {self.balance}.')
                time.sleep(0.001)

    def take(self):
        b = 0
        while b < 100:
            b += 1
            self.kesh_minus = random.randint(50, 500)
            print(f'Запрос на {self.kesh_minus}')
            if self.balance >= self.kesh_minus:
                self.balance -= self.kesh_minus
                print(f'Снятие: {self.kesh_minus}. Баланс: {self.balance}')
                time.sleep(0.001)
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')