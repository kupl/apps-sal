def stringify(node):

    count = 0
    next_node = ""

    while count < 100:

        try:

            current_node = eval("node." + count * "next." + "data")
            next_node += str(current_node) + " -> "
            count += 1

        except:
            return "None" if node == None else next_node + "None"
