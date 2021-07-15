def string_transformer(stg):
    return " ".join(word for word in stg.swapcase().split(" ")[::-1])
