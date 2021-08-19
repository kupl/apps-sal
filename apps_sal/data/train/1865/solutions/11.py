from collections import deque
directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]


def can_move(source, dest, a, walls, box):
    q = deque()
    q.append(source)
    visited = set()
    while q:
        item = q.popleft()
        if item == dest:
            return True
        if item in visited:
            continue
        visited.add(item)
        for direction in directions:
            new_item = (item[0] + direction[0], item[1] + direction[1])
            if is_valid(a, new_item, walls, box):
                q.append(new_item)


def is_valid(a, pos, walls, box=''):
    (x, y) = pos
    if 0 <= x < len(a) and 0 <= y < len(a[0]) and ((x, y) not in walls) and ((x, y) != box):
        return True
    return False


def get_info(a):
    walls = set()
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == '#':
                walls.add((i, j))
            if a[i][j] == 'S':
                person = (i, j)
            if a[i][j] == 'T':
                target = (i, j)
            if a[i][j] == 'B':
                box = (i, j)
    return (person, target, box, walls)


def get_min_moves(a):
    (person, target, box, walls) = get_info(a)
    q = deque()
    q.append((0, box, person))
    result = float('inf')
    visited = set()
    while q:
        (dist, box, person) = q.popleft()
        if (box, person) in visited:
            continue
        visited.add((box, person))
        if box == target:
            result = min(result, dist)
            continue
        for direction in directions:
            new_player_position = (box[0] + direction[0], box[1] + direction[1])
            new_box = (box[0] + direction[0] * -1, box[1] + direction[1] * -1)
            if is_valid(a, new_box, walls) and can_move(person, new_player_position, a, walls, box):
                if is_valid(a, new_player_position, walls):
                    q.append((dist + 1, new_box, box))
    return result if result != float('inf') else -1


class Solution:

    def minPushBox(self, grid: List[List[str]]) -> int:
        return get_min_moves(grid)
