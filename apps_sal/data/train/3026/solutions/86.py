def min_value(digits):
    if len(digits) > 1:
        digits.sort()

        output = []
        counter = 1
        for i in digits:
            if i != digits[counter]:
                output.append(i)
            if counter != len(digits) - 1:
                counter += 1
        output.append(digits[-1])

        output = [str(i) for i in output]
        output = int(''.join(output))
        return output
    return digits[0]
