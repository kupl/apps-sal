find_unknown_number = lambda *a: next((i for i in __import__('itertools').count(1) if all((i % x == a[j] for (j, x) in enumerate((3, 5, 7))))))
