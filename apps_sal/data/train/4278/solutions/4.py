import numpy as np

def diagonal(matrix):
  diag_1, diag_2 = sum(np.diag(matrix)), sum(np.diag(np.fliplr(matrix)))
  return 'Draw!' if diag_1 == diag_2 else f'{"Principal" if diag_1 > diag_2 else "Secondary"} Diagonal win!'
