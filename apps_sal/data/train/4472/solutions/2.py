bin_to_colors = {1: 'black', 2: 'brown', 3: 'dark brown', 4: 'white', 5: 'grey', 6: 'light brown'}
colors_to_bin = {v: k for (k, v) in bin_to_colors.items()}


def bear_fur(bears):
    return bin_to_colors.get(sum((colors_to_bin.get(k, 7) for k in set(bears))), 'unknown')
