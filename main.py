import pygame
import random
from enum import Enum
import os

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
DARK_GRAY = (100, 100, 100)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLUE = (0, 100, 200)

class Choice(Enum):
    """Enum representing the game choices"""
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"

class Result(Enum):
    """Enum representing the game result"""
    PLAYER_WINS = "player"
    COMPUTER_WINS = "computer"
    TIE = "tie"

class GameState(Enum):
    """Enum representing the game state"""
    CHOOSING = "choosing"
    SHOWING_RESULT = "showing_result"
    GAME_OVER = "game_over"

def load_background():
    """Load background image"""
    image_path = "assets/images"

    # Load background.png
    filepath = os.path.join(image_path, "background.png")
    background = pygame.image.load(filepath)
    return background

def load_images():
    """Load all game images"""
    images = {}
    image_path = "assets/images"

    # Load images
    for choice in Choice:
        filename = f"{choice.value}.png"
        filepath = os.path.join(image_path, filename)
        image = pygame.image.load(filepath)
        images[choice] = image

    # Use rock image as default for no choice
    images[None] = images[Choice.ROCK]

    return images

def determine_winner(player, computer):
    """Determines the winner based on the rules"""
    if player == computer:
        return Result.TIE

    winning_combinations = {
        (Choice.ROCK, Choice.SCISSORS),
        (Choice.SCISSORS, Choice.PAPER),
        (Choice.PAPER, Choice.ROCK)
    }

    if (player, computer) in winning_combinations:
        return Result.PLAYER_WINS
    else:
        return Result.COMPUTER_WINS

def main():
    # Setup screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Rock-Paper-Scissors - In tribute to Alex Kidd in Miracle World")
    clock = pygame.time.Clock()

    # Load background and images
    background = load_background()
    images = load_images()

    # Fonts
    result_font = pygame.font.Font(None, 56)
    instruction_font = pygame.font.Font(None, 28)

    # Choice list for cycling
    choice_list = [Choice.ROCK, Choice.PAPER, Choice.SCISSORS]

    # Game variables
    game_state = GameState.CHOOSING
    current_choice_index = 0  # Index in choice_list
    player_choice = None
    computer_choice = None
    result = None
    result_timer = 0

    running = True
    while running:
        clock.tick(FPS)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if game_state == GameState.CHOOSING:
                    if event.key == pygame.K_UP:
                        # Cycle backward
                        current_choice_index = (current_choice_index - 1) % len(choice_list)
                    elif event.key == pygame.K_DOWN:
                        # Cycle forward
                        current_choice_index = (current_choice_index + 1) % len(choice_list)
                    elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        # Confirm selection
                        player_choice = choice_list[current_choice_index]
                        computer_choice = random.choice(choice_list)
                        result = determine_winner(player_choice, computer_choice)
                        game_state = GameState.SHOWING_RESULT
                        result_timer = pygame.time.get_ticks()

                elif game_state == GameState.GAME_OVER:
                    # Reset the game on any key press
                    game_state = GameState.CHOOSING
                    current_choice_index = 0
                    player_choice = None
                    computer_choice = None
                    result = None

        # Check if we should transition to game over
        if game_state == GameState.SHOWING_RESULT:
            if result != Result.TIE and pygame.time.get_ticks() - result_timer > 2000:
                game_state = GameState.GAME_OVER
            elif result == Result.TIE and pygame.time.get_ticks() - result_timer > 1500:
                # Automatically restart if tie
                game_state = GameState.CHOOSING
                current_choice_index = 0
                player_choice = None
                computer_choice = None
                result = None

        # Drawing
        # Draw background
        screen.blit(background, (0, 0))

        # Draw player and computer images (ALWAYS VISIBLE)
        image_y = 250

        # Player image (left side) - shows the current selection or final choice
        if game_state == GameState.CHOOSING:
            display_choice = choice_list[current_choice_index]
        else:
            display_choice = player_choice

        player_image = images[display_choice]
        player_image_rect = player_image.get_rect(center=(150, image_y))
        screen.blit(player_image, player_image_rect)

        # Computer image (right side)
        computer_image = images[computer_choice]
        computer_image_rect = computer_image.get_rect(center=(600, image_y))
        screen.blit(computer_image, computer_image_rect)

        # Draw result message
        if game_state == GameState.SHOWING_RESULT or game_state == GameState.GAME_OVER:
            if result == Result.TIE:
                result_text = result_font.render("TIE! Try again...", True, DARK_GRAY)
            elif result == Result.PLAYER_WINS:
                result_text = result_font.render("YOU WIN!", True, GREEN)
            else:
                result_text = result_font.render("YOU LOSE!", True, RED)

            result_rect = result_text.get_rect(center=(SCREEN_WIDTH // 2, 260))
            screen.blit(result_text, result_rect)

        # Draw instructions
        if game_state == GameState.CHOOSING:
            instruction1 = instruction_font.render("Use UP/DOWN arrows to cycle through choices", True, BLACK)
            instruction1_rect = instruction1.get_rect(center=(SCREEN_WIDTH // 2, 120))
            screen.blit(instruction1, instruction1_rect)

            instruction2 = instruction_font.render("Press ENTER or SPACE to confirm", True, BLACK)
            instruction2_rect = instruction2.get_rect(center=(SCREEN_WIDTH // 2, 150))
            screen.blit(instruction2, instruction2_rect)

        elif game_state == GameState.GAME_OVER:
            restart_text = instruction_font.render("Press any key to play again", True, DARK_GRAY)
            restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, 150))
            screen.blit(restart_text, restart_rect)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()