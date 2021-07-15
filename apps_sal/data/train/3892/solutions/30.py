def grader(data):
    if data == 1:
        return "A"
    data = int(data * 10)
    return {6: "D", 7: "C", 8: "B", 9: "A"}.get(data, "F")

