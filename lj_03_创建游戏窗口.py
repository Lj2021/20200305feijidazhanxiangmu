import pygame
from plane_sprites import *
# 游戏初始化
pygame.init()
# 创建窗口。
screen = pygame.display.set_mode((480, 700))
# 绘制背景图像
# 1.加载图像数据
bg = pygame.image.load("E:/python code/飞机大战项目/images/background.png")
# 2.绘制图像
screen.blit(bg, (0, 0))
# 3.加载更新图像显示
# pygame.display.update()
# 1.绘制英雄的飞机
hero = pygame.image.load("E:/python code/飞机大战项目/images/me1.png")
screen.blit(hero, (120, 300))
pygame.display.update()
# 创建时钟对象
clock = pygame.time.Clock()

# 游戏循环-。意味着游戏正式开始！
# hero = pygame.time.Clock()
hero_rect = pygame.Rect(150, 300, 102, 126)

# 创建敌机的精灵
enemy = GameSprite("E:/python code/飞机大战项目/images/enemy1.png")
enemy1 = GameSprite("E:/python code/飞机大战项目/images/enemy1.png", 2)
# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)
while True:
    clock.tick(60)
    # 监听用户的退出事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("游戏退出。。。")
            pygame.quit()
            exit()
    # 获取用户的事件
    event_list = pygame.event.get()
    if len(event_list) > 0:

        print(event_list)
    hero_rect.y -= 1
    if hero_rect.bottom <= 0:
        hero_rect.y = 700
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    enemy_group.update()

    enemy_group.draw(screen)


    pygame.display.update()
pygame.quit()
