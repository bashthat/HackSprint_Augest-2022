import pygame
import spritesheet


class SpritesSheet(sprite_sheet):
    def __init__(self, filename):
        super().__init__(filename)

    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height])
        image.blit(self.sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(self.sheet.get_at((0, 0)))
        return image


if __name__ == "__main__":

    pygame.init()

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("PacMan")
    sprite_sheet_image = pygame.image.load(
        "custom_spritesheet.png").convert_alpha()
    sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

    BG = (50, 50, 50)
    BLACK = (0, 0, 0)

    frame_0 = sprite_sheet.get_image(0, 0, 32, 32)
    frame_1 = sprite_sheet.get_image(32, 0, 32, 32)
    frame_2 = sprite_sheet.get_image(64, 0, 32, 32)
    frame_3 = sprite_sheet.get_image(96, 0, 32, 32)
    frame_4 = sprite_sheet.get_image(128, 0, 32, 32)

    run = True
    while run:

        screen.fill(BG)

        screen.blit(frame_0, (0, 0))
        screen.blit(frame_1, (32, 0))
        screen.blit(frame_2, (64, 0))
        screen.blit(frame_3, (96, 0))
        screen.blit(frame_4, (128, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()
