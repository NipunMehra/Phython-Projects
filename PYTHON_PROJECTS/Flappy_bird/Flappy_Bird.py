import pygame
import neat
import time
import os
import random
pygame.font.init()

WIN_WIDTH = 500
WIN_HEIGHT = 800

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png")))]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))

STAT_FONT = pygame.font.SysFont("comicsans", 50)

WHITE = (255, 255, 255)

class Bird:
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25 # how much the bird will tilt upwards and downwards while moving up or down
    ROTATION_VEL = 20 # how much we are gonna rotate for every frame
    ANIMATION_TIME = 5 # how long we are going to each bird animation

    def __init__(self, x, y):
        self.x = x # x-position
        self.y = y # y-position
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):
        self.vel = -10.5 # upward in y-direction
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1

        displacement = self.vel * self.tick_count + 1.5*self.tick_count ** 2 # s = u * t + (1/2) (a) * (t^2) ----> assuming a random accleration in this case 3.
         
        if displacement >= 16:
             displacement = 16 # so our bird don't move down too fast, i.e. we don't acclerate anymore

        if displacement < 0:
            displacement -= 2 # when we are moving upward, it moves a little more, this makes our movement smoother

        self.y = self.y + displacement

        if displacement < 0 or self.y < self.height + 50: # if we are moving upward for our initial y-position
            if self.tilt < self.MAX_ROTATION:
             self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROTATION_VEL

    
    def draw(self, win):
        self.img_count += 1

        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME * 2:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME * 3:
            self.img = self.IMGS[2]
        elif self.img_count < self.ANIMATION_TIME * 4:
            self.img = self.IMGS[1]
        elif self.img_count == self.ANIMATION_TIME * 4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0


        if self.tilt <= -80:
            self.IMGS = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME*2

        # rotating the image around it's center in pygame:
        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        # placling the rotation from top left of the window top the center:
        new_rect = rotated_image.get_rect(center = self.img.get_rect(topleft = (self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft) # blit ----> means draw

    
    def get_mask(self): # colisions for our objects
        return pygame.mask.from_surface(self.img)


class Pipe:
    GAP  = 200
    VEL = 5

    def __init__(self, x):
        self.x = x
        self.height = 0
        self.gap = 0
        self.top = 0
        self.bottom = 0
        self.PIPE_TOP = pygame.transform.flip(PIPE_IMG, False, True) # flip the pipe image upside down to use it 
        self.PIPE_BOTTOM = PIPE_IMG

        self.past = False # if the bird id already past the pipe
        self.set_height()

    def set_height(self):
        self.height = random.randrange(50,450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP

    def move(self):
        self.x -= self.VEL

    def draw(self, win):
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    '''
    MASK-----> Collission
      --> we use MASK to set up our collision
      --> A MASK in pygame it looks at image and figure out where pixels in the png actually are. (because the png has a transparent background)
          Then it crests a 2-D List, which consists of as many rows as there are pixels gong down and as many columns as there are pixels going up.
          after that it checks if the two pixels are overlapping or not to determine the collission.

      '''

    def collide(self, bird):

        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)

        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        b_pont = bird_mask.overlap(bottom_mask, bottom_offset)
        t_pont = bird_mask.overlap(top_mask, top_offset)

        if b_pont or t_pont: # means if they are not none
            return True

        return False


class Base:
    VEL = 5
    WIDTH = BASE_IMG.get_width()
    IMG = BASE_IMG

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH

    def move(self):
        self.x1 -= self.VEL
        self.x2 -= self.VEL

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win):
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))



def draw_window(win, bird, pipes, base, score):
    win.blit(BG_IMG,(0,0))

    for pipe in pipes:
        pipe.draw(win)

    base.draw(win)
    bird.draw(win)

    text = STAT_FONT.render("Score: " + str(score), 1, WHITE)
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))

    pygame.display.update()


def main():
    bird = Bird(230,350)
    base = Base(730)
    pipes = [Pipe(700)]
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    score = 0

    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #bird.move()

        add_pipe = False
        remove_pipe = []
        for pipe in pipes:
            if pipe.collide(bird):
                pass

            if pipe.x + pipe.PIPE_TOP.get_width() < 0: # if pipe is off the screen
                remove_pipe.append(pipe)

            if not pipe.past and pipe.x < bird.x:
                pipe.past =  True
                add_pipe = True

            pipe.move()

        if add_pipe:
            score =+ 1
            pipes.append(Pipe(630))

        for rem in remove_pipe:
            pipes.remove(rem)

        if bird.y + bird.img.get_height() >= 730:
            pass


        base.move()
        draw_window(win, bird, pipes, base, score)

    pygame.quit()
    quit()

main()


        