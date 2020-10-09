import pygame
import random
import sys
from logics import get_empty_list, get_index_from_number, \
        is_zero_in_mas, pretty_print, insert_2_or_4

def draw_interface():
    pygame.draw.rect(screen, WHITE, TITLE_REC)
    font = pygame.font.SysFont('stxingkai', 70)
    pretty_print(mas)
    for row in range(BLOCKS):
        for column in range(BLOCKS):  #отрисовка интерфейса
            value = mas[row][column]
            text = font.render(f'{value}', True, BLACK)
            w = column * SIZE_BLOCK + (column + 1) * MARGIN
            h = row * SIZE_BLOCK + (row + 1) * MARGIN + SIZE_BLOCK
            pygame.draw.rect(screen, COLOURS[value], (w, h, SIZE_BLOCK, SIZE_BLOCK))
            if value != 0:
                font_w, font_h = text.get_size() # ширина и высота текста
                text_x = w + (SIZE_BLOCK - font_w) / 2
                text_y = h + (SIZE_BLOCK - font_h) / 2
                screen.blit(text, (text_x, text_y))

mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

COLOURS = {
    0: (130, 130, 130),
    2: (255, 255, 255),
    4: (255, 255, 128), 
    8: (255, 255, 0)
}

WHITE = (255, 255, 255) #по моделе RBG
GRAY = (130, 130, 130)
BLACK = (0, 0, 0)

BLOCKS = 4
SIZE_BLOCK = 110
MARGIN = 10
WIDTH = BLOCKS * SIZE_BLOCK + (BLOCKS + 1) * MARGIN
HEIGTH = WIDTH + 110
TITLE_REC = pygame.Rect(0, 0, WIDTH, 110)

mas[1][2] = 2 # положить в массив два значения
mas[3][0] = 4
print(get_empty_list(mas))
pretty_print(mas)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption('2048')
draw_interface()
pygame.display.update()

while is_zero_in_mas: # начать цикл игры
    for event in pygame.event.get(): #стандартный обработчик событий
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN: #input()
            empty = get_empty_list(mas) # найти пустые клетки, сформировать список чисел, которые не заполнены
            random.shuffle(empty) # если есть пустые клетки, случайно выбрать одну из них
            random_num = empty.pop()
            x, y = get_index_from_number(random_num) #в случайно выбранную ячейку положить либо 2, либо 4
            mas = insert_2_or_4(mas, x, y)
            print(f'Мы заполнили элемент под номером {random_num}') #если пустых клеток нет, нельзя двигать массив, то игра окончена
            draw_interface()
            pygame.display.update()
    