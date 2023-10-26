BOARD_COLS = 8
BOARD_ROWS = 8


class Board():
    def __init__(self):
        self.board = [[' ' for _ in range(BOARD_COLS)]
                      for _ in range(BOARD_ROWS)]
        self.turns = 0
        self.last_move = [-1, -1]

    def print_board(self):
        print("\n")

        for x in range(BOARD_COLS):
            print(f"  ({x+1}) ", end="")
        print("\n")

        for x in range(BOARD_ROWS):
            print('|', end="")
            for y in range(BOARD_COLS):
                print(f"  {self.board[x][y]}  |", end="")
            print("\n")

        print(f"{'-' * 42}\n")

    def which_turn(self):
        players = ['X', 'O']
        return players[self.turns % 2]

    def in_bounds(self, r, c):
        return (r >= 0 and r < BOARD_ROWS and c >= 0 and c < BOARD_COLS)

    def turn(self, col):

        for row in range(BOARD_ROWS-1, -1, -1):
            if self.board[row][col] == ' ':
                self.board[row][col] = self.which_turn()
                self.last_move = [row, col]

                self.turns += 1
                return True

        return False

    def check_winner(self):
        last_row = self.last_move[0]
        last_col = self.last_move[1]
        last_letter = self.board[last_row][last_col]

        directions = [[[-1, 0], 0, True],
                      [[1, 0], 0, True],
                      [[0, -1], 0, True],
                      [[0, 1], 0, True],
                      [[-1, -1], 0, True],
                      [[1, 1], 0, True],
                      [[-1, 1], 0, True],
                      [[1, -1], 0, True]]

        for a in range(4):
            for d in directions:
                r = last_row + (d[0][0] * (a+1))
                c = last_col + (d[0][1] * (a+1))

                if d[2] and self.in_bounds(r, c) and self.board[r][c] == last_letter:
                    d[1] += 1
                else:

                    d[2] = False

        for i in range(0, 7, 2):
            if (directions[i][1] + directions[i+1][1] >= 3):
                self.print_board()
                print(f"{last_letter} is the winner!")
                return last_letter

        return False


def Now_play():

    game = Board()

    game_over = False
    while not game_over:
        game.print_board()

        valid_move = False
        while not valid_move:
            user_move = input(
                f"{game.which_turn()}'s Turn - pick a column (1-{BOARD_COLS}): ")
            try:
                valid_move = game.turn(int(user_move)-1)
            except:
                print(f"Please choose a number between 1 and {BOARD_COLS}")

        game_over = game.check_winner()

        if not any(' ' in x for x in game.board):
            print("The game is a draw..")
            return


if __name__ == '__main__':
    Now_play()
