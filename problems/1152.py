t = input()
if len(t) > 1000000:
    print("잘못했습니다.")
else:
    words = t.split(' ')
    cnt = 0

    for i in words:
        if i.isalpha():
            cnt += 1

print(cnt)