def enough(cap, on, wait):
    resultado = (on + wait - cap)
    return resultado if resultado > 0 else 0
    # Your code here
