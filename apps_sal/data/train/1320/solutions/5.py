# 1 —> B will lose (A takes 1)
# 2 —> B will lose (A takes 2)
# 3 —> A will lose (A takes 1/2, B takes 2/1)
# 4 —> B will lose (A takes 1, B takes 1/2, A takes 2/1)
# 5 —>  B will lose (A takes 2, B takes 1/2, A takes 2/1)
# 6 —>  B will lose (A takes 3, B has turn and 3 marbles, see above)
# 7 —> B will lose (A takes 4, B has turn and 3 marbles, see above)
# 8 —> B will lose [ - A takes 1, B has turn and 7 marbles, see above
# 			 [ - A takes 2, B has turn and 6 marbles, see above
# 			 [ - A takes 4, B has turn and 4 marbles, see above
# 			 [ - A takes 6, B has turn and 2 marbles, see above
# 			 [ - A takes 8
# Even —> B will lose
# Odd —> B will lose (unless 3)
for _ in range(int(input())):
    n = int(input())
    print("A") if(n == 3) else print("B")
