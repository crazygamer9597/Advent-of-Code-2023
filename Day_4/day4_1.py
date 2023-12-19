# https://adventofcode.com/2023/day/4

def part1(puzzle_input):
    lines = puzzle_input.splitlines()
    counts = []
    for line in lines:
        split_data = line.strip().split('|') # Splitting Data based on | 
        first_set = set(split_data[0].strip().split()[2:]) # Our numbers
        second_set = set(split_data[1].strip().split()) # Winning Numbers
        counts.append(len(first_set.intersection(second_set))) # Appending length of common elements between the sets
    new_list = [2 ** (ele - 1) if ele != 0 else 0 for ele in counts] 
    return sum(new_list)

with open("input4_2.txt", 'r') as file:
    puzzle_input = file.read()

print(part1(puzzle_input))