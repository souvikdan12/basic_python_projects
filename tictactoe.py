import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tic-Tac-Toe Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Board settings
cell_size = 200
board = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]

# Game variables
current_player = "X"
font = pygame.font.Font(None, 100)
winner_font = pygame.font.Font(None, 50)
game_over = False
winner = None

# Function to check for a winner
def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != "":
            return row[0]
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    # Check for draw
    if all(cell != "" for row in board for cell in row):
        return "Draw"
    return None

# Main game loop
running = True
while running:
    screen.fill(WHITE)
    
    # Draw the grid lines
    pygame.draw.line(screen, BLACK, (cell_size, 0), (cell_size, screen_height), 5)
    pygame.draw.line(screen, BLACK, (2 * cell_size, 0), (2 * cell_size, screen_height), 5)
    pygame.draw.line(screen, BLACK, (0, cell_size), (screen_width, cell_size), 5)
    pygame.draw.line(screen, BLACK, (0, 2 * cell_size), (screen_width, 2 * cell_size), 5)
    
    # Draw the X's and O's
    for row in range(3):
        for col in range(3):
            if board[row][col] != "":
                text = font.render(board[row][col], True, BLACK)
                screen.blit(text, (col * cell_size + 70, row * cell_size + 50))
    
    # Display winner message if game is over
    if game_over:
        if winner == "Draw":
            message = "It's a draw!"
        else:
            message = f"Player {winner} wins!"
        winner_text = winner_font.render(message, True, reversed(BLACK))
        screen.blit(winner_text, (screen_width // 2 - winner_text.get_width() // 2, screen_height // 2 - winner_text.get_height() // 2))
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            row = mouse_y // cell_size
            col = mouse_x // cell_size
            if board[row][col] == "":
                board[row][col] = current_player
                winner = check_winner(board)
                if winner:
                    game_over = True
                else:
                    current_player = "O" if current_player == "X" else "X"
    
    pygame.display.update()

pygame.quit()
