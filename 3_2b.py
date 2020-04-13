# Очередь с приоритетным включением — такая очередь, в которой новый элемент добавляется в конец, а
# при удалении ищется элемент с наибольшим приоритетом


class Stack:
    def __init__(self):
        self.items = []

    # ДОБАВЛЕНИЕ В КОНЕЦ СПИСКА
    def push(self, item, priority):
        self.items.append([item, priority])
        print("Added new entry {} with priority {}".format(item, priority))

    # УДАЛЕНИЕ ЭЛЕМЕНТА С НАИБОЛЬШИМ ПРИОРИТЕТОМ
    def delete(self):
        # НАХОЖДЕНИЕ НАИБОЛЬШЕГО ПРИОРИТЕТА
        max_priority = 0

        for item in self.items:
            if max_priority < item[1]:
                max_priority = item[1]

        # НАХОЖДЕНИЕ index-а ЭТОЙ ЗАПИСИ И УДАЛЕНИЕ
        index = 0

        for item in self.items:
            if max_priority == item[1]:
                print('Entry {} delete with priority {}'.format(item[0], item[1]))
                self.items.pop(index)
                break
            index += 1

    # ВЫВЕДЕНИЕ ИТОГОВ
    def total(self):
        for item in self.items:
            print('Entry {} with priority {}'.format(item[0], item[1]))


stack = Stack()

print('========== List of added items ==========')
stack.push('Lada', 1)
stack.push('Mercedes', 7)
stack.push('Lexus', 9)
stack.push('BMW', 7)
stack.push('Toyota', 2)
stack.push('Ford', 5)
stack.push('Volvo', 6)
stack.push('Cherry', 1)
stack.push('Nissan', 4)
stack.push('Mazda', 6)
stack.push('Jaguar', 9)

print('\n========== List of deleted items ==========')
stack.delete()

print('\n========== The final list ==========')
stack.total()






