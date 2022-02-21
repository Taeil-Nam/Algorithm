T = int(input())

for i in range(T):
    R, S = input().split()
    P = ""
    for i in S:
        P = P + i * int(R)
    print(P)
