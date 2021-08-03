def human_years_cat_years_dog_years(n): return [n] + [15 * (n > 0) + 9 * (n > 1) + d * max(0, n - 2)for d in (4, 5)]
