def solve(arr):
    alfabetet = 'abcdefghijklmnopqrstuvwxyz'
    res = []
    r = 0
#     for d in range(0, len(arr)):
#         for t in range(0, len(arr[d])):
#             if arr[d][t].lower() == alfabetet[t]:
#                 r += 1
#         res.append(r)
#         r = 0
#     return res

#     for char in arr:
#         for c in char.lower():
#             print(c)
#              if c == alfabetet[c]:
#                  r += 1

    for char in arr:
        for a, b in zip(char.lower(), alfabetet):
            if a == b:
                r += 1
        res.append(r)
        r = 0
    return res
