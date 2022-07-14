#chr(97)='a'
#ord('a')=97
#ord('b') - ord('a')

alph = []
c = input()
for _ in range(26):
    alph.append(-1)

for i in range(len(c)):
     if alph[ord(c[i]) - 97] == -1:
        alph[ord(c[i]) - 97] = i

for i in range(len(alph)):
    print(alph[i], end=' ')

# a = input()
# d = {}
# for i in range(len(a)):
#     if a[i] not in d:
#         d[a[i]] = i
        
# for i in "abcdefghijklmnopqrstuvwxyz":
#     if i in d:
#         print(d[i], end=" ")
#     else:
#         print(-1, end=" ")