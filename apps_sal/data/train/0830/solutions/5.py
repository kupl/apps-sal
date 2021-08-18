for _ in range(int(input())):
    N = int(input())
    c_str = str(input())
    target_str = str(input())
    no_match = False

    for i in range(N):

        if c_str[i] < target_str[i]:
            no_match = True
            break

        if target_str[i] not in c_str:
            no_match = True
            break

    if no_match:
        print(-1)

    else:
        indices = {char: index for index, char in enumerate(c_str)}
        m_match = {}
        for i in range(N):
            if c_str[i] != target_str[i]:
                if m_match.get(target_str[i]):
                    m_match[target_str[i]].append(str(i))

                else:
                    m_match[target_str[i]] = [str(i)]

        print(len(m_match))

        for i in sorted(m_match.keys(), reverse=True):

            print(len(m_match[i]) + 1, " ".join(m_match[i]), indices[i])
