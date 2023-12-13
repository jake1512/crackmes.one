import itertools
import multiprocessing
import os

# Define the character array
char_array = [chr(i) for i in range(48, 58)] + [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]

# Define the combination length
comb_length = 8

# Define the chunk size for each file
chunk_size = 1000000

def worker(chunk):
    # Define the filename for this chunk
    filename = f"combinations_{chunk}.txt"

    # Open the file
    with open(filename, "w") as f:
        # Generate the combinations for this chunk
        for i in range(chunk * chunk_size, (chunk + 1) * chunk_size):
            # Convert the integer to a combination
            combination = ""
            for _ in range(comb_length):
                i, index = divmod(i, len(char_array))
                combination = char_array[index] + combination

            # Write the combination to the file
            f.write(combination + "\n")

# Calculate the total number of combinations
total_combinations = len(char_array) ** comb_length

# Calculate the total number of chunks
total_chunks = (total_combinations + chunk_size - 1) // chunk_size

# Create a pool of workers
with multiprocessing.Pool() as pool:
    # Map the worker function to the chunks
    pool.map(worker, range(total_chunks))
