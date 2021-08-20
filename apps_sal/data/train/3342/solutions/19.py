def pattern(n):
    message_to_return = []
    if n >= 1:
        for i in range(1, n + 1):
            message_to_return.append(''.join([str(i)] * i))
    return '\n'.join(message_to_return)
