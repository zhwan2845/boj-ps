alph = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
s = input()
cnt = 0

for i in range(len(s)):
    for j in range(len(alph)):
        if s[i] in alph[j]:
            cnt += j + 3

print(cnt)
