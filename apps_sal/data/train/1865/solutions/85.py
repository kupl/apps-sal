class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        dire = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def can_get(cur_b, cur_p, tar):
            seen, cur = set([cur_p]), set([cur_p])
            while cur:
                tmp = []
                for loc in cur:
                    for x, y in dire:
                        if 0 <= loc[0] + x < len(grid) and 0 <= loc[1] + y < len(grid[0]) and (
                                loc[0] + x, loc[1] + y) != cur_b and grid[loc[0] + x][loc[1] + y] != '#' and (
                                loc[0] + x, loc[1] + y) not in seen:
                            tmp += [(loc[0] + x, loc[1] + y)]
                cur = set(tmp)
                seen |= cur
                if tar in seen:
                    return True
            return False

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'B':
                    box = (i, j)
                if grid[i][j] == 'S':
                    player = (i, j)
                if grid[i][j] == 'T':
                    target = (i, j)

        seen, cur, res = set([(box, player)]), set([(box, player)]), 0
        while cur:
            tmp = []
            res += 1
            for b, p in cur:
                for x, y in dire:
                    if 0 <= b[0] + x < len(grid) and 0 <= b[1] + y < len(grid[0]) and grid[b[0] + x][
                            b[1] + y] != '#' and can_get(b, p, (b[0] - x, b[1] - y)) and (
                            (b[0] + x, b[1] + y), b) not in seen:
                        tmp += [((b[0] + x, b[1] + y), b)]
            cur = set(tmp)
            seen |= cur
            for x, y in dire:
                if (target, (target[0] + x, target[1] + y)) in seen:
                    return res
        return -1
