t = int(input())
for _ in range(t):
    string = input()
    string = list(string)
    for i in range(len(string)):
        if string[i] == 'm' and i > 0 and string[i - 1] == 's':
            string[i - 1] = 'x'
        elif string[i] == 'm' and i < len(string) - 1 and string[i + 1] == 's':
            string[i + 1] = 'x'
    s_count = 0
    m_count = 0
    for i in range(len(string)):
        if string[i] == 's':
            s_count += 1
        elif string[i] == 'm':
            m_count += 1
    if s_count > m_count:
        print('snakes')
    elif m_count > s_count:
        print('mongooses')
    else:
        print('tie')
