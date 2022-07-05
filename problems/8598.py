x = int(input())

for _ in range(x):
    ox = list(input())
    a = 0
    sum = 0
    for i in ox:
        if i == 'O':
            a += 1
            sum += a
        else:
            a = 0
    
    print(sum)
