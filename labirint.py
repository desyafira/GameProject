from pygame import*
window = display.set_mode((700, 500))
display.set_caption('Save the capybara!')
run = True
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed, player_y_speed):
        GameSprite.__init__(self, player_image,player_x, player_y,size_x, size_y)
        self.x_speed = player_x_speed
        self.y_speed = player_y_speed
    def update(self):
        if snoopy.rect.x <= 620 and snoopy.x_speed > 0 or snoopy.rect.x >= 0 and snoopy.x_speed < 0:
            self.rect.x += self.x_speed
            platforms_touched = sprite.spritecollide(self, barriers, False)
            if self.x_speed > 0:
                for p in platforms_touched:
                   self.rect.right = min(self.rect.right, p.rect.left)
            elif self.x_speed < 0:
                for p in platforms_touched:
                   self.rect.left = max(self.rect.left, p.rect.right)
        if snoopy.rect.y <= 420 and snoopy.y_speed > 0 or snoopy.rect.y >= 0 and snoopy.y_speed < 0:
            self.rect.y += self.y_speed
            platforms_touched = sprite.spritecollide(self, barriers, False)
            if self.y_speed > 0:
                for p in platforms_touched:
                    self.y_speed = 0
                    if p.rect.top < self.rect.bottom:
                        self.rect.bottom = p.rect.top
                    elif self.y_speed < 0:
                        for p in platforms_touched:
                            self.y_speed = 0
                            self.rect.top = max(self.rect.top, p.rect.bottom)
class Enemy(GameSprite):
    side = "left"
    def __init__(self, player_image, player_x, player_y, size_x,size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x,size_y)
        self.speed = player_speed
    def update(self):
        if self.rect.x <= 420:
            self.side = "right"
        if self.rect.x >= 650:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


                
barriers = sprite.Group()            
background = GameSprite('Background.jpg',0, 0, 700, 500)
snoopy =Player('snoopy.png', 100, 75, 100, 100, 0,0)
obstacle = GameSprite('brick.jpg',350, 350, 100, 50)
barriers.add(obstacle)
obstacle2 = GameSprite('brick.jpg',100, 250, 100, 50)
barriers.add(obstacle2)
friend = GameSprite('capybara.png.', 500, 350, 100, 75)
enemy = Enemy('villian.png', 250, 250, 50, 50, 5)
while run:
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                snoopy.x_speed = -5
            elif e.key == K_RIGHT:
                snoopy.x_speed = 5
            elif e.key == K_UP:
                snoopy.y_speed = -5
            elif e.key == K_DOWN:
                snoopy.y_speed = 5
        elif e.type == KEYUP:
            if e.key == K_LEFT:
                snoopy.x_speed = 0
            elif e.key == K_RIGHT:
                snoopy.x_speed = 0
            elif e.key == K_UP:
                snoopy.y_speed = 0
            elif e.key == K_DOWN:
                snoopy.y_speed = 0
    
    background.reset()
    snoopy.update()
    snoopy.reset()
    obstacle.reset()
    obstacle2.reset()
    friend.reset()
    enemy.reset()
    enemy.update()
    if sprite.collide_rect(snoopy, friend):
        finish = True
        img = image.load('win.png')
        window.fill((255, 255, 255))
        window.blit(transform.scale(img, (700, 500)), (0,0))
    if sprite.collide_rect(snoopy, enemy):
        finish = True
        img = image.load('lose.png')
        window.fill((255, 255, 255))
        window.blit(transform.scale(img, (700, 500)), (0,0))    
    for e in event.get():
        if e.type == QUIT:
            run = False
    display.update()