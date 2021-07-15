def array(string):
    numbers = string.split(',')
    return None if len(numbers) < 3 else ' '.join(string.split(',')[1:-1])
