import itertools

def mastermind(game):
    colours = "Red Blue Green Orange Purple Yellow".split()
    def check(solution, guess):
        black = sum(a == b for a, b in zip(solution, guess))
        white = sum(max(0, min(solution.count(c), guess.count(c))) for c in colours) - black
        return ["Black"] * black + ["White"] * white
    candidates = list(itertools.product(colours, repeat=4))
    while candidates:
        candidate = candidates.pop()
        score = sorted(game.check(list(candidate)))
        candidates = [c for c in candidates if check(candidate, c) == score]
