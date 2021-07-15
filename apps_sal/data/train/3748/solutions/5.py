def six_column_encryption(msg):
    msg = msg.replace(" ", ".") + "." * (6 - len(msg) % 6 if len(msg) % 6 != 0 else 0)
    return " ".join([msg[i::6] for i in range(6)])
