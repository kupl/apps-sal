def rotate(list_):
    return list_[1:] + list_[:1]


def is_palindrome(list_):
    return list_ == list_[::-1]


def solve(st):
    list_ = list(st)
    for _ in range(len(st)):
        if is_palindrome(list_):
            return True
        else:
            list_ = rotate(list_)
    return False

