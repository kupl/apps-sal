def order_weight(strng):
    slw = [(sum(int(x) for x in str(weight)), weight) for weight in strng.split()]
    return " ".join(x[1] for x in sorted(slw))
