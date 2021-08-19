def unique(integers):
    # The return value of set.add() is always None
    dedupe = set()
    return [i for i in integers if i not in dedupe and not dedupe.add(i)]
