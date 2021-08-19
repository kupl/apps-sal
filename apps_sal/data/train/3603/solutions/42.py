def lovefunc(flower1, flower2):

    def even(x):
        return x % 2 == 0
    a = even(flower1)
    b = even(flower2)
    return a and (not b) or (b and (not a))
