check = __import__('re').compile('(?=[MDCLXVI])M*(C[MD]|D?C*)(X[CL]|L?X*)(I[XV]|V?I*)').fullmatch


def valid_romans(arr):
    return list(filter(check, arr))
