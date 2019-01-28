import pygame #needed to import the pygame framework
import random #needed to generate random numbers

#initializes all the modules required for PyGame
pygame.init()
pygame.font.init()

#launch a window of the desired size, screen equals a Surface which is an object
#we can perform graphical operations on. Think of a Surface as a blank piece of paper
screen = pygame.display.set_mode((800, 600))

#variable to control the game loop, keeps our code running until we flip it to True
done = False
gameStatus = "playing"
finalScore = 0

#player variables
x = 400
y = 300
size = 15
speed = 7
color = (255,255,255)

# list of enemies that move down, right, up
downEnemies = []
rightEnemies = []
upEnemies = []
leftEnemies = []

#timer for the game
timer = pygame.time.get_ticks()
lastRestartTime = 0
myFont = pygame.font.SysFont('Comic Sans MS', 30)
clock = pygame.time.Clock()

def handlePlayerInput():
    global x #because I want to CHANGE x
    global y #because I want to CHANGE y
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_d]:
        x += speed
        if x > 785:
            x = 785
    if pressed[pygame.K_a]:
        x -= speed
        if x < 0:
            x = 0
    if pressed[pygame.K_w]:
        y -= speed
        if y < 0:
            y = 0
    if pressed[pygame.K_s]:
        y += speed
        if y > 585:
            y = 585

def draw():
    #clear screen
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(0,0,800,600),0)

    #draw the player
    pygame.draw.rect(screen, color, pygame.Rect(x,y,size,size), 0)

    #draw the enemies
    drawEnemies()

    #draw the time
    textSurface = myFont.render("Time " + str((pygame.time.get_ticks()-lastRestartTime)/1000), False, (255,255,255))
    screen.blit(textSurface, (367, 10))

def initEnemies():
    global downEnemies
    global rightEnemies

    downEnemies.append(pygame.Rect(200, -50, 20, 20))
    downEnemies.append(pygame.Rect(400, -50, 20, 20))
    downEnemies.append(pygame.Rect(300, -50, 20, 20))
    downEnemies.append(pygame.Rect(600, -50, 20, 20))
    downEnemies.append(pygame.Rect(100, -50, 20, 20))

    rightEnemies.append(pygame.Rect(-50, 300, 20, 20))
    rightEnemies.append(pygame.Rect(-50, 100, 20, 20))
    rightEnemies.append(pygame.Rect(-50, 500, 20, 20))
    rightEnemies.append(pygame.Rect(-50, 200, 20, 20))

    upEnemies.append(pygame.Rect(100, 700, 20, 20))
    upEnemies.append(pygame.Rect(300, 700, 20, 20))

    leftEnemies.append(pygame.Rect(850, 100, 20, 20))
    leftEnemies.append(pygame.Rect(850, 400, 20, 20))

def drawEnemies():
    #for every enemy in the list downEnemies
    for enemy in downEnemies:
        pygame.draw.rect(screen, (255,0,0), enemy)

    # for every enemy in the list rightEnemies
    for enemy in rightEnemies:
        pygame.draw.rect(screen, (0, 255, 0), enemy)

    # for every enemy in the list upEnemies
    for enemy in upEnemies:
        pygame.draw.rect(screen, (0, 255, 255), enemy)

    # for every enemy in the list leftEnemies
    for enemy in leftEnemies:
        pygame.draw.rect(screen, (255, 0, 255), enemy)

def clearEnemies():
    global upEnemies
    global downEnemies
    global rightEnemies
    global leftEnemies
    upEnemies = []
    downEnemies = []
    rightEnemies = []
    leftEnemies = []

def resetGame():
    global lastRestartTime
    clearEnemies()
    initEnemies()
    #time stamp the restart
    lastRestartTime = pygame.time.get_ticks()


def checkCollisions():
    global upEnemies
    global downEnemies
    global rightEnemies
    global leftEnemies
    global gameStatus
    global finalScore
    for enemy in downEnemies:
        if enemy.colliderect(pygame.Rect(x,y,size,size)):
            gameStatus = "gameover"
            finalScore = pygame.time.get_ticks() - lastRestartTime
    for enemy in upEnemies:
        if enemy.colliderect(pygame.Rect(x,y,size,size)):
            gameStatus = "gameover"
            finalScore = pygame.time.get_ticks() - lastRestartTime
    for enemy in leftEnemies:
        if enemy.colliderect(pygame.Rect(x,y,size,size)):
            gameStatus = "gameover"
            finalScore = pygame.time.get_ticks() - lastRestartTime
    for enemy in rightEnemies:
        if enemy.colliderect(pygame.Rect(x,y,size,size)):
            gameStatus = "gameover"
            finalScore = pygame.time.get_ticks() - lastRestartTime

def drawGameOver():
    # clear screen
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 800, 600), 0)

    # draw the game over
    textSurface = myFont.render("Game Over", False, (255, 255, 255))
    screen.blit(textSurface, (367, 10))

    # draw the final score
    textSurface = myFont.render("Final Score: " + str(finalScore), False, (255, 255, 255))
    screen.blit(textSurface, (367, 200))

    # draw continue code
    textSurface = myFont.render("Press Spacebar to play again", False, (255, 255, 255))
    screen.blit(textSurface, (367, 400))


def moveEnemies():
    for enemy in downEnemies:
        enemy.y += 2
        #if the enemy goes off the screen
        if enemy.y > 600:
            enemy.y = -50 #reset it up top
            enemy.x = random.randint(0,780) #random x value

    for enemy in rightEnemies:
        enemy.x += 2
        #if the enemy goes off the screen
        if enemy.x > 800:
            enemy.x = -50 #reset it up top
            enemy.y = random.randint(0,580) #random x value

    for enemy in upEnemies:
        enemy.y -= 2
        #if the enemy goes off the screen
        if enemy.y < -20:
            enemy.x = random.randint(0,780) #reset it up top
            enemy.y = 650 #random x value

    for enemy in leftEnemies:
        enemy.x -= 2
        #if the enemy goes off the screen
        if enemy.x < -20:
            enemy.x = 850
            enemy.y = random.randint(0,550) #random y value

# code to set everything up BEFORE the game starts
initEnemies()

#continually run the game loop until done is switch to True
while not done:

    # set the game to 60 FPS
    clock.tick(60)

    #loop through and empty the event queue, key presses, button clicks, etc.
    for event in pygame.event.get():

        #if the event is a click on the "X" close button
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if gameStatus == "gameover":
                    resetGame()
                    gameStatus = "playing"


    if gameStatus == "playing":
        handlePlayerInput()
        moveEnemies()
        checkCollisions()
        draw()
    elif gameStatus == "gameover":
        drawGameOver()

    #Show any graphical updates you have made to the screen
    pygame.display.flip()