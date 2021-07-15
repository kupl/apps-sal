def original_number(s):
    dic = {i:0 for i in range(10)}
    dic[0] = s.count('Z')
    dic[2] = s.count('W')
    dic[4] = s.count('U')
    dic[6] = s.count('X')
    dic[8] = s.count('G')
    dic[1] = s.count('O') - dic[0] - dic[2] - dic[4]
    dic[3] = s.count('H') - dic[8]
    dic[5] = s.count('F') - dic[4]
    dic[7] = s.count('S') - dic[6]
    dic[9] = s.count('I') - dic[5] - dic[6] - dic[8]
    result = ''
    for i in range(10):
      result += str(i)*dic[i]
    return result
