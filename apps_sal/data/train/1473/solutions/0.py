import sys


def __starting_point():
    t = int(input())
    for iteration in range(t):
        r, c, m_inp, k_inp, j_inp = input().strip().split(" ")
        r = int(r)
        c = int(c)
        m_inp = int(m_inp)
        k_inp = int(k_inp)
        j_inp = int(j_inp)

        ans = ""
        if (r * c) != (m_inp + k_inp + j_inp):
            print("No")
            continue
        else:
            flag = False
            for i in range(6):
                if flag:
                    break
                if i == 0:
                    m = m_inp
                    k = k_inp
                    j = j_inp
                elif i == 1:
                    m = j_inp
                    k = m_inp
                    j = k_inp
                elif i == 2:
                    m = k_inp
                    k = j_inp
                    j = m_inp
                elif i == 3:
                    m = m_inp
                    k = j_inp
                    j = k_inp
                elif i == 4:
                    m = k_inp
                    k = m_inp
                    j = j_inp
                elif i == 5:
                    m = j_inp
                    k = k_inp
                    j = m_inp
                if m % r == 0:
                    r_remain_1 = r
                    c_remain_1 = c - (m / r)

                    if k % r_remain_1 == 0:
                        r_remain_2 = r_remain_1
                        c_remain_2 = c_remain_1 - (k / r_remain_1)
                        if r_remain_2 * c_remain_2 == j:
                            print("Yes")
                            flag = True
                            continue
                    if k % c_remain_1 == 0:
                        c_remain_2 = c_remain_1
                        r_remain_2 = r_remain_1 - (k / c_remain_1)
                        if r_remain_2 * c_remain_2 == j:
                            print("Yes")
                            flag = True
                            continue

                    if j % r_remain_1 == 0:
                        r_remain_2 = r_remain_1
                        c_remain_2 = c_remain_1 - (j / r_remain_1)
                        if r_remain_2 * c_remain_2 == k:
                            print("Yes")
                            flag = True
                            continue
                    if j % c_remain_1 == 0:
                        c_remain_2 = c_remain_1
                        r_remain_2 = r_remain_1 - (j / c_remain_1)
                        if r_remain_2 * c_remain_2 == k:
                            print("Yes")
                            flag = True
                            continue

                if m % c == 0:
                    c_remain_1 = c
                    r_remain_1 = r - (m / c)

                    if k % r_remain_1 == 0:
                        r_remain_2 = r_remain_1
                        c_remain_2 = c_remain_1 - (k / r_remain_1)
                        if r_remain_2 * c_remain_2 == j:
                            print("Yes")
                            flag = True
                            continue
                    if k % c_remain_1 == 0:
                        c_remain_2 = c_remain_1
                        r_remain_2 = r_remain_1 - (k / c_remain_1)
                        if r_remain_2 * c_remain_2 == j:
                            print("Yes")
                            flag = True
                            continue

                    if j % r_remain_1 == 0:
                        r_remain_2 = r_remain_1
                        c_remain_2 = c_remain_1 - (j / r_remain_1)
                        if r_remain_2 * c_remain_2 == k:
                            print("Yes")
                            flag = True
                            continue
                    if j % c_remain_1 == 0:
                        c_remain_2 = c_remain_1
                        r_remain_2 = r_remain_1 - (j / c_remain_1)
                        if r_remain_2 * c_remain_2 == k:
                            print("Yes")
                            flag = True
                            continue
            if not flag:
                print("No")


__starting_point()
