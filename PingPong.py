from pygame import *

WIN_WIDTH = 800
WIN_HEIGHT = 700
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
        if keys[ K_w ] and self.rect.x > 5:
            self.rect.x -= self.speed


        if keys[ K_s ] and self.rect.x < WIN_WIDTH - 80:
            self.rect.x += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[ K_UP ] and self.rect.y > 5:
            self.rect.y -= self.speed


        if keys[ K_DOWN ] and self.rect.y < WIN_WIDTH - 80:
            self.rect.y += self.speed
        

class Ball(GameSprite):
    def update (self):
        self.rect.y += self.speed

player_left = Player('racket.png', 5, WIN_HEIGHT - 100, 50, 150, 10)
player_right = Player('racket.png', 5, WIN_HEIGHT - 100, 50, 150, 10)
# background = transform.scale(image.load("pingpongpng.avif"), (800, 700))
ball = Ball('tenis_ball.png', 3, WIN_HEIGHT - 50, 50, 50, 50)

window.blit(background, (0, 0))
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

        background.update()
        background.draw(window)

        player_left.update()
        player_left.draw(window)

        player_right.update()
        player_right.draw(window)
        
        ball.update()
        ball.draw(window)
