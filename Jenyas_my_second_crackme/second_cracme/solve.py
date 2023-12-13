v1 = 0
v2 = 0 
v3 = 0
pool = []
for i in range(48, 123):
    print('char =', i, chr(i))
    if i < 48:
        print('0')
        continue
    if i > 57:
        if i < 65:
            print('0')
            continue
        if i > 90:
            if i < 97 or i > 122:
                print('0')
                continue
            v3 = 1
            pool.append(i)
        else:
            v2 = 1
            pool.append(i)
    else:
        v1 = 1
        pool.append(i)
    
print(v1 + v2 + v3)
print(pool)
print(len(pool))