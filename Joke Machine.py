#Made by Nick Vasilikiotis

import pygame, sys, random
from pygame.locals import *

def getRandomJoke():
    print('getRandomJoke Start')
    # This function returns a random joke and its answer
    i = random.randint(0, len(jokes) - 1)

    #clear previous text
    pygame.draw.rect(windowSurface, WHITE, (0, 250, 1000, 300))
    
    #Display the joke
    joketext = basicFont.render(jokes[i], True, BLACK, GREY)
    joketextRect = joketext.get_rect()
    joketextRect.centerx = windowSurface.get_rect().centerx
    joketextRect.centery = windowSurface.get_rect().centery
    
    #Draw the text onto the surface.
    windowSurface.blit(joketext, joketextRect)

    #Display the answer
    answertext = basicFont.render(jokeanwers[i], True, BLACK, GREEN)
    answertextRect = answertext.get_rect()
    answertextRect.centerx = windowSurface.get_rect().centerx
    answertextRect.centery = windowSurface.get_rect().centery + 50
    
    #Draw the text onto the surface.
    windowSurface.blit(answertext, answertextRect)

    #Draw the window onto the screen.
    pygame.display.update()
    
    pygame.time.delay(500)
    
    #Display the prompt
    prompttext = basicFont.render('Would you like to hear another joke? (Press Y or N)', True, BLACK)
    prompttextRect = prompttext.get_rect()
    prompttextRect.centerx = windowSurface.get_rect().centerx
    prompttextRect.centery = windowSurface.get_rect().centery + 100
    
    #Draw the text onto the surface.
    windowSurface.blit(prompttext, prompttextRect)
    
    #Draw the window onto the screen.
    pygame.display.update()

# Set up pygame.
pygame.init()

# Set up the window.
windowSurface = pygame.display.set_mode((1000, 600), 0, 32)
pygame.display.set_caption('Joke Machine')

#Save the Jokes in a list and their answers in an other
jokes = ['What do you get when you cross a snowman with a vampire?', 'What do dentists call an astronaut\'s cavity?', 'Why did the chicken cross the road?', 'What do you call a boomerang that won’t come back?', 'What’s the best thing about having Alzheimer’s Disease?']
jokeanwers = ['Frostbite!', 'A black hole!', 'To get to the other side', 'A stick!', 'I can\'t quite remember..']

# Set up the colors.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the fonts.
basicFont = pygame.font.SysFont(None, 48)

# Draw the White background onto the surface.
windowSurface.fill(WHITE)

# Draw the dividing line
pygame.draw.line(windowSurface, BLACK, (0, 100), (1000, 100), 4)

# Set up the text.
text = basicFont.render('Joke Machine', True, BLACK)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().top + 60

#Draw the text onto the surface.
windowSurface.blit(text, textRect)

#Draw the window onto the screen.
pygame.display.update()

#block all events
pygame.event.set_blocked(None)
#allow events
pygame.event.set_allowed(pygame.QUIT)
pygame.event.set_allowed(pygame.KEYUP)
pygame.event.set_allowed(pygame.KEYDOWN)

#Give a first joke
getRandomJoke()

#Run the game loop.
while True:
      for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        else:
            # Check if the player wants another joke
            if event.type == KEYDOWN:
                if event.key == pygame.K_y:
                    getRandomJoke()
                elif event.key == pygame.K_n:
                    #clear previous text
                    pygame.draw.rect(windowSurface, WHITE, (0, 250, 1000, 300))
    
                    #Display the joke
                    byetext = basicFont.render('BYE!', True, BLACK)
                    byetextRect = byetext.get_rect()
                    byetextRect.centerx = windowSurface.get_rect().centerx
                    byetextRect.centery = windowSurface.get_rect().centery

                    #Draw the text onto the surface.
                    windowSurface.blit(byetext, byetextRect)

                    #Update Display
                    pygame.display.update()

                    #Pause the game so we get to say goodbye!
                    pygame.time.delay(500)
                    
                    pygame.quit()
                    sys.exit()
        

