from threading import Thread
import time
import random
import queue
class Table:
    def __init__(self, *number):
        self.number = number
        self.guest = None
class Guest(Thread):
    def __init__(self, *name):
        super().__init__()
        self.name = name
    def run(self):
        time.sleep(random.randint(3, 10))
class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = queue.Queue()
    def guest_arrival(self, *guests):
        self.guests = guests
        for i in self.guests:
            Table_none = False
            for j in self.tables:
                if j.guest is None:
                    Table_none = True
            if Table_none == True:
                for k in self.tables:
                    if k.guest is None:
                        k.guest = i.name
                        i.start()
                        print(f'{i.name} сел(-а) за стол номер {k.number[0]}')
                        break
                    else:
                        continue
            else:
                self.queue.put(i)
                print(f'{i.name} в очереди')
    def discuss_guests(self):
        for table in self.tables:
            while table.guest is not None:
                for m in self.tables:
                    for n in self.guests:
                        if m.guest == n.name and n.is_alive() == False:
                            print(f'{m.guest} покушал(-а) и ушёл(ушла)')
                            m.guest = None
                            print(f'Стол номер {m.number[0]} свободен')
                            if self.queue.empty():
                                break
                            else:
                                next = self.queue.get()
                                m.guest = next.name
                                next.start()
                                print(f'{m.guest} вышел(-ла) из очереди и сел(-а) за стол номер {m.number[0]}')
                        else:
                            continue
# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()