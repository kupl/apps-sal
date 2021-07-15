valid_card=lambda c:sum(sum(divmod(int(d)<<i%2,10))for i,d in enumerate(c.replace(' ','')[::-1]))%10<1
