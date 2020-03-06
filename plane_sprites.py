import random
import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件【这里的 USERAGENT+1是为了区别上面已经被占用的。】
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image_name, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self, *args):
        self.rect.y += self.speed


# 游戏背景类
class Background(GameSprite):
    # 游戏背景精灵

    def __init__(self, is_alt=False):
        super().__init__("E:/python code/飞机大战项目/images/background.png")
        # 1.调用父类方法实现精灵的创建
        # 2.判断是否是交替图像，如果是，需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 1.调用父类的方法实现
        super().update()
        #  2.判断是否移除屏幕，如果移出屏幕，将图像设置到图像上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


# 敌机类
class Enemy(GameSprite):
    # 敌机精灵
    def __init__(self):
        # 1.调用父类方法，创建敌机精灵，同时制定敌机的图片
        super().__init__("E:/python code/飞机大战项目/images/enemy1.png")

        # 2.制定敌机的初始随机速度 1-3
        self.speed = random.randint(1, 3)
        # 3.指定敌机初始的随机位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self, *args):
        # 1.调用父类方法，保持垂直方向的飞行
        super().update()
        # 2.判断是否飞出屏幕。若飞出则删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            # print("飞出屏幕，需要从精灵组删除")
            # kill方法可以将精灵从精灵组中移除，销毁敌机，释放内存。
            self.kill()

    def __del__(self):
        # print("敌机挂了 %s" % self.rect)
        pass


# 英雄类
class Hero(GameSprite):
    # 英雄精灵
    def __init__(self):
        # 1.调用父类方法，设置image和speed
        super().__init__("E:/python code/飞机大战项目/images/me1.png", 0)
        # 2.设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        # 3.创建子弹的精灵，和精灵组
        self.bullets = pygame.sprite.Group()

    def update(self, *args):
        # 英雄在水平方向移动
        self.rect.x += self.speed
        # 判断英雄是否在屏幕上移出去。控制英雄不能离开屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        print("发射子弹。。。")

        for i in (0, 1, 2):
            # 1.创建子弹精灵
            bullet = Bullet()
            bullet1 = Bullet()
            # 2.设置精灵的位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            bullet1.rect.bottom = self.rect.y - i * 20
            bullet1.rect.centerx = self.rect.centerx
            # 3.将精灵添加至精灵组
            self.bullets.add(bullet, bullet1)


# 子弹类
class Bullet(GameSprite):
    # 子弹精灵
    def __init__(self):
        # 调用父类方法,设置子弹图片，设置子弹出事速度
        super().__init__("E:/python code/飞机大战项目/images/bullet1.png", -2)

    def update(self):
        # 调用父类方法，让子弹沿垂直方向飞行
        super().update()

        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("子弹被销毁。。。。")
