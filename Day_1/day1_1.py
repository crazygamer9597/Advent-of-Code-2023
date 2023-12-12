def calculate_part1(line):
    digits = [char for char in line.strip() if char.isdigit()]
    calib = int(digits[0] + digits[-1])
    return calib

def find_first_digit(striped_input):
    for i in range(len(striped_input)):
        if striped_input[i].isdigit():
            return striped_input[i]
        for word in digit_words:
            if striped_input[i:].startswith(word):
                return digit_words[word]

def find_last_digit(striped_input):
    for i in range(len(striped_input)-1, -1, -1):
        if striped_input[i].isdigit():
            return striped_input[i]
        for word in digit_words:
            if striped_input[i:].startswith(word):
                return digit_words[word]

def calculate_part2(line):
    first_digit = find_first_digit(line.strip())
    last_digit = find_last_digit(line.strip())
    calib = int(first_digit + last_digit)
    return calib

total_part1 = 0
total_part2 = 0

digit_words = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6',
               'seven': '7', 'eight': '8', 'nine': '9'}

with open('input1.txt', 'r') as file:
    for line in file.readlines():
        total_part1 += calculate_part1(line)
        total_part2 += calculate_part2(line)

print(total_part1)
print(total_part2)