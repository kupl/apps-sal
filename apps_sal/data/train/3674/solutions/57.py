def add_binary(a, b):
    # your code here
    count = a + b
    output = ''

    while True:
        output += str(count % 2)
        count = count // 2

        if count < 2:
            output += str(count)
            output = output[::-1]

            while output.startswith('0'):
                output = output[1:]

            return output
