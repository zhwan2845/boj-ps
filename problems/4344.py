x = int(input())

for _ in range(x):
    scores = input().split()
    for i in range(len(scores)):
        scores[i] = int(scores[i])
    num = scores[0]
    scores.pop(0)
    
    sum = 0
    for i in range(num):
        sum += scores[i]

    average = sum / num
    cnt = 0
    for i in scores:
        if i > average:
            cnt += 1

    a = cnt / num * 100
    print(f"{a:.3f}%")