def animals(h, l): return l % 2 < 1 and h <= l // 2 <= h * 2 and (2 * h - l // 2, l // 2 - h) or "No solutions"
