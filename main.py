import random
from logics import get_empty_list, get_index_from_number, \
        is_zero_in_mas, pretty_print, insert_2_or_4
mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

mas[1][2] = 2 # положить в массив два значения
mas[3][0] = 4
print(get_empty_list(mas))
pretty_print(mas)

while is_zero_in_mas: # начать цикл игры
    input()
    empty = get_empty_list(mas) # найти пустые клетки, сформировать список чисел, которые не заполнены
    random.shuffle(empty) # если есть пустые клетки, случайно выбрать одну из них
    random_num = empty.pop()
    x, y = get_index_from_number(random_num) #в случайно выбранную ячейку положить либо 2, либо 4
    mas = insert_2_or_4(mas, x, y)
    print(f'Мы заполнили элемент под номером {random_num}') #если пустых клеток нет, нельзя двигать массив, то игра окончена
    pretty_print(mas)
