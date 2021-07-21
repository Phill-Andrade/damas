from src.piece_generator.piece import Piece

def create_peon(color, board):
    peon = Piece(color, board)
    return peon

def refresh_peaces(board):
    for row in board:
        for peon in row:
            if isinstance(peon, Piece):
                peon.refresh_position()
                peon.make_me_king()
