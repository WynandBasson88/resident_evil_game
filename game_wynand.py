# Import pygame module to be able to access the built in pygame methods
# Import random module to be able to generate random numbers
import pygame
import random

# Initialise the pygame modules
pygame.init()

# Create variables for the screen width and height and give it values
screen_width = 1200
screen_height = 650

# Use pygame method pygame.display.set_mode() to create the game screen object with a specified width and height
game_screen = pygame.display.set_mode((screen_width, screen_height))
# print(type(game_screen)) # Returns <class 'pygame.Surface'> meaning game_screen is an object of class pygame.Surface


# Use pygame method pygame.image.load() to create the background object. raccoon_city is an object of class pygame.Surface
# Use pygame method pygame.image.load() to create the player, enemies and prize objects. i.e. zombie_enemy is an object of class pygame.Surface
raccoon_city = pygame.image.load("RaccoonCity.png")
leon = pygame.image.load("Leon.png")
zombie_enemy = pygame.image.load("ZombieMale.jpg")
dog_enemy = pygame.image.load("ZombieDog.png")
licker_enemy = pygame.image.load("Licker.png")
g_virus_enemy = pygame.image.load("GVirus.jpg")
cure = pygame.image.load("Cure.jpg")

# Use pygame method pygame.transform.scale() to specify the background object's width and height exactly to that of the game screen
# Use pygame method pygame.transform.scale() to specify the player, enemies and prize object's width and height
raccoon_city = pygame.transform.scale(raccoon_city, (1200, 650))
leon = pygame.transform.scale(leon, (100, 150))
zombie_enemy = pygame.transform.scale(zombie_enemy, (100, 150))
dog_enemy = pygame.transform.scale(dog_enemy, (100, 150))
licker_enemy = pygame.transform.scale(licker_enemy, (100, 150))
g_virus_enemy = pygame.transform.scale(g_virus_enemy, (100, 150))
cure = pygame.transform.scale(cure, (150, 100))

# Get the width and height of the player and enemy images and store it in variables. This is needed for boundary detection
image_width_leon = leon.get_width()
image_height_leon = leon.get_height()
image_width_zombie = zombie_enemy.get_width()
image_height_zombie = zombie_enemy.get_height()
image_width_dog = dog_enemy.get_width()
image_height_dog = dog_enemy.get_height()
image_width_licker = licker_enemy.get_width()
image_height_licker = licker_enemy.get_height()
image_width_gvirus = g_virus_enemy.get_width()
image_height_gvirus = g_virus_enemy.get_height()

#Use print() function to check these values
print("The width of the leon player image is: {} and the height of the leon player image is: {}".format(image_width_leon, image_height_leon))
print("The width of the zombie enemy image is: {} and the height of the zombie enemy image is: {}".format(image_width_zombie, image_height_zombie))
print("The width of the dog enemy image is: {} and the height of the dog enemy image is: {}".format(image_width_dog, image_height_dog))
print("The width of the licker enemy image is: {} and the height of the licker enemy image is: {}".format(image_width_licker, image_height_licker))
print("The width of the gvirus enemy image is: {} and the height of the gvirus enemy image is: {}".format(image_width_gvirus, image_height_gvirus))

# Create variables to specify the player and the enemies starting positions (The enemies should start off screen)
leon_position_x = 0
leon_position_y = 100
zombie_position_x = screen_width
zombie_position_y = random.randint(0, (screen_height - image_height_zombie))
licker_position_x = (screen_width + image_width_zombie + (random.randint(0, 600)))
licker_position_y = random.randint(0, (screen_height - image_height_licker))
gvirus_position_x = (screen_width + image_width_zombie + image_width_licker + (random.randint(0, 600)))
gvirus_position_y = random.randint(0, (screen_height - image_height_gvirus))
dog_position_x = (screen_width + image_width_zombie + image_width_licker + image_width_gvirus + (random.randint(0, 600)))
dog_position_y = random.randint(0, (screen_height - image_height_dog))

# Initialize boolean variables for the keys to be pressed. This checks if the up, down, left or right keys are pressed. 
key_up = False
key_down = False
key_right = False
key_left = False

# Game loop (While the game is running)
while 1:
    # This will clear the screen with every loop
    game_screen.fill(0) 

    # Use blit() method to draw the background image onto the game screen at the spesified destination
    game_screen.blit(raccoon_city, (0, 0))
    
    # Use blit() method to draw images of the player, enemies and prize onto the game screen at spesified destinations
    game_screen.blit(leon, (leon_position_x, leon_position_y))  
    game_screen.blit(zombie_enemy, (zombie_position_x, zombie_position_y))
    game_screen.blit(dog_enemy, (dog_position_x, dog_position_y))
    game_screen.blit(licker_enemy, (licker_position_x, licker_position_y))
    game_screen.blit(g_virus_enemy, (gvirus_position_x, gvirus_position_y))
    game_screen.blit(cure, (1050, 300))

    # Update the display with every loop
    pygame.display.flip()

    # This for loop loops through events in the game
    for event in pygame.event.get():
        
        # This checks if the user quits the game by pressing the red cross in the top right corner. If the pygame.QUIT event is true the game will be quit
        if (event.type == pygame.QUIT):
            pygame.quit()
            exit(0)

        # This checks if the user presses a key down            
        if (event.type == pygame.KEYDOWN):
            # This checks if the key pressed is either the up, down, left or right arrows
            if (event.key == pygame.K_UP):
                key_up = True
            if (event.key == pygame.K_DOWN):
                key_down = True
            if (event.key == pygame.K_RIGHT):
                key_right = True
            if (event.key == pygame.K_LEFT):
                key_left = True

        # This checks if the user releases a key down 
        if (event.type == pygame.KEYUP):
            # This checks if the key released is either the up, down, left or right arrows
            if (event.key == pygame.K_UP):
                key_up = False
            if (event.key == pygame.K_DOWN):
                key_down = False
            if (event.key == pygame.K_RIGHT):
                key_right = False
            if (event.key == pygame.K_LEFT):
                key_left = False

    # If the up key is pressed Leon will move in the upward direction (by subtracting 1 from his current position)
    if (key_up == True):
        if (leon_position_y > 0): # This ensures Leon stays on screen
            leon_position_y -= 1

    # If the down key is pressed Leon will move in the downward direction (by adding 1 to his current position)
    if (key_down == True):
        if (leon_position_y < (screen_height - image_height_leon)): # This ensures Leon stays on screen
            leon_position_y += 1

    # If the right key is pressed Leon will move in the right direction (by adding 1 to his current position)
    if (key_right == True):
        if (leon_position_x < (screen_width - image_width_leon)): # This ensures Leon stays on screen
            leon_position_x += 1

     # If the left key is pressed Leon will move in the left direction (by subtracting 1 from his current position)
    if (key_left == True):
        if (leon_position_x > 0): # This ensures Leon stays on screen
            leon_position_x -= 1


    # Create a rectangular bounding box for the player and enemy objects
    leon_box = pygame.Rect(leon.get_rect())
    # This ensures that the bounding box stays around the moving player
    leon_box.top = leon_position_y
    leon_box.left = leon_position_x

    zombie_box = pygame.Rect(zombie_enemy.get_rect())
    # This ensures that the bounding box stays around the moving enemy by updating the position of the bounding box 
    zombie_box.top = zombie_position_y
    zombie_box.left = zombie_position_x

    dog_box = pygame.Rect(dog_enemy.get_rect())
    # This ensures that the bounding box stays around the moving enemy by updating the position of the bounding box 
    dog_box.top = dog_position_y
    dog_box.left = dog_position_x

    licker_box = pygame.Rect(licker_enemy.get_rect())
    # This ensures that the bounding box stays around the moving enemy by updating the position of the bounding box 
    licker_box.top = licker_position_y
    licker_box.left = licker_position_x

    gvirus_box = pygame.Rect(g_virus_enemy.get_rect())
    # This ensures that the bounding box stays around the moving enemy by updating the position of the bounding box 
    gvirus_box.top = gvirus_position_y
    gvirus_box.left = gvirus_position_x

    cure_box = pygame.Rect(cure.get_rect())
    cure_box.top = 300
    cure_box.left = 1050

    # If the player's bounding box collides with the enemy bounding box the player loses the game. An appropriate message is displayed to the screen and the game is exited 
    if (leon_box.colliderect(zombie_box) or leon_box.colliderect(licker_box) or leon_box.colliderect(gvirus_box) or leon_box.colliderect(dog_box)):
        print("You lose the game!")
        pygame.quit()
        exit(0)

    # If the player's bounding box collides with the cure bounding box the player wins the game. An appropriate message is displayed to the screen and the game is exited 
    if (leon_box.colliderect(cure_box)):
        print("Congratulations, you beat the game!")
        pygame.quit()
        exit(0)
    
    
    # Make the enemies approach the player
    zombie_position_x -= 0.2
    licker_position_x -= 0.4
    gvirus_position_x -= 0.6
    dog_position_x -= 1
            
