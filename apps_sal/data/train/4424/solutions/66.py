def expression_matter(a, b, c):
    return max([(a+b+c),
                (a+b) * c,
                (b+c) * a,
                (a*b*c)
    ])
