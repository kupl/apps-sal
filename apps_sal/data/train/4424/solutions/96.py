def expression_matter(a,
                      b,
                      c):

    potential = [a + b + c,
                 a + b * c,
                 (a + b) * c,
                 a * b + c,
                 a * (b + c),
                 a * b * c,
                 a * c + b,
                 a * (c + b)]

    return max(potential)
