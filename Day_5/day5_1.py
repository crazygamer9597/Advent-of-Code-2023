#https://adventofcode.com/2023/day/5
import re

def part1(puzzle_input):
    segments = puzzle_input.split('\n\n') #Split and store in segments list
    seeds = re.findall(r'\d+', segments[0]) #Store in seeds list
    min_location = float('inf') #Initializing min location to very large value
    for x in map(int, seeds): #Iterates through each seed, converted to int
        for seg in segments[1:]: #Iterates through segments excluding seeds
            for conversion in re.findall(r'(\d+) (\d+) (\d+)', seg): #Finding sets of 3 numbers in each segment using regular expression
                destination, start, delta = map(int, conversion) #Assign the values from before to the following names
                if x in range(start, start + delta): #Checks if within range
                    x += destination - start #If within range modifies values
                    break
        min_location = min(x, min_location) #updating min location
    return min_location #Returns smallest value found in min location after following the prev rules

with open('input5_1.txt', 'r') as file:
    puzzle_input = file.read()
print('Part 1:', part1(puzzle_input))