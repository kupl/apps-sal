def first_non_consecutive(arr): return (lambda x: None if len(x) == 0 else min(x) + 1)({*range(min(arr), max(arr) + 1)}.difference({*arr}))
