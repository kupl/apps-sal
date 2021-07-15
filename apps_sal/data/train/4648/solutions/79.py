def automorphic(n):
    suka=str(n)
    print(suka," SUKA", len(suka))
    
    blyat=str(n**2)
    print(blyat," BLYAT", blyat[-len(suka):])
    if suka == blyat[-len(suka):]:
        print("YES")
        return "Automorphic"
    else:
        print("Not")
        return "Not!!"
