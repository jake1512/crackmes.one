characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

secret = 'secret'
correct_answer = 0
for i in range(len(secret)):
    tmp = i ^ ord(secret[i])
    correct_answer += tmp

answer = 0
for one in characters:
    answer += 0 ^ ord(one)
    for two in characters:
        answer += 1 ^ ord(two)
        for three in characters:
            answer += 2 ^ ord(three)
            for four in characters:
                answer += 3 ^ ord(four)
                for five in characters:
                    answer += 4 ^ ord(five)
                    if answer == correct_answer:
                        print('{}{}{}{}{}'.format(one, two, three, four, five))
                        answer = 0
                    else:
                        print(answer)
                        answer = 0
                        continue