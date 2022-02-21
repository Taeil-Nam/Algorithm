S = input().upper()  # baaa
S_word = list(set(S))  # B, A
count = []

for i in S_word:  # B, A
    count.append(S.count(i))  # 1, 3

if count.count(max(count)) >= 2:
    print("?")
else:
    print(S_word[count.index(max(count))])
