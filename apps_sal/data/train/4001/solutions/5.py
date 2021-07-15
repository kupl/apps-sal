def dot(n,m):
    inter = "\n" + "+"+ "+".join("---" for i in range(n)) + "+" + "\n"
    bigo = "|"+ "|".join(" o " for i in range(n)) + "|"
    return (inter + (inter).join(bigo for i in range(m)) + inter)[1:-1]
