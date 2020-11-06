import math
import random
import pygame
from pygame import mixer

# Initialize the pygame
pygame.init()

# Dimensions
WIDTH, HEIGHT = 750, 750

# Clock
clock = pygame.time.Clock()

# Fonts
lost_font = pygame.font.SysFont("comicsans", 50)

# screen resolution
screen = pygame.display.set_mode((800, 600))

# Background Image
background = pygame.image.load('assets/background.png')

# Opening Sound
mixer.music.load("assets/background.wav")
mixer.music.play(-1)

# Game Title and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('assets/player.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('assets/enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)


# Bullet

# Ready - You can't see the bullet
# Fire - The bullet is currently moving
bulletImg = pygame.image.load('assets/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change=0
bulletY_change=10
bullet_state="ready"

# Score
score_value=0
font=pygame.font.Font('freesansbold.tff',32)
textX=10
textY=10

# define game pause here
# def pause()
 
# Game Over
over_font=pygame.font.Font('freesansbold.ttf',64)

def endofLevel1 ():
    levelEnd = over_font.render("Thanks for play!", True, (255, 255, 255))
    screen.blit(levelEnd, (200, 250))
    levelEnd = over_font.render("Level 1 Completed", True, (255, 255, 255))
    screen.blit(levelEnd, (110, 340))

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

running = True


# Game Loop
def main():

    global playerImg
    global playerX
    global playerY
    global playerX_change
    global bulletY
    global bulletX
    global bullet_state
    global score_value
    global running

    

    

