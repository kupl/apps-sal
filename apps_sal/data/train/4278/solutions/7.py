def diagonal(matrix):
    res = sum(row[i] - row[-i-1] for i,row in enumerate(matrix))
    return f"{'Principal' if res > 0 else 'Secondary'} Diagonal win!" if res else "Draw!"
