from collections import Counter
def mystery_range(s,n):
    counts = Counter(s)
    for num in range(1, 100):
        if counts == Counter(''.join(map(str, range(num, num + n)))):
           if all(str(i) in s for i in range(num, num + n)):
               return [num, num + n - 1]
