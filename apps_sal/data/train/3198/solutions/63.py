def check_exam(arr1, arr2):
    def grade(a, b):
        if not b:
            return 0
        if a == b:
            return 4
        if a != b:
            return -1
    s = sum(map(lambda x, y: grade(x, y), arr1, arr2))
    return s if s > 0 else 0
