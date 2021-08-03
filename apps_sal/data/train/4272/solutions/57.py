def greet(name):
    small_name = name.lower()
    n_a_m_e = list(small_name)
    x = 0
    if name == "Johnny":
        return "Hello, my love!"
    while x != len(n_a_m_e):
        if x == 0:
            n_a_m_e[x] = n_a_m_e[x].upper()
            x = x + 1
            print(x)
        elif x <= len(n_a_m_e):
            n_a_m_e[x] = n_a_m_e[x]
            x = x + 1
            print(x)
    n_a_m_e += "!"
    end = ["H", "e", "l", "l", "o", ",", " "] + n_a_m_e
    end = ''.join(end)
    return end
