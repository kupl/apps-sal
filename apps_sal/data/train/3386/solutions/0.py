from string import ascii_uppercase as u

def get_column_title(n):
    assert isinstance(n, int) and n > 0
    col = []
    while n:
        n, r = divmod(n-1, 26)
        col.append(u[r])
    return ''.join(reversed(col))
