a = []
b = []
for i in range(1, 10001):
    a.append(i)
for i in a:
    str_i = str(i)
    num = int(str_i)
    for j in str_i:
        num += int(j)
    if num < 10001:
        b.append(num)
a = set(a)
b = set(b)
c = a - b
c = list(c)
for i in sorted(c):
    print(i)