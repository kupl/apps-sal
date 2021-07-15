def oracle(arr):
    lines = ["----x----", "---------", "---- ----", "----o----"]
    data = {row[0]: row[1:].count('h') for row in arr}
    arr = [data[key] for key in ["six", "five", "four", "three", "two", "one"]]
    
    return "\n".join(lines[count] for count in arr)

