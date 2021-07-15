def calculate(n1, n2, o):
    if o == 'add': return bin(int(n1,2) + int(n2,2))[2:]
    if o == 'subtract': 
        result = bin(int(n1,2) - int(n2,2))
        if result[0] == '-':
            return result[0] + result[3:]
        return result[2:]
    if o == 'multiply': return bin(int(n1,2) * int(n2,2))[2:]
    if o == 'divide': return bin(int(n1,2) / int(n2,2))[2:]
