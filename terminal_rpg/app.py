import pygame


class App:
    def __init__(self, width: int, height: int) -> None:
        pygame.init()

        # Setup game window
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Terminal RPG")

        # Setup variables
        self.clock = pygame.time.Clock()
        self.running = True
        self.delta_time = 0

    def run(self) -> None:
        while self.running:
            self.process_input()
            self.update()
            self.render()
            self.dt = self.clock.tick(60) / 1000
        pygame.quit()

    def process_input(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self) -> None:
        # Update game here
        pass

    def render(self) -> None:
        # Fill the screen with black
        self.screen.fill((0, 0, 0))

        # Draw a red circle
        pygame.draw.circle(self.screen, "red", (100, 100), 50)

        # Update the display
        pygame.display.flip()
