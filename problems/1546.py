num = input()
num = int(num)
max = -1

scores = input().split()
for i in range(num):
    scores[i] = int(scores[i])

    if scores[i] > max:
        max = scores[i]

new = []
sum = 0

for i in range(num):
    new.append(scores[i] / max * 100)
    sum += new[i]

average = sum / num

print(average)
