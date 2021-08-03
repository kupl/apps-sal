rules = [
    (lambda x: x == 88, "Leo finally won the oscar! Leo is happy"),
    (lambda x: x == 86, "Not even for Wolf of wallstreet?!"),
    (lambda x: x < 88, "When will you give Leo an Oscar?"),
    (lambda x: True, "Leo got one already!")
]


def leo(oscar): return next(text for (predicate, text) in rules if predicate(oscar))
