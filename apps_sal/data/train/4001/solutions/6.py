def dot(n, m):
    return '\n'.join(['+---+' * n, '| o |' * n] * m).replace('||', '|').replace('++', '+') + '\n' + ('+---+' * n).replace('++', '+')
