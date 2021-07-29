from src.piece_generator import piece_generator


def generate_board():
    return [[None for caos in range(8)] for destruicao in range (8)]


def organize_piece(board):
    for row in range(len(board)):
        for house in range(len(board[row])):
            if row < 3:
                if row % 2 == 1:    
                    if house % 2 == 0:
                        board[row][house] = piece_generator.create_peon(is_white=True, board=board)
                if row % 2 == 0:
                    if house % 2 == 1:
                        board[row][house] = piece_generator.create_peon(is_white=True, board=board)
            if row > 4:
                if row % 2 == 1:    
                    if house % 2 == 0:
                        board[row][house] = piece_generator.create_peon(is_white=False, board=board)
                if row % 2 == 0:
                    if house % 2 == 1:
                        board[row][house] = piece_generator.create_peon(is_white=False, board=board)
                
    piece_generator.refresh_peaces(board=board)                    
    return board
