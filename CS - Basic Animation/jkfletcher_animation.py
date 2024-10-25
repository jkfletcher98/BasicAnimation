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
    
    #E - Entities
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((112, 105, 120))
    
    skull = pygame.image.load("skull_copy.gif")
    skull = skull.convert()
    skull = pygame.transform.scale(skull, (100, 100))
    skull_x = 260
    skull_y = 200
    
    #A - Action (broken into ALTER steps)
        
        #A - Assign values to kay varibles
    clock = pygame.time.Clock()
    keepGoing = True
    
        #L - Set up main loop
    while keepGoing:
        
        #T - Timer to set frame rate
        clock.tick(30)
        
        #E - Event handling
        skull_y += 5
        if skull_y > screen.get_height():
            skull_y = 0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        #R - Refresh display
        screen.blit(background, (0, 0))
        screen.blit(skull, (skull_x, skull_y))
        pygame.display.flip()
        
    pygame.quit()
    
if __name__ == "__main__":
    main()