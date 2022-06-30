a = input()
a = int(a)

b = input()
b = int(b)

c = input()
c = int(c)

num = []
for _ in range(10):
    num.append(0)

d = a * b * c
while d != 0:
    num[d % 10] += 1
    d = d // 10

for i in num:
    print(i)
