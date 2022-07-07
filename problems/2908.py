a, b = input().split()

for i in range(len(a) // 2):
    tmp = a[i]
    a[i] = a[len(a) - i - 1]
    a[len(a) - i - 1] = tmp


for i in range(len(b) // 2):
    tmp = b[i]
    b[i] = b[len(b) - i - 1]
    b[len(b) - i - 1] = tmp

if int(a) > int(b):
    print(int(a))
else:
    print(int(b))


