class State:
    def __init__(self, quan, src, dest, tmp, step):
        self.quan = quan      # количество дисков
        self.src = src      # стержень с которого выполняется перемещение
        self.dest = dest        # стержень на который выполняется перемещение
        self.tmp = tmp      # вспомогательной стержень
        self.step = step        # ifu, на которой находится выполнение алгоритма


def tower(quan, src, dest, tmp):
    stack = []      # создаем стек
    state = State(quan, src, dest, tmp, 0)     # добавляем в него состояние с параметрами, переданными в функцию
    stack.append(state)     # добавляем состояние в стек
    while len(stack) > 0:       # пока стек не пуст
        state = stack[-1]       # берем последний добавленный элемент стека
        if state.step == 0:
            if state.quan == 0:        # если число дисков равно нулю
                stack.pop()     # то удалить рассматриваемый элемент стека
            else:
                state.step += 1       # иначе перейти к следующему шагу (для данного состояния)
                newState = State(state.quan-1, state.src, state.tmp, state.dest, 0)    # переложить n-1 дисков на вспомогательную, используя конечную
                stack.append(newState)      # добавить новое состояние в стек
            continue
        if state.step == 1:
            print(str(state.src) + "->" + str(state.dest))    # вывести данные о перемещении диска на экран
            state.step += 1
            newState = State(state.quan-1, state.tmp, state.dest, state.src, 0)    # переложить n-1 дисков со вспомогательной оси на конечную, используя начальную
            stack.append(newState)      # добавить новое состояние в стек
            continue
        if state.step == 2:
            stack.pop()     # удалить рассматриваемый элемент стека
            continue


tower(7, 1, 3, 2)
