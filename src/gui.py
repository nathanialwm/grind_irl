import pygame
import pygame_gui

class GUIManager:
    def __init__(self, window_surface: pygame.Surface):
        # store reference to your main window
        self.window_surface = window_surface
        # create a UIManager for all your widgets
        self.ui_manager = pygame_gui.UIManager(window_surface.get_size())
        

    def process_events(self, events):
        for event in events:
            self.ui_manager.process_events(event)

    def update(self, dt):
        # advance animations, handle timers, etc.
        self.ui_manager.update(dt)

    def draw(self):
        # let pygame_gui draw onto your main surface
        self.ui_manager.draw_ui(self.window_surface)
