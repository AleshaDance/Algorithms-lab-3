from datetime import datetime
from random import randint
import threading
import time


start = datetime.now()      # для просмотра затраченного времени

# СОЗДАЕМ ИЗНАЧАЛЬНЫЙ ОЧЕРЕДЬ ИЗ КЛИЕНТОВ И ЗАДАЕМ ИМ НОМЕРА
M = []
for i in range(0, 201):
    alphabet = "ABCDEGHN"
    M.append(alphabet[randint(0, 7)] + str(randint(1, 999)))    # пример: А211


def work(mass, number):
    people = 67      # для подсчета количества оставшихся
    for client in mass:
        print('Window {}: {} people'.format(number, people))
        print('Client {} approached window number {}'.format(client, number))
        # time.sleep(randint(1, 3))       # пауза в 1-3 секунд
        print('The client {} left the window at number {}'.format(client, number))
        # time.sleep(randint(0, 1))       # пауза в 0-1 секунд
        people -= 1     # клиент прошел через окно


# СОЗДАЕМ 3 ОКНА (ОКНАМИ ЯВЛЯЮТСЯ *ПОТОКИ)
startTime = datetime.now()
window_1 = threading.Thread(target=work, args=(M[0: 67], '1'))      # работаем в функции work со значениями args=...
window_2 = threading.Thread(target=work, args=(M[67: 134], '2'))
window_3 = threading.Thread(target=work, args=(M[134: 201], '3'))

# НАЧИНАЕМ РАБОТУ С ПОТОКАМИ
window_1.start()        # start() - запускает ранее созданный поток
window_2.start()
window_3.start()
window_1.join()         # join() останавливает поток, когда тот выполнит свои задачи
window_2.join()
window_3.join()

print("Время выполнения: ", str(datetime.now() - start))        # время выполнения программы
# Время выполнения:  0:00:00.008001
# Время выполнения:  0:00:00.007001
# Время выполнения:  0:00:00.009001
# Время выполнения:  0:00:00.007002
# Время выполнения:  0:00:00.008002
