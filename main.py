import pygame
pygame.init()
pygame.font.init()

font = pygame.font.SysFont('ubuntu',16)
screen = pygame.display.set_mode((400, 700))

bottom = 0
scrolldown = False
scrollup = False
done = False
hide = False

def isPrime(n):
    if n <= 3:
        return n > 1
    elif n%2==0 or n%3==0:
        return False
    i = 5
    while i*i <= n:
        if n%i == 0 or n%(i+2) == 0:
            return False
        i += 6
    return True

while not done:

    screen.fill((0,0,0))

    for number in range(bottom,bottom+234):
        displayed_number = number + 2
        if isPrime(displayed_number):
            color = (0,0,255)
        else:
            if hide: continue
            color = (255,255,255)
        textsurface = font.render(str(displayed_number),False,color)
        screen.blit(textsurface,((number%6)*64+5, (number//6)*18+2-bottom*3))


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE:
                done = True
            if event.key == pygame.K_0:
                hide = not hide
            if event.key == pygame.K_DOWN:
                scrolldown = True
                #bottom += 6
            if event.key == pygame.K_UP:
                scrollup = True
                #bottom -= 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                scrolldown = False
            if event.key == pygame.K_UP:
                scrollup = False

    if scrolldown:
        bottom += 66
    if scrollup:
        bottom -= 66

    pygame.display.flip()