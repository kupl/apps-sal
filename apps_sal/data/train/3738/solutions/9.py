def calc(k, n, m, x):
    # solve how many people get on board at station 2:
    on_list_x = [0, 1, 1, 2, 3]  # num of times x people get on
    on_list_k = [k, 0, k, k, 2 * k]  # k people get on

    off_list_x = [0, 1, 1, 1, 2]
    off_list_k = [0, 0, 0, k, k]
    # total a*x + b*k at index n-1 == m
    while len(on_list_x) < n - 1:
        on_list_x.append(on_list_x[-1] + on_list_x[-2])
        on_list_k.append(on_list_k[-1] + on_list_k[-2])
        off_list_x.append(off_list_x[-1] + off_list_x[-2])
        off_list_k.append(off_list_k[-1] + off_list_k[-2])
    num_x = sum(on_list_x) - sum(off_list_x)
    num_k = sum(on_list_k) - sum(off_list_k)
    x_val = (m - num_k) / num_x  # people at station 2

    # now all numbers of boarding and leaving people can be calculated:
    passengers_station_x = (sum(on_list_x[:x]) - sum(off_list_x[:x])) * x_val + sum(on_list_k[:x]) - sum(off_list_k[:x])

    return int(passengers_station_x)
