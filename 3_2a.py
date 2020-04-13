# Очередь с приоритетным включением — такая очередь, в которой последовательность элементов все время
# поддерживается упорядоченной по убыванию приоритета. То есть, при включении элемента, выполняется
# поиск места, куда он будет включен, а затем происходит сама процедура включения.


class Stack:
    def __init__(self):
        self.items = []

    def find_item(self, item, priority):
        index = 0
        identicFlag = False

        for item in self.items:
            index += 1
            if item[1] == priority:     # Есть ли схожий приоритет в массиве?
                identicFlag = True    # Есть!
                break
        return identicFlag, index

    def push(self, new_item, priority):
        # ПОИСК ПО СХОЖЕМУ ПРИОРИТЕТУ (через костыли, явно можно было сделать проще)
        index, identicFlag = self.find_item(new_item, priority)

        # ВСТАВКА ЭЛЕМЕНТА
        if identicFlag:
            self.items.insert(index - 1, [new_item, priority])
        else:   # т.к похожего элемента нету, придется искать место для записи
            for i in range(priority + 1, 11):
                similar_index, similarFlag = self.find_item(new_item, i)
                if similarFlag:
                    self.items.insert(similar_index - 1, [new_item, priority])
                    break
            if not similarFlag:
                self.items.append([new_item, priority])

        print("Added new entry {} with priority {}".format(new_item, priority))

    def total(self):
        for item in self.items:
            print("Entry {} with priority {}".format(item, item[1]))


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

print('\n========== The final list ==========')
stack.total()






