from re import search


def is_uppercase(inp):
    return not search(r'[a-z]', inp)

                  

