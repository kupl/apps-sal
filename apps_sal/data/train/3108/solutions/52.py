def multi_table(n):
    return '\n'.join([f'{str(i)} * {str(n)} = {str(i*n)}' for i in range(1, 11)])
