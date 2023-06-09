from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        w.blit(self.image, (self.rect.x, self.rect.y))
w_w = 600
w_h = 500
w = display.set_mode((w_w, w_h))
display.set_caption('Ping pong')
bg = GameSprite('bg.png', 0,0,0, w_w, w_h)
run = True
finish = False
clock = time.Clock()
fps = 60
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        bg.reset()
    display.update()
    clock.tick(fps)