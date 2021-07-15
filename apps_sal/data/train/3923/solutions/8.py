def micro_world(bacteria, k):
    bacteria.sort()
    while True:
        last = len(bacteria)
        for j in range(len(bacteria)):
            has_eat = False
            for i in range(j+1, len(bacteria)):
                if bacteria[i] > bacteria[j] and bacteria[i] <= k+bacteria[j]:
                    bacteria.remove(bacteria[j])
                    has_eat = True
                    break
            if has_eat:
                break
        if len(bacteria) == last:
            break
    return len(bacteria)
