# Two possible resolutions: using ifs to decide which one will be the largest or max between all possibilities

# def expression_matter(a, b, c):
#     if a == 1 and c == 1:
#         return a + b + c
#     if a == 1:
#         return (a + b) * c 
#     if c == 1:
#         return a * (b + c)
#     if b == 1:
#         return max(a * (b + c), (a + b) * c)
#     return a * b * c

def expression_matter(a, b, c):
    return max([a + b + c, (a + b) * c, a * (b + c), a * b * c])
