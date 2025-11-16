def count_words(filename):
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()
        return len(words)

word_count = count_words('sample.txt')
print(f"The file contains {word_count} words.")

def read_binary_file(filename):
    with open(filename, 'rb') as file:
        content = file.read()
        print("Binary content:", content)

read_binary_file('binary_sample.bin')

def append_to_binary_file(filename, data):
    with open(filename, 'ab') as file:
        file.write(data)

append_to_binary_file('binary_sample.bin', bytes([6, 7, 8, 9]))
print("Bytes appended to binary file.")
read_binary_file('binary_sample.bin')  # Verify the appended bytes
