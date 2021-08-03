def even_numbers(lst, k): return [n for n in lst if not n & 1][-k:]
