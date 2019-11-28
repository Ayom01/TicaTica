import pygame
from time import sleep
from pygame.locals import *
from random import randint


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
clock = pygame.time.Clock()

def check_collision(c1, c2, dist_x, dist_y):
    if c1.pos_x >= c2.pos_x - dist_x and c1.pos_x <= c2.pos_x + dist_x: 
        if c1.pos_y >= c2.pos_y - dist_y and c1.pos_y <= c2.pos_y + dist_y:
            return True

# PLAYER
class Player:
    def __init__(self):
        self.pos_x = SCREEN_WIDTH / 2
        self.pos_y = SCREEN_HEIGHT / 2
        self.size = 20
        self.speed_x = 0
        self.speed_y = 0
        self.velocity = 2
        self.score = 0
    def play_bot(self, fruit_x, fruit_y):
            if fruit_y > self.pos_y:
                self.speed_y = self.velocity
                self.speed_x = 0
            elif fruit_y < self.pos_y:
                self.speed_y = -self.velocity
                self.pos_x = 0
            elif fruit_x > self.pos_x:
                self.speed_x = self.velocity
                self.speed_y = 0
            elif fruit_x < self.pos_x:
                self.speed_x = -self.velocity
                self.speed_y = 0

# FRUIT
class Fruit:
    def __init__(self):
        self.size = 20
        self.color = [255, 0, 0]
        self.pos_x = 0
        self.pos_y = 0
    
    def set_location(self):
        self.pos_x = (randint(0, SCREEN_WIDTH - 25) // 10) * 10
        self.pos_y = (randint(0, SCREEN_HEIGHT - 25) // 10) * 10

# WALL
class Wall:
    def __init__(self, position):
        self.position = position
        self.color = (0,0,0)
        if self.position == "UP":
            self.x = SCREEN_WIDTH
            self.y = 5
            self.pos_x = 0
            self.pos_y = 0
        elif self.position == "RIGHT":
            self.x = 5
            self.y = SCREEN_HEIGHT
            self.pos_x = 0
            self.pos_y = 0
        elif self.position == "DOWN":
            self.x = SCREEN_WIDTH
            self.y = 5
            self.pos_x = 0
            self.pos_y = SCREEN_HEIGHT - 5
        elif self.position == "LEFT":
            self.x = 5
            self.y = SCREEN_HEIGHT
            self.pos_x = SCREEN_WIDTH - 5
            self.pos_y = 0


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("NotEXE")

player_1 = Player()
player_2 = Player()
bot = Player()
fruit = Fruit()
wall_up = Wall("UP")
wall_right = Wall("RIGHT")
wall_down = Wall("DOWN")
wall_left = Wall("LEFT")

fruit.set_location()


while True:
    clock.tick(80)
    bot.play_bot(fruit.pos_x, fruit.pos_y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                player_1.speed_x = player_1.velocity
                player_1.speed_y = 0
            elif event.key == K_LEFT:
                player_1.speed_x = -player_1.velocity
                player_1.speed_y = 0
            elif event.key == K_UP:
                player_1.speed_y = -player_1.velocity
                player_1.speed_x = 0
            elif event.key == K_DOWN:
                player_1.speed_y = player_1.velocity
                player_1.speed_x = 0
        if event.type == KEYDOWN:
            if event.key == K_d:
                player_2.speed_x = player_2.velocity
                player_2.speed_y = 0
            elif event.key == K_a:
                player_2.speed_x = -player_2.velocity
                player_2.speed_y = 0
            elif event.key == K_w:
                player_2.speed_y = -player_2.velocity
                player_2.speed_x = 0
            elif event.key == K_s:
                player_2.speed_y = player_2.velocity
                player_2.speed_x = 0

    screen.fill((255, 255, 255))

    # Collisions
    if check_collision(player_1, fruit, 20, 20):
        player_1.velocity += 1
        player_1.score += 1
        fruit.set_location()
    
    if check_collision(player_2, fruit, 20, 20):
        player_2.velocity += 1
        player_2.score += 1
        fruit.set_location()

    if check_collision(bot, fruit, 20, 20):
        bot.velocity += 1
        bot.score += 1
        fruit.set_location()

    if check_collision(player_1, wall_up, wall_up.x, wall_up.y) or check_collision(player_1, wall_right, wall_right.x, wall_right.y) or check_collision(player_1, wall_down, wall_down.x,wall_down.y) or check_collision(player_1, wall_left, wall_left.x, wall_left.y):
        player_1.pos_x = SCREEN_WIDTH / 2
        player_1.pos_y = SCREEN_HEIGHT / 2
        player_1.velocity -= 1

    if check_collision(player_2, wall_up, wall_up.x, wall_up.y) or check_collision(player_2, wall_right, wall_right.x, wall_right.y) or check_collision(player_2, wall_down, wall_down.x,wall_down.y) or check_collision(player_2, wall_left, wall_left.x, wall_left.y):
        player_2.pos_x = SCREEN_WIDTH / 2
        player_2.pos_y = SCREEN_HEIGHT / 2
        player_2.velocity -= 1
    
    if check_collision(bot, wall_up, wall_up.x, wall_up.y) or check_collision(bot, wall_right, wall_right.x, wall_right.y) or check_collision(bot, wall_down, wall_down.x,wall_down.y) or check_collision(bot, wall_left, wall_left.x, wall_left.y):
        bot.pos_x = SCREEN_WIDTH / 2
        bot.pos_y = SCREEN_HEIGHT / 2
        bot.velocity -= 1

    # Player_1
    player_1.pos_x += player_1.speed_x
    player_1.pos_y += player_1.speed_y 
    pygame.draw.rect(screen, (0, 0, 0), 
    [player_1.pos_x, player_1.pos_y, 
    player_1.size, player_1.size])

    # Player_2
    player_2.pos_x += player_2.speed_x
    player_2.pos_y += player_2.speed_y 
    pygame.draw.rect(screen, (48, 40, 201), 
    [player_2.pos_x, player_2.pos_y, 
    player_2.size, player_2.size])

    # Bot
    bot.pos_x += bot.speed_x
    bot.pos_y += bot.speed_y 
    pygame.draw.rect(screen, (24, 163, 66), 
    [bot.pos_x, bot.pos_y, 
    bot.size, bot.size])

    # Fruit
    pygame.draw.rect(screen, fruit.color, 
    [fruit.pos_x, fruit.pos_y, 
    fruit.size, fruit.size])

    # Walls
    pygame.draw.rect(screen, wall_up.color, 
    [wall_up.pos_x, wall_up.pos_y, 
    wall_up.x, wall_up.y])

    pygame.draw.rect(screen, wall_right.color, 
    [wall_right.pos_x, wall_right.pos_y, 
    wall_right.x, wall_right.y])

    pygame.draw.rect(screen, wall_down.color, 
    [wall_down.pos_x, wall_down.pos_y, 
    wall_down.x, wall_down.y])

    pygame.draw.rect(screen, wall_left.color, 
    [wall_left.pos_x, wall_left.pos_y, 
    wall_left.x, wall_left.y])

    # Game-Over
    if player_1.score == 20 or player_2.score == 20:
        print("\33[31m-=-" * 5 + "SCORE" + "-=-" * 5 + "\33[m")
        print(f"""\33[34mPlayer 1: {player_1.score}\33[m
\33[35mPlayer 2: {player_2.score}\33[m""")
        sleep(1)
        break

    pygame.display.update()
