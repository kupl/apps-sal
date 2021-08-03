def number(bus_stops):
    first_tuple_elements = []
    second_tuple_elements = []
    result = []
    for i in bus_stops:
        first_tuple_elements.append(i[0])
        second_tuple_elements.append(i[1])
    x = 0
    result = 0
    for i in first_tuple_elements:
        result += first_tuple_elements[x] - second_tuple_elements[x]
        print(result)
        x += 1
    return result
