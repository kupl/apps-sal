from collections import Counter


def solution(tiles):

    def candidate(d):
        game[d] += 1
        isGood = dfs()
        game[d] -= 1
        return isGood

    def dfs(hasPair=False):
        isGood, dig = False, min(k for k, v in game.items() if v)

        for iPair, config in enumerate([(3,), (1, 1, 1)] + [(2,)] * (not hasPair)):
            cMeld = Counter({dig + i: v for i, v in enumerate(config)})

            if sum((game & cMeld).values()) == sum(config):
                game.__isub__(cMeld)
                isGood |= sum(game.values()) == 0 or dfs(hasPair or iPair == 2)
                game.__iadd__(cMeld)
                if isGood:
                    break
        return isGood

    game = Counter(map(int, tiles))
    return ''.join(str(d) for d in range(1, 10) if game[d] < 4 and candidate(d))
