a = []
for _ in range(42):
    a.append(0)

for _ in range(10):
    num = input()
    num = int(num)
    a[num % 42] += 1

sum = 0
for i in a:
    if i > 0:
        sum += 1

print(sum)