# Today I am mostly implementing Scala's pattern matching in Python...
# Wondering if I can implement the Elixir pipe operator |> via decorators next
# I may be bored.

_ = '_'

def match(patterns, *args):
    for pattern, result in patterns:
        if all(p == _ or p == actual for p, actual in zip(pattern, args)):
            return result

def final_grade(exam, projects):
    patterns = [
        ((True, ),  100),
        ((_, _, _, True), 100),
        ((_, True, _, _, True), 90),
        ((_, _, True, _, _, True), 75),
        ((), 0)
    ]
    return match(patterns,
        exam > 90, exam > 75, exam > 50, 
        projects > 10, projects > 4, projects > 1
    )
