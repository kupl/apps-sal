def words_to_marks(s):
    lett = [chr(i) for i in range(ord('a'),ord('z')+1)]
    nums = [i for i in range(1, 27)]
    z = zip(lett, nums)
    d = dict(z)
    s1 = [d[i] for i in s]
    return sum(s1)
