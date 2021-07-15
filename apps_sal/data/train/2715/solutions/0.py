def counter_effect(hit_count):
    return [[i for i in range(int(hit_count[x]) + 1)] for x in range(4)]
