"""Basic Animation
    Learning Pygame
    Use Andy's code as a base"""

def main():
    #I - Import and initialize
    import pygame
    pygame.init()
    
    #D - Display configuration
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Hello, world!")
    
    #E - Entities (just background for now)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 255))
    
    #A - Action (broken into ALTER steps)
        
        #A - Assign values to kay varibles
    clock = pygame.time.Clock()
    keepGoing = True
    
        #L - Set up main loop
    while keeepGoing:
        
        #T - Timer to set frame rate
        clock.tick(30)
        
        #E - Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        #R - Refresh display
        screen.blit(background, (0, 0))
        pygame.display.flip()
        
    pygame.quit()
    
if __name__ == "__main__":
    main()