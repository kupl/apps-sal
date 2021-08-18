def winner(candidates):
    if len(candidates) != 3 or any(
            not c.get("name") or not c.get("scores") or
            len(c["scores"]) not in (1, 2) or
            any(s % 5 or not (5 <= s <= 100) for s in c["scores"])
            for c in candidates):
        return False

    qualified = [c for c in candidates if sum(c["scores"]) <= 100]
    if not qualified:
        return False

    winner = max(qualified, key=lambda c: sum(c["scores"]))
    return winner["name"]
