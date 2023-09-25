import pygame as pg
from epylepsy.stage import Stage
def main():
    pg.init()

    screen = pg.display.set_mode((1080, 1080))
    stage = Stage(screen, 800)
    stage.draw()
    pg.display.update()
    while True:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()

if __name__ == '__main__':
    main()
