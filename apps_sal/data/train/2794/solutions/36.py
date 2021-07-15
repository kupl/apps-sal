def calculate_age(b, c):
    return f"You will be born in {str(b-c)+' year' if b-c<=1 else str(b-c)+' years'}." if c-b<0 else  f"You were born this very year!" if c==b else f"You are {str(c-b)+' year' if c-b<=1 else str(c-b)+' years'} old."
