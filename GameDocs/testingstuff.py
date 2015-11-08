import pygame
pygame.init()

class button_example():
    def __init__(self):
        self.main()

    def display(self): #creating a display
        self.screen = pygame.display.set.mode((500,500), 0, 32)
        pygame.display.set_caption("this is the title page")

    def update_display(self):
        self.screen.fill(0,255,255)
        self.Button1.create_button(self.screen, (0, 0, 0), 150, 200, 200, 100, 0, "New Game", (255,255,255))
        self.Button2.create_button(self.screen, (250,250,250), 125, 50, 150, 75, 0, "Continue Game", (0,0,0))
        pygame.display.flip()

    def main(self):
        self.Button1 = Buttons.Button()
        self.Button2 = Buttons.Button()
        self.display
        while True:
            self.update_display()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.quit()
                elif event.type == MOUSEBUTTONDOWN:
                    if self.Button1.pressed(pygame.mouse.get_pos()):
                        print "New Game Has Begun!"
                    if self.Button2.pressed(pygame.mouse.get_pos()):
                        print "Now Contunuing Game!"

button = button_example()


