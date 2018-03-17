import pygame
import time
import random

pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()

white = (255,255,255)
green = (0,255,0)
sakegreen = (0,155,0)
red = (255,0,0)
black= (0,0,0)
brown = (139,69,19)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Snake AI')

icon = pygame.image.load("snake-icon.png")
pygame.display.set_icon(icon)

img = pygame.image.load("snake.png")
appleimg = pygame.image.load("apple.png")
brickimg = pygame.image.load("brick.png")
brickimg1 = pygame.image.load("brick-1.jpg")
brickimg2 = pygame.image.load("brick-2.jpg")
brickimg3 = pygame.image.load("brick-3.jpg")
mongooseimg = pygame.image.load("mongoose.png")

clock = pygame.time.Clock()

BrickThickness = 30
MongooseThickness = 30
AppleThickness = 30
block_size = 20
FPS = 10

smallfont = pygame.font.SysFont("Purisa",15)
medfont = pygame.font.SysFont("Purisa",30)
largefont = pygame.font.SysFont("TakaoPGothic",40)

direction = "right"

def pause():

    pygame.mixer.music.pause()

    paused = True

    message_to_screen("Paused", black, -100, size="large")
    message_to_screen("Press C to continue or Q to quit", red, 50, size="small")
    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                    pygame.mixer.music.unpause()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        #gameDisplay.fill(white)

        clock.tick(5)

def score(score):
    text = smallfont.render("Score: "+str(score),True, black)
    gameDisplay.blit(text,[30,30])


def game_intro():

    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()


        gameDisplay.fill(white)
        message_to_screen("Welcome to Athul's Snake Game",green,-100,size="large")
        message_to_screen("Instructions: ",black,0,size="medium")
        message_to_screen("1) Objective is to eat the apple and grow the snake in length and achieve a max score",black,30)
        message_to_screen("2) Avoid the bricks and the Mongoose ",black,50)
        message_to_screen("2) Use arrow keys to move the snake",black,70)
        message_to_screen("3) Press Esc or P to pause the game",black,90)
        message_to_screen("This game is dedicated to Mottu",black,170)
        message_to_screen("Press C to play or Q to quit", red,250)
        message_to_screen("Developed by Athul",black,280)
        pygame.display.update()
        clock.tick(15)


def snake(block_size,snakeList):

    if direction == "right":
        head = pygame.transform.rotate(img,270)

    if direction == "left":
        head = pygame.transform.rotate(img,90)

    if direction == "up":
        head = img

    if direction == "down":
        head = pygame.transform.rotate(img,180)

    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))

    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay, sakegreen, [XnY[0],XnY[1], block_size, block_size])

def text_objects(text, color,size):
    if size == "small":
        textSurface = smallfont.render(text,True,color)
    elif size == "medium":
        textSurface = medfont.render(text,True,color)
    elif size == "large":
        textSurface = largefont.render(text,True,color)
    return textSurface, textSurface.get_rect()


def message_to_screen(msg,color,y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg,color,size)
    # screen_text = font.render(msg, True, color)
    # #gameDisplay.blit(screen_text, [display_width/2, display_height/2])
    # gameDisplay.blit(screen_text, [display_width / 2 - screen_text.get_width() / 2,
    #                                display_height / 2 - screen_text.get_height() / 2])
    textRect.center = (display_width/2),(display_height/2)+y_displace
    gameDisplay.blit(textSurf,textRect)

def gameLoop():

    pygame.mixer.music.load("flute.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    global direction
    direction = "right"

    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX = round(random.randrange(0,display_width-AppleThickness))#/10.0)*10.0
    randAppleY = round(random.randrange(0,display_height-AppleThickness))#/10.0)*10.0

    randMongX = round(random.randrange(0,display_width-AppleThickness-MongooseThickness))#/10.0)*10.0
    randMongY = round(random.randrange(0,display_height-AppleThickness-MongooseThickness))#/10.0)*10.0

    gameExit = False
    gameOver = False

    while not gameExit:

        if gameOver == True:
            #gameDisplay.fill(white)
            message_to_screen("Game Over",red, -150,size="large")
            message_to_screen("Press C to play again or Q to quit!",black,150,size="medium")
            text2 = medfont.render("Your Score: " + str(snakeLength-1), True, green)
            gameDisplay.blit(text2, [300, 300])
            pygame.display.update()


        while gameOver == True:

            pygame.mixer.music.pause()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                    pygame.mixer.music.stop()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit=True
                        gameOver=False
                        pygame.mixer.music.stop()
                    if event.key == pygame.K_c:
                        gameLoop()
                        pygame.mixer.music.unpause()




        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_ESCAPE:
                    pause()

        if lead_x >= display_width or lead_x <=0 or lead_y >= display_height or lead_y <=0:
                gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)

        gameDisplay.blit(brickimg1, [0,0])
        #pygame.display.update()

        gameDisplay.blit(brickimg2, [0,0])
        #pygame.display.update()

        gameDisplay.blit(brickimg3, [0,590])
        #pygame.display.flip()

        gameDisplay.blit(brickimg2,[790,0])
        pygame.display.flip()

        #pygame.draw.rect(gameDisplay, brown, [randAppleX,randAppleY,AppleThickness,AppleThickness])
        gameDisplay.blit(appleimg,(randAppleX,randAppleY))
        pygame.display.update()

        gameDisplay.blit(mongooseimg,(randMongX,randMongY))
        pygame.display.flip()


        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        #print(snakeHead)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        # for eachSegment in snakeList[:-1]:
        #     if eachSegment == snakeHead:
        #         gameOver = True

        snake(block_size,snakeList)

        score(snakeLength-1)

        pygame.display.update()

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        # if lead_x == randAppleX and lead_y == randAppleY:
        #     randAppleX = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
        #     randAppleY = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0
        #     snakeLength += 1

        # if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness - block_size:
        #     if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness - block_size:
        #       randAppleX = round(random.randrange(0, display_width - block_size))# / 10.0) * 10.0
        #       randAppleY = round(random.randrange(0, display_height - block_size))# / 10.0) * 10.0
        #       snakeLength += 1
        if lead_x >  randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
             if lead_y > randAppleY and lead_y < randAppleY + AppleThickness or lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                randAppleX = round(random.randrange(0, display_width - AppleThickness))# / 10.0) * 10.0
                randAppleY = round(random.randrange(0, display_height - AppleThickness))# / 10.0) * 10.0
                snakeLength += 1
                randMongX = round(random.randrange(0, display_width - randAppleX - MongooseThickness))# / 10.0) * 10.0
                randMongY = round(random.randrange(0, display_height - randAppleY - MongooseThickness))# / 10.0) * 10.0


        if lead_x >  randMongX and lead_x < randMongX + MongooseThickness or lead_x + block_size > randMongX and lead_x + block_size < randMongX + MongooseThickness:
             if lead_y > randMongY and lead_y < randMongY + MongooseThickness or lead_y + block_size > randMongY and lead_y + block_size < randMongY + MongooseThickness:
                randMongX = round(random.randrange(0, display_width - randAppleX - MongooseThickness))# / 10.0) * 10.0
                randMongY = round(random.randrange(0, display_height - randAppleY - MongooseThickness))# / 10.0) * 10.0
                gameOver = True

        clock.tick(FPS)

    #message_to_screen("Loser", red)
    #pygame.display.update()
    #time.sleep(2)
    pygame.quit()
    quit()
    pygame.mixer.music.stop()
game_intro()
gameLoop()