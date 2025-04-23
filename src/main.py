import pygame
from gui import GUIManager

def main():
    pygame.init()
    screen = pygame.display.set_mode((220, 300))
    clock  = pygame.time.Clock()

    # instantiate GUI manager, passing it the main window
    gui = GUIManager(screen)

    running = True
    while running:
        # 1) collect events
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                running = False

        # 2) hand off events to GUI
        gui.process_events(events)

        # 3) update GUI state
        dt: float = clock.tick(60) / 1000.0  # seconds since last frame
        gui.update(dt)

        # 4) draw everything
        screen.fill((30, 30, 30))       
        

        gui.draw()                     
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
