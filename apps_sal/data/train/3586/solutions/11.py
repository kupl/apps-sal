def html(A, *B, **C):
    Cs = ' '.join('{}="{}"'.format("class" if i == "cls" else i, C[i]) for i in C)
    if len(B) == 0:
        return '<{}{}{} />'.format(A,' ' if Cs else '', Cs)
    return '\n'.join('<{}{}{}>{}</{}>'.format(A,' ' if Cs else '', Cs, i, A) for i in B)
