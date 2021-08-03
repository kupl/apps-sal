T = str.maketrans('AOaoEUeuIYiy', 'ÄÖäöËÜëüÏŸïÿ')


def heavy_metal_umlauts(s):
    return s.translate(T)
