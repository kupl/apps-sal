def winner(candidates):
    try:
        assert len(candidates) == 3
        max_total = 0
        for c in candidates:
            name, scores = c['name'], c['scores']
            assert 1 <= len(scores) <= 2
            assert all(not s % 5 and 0 < s <= 100 for s in scores)
            total = sum(scores)
            if max_total < total <= 100:
                selected, max_total = name, total
        return selected
    except:
        return False
