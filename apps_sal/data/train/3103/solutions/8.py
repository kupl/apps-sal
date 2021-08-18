def unique(integers):
    dedupe = set()
    return [i for i in integers if i not in dedupe and not dedupe.add(i)]
