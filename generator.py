import pygame
import random


class Stack:
    def __init__(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]


class Square:
    def __init__(self, x, y, width):
        self.east = False
        self.south = False
        self.total_width = width
        self.square_width = width * 4/5
        self.square_x = width*x + width/10
        self.square_y = width*y + width/10
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.square_x, self.square_y,
                                self.square_width, self.square_width)

    def draw(self, screen):
        vx = vy = 0
        if self.east:
            vx = self.total_width/5
        if self.south:
            vy = self.total_width/5
        rect_east = pygame.Rect(self.square_x, self.square_y,
                                self.square_width + vx, self.square_width)
        rect_south = pygame.Rect(self.square_x, self.square_y,
                                 self.square_width, self.square_width + vy)
        pygame.draw.rect(screen, 0xffffff, rect_east)
        pygame.draw.rect(screen, 0xffffff, rect_south)


def draw_screen(screen, squares, stack):
    for square in squares:
        square.draw(screen)
    pygame.draw.rect(screen, (0, 255, 0), stack.top().rect)


def next_square(stack, squares, maze_width, maze_height, square_width):
    visited = [(square.x, square.y) for square in squares]
    last = stack.top()
    x = last.x
    y = last.y
    possibility = [1, 1, 1, 1]
    if x == 0 or (x-1, y) in visited:
        possibility[0] = 0
    if x == maze_width-1 or (x+1, y) in visited:
        possibility[1] = 0
    if y == 0 or (x, y-1) in visited:
        possibility[2] = 0
    if y == maze_height-1 or (x, y+1) in visited:
        possibility[3] = 0

    if sum(possibility):
        index = random.randint(0, 3)
        while possibility[index] == 0:
            index = random.randint(0, 3)
        if index == 0:
            s = Square(x-1, y, square_width)
            s.east = True
        elif index == 1:
            last.east = True
            s = Square(x+1, y, square_width)
        elif index == 2:
            s = Square(x, y-1, square_width)
            s.south = True
        else:
            last.south = True
            s = Square(x, y+1, square_width)

        stack.push(s)
        squares.append(s)
        return True
    return False


def main(screen, maze_width, maze_height, square_width):
    loop = True
    stack = Stack()
    stack.push(Square(0, 0, square_width))
    squares = [stack.top()]
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

        screen.fill((0, 0, 0))
        draw_screen(screen, squares, stack)
        while not next_square(stack, squares, maze_width, maze_height, square_width) and len(stack) != 1:
            stack.pop()
        if len(squares) == maze_width*maze_height and len(stack) == 1:
            pygame.draw.rect(screen, (255, 0, 0), Square(maze_width-1, maze_height-1, square_width).rect)
        pygame.display.flip()


if __name__ == '__main__':
    maze_w = 20
    maze_h = 20
    square_w = 20

    pygame.init()

    win = pygame.display.set_mode((maze_w*square_w, maze_h*square_w))
    main(win, maze_w, maze_h, square_w)

    pygame.quit()