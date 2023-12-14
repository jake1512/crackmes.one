key = 'AAHoT'

ans = 0
for i in range(len(key)):
    print(i)
    ans += i ^ ord(key[i])

print(ans)