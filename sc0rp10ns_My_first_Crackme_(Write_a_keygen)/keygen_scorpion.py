import math
import random
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

primes = [
    193, 197, 199, 211, 223, 227, 229, 233, 239, 241,
    251, 257, 263, 269, 271, 277, 281, 283, 293, 307,
    311, 313, 317, 331, 337, 347, 349, 353, 359, 367,
    373, 379, 383, 389, 397, 401, 409, 419, 421, 431,
    433, 439, 443, 449, 457, 461, 463, 467, 479, 487
        ]

blocks = []
def generate_blocks():
    for prime in primes:
        for one in characters:
            for two in characters:
                for three in characters:
                    s = ord(one) + ord(two) + ord(three)
                    four = prime - s
                    if four < 48 or four > 122 or chr(four) not in characters:
                        continue
                    else:
                        blocks.append('{}{}{}{}'.format(one, two, three, chr(four)))

def sum_block(block):
    sum = 0
    for char in block:
        sum += ord(char)
    return sum

generate_blocks()


key_count = 0
while key_count < 10:
    startSeed = random.randint(0, len(blocks))
    for one in blocks[startSeed:]:
        for two in blocks[(startSeed + 1):]:
            if sum_block(one) < sum_block(two):
                for three in blocks[(startSeed + 2):]:
                    if sum_block(two) < sum_block(three):
                        for four in blocks[(startSeed + 3):]:
                            if sum_block(three) < sum_block(four):
                                print('{}-{}-{}-{}'.format(one, two, three, four))
                                break
                        break
                break
        break
    key_count += 1

# print('{}-{}-{}-{}'.format(blocks[0], blocks[1], blocks[2], blocks[3]))
