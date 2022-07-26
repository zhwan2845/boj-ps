def n(a):
    if a < 100:
        hansu = a
    else:
        hansu = 99
        for i in range(100, a + 1):
            str_i = str(i)
            num = []
            for j in range(len(str_i)):
                s = str_i[j]
                num.append(int(s))
            if num[0] - num[1] == num[1] - num[2]:
                hansu += 1

    return hansu

hansu_num = int(input())
print(n(hansu_num))