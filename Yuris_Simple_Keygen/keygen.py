import random
import os

candidates = []

for i in range(0, 9):
    tmp = [i, i + 1]
    candidates.append(tmp)

result = ''
while len(result) < 16:
    candidate = random.randint(0, len(candidates) - 1)
    result = result + str(candidates[candidate][0]) + str(candidates[candidate][1])
command = '/home/kali/SimpleKeyGen ' + result
print(command)
os.system(command)