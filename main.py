import pygame
import os
import tkinter as tk
from tkinter import simpledialog
from modules.classes import *
from modules.mapsetting import map

def display_rules(window):
    rules = [
        "Правила гри:",
        "1. Гравець 1 (Синій) і Гравець 2 (Червоний) керують своїми персонажами за допомогою клавіатури.",
        "2. Кожен гравець може стріляти кулями, щоб зруйнувати стіни і намагатися влучити в іншого гравця.",
        "3. Перший гравець, який влучить в супротивника кулею, виграє.",
        "4. Використовуйте клавіші зі стрілками для Гравця 1 і клавіші WASD для Гравця 2.",
        "Натисніть будь-яку клавішу, щоб почати гру..."
    ]
    
    font = pygame.font.Font(None, 36)
    y_offset = SCREEN_HEIGHT // 4
    window.fill((0, 0, 0))
    
    for line in rules:
        text_surface = font.render(line, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, y_offset))
        window.blit(text_surface, text_rect)
        y_offset += 40
        
    pygame.display.flip()
    
    waiting_for_key = True
    while waiting_for_key:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                waiting_for_key = False

def start_game(player1_nickname, player2_nickname):
    pygame.init()
    global window
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    background = pygame.image.load(os.path.join(PATH, 'images/background.png'))
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    font = pygame.font.Font(None, 120)
    winner1_text = font.render(f'{player1_nickname} WIN', True, (0, 0, 255))
    winner2_text = font.render(f'{player2_nickname} WIN', True, (255, 0, 0))

    x = 0
    y = 0
    blocks_list = []

    wall_image1 = os.path.join(PATH, 'images/wall.png')
    wall_image2 = os.path.join(PATH, 'images/wall1.png')

    for row in map:
        for i in row:
            if i == 1:
                blocks_list.append(Block(x, y, 1, wall_image1))
            elif i == 2:
                blocks_list.append(Block(x, y, 2, wall_image2))
            x += STEP
        y += STEP
        x = 0

    player1 = Player(1, 1)
    player2 = Player2(1, 3)
    clock = pygame.time.Clock()

    is_game_running = True
    winner = None

    display_rules(window)

    while is_game_running:
        window.blit(background, (0, 0))
        for block in blocks_list:
            block.blit()
            if block.colliderect(player1.bullet):
                player1.bullet.stop()
                if block.type_block == 1:
                    map[block.y // STEP][block.x // STEP] = 0
                    block.x = 1000000
            if block.colliderect(player2.bullet):
                player2.bullet.stop()
                if block.type_block == 1:
                    map[block.y // STEP][block.x // STEP] = 0
                    block.x = 1000000
        player1.bullet.move()
        player2.bullet.move()
        player1.blit()
        player2.blit()
        if player1.colliderect(player2.bullet):
            winner = 2
            is_game_running = False
            is_winner = True
        elif player2.colliderect(player1.bullet):
            winner = 1
            is_game_running = False
            is_winner = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_game_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    player1.increase_power()
                elif event.key == pygame.K_e:
                    player2.increase_power()

        clock.tick(10)
        pygame.display.flip()

    cors = (SCREEN_WIDTH // 2 - winner1_text.get_width() // 2,
            SCREEN_HEIGHT // 2 - winner1_text.get_height() // 2)
    while is_winner:
        window.blit(background, (0, 0))
        if winner == 1:
            window.blit(winner1_text, cors)
        elif winner == 2:
            window.blit(winner2_text, cors)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_winner = False
        pygame.display.flip()

# Tkinter setup
root = tk.Tk()
root.withdraw()  # Hide the main window

player1_nickname = simpledialog.askstring("Введіть дані", "Введіть нікнейм для Гравця 1 (Синій):", parent=root)
player2_nickname = simpledialog.askstring("Введіть дані", "Введіть нікнейм для Гравця 2 (Червоний):", parent=root)

if player1_nickname and player2_nickname:
    start_game(player1_nickname, player2_nickname)
else:
    print("Налаштування гри не було надано. Вихід.")
