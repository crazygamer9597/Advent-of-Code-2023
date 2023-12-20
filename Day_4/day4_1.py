# https://adventofcode.com/2023/day/4
def part1(puzzle_input):
    lines = puzzle_input.splitlines()
    match = []
    for line in lines:
        split_data = line.strip().split('|') # Splitting Data based on | 
        first_set = set(split_data[0].strip().split()[2:]) # Our numbers
        second_set = set(split_data[1].strip().split()) # Winning Numbers
        match.append(len(first_set.intersection(second_set))) # Appending length of common elements between the sets
    points = [2 ** (ele - 1) if ele != 0 else 0 for ele in match] 
    return sum(points)

def part2(puzzle_input):
    lines = puzzle_input.splitlines()
    match = []
    cards = [1] * len(lines) #Initializing an list of 1's for each line of input data
    for line in lines:
        split_data = line.strip().split('|') # Splitting Data based on | 
        first_set = set(split_data[0].strip().split()[2:]) # Our numbers
        second_set = set(split_data[1].strip().split()) # Winning Numbers
        match.append(len(first_set.intersection(second_set))) # Appending length of common elements between the sets   
    for index, count in enumerate(match):
        for j in range(index + 1, index + 1 + count): 
            cards[j] += cards[index]
    return sum(cards)

with open("input4.txt", 'r') as file:
    puzzle_input = file.read()
print(part1(puzzle_input))
print(part2(puzzle_input))
