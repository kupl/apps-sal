def inside_out(text):
    return ' '.join(next(f'{w[:i][::-1]}{w[i:j]}{w[j:][::-1]}' for i, j in [[len(w) // 2, (len(w) + 1) // 2]]) for w in text.split())
