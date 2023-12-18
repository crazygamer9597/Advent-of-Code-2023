import re

with open('input3.txt', 'r') as file:
    puzzle_input = file.read()

def part1(puzzle_input):
    lines = puzzle_input.split('\n')
    symbol = r'[^.\d]'  # except period and digits
    symbol_adjacent = []  # Initialize empty list
    for i, line in enumerate(lines):
        for match in re.finditer(symbol, line):
            j = match.start()  # Assign starting value to variable j
            for r in range(i - 1, i + 2): #Loops through rows surrounding current row, prev row and the row below
                for c in range(j - 1, j + 2): #Loops through columns surrounding current column and to its right & left columns
                    if 0 <= r < len(lines) and 0 <= c < len(lines[r]):
                        symbol_adjacent.append((r, c))  # Add valid coordinates to a list

    number = r'\d+' # Find the entire digit and not just the trailing digit
    part_num_sum = 0 #Initializing variable
    for i, line in enumerate(lines):
        for match in re.finditer(number, line): #Loops through items matching the expression
            if any((i, j) in symbol_adjacent for j in range(*match.span())): #if digit is adjacent to a symbol unpack the tuple to separate values
                part_num_sum += int(match.group()) #retreives matched string and converts to int and adds it
    return part_num_sum


def part2(puzzle_input):
    lines = puzzle_input.split('\n')
    gear_regex = r'\*' # Expression to match a * literal
    gears = dict() #Initialize empty dictionary
    for i, line in enumerate(lines):
        for match in re.finditer(gear_regex, line): #Search for match in input 
            gears[(i, match.start())] = [] #Initialize empty list as keys for the Dictionary where the tuple represents coords where * is found

    number = r'\d+'
    for i, line in enumerate(lines):
        for match in re.finditer(number, line):
            for r in range(i-1, i+2): #Prev row to the trailing row
                for c in range(match.start()-1, match.end()+1): #Previous column to the trailing column
                    if (r, c) in gears:
                        gears[(r, c)].append(int(match.group())) # Appending into Dictionary

    gear_ratio_sum = 0
    for nums in gears.values(): #nums is an iterator variable which contains values of gears dictionary
        if len(nums) == 2: 
            gear_ratio_sum += nums[0] * nums[1] # Increments gear ratio sum by the value of product of 2 values
    return gear_ratio_sum

print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))