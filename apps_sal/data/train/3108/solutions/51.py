def multi_table(number):
    final = []
    count = 1
    for i in range(10):
        final.append(str(count))
        final.append(" * ")
        final.append(str(number))
        final.append(" = ")
        prod = count * number
        final.append(str(prod))
        if count != 10:
            final.append("\n")
        count+=1
    return ("").join(final)

