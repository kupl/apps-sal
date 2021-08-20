def problem(a):

    def z(a):
        return 'Error' if str(a).isalpha() else a * 50 + 6
    return z(a)
