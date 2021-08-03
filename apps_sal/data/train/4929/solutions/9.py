def generator(strings: list):
    while True:
        for q in strings:
            yield q
        for q in strings[-2: 0: -1]:
            yield q


def get_diagonale_code(grid: str) -> str:
    strings = [q.replace(' ', '') for q in grid.split('\n')]
    result = []
    for index, row in enumerate(generator(strings)):
        if index < len(row):
            result.append(row[index])
        else:
            return ''.join(result)
