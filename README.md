# Rock-Paper-Scissors Game

A graphical rock-paper-scissors game built with Pygame.

## Description

This is a classic rock-paper-scissors game where you play against the computer. The game features a graphical interface with images for each choice and a custom background.

## Rules

- **Rock** beats **Scissors**
- **Scissors** beats **Paper**
- **Paper** beats **Rock**
- If both players choose the same option, it's a tie and you play again
- The game continues until either you or the computer wins

## Requirements

- Python 3.13.7
- Pygame

## Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install pygame
   ```

## How to Play

1. Run the game:
   ```bash
   python main.py
   ```

2. **Controls:**
    - **UP Arrow** - Cycle backward through choices (Rock → Scissors → Paper)
    - **DOWN Arrow** - Cycle forward through choices (Rock → Paper → Scissors)
    - **ENTER or SPACE** - Confirm your selection and play
    - **Any Key** - Restart the game after it ends

3. Your current choice is displayed on the left side of the screen
4. After confirming, the computer makes its choice and the winner is determined
5. If it's a tie, the game automatically restarts after a short delay
6. If there's a winner, press any key to play again

---

Enjoy playing! 🎮