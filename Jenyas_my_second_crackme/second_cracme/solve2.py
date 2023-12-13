import itertools
import multiprocessing



def generate_combinations_chunk(characters, length, chunk_size):
    return [''.join(combination) for combination in itertools.product(characters, repeat=length)][:chunk_size]

def process_combination(combination):
    # Replace this function with your actual processing logic
    v2 = 17
    v3 = 19
    v4 = 25
    for character in combination:
        i = ord(character)
        if i > 57:
            if i > 90:
                v4 -= i -97 + 1
            else:
                v3 -= i - 64
        else:
            v2 -= i - 47
    if v2 == 17 and v3 == 19 and v4 == 25:
        answers.append(combination)

def generate_combinations_and_process(characters, length, num_processes=4):
    chunk_size = 1000000  # Adjust the chunk size based on your needs
    total_combinations = 62 ** length

    processes = []

    chunks = [chunk_size] * (total_combinations // chunk_size)
    chunks[-1] = total_combinations % chunk_size

    for chunk in chunks:
        process = multiprocessing.Process(target=process_combination, args=(generate_combinations_chunk(characters, length, chunk),))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
length = 8
num_threads = 4

answers = []
generate_combinations_and_process(characters, length, num_threads)
    

for i in answers:
    print(i)