def draw_spider(L, B, M, E):
    return '^%s^ /\\%s/\\ /╲%s╱\\ ╱╲%s╱╲'.split()[L - 1] % ('(' * B + E * 2 ** (B - 1) + M + E * 2 ** (B - 1) + ')' * B)
