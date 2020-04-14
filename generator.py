import math
import random

import board

class InitiliseDict(dict):
  def __getitem__(self, idx):
    self.setdefault(idx, [])
    return dict.__getitem__(self, idx)

def get_coordinates(data_index, size):
  x = data_index // size
  y = data_index % size
  return x, y

def get_possible_option(_board, data_index):
  size = _board.get_size()
  x, y = get_coordinates(data_index, size)
  board_data = _board.get_board()
  all_options = list(range(1, size + 1))

  # check this row
  not_options = set(board_data[x])
  # check this column
  not_options.update(_board.get_transpose_data()[y])
  # check this square
  square_size = round(math.sqrt(size))
  x_top_left = x // square_size * square_size
  y_top_left = y // square_size * square_size
  for i in range(x_top_left, x_top_left + square_size):
    for j in range(y_top_left, y_top_left + square_size):
      not_options.add(board_data[i][j])

  # options lefts
  options = [option for option in all_options if option not in not_options]
  return options

def generate_sudoku(_board, data_index, size, checked_options):
  print(data_index)
  _board.print_board()
  if data_index >= size**2:
    return
  x, y = get_coordinates(data_index, size)
  options = get_possible_option(_board, data_index)
  new_options = [option for option in options if option not in checked_options[data_index]]
  if not new_options:
    print("Backtracking")
    checked_options[data_index] = []
    _board.set_board(x, y, 0)
    generate_sudoku(_board, data_index - 1, size, checked_options)
  else:
    num = random.choice(new_options)
    checked_options[data_index].append(num)
    _board.set_board(x, y, num)
    generate_sudoku(_board, data_index + 1, size, checked_options)

if __name__ == "__main__":
  size = int(input())
  sqrt_size = math.sqrt(size)
  while (sqrt_size != math.ceil(sqrt_size) or sqrt_size != math.floor(sqrt_size)):
    print("Input a square number")
    size = int(input())
    sqrt_size = math.sqrt(size)

  _board = board.Board(size)
  check_options = InitiliseDict()
  generate_sudoku(_board, 0, size, check_options)
  print("Is the board valid: %s" % (_board.is_valid()))
