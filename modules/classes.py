import pygame
import os
from modules.mapsetting import map

PATH = os.path.abspath(__file__ + '/../..')
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
STEP = 50

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tanks 2D')


class Block(pygame.Rect):
    def __init__(self, x, y, type_block, image):
        super().__init__(x, y, STEP, STEP)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (STEP, STEP))
        self.type_block = type_block

    def blit(self):
        window.blit(self.image, (self.x, self.y))


class Bullet(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x, y, 20, 20)
        self.image = pygame.image.load(os.path.join(PATH, 'images/bullet.png'))
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.direction = None
        self.speed = 50
        self.count = 0

    def move(self):
        if self.count != 0:
            window.blit(self.image, (self.x, self.y))
            if self.direction == 0:
                self.y -= self.speed
            elif self.direction == 180:
                self.y += self.speed
            elif self.direction == 90:
                self.x -= self.speed
            elif self.direction == 270:
                self.x += self.speed
            self.count -= 1
            if self.count == 0:
                self.stop()

        # Проверка столкновения пули с игроком 2
        if self.colliderect(player2):
            player2.kill()  # Убиваем игрока 2
    def stop(self):
        self.count = 0
        self.x = 100000



class Panzar(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x * STEP, y * STEP, STEP, STEP)
        self.image = None
        self.pos = [x, y]
        self.bullet = Bullet(x, y)
        self.angle = 0

    def move(self):
        pass

    def blit(self):
        self.move()
        window.blit(self.image, (self.x, self.y))

    def rotate_to(self, angle):
        rotate = (360 - self.angle + angle)
        self.angle = angle
        self.image = pygame.transform.rotate(self.image, rotate)

    def strike(self):
        if self.bullet.count == 0:
            self.bullet.x = self.x + STEP / 2 - 10
            self.bullet.y = self.y + STEP / 2 - 10
            self.bullet.count = 10
            self.bullet.direction = self.angle


class Player(Panzar):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load(os.path.join(PATH, 'images/panzer.png'))
        self.image = pygame.transform.scale(self.image, (STEP, STEP))
        self.power = 1  # Начальная сила стрельбы

    def strike(self):
        if self.bullet.count == 0:
            self.bullet.x = self.x + STEP / 2 - 10
            self.bullet.y = self.y + STEP / 2 - 10
            self.bullet.count = 10
            self.bullet.direction = self.angle
            if self.power > 1:  # Увеличиваем силу стрельбы
                self.bullet.count *= self.power
            self.power = 1  # Сбрасываем силу стрельбы после выстрела

    def increase_power(self):
        self.power += 1  # Увеличиваем силу стрельбы при нажатии Q

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if map[self.pos[1] - 1][self.pos[0]] == 0:
                self.y -= STEP
                self.pos[1] -= 1
            self.rotate_to(0)
        elif keys[pygame.K_s]:
            if map[self.pos[1] + 1][self.pos[0]] == 0:
                self.y += STEP
                self.pos[1] += 1
            self.rotate_to(180)
        elif keys[pygame.K_a]:
            if map[self.pos[1]][self.pos[0] - 1] == 0:
                self.x -= STEP
                self.pos[0] -= 1
            self.rotate_to(90)
        elif keys[pygame.K_d]:
            if map[self.pos[1]][self.pos[0] + 1] == 0:
                self.x += STEP
                self.pos[0] += 1
            self.rotate_to(270)
        elif keys[pygame.K_z]:
            self.strike()


class Player2(Panzar):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load(os.path.join(PATH, 'images/enemy.png'))
        self.image = pygame.transform.scale(self.image, (STEP, STEP))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if map[self.pos[1] - 1][self.pos[0]] == 0:
                self.y -= STEP
                self.pos[1] -= 1
            self.rotate_to(0)
        elif keys[pygame.K_DOWN]:
            if map[self.pos[1] + 1][self.pos[0]] == 0:
                self.y += STEP
                self.pos[1] += 1
            self.rotate_to(180)
        elif keys[pygame.K_LEFT]:
            if map[self.pos[1]][self.pos[0] - 1] == 0:
                self.x -= STEP
                self.pos[0] -= 1
            self.rotate_to(90)
        elif keys[pygame.K_RIGHT]:
            if map[self.pos[1]][self.pos[0] + 1] == 0:
                self.x += STEP
                self.pos[0] += 1
            self.rotate_to(270)
        elif keys[pygame.K_x]:
            self.strike()