def do_math(s):
    tuples_with_pairs = [(letter, element) for element in s.split() for letter in element if letter.isalpha()]
    letters = [element[0] for element in tuples_with_pairs]
    letters.sort()
    a_list = []
    m_list = []
    b_list = []
    n_list = []
    c_list = []
    o_list = []
    d_list = []
    p_list = []
    e_list = []
    q_list = []
    f_list = []
    r_list = []
    g_list = []
    s_list = []
    h_list = []
    t_list = []
    i_list = []
    u_list = []
    j_list = []
    v_list = []
    k_list = []
    w_list = []
    l_list = []
    x_list = []
    y_list = []
    z_list = []
    for pairs in tuples_with_pairs:
        if pairs[0] == "a":
            a_list.append(pairs[1])
        elif pairs[0] == "b":
            b_list.append(pairs[1])
        elif pairs[0] == "c":
            c_list.append(pairs[1])
        elif pairs[0] == "d":
            d_list.append(pairs[1])
        elif pairs[0] == "e":
            e_list.append(pairs[1])
        elif pairs[0] == "f":
            f_list.append(pairs[1])
        elif pairs[0] == "g":
            g_list.append(pairs[1])
        elif pairs[0] == "h":
            h_list.append(pairs[1])

        elif pairs[0] == "i":
            i_list.append(pairs[1])
        elif pairs[0] == "j":
            j_list.append(pairs[1])
        elif pairs[0] == "k":
            k_list.append(pairs[1])
        elif pairs[0] == "l":
            l_list.append(pairs[1])
        elif pairs[0] == "m":
            m_list.append(pairs[1])
        elif pairs[0] == "n":
            n_list.append(pairs[1])
        elif pairs[0] == "o":
            o_list.append(pairs[1])

        elif pairs[0] == "p":
            p_list.append(pairs[1])
        elif pairs[0] == "q":
            q_list.append(pairs[1])
        elif pairs[0] == "r":
            r_list.append(pairs[1])
        elif pairs[0] == "s":
            s_list.append(pairs[1])
        elif pairs[0] == "t":
            t_list.append(pairs[1])
        elif pairs[0] == "u":
            u_list.append(pairs[1])
        elif pairs[0] == "v":
            v_list.append(pairs[1])
        elif pairs[0] == "w":
            w_list.append(pairs[1])
        elif pairs[0] == "x":
            x_list.append(pairs[1])
        elif pairs[0] == "y":
            y_list.append(pairs[1])
        elif pairs[0] == "z":
            z_list.append(pairs[1])

    output_list = a_list + b_list + c_list + d_list + e_list + f_list + g_list + h_list + i_list + j_list + \
        k_list + l_list + m_list + n_list + o_list + p_list + q_list + r_list + s_list + t_list + u_list + v_list + \
        w_list + x_list + y_list + z_list

    duplicates = []
    right_strings = []
    for strings in output_list:
        if strings in duplicates and strings in right_strings:
            continue
        elif strings in right_strings and strings not in duplicates:
            duplicates.append(strings)
        else:
            right_strings.append(strings)
    print(right_strings)
    digits_list = []
    changed_string = ""
    for string in right_strings:
        for digits in string:
            if digits.isdigit():
                changed_string += digits
            continue
        digits_list.append(int(changed_string))
        changed_string = ""

    first_even_list = [0, 4, 8]
    second_even_list = [2, 6, 10]
    first_odd_list = [1, 5, 9]
    second_odd_list = [3, 7, 11]

    result = digits_list[0]
    digits_list.remove(digits_list[0])

    for number in range(len(digits_list)):
        if number in first_even_list:
            result += digits_list[number]
        elif number in first_odd_list:
            result -= digits_list[number]
        elif number in second_even_list:
            result *= digits_list[number]
        elif number in second_odd_list:
            result /= digits_list[number]

    return round(result)


print((do_math("2j 87j 169a 1275c 834f 683v")))
