def odd_row(n):
        return [x for x in range((n**2)-(n-1), (2*n)+ ((n**2)-(n-1))) if (x%2)]
