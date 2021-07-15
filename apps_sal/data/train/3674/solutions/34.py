def add_binary(a, b):
    sum = a + b

    divisors = list()
    for r in range(sum):
        x = 2 ** r
        if x > sum:
            break
        divisors.append(x)

    divisors = list(reversed(divisors))

    output = ""
    count = 0
    while sum > 0:
        if divisors[count] > sum:
            output = output + "0"
        else:
            output = output + "1"
            sum -= divisors[count]
            if sum == 0:
                output = output + "0" * (len(divisors) - count - 1)
        count += 1

    return output

