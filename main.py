from constants import *
import pygame
import light
import clock

pygame.init()

game_clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()


clock = clock.Clock()


def main():
    global states
    running = True


    while running:
        game_clock.tick(TICK_RATE)
        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    pygame.quit()





        draw()
        update()

    pygame.quit()




def draw():
    surface.fill((0, 0, 0))

    clock.draw(surface)


    pygame.display.flip()


def update():
    clock.update()



if __name__ == "__main__":
    main()
