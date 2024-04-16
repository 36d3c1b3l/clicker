import pygame
import math
import time
import random
WIDTH = 800
HEIGHT = 600
FPS = 60
BG_COLOR = "pink"
MAX_RADIUS = 30

class Target:
    max_radius = MAX_RADIUS
    growth_rate = 0.2
    color1 = "black"
    color2 = "white"

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True

    def update(self):
        #print(self.size, self.max_radius)
        if self.size >= self.max_radius:
            self.grow= False

        #print(self.size)
        #print(self.grow)
        if self.grow:
            self.size += self.growth_rate
        else:
            self.size -= self.growth_rate

    def draw(self, win):
        for i in range(10, 0, -2):
            pygame.draw.circle(win, self.color1, (self.x, self.y), i/10 * self.size)
            pygame.draw.circle(win, self.color2, (self.x, self.y), (i/10 - 0.1) * self.size)


    def hit(self, x, y):
        return self.size >= math.sqrt((self.y - y)**2 + (self.x - x)**2)
    

def draw(win, targets):
    win.fill(BG_COLOR)
    for target in targets:
        target.draw(win)

def create_target():
    return Target(random.randint(MAX_RADIUS, WIDTH - MAX_RADIUS), random.randint(MAX_RADIUS, HEIGHT - MAX_RADIUS))
    

def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))

    target1 = Target(100, 100)
    targets = [target1]
    target_spawn_period = 600
    target_spawn = pygame.USEREVENT
    pygame.time.set_timer(target_spawn, target_spawn_period)

    clock = pygame.time.Clock()

    run = True
    

    while run:
        clock.tick(60)
        click = False
        mpos_x, mpos_y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            
            if event.type == target_spawn:
                new_target = create_target()
                targets.append(new_target)

        #target things
        for target in targets:
            target.update()

            if target.size < 0:
                targets.remove(target)

            if click and target.hit(mpos_x, mpos_y):
                targets.remove(target)

        
        draw(win, targets)
        pygame.display.update()


if __name__ == "__main__":
    main()