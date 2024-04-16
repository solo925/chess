import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Board representation
board = [
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
]

# Initial positions of the pieces
queen_pos = [3, 3]  # Example position, you can change it
pawn_pos = [4, 4]   # Example position, you can change it

def draw_board():
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                pygame.draw.rect(screen, WHITE, (i * 100, j * 100, 100, 100))
            else:
                pygame.draw.rect(screen, BLACK, (i * 100, j * 100, 100, 100))

def draw_pieces():
    for i in range(8):
        for j in range(8):
            if board[i][j] != " ":
                piece = board[i][j]
                x, y = i * 100, j * 100
                if piece == "P":
                    pygame.draw.polygon(screen, BLACK, [(x, y), (x + 50, y), (x + 50, y + 50), (x, y + 50)])
                elif piece == "Q":
                    pygame.draw.rect(screen, BLACK, (x, y, 100, 100))
                    pygame.draw.line(screen, BLACK, (x, y + 50), (x + 100, y + 50), 5)

def handle_input():
    global queen_pos, pawn_pos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                queen_pos[0] -= 1
            elif event.key == pygame.K_RIGHT:
                queen_pos[0] += 1
            elif event.key == pygame.K_UP:
                queen_pos[1] -= 1
            elif event.key == pygame.K_DOWN:
                queen_pos[1] += 1
            elif event.key == pygame.K_a:
                pawn_pos[0] -= 1
            elif event.key == pygame.K_d:
                pawn_pos[0] += 1
            elif event.key == pygame.K_w:
                pawn_pos[1] -= 1
            elif event.key == pygame.K_s:
                pawn_pos[1] += 1

def game_loop():
    running = True
    while running:
        screen.fill(BLACK)
        draw_board()
        draw_pieces()
        handle_input()
        pygame.display.flip()

if __name__ == "__main__":
    game_loop()
