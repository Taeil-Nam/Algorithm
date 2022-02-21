n = int(input())
list_ox = []

for i in range(0, n):
    result = 0
    count = 0
    list_ox = input()
    for j in list_ox:
        if j == "O":
            count = count + 1
            result = result + count
        else:
            count = 0
    print(result)
