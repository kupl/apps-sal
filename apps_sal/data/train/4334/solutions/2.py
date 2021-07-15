def skiponacci(n):
    result = ["1","skip"]
    suite = [1,1]
    for i in range(2,n):
        suite.append(suite[i-2]+suite[i-1])
        if i % 2 != 0:
            result.append("skip")
        else:
            result.append(str(suite[i]))
    return " ".join(result[0:n])
