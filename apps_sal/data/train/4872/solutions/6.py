def M(H):
    class R:
        __init__, compute = lambda O, Q, S=[]: setattr(O, 'O', Q if [] == S else getattr(int, f'__{H}__')(Q.O, S.O)), lambda O: O.O
    return R


value, add, sub, mul, truediv, mod, pow = map(M, '* add sub mul truediv mod pow'.split())
