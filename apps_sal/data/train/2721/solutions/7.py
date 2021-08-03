def pyramid(n):
    output = [" " * (n - i - 1) + "/" + " " * (i * 2) + "\\\n" for i in range(n)]
    output[-1] = output[-1].replace(" ", "_")
    return "".join(output)
