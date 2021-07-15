def solve(n):
#Imagine a table, 1 to n on the top, and 1 to n on the side.
#The contents of the table are the difference between the columnNo.^2 minus the rowNo.^2 (positive values only)
#Therefore the row must always be smaller in value than the column number.
#The first diagonal shows values of the pattern 2*rowNo. + 1, the second 4*rowNo. + 4, the third 6*rowNo. + 9.
#Therefore let rowNo. = R, and the diagonal = D and the value in the table be n.
#n = 2*D*R - D^2
#Rerarrage to get  R = (n-(D ** 2))/(2 * D) 

    answer = -1
    for D in range(1, max(int(n ** 0.5),5)):
        R = (n-(D ** 2))/(2 * D)
        if R.is_integer() and R > 0:
            answer = R ** 2

    return answer
