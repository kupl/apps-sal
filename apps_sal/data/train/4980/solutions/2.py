def sort_csv_columns(csv_file_content):
    array = (line.split(";") for line in csv_file_content.split("\n"))
    trans = list(zip(*array))
    sortd = sorted(trans, key=lambda col: col[0].lower())
    untrans = list(zip(*sortd))
    return "\n".join(";".join(line) for line in untrans)

    # ugly one-liner
    # return "\n".join(";".join(t) for t in zip(*sorted(zip(*(line.split(";") for line in csv_file_content.split("\n"))), key=lambda t: t[0].lower())))
