def seven(m):
    m_list = list(str(m))
    if not len(m_list) >= 2:
        final = m
        step = 0
    else:
        step = 0
        while len(m_list) >= 2:
            step += 1
            if len(m_list) > 2:
                result = int(''.join(m_list[0:len(m_list) - 1])) - 2 * int(m_list[-1])
                result_list = list(str(result))
                if len(result_list) >= 2:
                    m_list = result_list
                else:
                    m_list = result_list
                    final = int(''.join(result_list))
            else:
                step -= 1
                final = int(''.join(m_list))
                break
    return (final, step)
