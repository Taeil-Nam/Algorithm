n = int(input())  # 2
score = []
new_score = []
sum = 0


score = list(map(int, input().split()))  # 50, 70

max_score = max(score)  # 70

for i in range(n):
    new_score.append(score[i] / max_score * 100)  # 7000 / score[i]

for i in range(n):
    sum = sum + new_score[i]

avg = sum / n

print(avg)
