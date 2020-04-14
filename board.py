"""
Author: Thao Le
"""
import math

class Board():
  def __init__(self, size):
    self.SIZES = size
    self.board_data = [[0 for c in range(self.SIZES)] for r in range(self.SIZES)]
  
  def set_board(self, row, col, data):
    self.board_data[row][col] = data
  
  def get_board(self):
    return self.board_data
  
  def get_size(self):
    return self.SIZES

  def get_data(self, row, col):
    return self.board_data[row][col]

  def get_transpose_data(self):
    return list(map(list, zip(*self.board_data)))
  
  def is_valid_row_or_col(self, row):
    for num in row:
      if num <= 0 or num > self.SIZES:
        return False
    if len(row) > len(set(row)):
      return False
    return True

  def is_valid(self):
    """
    check if the board is valid:
      - Each row contains unique values from 1-9.
      - Each column contains unique values from 1-9.
      - Each of the 9 sub-squares, of size 3x3, ​contains a unique value from 1-9.
    """
    # check rows and columns
    for r in range(self.SIZES):
      if not self.is_valid_row_or_col(self.board_data[r]):
        return False
    transpose_board = list(map(list, zip(*self.board_data)))
    for c in range(self.SIZES):
      if not self.is_valid_row_or_col(transpose_board[c]):
        return False
    # check sub-squares
    square_size = int(math.sqrt(self.SIZES))
    for r in range(0, self.SIZES, square_size):
      for c in range(0, self.SIZES, square_size):
        square = []
        for i in range(0, square_size):
          for j in range(0, square_size):
            square.append(self.board_data[r + i][c + j])
        if not self.is_valid_row_or_col(square):
          return False
    return True
  
  def print_board(self):
    for r in range(self.SIZES):
      for c in range(self.SIZES):
        print(str(self.board_data[r][c]) + " ", end='')
      print()
    print("------------------------------------")
