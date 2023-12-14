from tqdm import tqdm
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

secret = 'secret'
correct_answer = 0
for i in range(len(secret)):
    tmp = i ^ ord(secret[i])
    correct_answer += tmp

answer = 0
correct_keys = []
for one in tqdm(characters):
    for two in tqdm(characters):
        for three in characters:
            for four in characters:
                for five in characters:
                    answer = (0 ^ ord(one)) + (1 ^ ord(two)) + (2 ^ ord(three)) + (3 ^ ord(four)) + (4 ^ ord(five))
                    # print(answer)
                    if answer == correct_answer:
                        print('{}{}{}{}{} is correct'.format(one, two, three, four, five))
                        correct_keys.append('{}{}{}{}{}'.format(one, two, three, four, five))
                    # else:
                        # print('{}{}{}{}{} is incorrect'.format(one, two, three, four, five))
