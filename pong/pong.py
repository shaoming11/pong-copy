import pygame
import random
import os

pygame.init()

size = screenwidth, screenheight = 500, 500
fps = 60
window = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
directory_path = os.path.dirname(__file__)
retropath = os.path.join(directory_path, r".\retrofont.ttf")
logopath = os.path.join(directory_path, r".\pingpongball.png")
keys = pygame.key.get_pressed()
white = (255, 255, 255)
black = (0, 0, 0)

VEL = 2.5

def preload():
    logo = pygame.image.load(logopath)
    pygame.display.set_caption("Shao's Game (pong)")
    pygame.display.set_icon(logo)

def draw(ball, pad1, pad2, ballspeedX, ballspeedY):
    pygame.draw.rect(window, white, ball)
    pygame.draw.rect(window, white, pad1)
    pygame.draw.rect(window, white, pad2)

def handle_keys(keys, paddle1, paddle2, paddlespeed):
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.top -= paddlespeed
    if keys[pygame.K_s] and paddle1.top < screenheight-paddle1.height:
        paddle1.top += paddlespeed
    if keys[pygame.K_UP] and paddle2.top > 0:
        paddle2.top -= paddlespeed
    if keys[pygame.K_DOWN] and paddle2.top < screenheight-paddle2.height:
        paddle2.top += paddlespeed

def startState():
    start = pygame.font.Font(retropath, 40)
    size25 = pygame.font.Font(retropath, 28)
    startText = start.render("Welcome to Pong!", False, white)
    pressSpace = size25.render("Press [SPACE] to begin.", False, white)
    window.blit(startText, (30, screenheight/2-50))
    window.blit(pressSpace, (30, (screenheight/2)))
    pygame.display.update()

def endState():
    retro = pygame.font.Font(retropath, 40)
    size25retro = pygame.font.Font(retropath, 25)
    endText = retro.render("GAME OVER", False, white)
    playAgain = size25retro.render("Press [ENTER] to play again!", False, white)
    window.blit(endText, (100, 100))
    window.blit(playAgain, (25, 300))
    pygame.display.update()

def main():
    running = True
    clock = pygame.time.Clock()

    ball = pygame.Rect(screenwidth/2, screenheight/2, 4, 4)
    paddle1 = pygame.Rect(10, screenheight/2, 4, 40)
    paddle2 = pygame.Rect(screenwidth-14, screenheight/2, 4, 40)

    ballspeedX = 0
    ballspeedY = 0

    paddlespeed = 5

    starting_sideX = random.randint(0, 1)
    starting_sideY = random.randint(0, 1)

    p1score = 0
    p2score = 0

    state = "Start"

    if starting_sideX == 0:
        ballspeedX = 3
    if starting_sideX == 1:
        ballspeedX = -3
    if starting_sideY == 0:
        ballspeedY = 2
    if starting_sideY == 1:
        ballspeedY = -2

    preload()
    print(ball.x)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and state == "Start":
                    state = "Main"
                if event.key == pygame.K_RETURN and state == "End":
                    ball.x = screenwidth/2
                    ball.y = screenheight/2
                    state = "Main"

        keys = pygame.key.get_pressed()
        clock.tick(fps)
        window.fill(black)

        scorefont = pygame.font.Font(retropath, 50)
        p1text = scorefont.render("P1: " + str(p1score), False, white)
        p2text = scorefont.render("P2: " + str(p2score), False, white)
        window.blit(p1text, (25, 25))
        window.blit(p2text, (screenwidth-175, 25))

        if state == "Start":
            startState()

        if state == "Main":

            draw(ball, paddle1, paddle2, ballspeedX, ballspeedY)
            handle_keys(keys, paddle1, paddle2, paddlespeed)

            ball.x += ballspeedX
            ball.y += ballspeedY

            if ball.left >= screenwidth or pygame.Rect.colliderect(ball, paddle2):
                ballspeedX = -3
            if ball.left <= 0 or pygame.Rect.colliderect(ball, paddle1):
                ballspeedX = 3
            if ball.top >= screenheight:
                ballspeedY = -2
            if ball.top <= 0:
                ballspeedY = 2

            if ball.x == 4:
                p2score += 1
                state = "End"
            if ball.x == screenwidth-4:
                p1score += 1
                state = "End"
        
        if state == "End":
            paddle1.y = screenheight/2
            paddle2.y = screenheight/2

            a = random.randint(0, 1)
            b = random.randint(0, 1)
            if a == 0:
                ballspeedX = 3
            if a == 1:
                ballspeedX = -3
            if b == 0:
                ballspeedY = 2
            if b == 1:
                ballspeedY = -2

            endState()

        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()

#States: Start, Main, End
# MAKE PADDLE X AND PADDLE Y RESET WHEN THE GAME RESETS