inp = input("Введите последоватиельность скобок ")
lst = list(inp)

s = ["[", "]"]
r = ["(", ")"]
c = ["{", "}"]


def search(x):  # Функция определяет сбалансированность последовательности скобок
    while x[0] in lst and x[1] in lst and lst.index(x[0]) < lst.index(x[1]) and lst.count(x[0]) == lst.count(x[1]):
        k = 0   # Счётчик левых одинаковых скобок следующих за открывающей
        for ind, i in enumerate(lst[1:]):     # Цикл по списку входящих данных
            if i == x[1] and k == 0:    # Условие для определения закрывающе скобки
                slice = lst[lst.index(x[0]) + 1:ind + 1]     # Срез списка внутри рассматриваемых скобок
                if slice.count(s[0]) == slice.count(s[1]) and slice.count(r[0]) == slice.count(r[1]) and \
                        slice.count(c[0]) == slice.count(c[1]):   # Условие правильности скобок внутри среза
                    lst.pop(ind + 1)
                    lst.remove(x[0])
                else:
                    return None
            elif i == x[0] and ind != lst.index(x[0])-1:  # Условиие для увеличение счётчика при одинаковой скобки
                k += 1
            elif i == x[1] and k != 0:  # Условие для уменьшения счетчика при появлении правой закрывающей скобки
                k -= 1


search(s)
search(r)
search(c)

if len(lst) == 0:
    print("Сбалансированно")
else:
    print("Несбалансированно")
