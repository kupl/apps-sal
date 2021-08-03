def to_pretty(seconds):
    w, d, h, m, s = seconds // 604800, seconds % 604800 // 86400, seconds % 604800 % 86400 // 3600, seconds % 604800 % 86400 % 3600 // 60, seconds % 604800 % 86400 % 3600 % 60
    return ('just now' if not seconds else
            [f'a week ago', f'{w} weeks ago'][w > 1] if w > 0 else
            [f'a day ago', f'{d} days ago'][d > 1] if d > 0 else
            [f'an hour ago', f'{h} hours ago'][h > 1] if h > 0 else
            [f'a minute ago', f'{m} minutes ago'][m > 1] if m > 0 else
            [f'a second ago', f'{s} seconds ago'][s > 1])
