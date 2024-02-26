from pygame import *
'''Игровая сцена'''

scr_W = 1280
scr_H = 720

fps = 45

screen = display.set_mode((scr_W, scr_H)) #Настраиваем размер окна
display.set_caption('Shadows of the past') # называем нашу игру!
display.set_icon(image.load('Placeholders/PH_Icon.png'))

background = transform.scale(image.load('Placeholders/PH_background.png'), (scr_W, scr_H)) #добавление фона и настраиваем его
clock = time.Clock()

#hero = transform.scale(image.load("Placeholders/PH_Anims/PH_RightAnim/PHR_1.png"),(90, 90)) # я с этим говном мучалась долго ибо ему всё не то
# Крч, тут мы даем герою спарйт(1)
'''Анимация персонажей'''

walk_left = [
    image.load('Placeholders/PH_Anims/PH_LeftAnim/PHL_1.png'),
    image.load('Placeholders/PH_Anims/PH_LeftAnim/PHL_2.png'),
    image.load('Placeholders/PH_Anims/PH_LeftAnim/PHL_3.png'),
    image.load('Placeholders/PH_Anims/PH_LeftAnim/PHL_4.png')
]

walk_right = [
    image.load('Placeholders/PH_Anims/PH_RightAnim/PHR_1.png'),
    image.load('Placeholders/PH_Anims/PH_RightAnim/PHR_2.png'),
    image.load('Placeholders/PH_Anims/PH_RightAnim/PHR_3.png'),
    image.load('Placeholders/PH_Anims/PH_RightAnim/PHR_4.png')
    
]


'''Шаблон пресонажей!'''

class MainHero(sprite.Sprite):
    def __init__(self, player_img, x, y, w, h, speed):
        sprite.Sprite.__init__(self) #говорим что наследуем sprite.Sprite
        self.image = transform.scale(image.load(player_img), (w,h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.left = False
        self.right = False
        self.count = 0 #количество проиграных анимаций, изначально оно будет приравниватся 0

class Player(MainHero):

    def update(self):
        keys = key.get_pressed()

        if keys[K_d] and self.rect.x > 5:
            self.rect.x -= self.speed
            self.left = True
            self.right = False
        elif keys[K_a] and self.rect.x < scr_W - 5:
            self.rect.x += self.speed
            self.left = False
            self.right = True
        else:
            self.left = False
            self.right = False
            self.count = 0
        
    def animation(self):
        if self.count + 1 >= 45:
            self.count = 0
        if self.left == True:
            screen.blit(walk_left[self.count // 5], (self.rect.x, self.rect.y))
            self.count += 1
        elif self.right == True:
            screen.blit(walk_right[self.count // 5], (self.rect.x, self.rect.y))
            self.count += 1
        else:
            screen.blit(self.image, (self.rect.x, self.rect.y))
            self.count = 0








'''Персонажи'''

hero = Player('Placeholders/PH_Anims/PH_RightAnim/PHR_1.png', 100, 300, 90, 90, 8)






'''Игровой цикл'''
game = True

x = 100
y = 300
speed = 10

while game: # Цикл игры

    
    screen.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False

        hero.update()
        hero.animation()

    display.update()
    clock.tick(fps)