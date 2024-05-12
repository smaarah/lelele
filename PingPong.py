from pygame import *

WIN_WIDTH = 800
WIN_HEIGHT = 500
FPS = 60
lost = 0
score = 0 
max_lost = 2
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

window = display.set_mode((WIN_WIDTH, WIN_HEIGHT))
display.set_caption('PingPong.py')

clock = time.Clock()

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[ K_w ] and self.rect.y > 5:
            self.rect.y -= self.speed


        if keys[ K_s ] and self.rect.y < WIN_WIDTH - 80:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[ K_UP ] and self.rect.y > 5:
            self.rect.y -= self.speed


        if keys[ K_DOWN ] and self.rect.y < WIN_WIDTH - 80:
            self.rect.y += self.speed
        

class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, speed_x, speed_y):
        super().__init__(player_image, player_x, player_y, size_x, size_y, speed_x)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update (self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
    
        if self.rect.y <= 0:
            self.speed_y >= -3*-1 
            self.speed_x >= 


    def collide_rect(self, player):
        if self.rect.colliderect(player):
            self.speed_x *= -1

player_left = Player('racket.png', 5, WIN_HEIGHT - 300, 50, 150, 10)
player_right = Player('racket.png', WIN_WIDTH - 55, WIN_HEIGHT - 300, 50, 150, 10)
background = transform.scale(image.load("tennis.png"), (800, 700))
ball = Ball('tenis_ball.png', 50, WIN_HEIGHT - 450, 50, 50, 6, 6)

window.blit(background, (0, 0))
game = True
finish = False

font.init()
font_win = font.SysFont('Arial', 70)
win_r = font_win.render("Выиграл правый игрок", True, (255, 255, 255))
win_l = font_win.render("Выиграл левый игрок", True, (255, 255, 255))
winner = None
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0, 0))

    player_left.update_l()
    player_left.reset()

    player_right.update_r()
    player_right.reset()
    
    ball.update()
    ball.reset()

    ball.collide_rect(player_left)
    ball.collide_rect(player_right)

    if ball.rect.x < 50:
        winnner = win_r
    if ball.rect.x > WIN_WIDTH - 50:
        winner = win_l
    elif finish:
        window.blit(winner, (50, 200))
    display.update()
    clock.tick(FPS)