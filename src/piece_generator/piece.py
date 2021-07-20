class Piece:
    def __init__(self, is_white: bool, board: list):
        self.__type = 'peon'
        self.__color = 'white' if is_white else 'black'
        self.__board = board
        
    @property
    def describe(self) -> dict:
        return {
            'type': self.__type,
            'color': self.__color,
            'position': self.__position
        }

    def refresh_position(self):
        for row in range(len(self.__board)):
            for column in range(len(self.__board[row])):
                if self == self.__board[row][column]:
                    self.__position = (row, column)

    def move(self):
        self.__board[self.__position[0]][self.__position[1]] = None
        return self

    def kill_me(self):
        self.move()

    def make_me_king(self):
        if self.__type == 'peon' and (
                self.__color == 'black' and self.__position[0] == len(self.__board) - 1
            ) or (
                self.__color == 'white' and self.__position[0] == 0
            ):# noqa
            self.__type = 'king'
