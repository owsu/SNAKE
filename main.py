# Simple snake game ran with Pygame
import pygame

pygame.init()
screen_width, screen_height = 400, 400
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

running = True
clock = pygame.time.Clock()
FPS = 60
bg_color = (63, 112, 26)


def inputs(): # controls
  global running

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_w or event.key == pygame.K_UP:
        playerSnake.change_direction("W")

      if event.key == pygame.K_a or event.key == pygame.K_LEFT:
        playerSnake.change_direction("A")
      
      if event.key == pygame.K_s or event.key == pygame.K_DOWN:
        playerSnake.change_direction("S")

      if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
        playerSnake.change_direction("D")

class Snake():
    def __init__(self):
      self.direction = [1, 0]
      self.length = 3
      self.xpos = 10
      self.ypos = 50
      self.rect = pygame.Rect((10, 10), (20*self.length, 20))
    
    def change_direction(self, input):
       match input:
          case "W":
             self.direction = [0, -1]
          case "A":
             self.direction = [-1, 0]
          case "S":
             self.direction = [0, 1]
          case "D":
             self.direction = [1, 0]
    
    def move(self):
       self.xpos += self.direction[0]
       self.ypos += self.direction[1] 
       self.rect = pygame.Rect((self.xpos, self.ypos), (20*self.length, 20))
       pygame.draw.rect(screen, (50, 82, 168), self.rect)
    

       
playerSnake = Snake()

while running:
    clock.tick(FPS)
    screen.fill(bg_color) # green background
    inputs()
    playerSnake.move()

    pygame.display.update()
