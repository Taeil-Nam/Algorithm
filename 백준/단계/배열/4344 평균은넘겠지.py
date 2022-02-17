c = int(input())
list_score = []

for i in range(c):
    list_score = input().split()
    student_num = int(list_score[0])
    sum = 0
    avg = 0
    count = 0

    for i in range(1, student_num + 1):
        sum = sum + int(list_score[i])
    avg = sum / int(student_num)

    for i in range(1, student_num + 1):
        if avg < int(list_score[i]):
            count = count + 1

    result = count / student_num * 100
    print(format(round(result, 3), ".3f") + "%")
