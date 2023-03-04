import random
import pygame
pygame.init()

width, height = 1000, 700
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Algorithm Visualizer")


class sortItem:
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    COLORS = [WHITE, GREEN, BLUE, RED]
    GRAY = (25, 25, 25)

    def __init__(self, radius, color, x, y):
        self.radius = radius
        self.x = x
        self.y = y
        self.color = color

    def drawSortItem(self):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)


score = "Sorting using bubble sort......"
font = pygame.font.Font('./moochio/MOOCHIO.ttf', 32)


def write(x, y):
    text = font.render(score, True, sortItem.BLUE)
    window.blit(text, (x, y))


def BubbleSort(radius):
    for i in range(0, len(radius)):
        for j in range(0, len(radius)-1-i):
            if radius[j] > radius[j+1]:
                radius[j], radius[j+1] = radius[j+1], radius[j]

    print("Sorted radius:  ", radius)
    x = [100, 300, 500, 700, 900]
    ss1 = sortItem(radius[0], sortItem.WHITE, x[0], 400)
    ss2 = sortItem(radius[1], sortItem.WHITE, x[1], 400)
    ss3 = sortItem(radius[2], sortItem.WHITE, x[2], 400)
    ss4 = sortItem(radius[3], sortItem.WHITE, x[3], 400)
    ss5 = sortItem(radius[4], sortItem.WHITE, x[4], 400)

    write(200, 250)
    items = [ss1, ss2, ss3, ss4, ss5]
    for ss in items:
        ss.color = sortItem.RED
        ss.drawSortItem()


def main():
    run = True
    clock = pygame.time.Clock()
    clock.tick(60)

    s1 = sortItem(70, sortItem.WHITE, 100, 100)
    s2 = sortItem(25, sortItem.WHITE, 300, 100)
    s3 = sortItem(45, sortItem.WHITE, 500, 100)
    s4 = sortItem(10, sortItem.WHITE, 700, 100)
    s5 = sortItem(35, sortItem.WHITE, 900, 100)
    items = [s1, s2, s3, s4, s5]

    item_radius = []
    for s in items:
        item_radius.append(s.radius)
    print("Unsorted radius: ", item_radius)

    BubbleSort(item_radius)

    while run:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                run = False
        for item in items:
            item.drawSortItem()

        pygame.display.update()


if __name__ == '__main__':
    main()
