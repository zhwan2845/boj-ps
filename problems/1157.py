a = input().upper()
d = {}
for i in a:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

max = -1
max_key = ""

for k, v in d.items():
    if v > max:
        max = v
        max_key = k
cnt = 0
for v in d.values():
    if v == max:
        cnt += 1

if cnt != 1:
    print('?') 
else:
    print(max_key)