def scramble(s1, s2):
    if len(s2) > len(s1):
        return False
    let1 = [s1.count(chr(i)) for i in range(97, 123)]
    let2 = [s2.count(chr(i)) for i in range(97, 123)]
    sub = [True if (let1[i] >= let2[i]) else False for i in range(26)]
    return (True if False not in sub else False)
