def merge(row):
    new_row, last_tile = [], 0
    
    for tile in row:
        if tile and tile == last_tile:
            new_row[-1] *= 2
            last_tile = 0
        elif tile != 0:
            new_row.append(tile)
            last_tile = tile
  
    return new_row + [0] * (len(row) - len(new_row))
