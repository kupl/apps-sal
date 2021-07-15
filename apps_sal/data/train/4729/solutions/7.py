numbers = 'zero one two three four five six seven eight nine'.split()

def f(n):  return ''.join(numbers[int(i)] for i in str(n))

def numbers_of_letters(n):
    ans = [f(n)]
    while ans[-1]!='four':
        ans.append(f(len(ans[-1])))
    return ans
