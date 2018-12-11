#!/usr/bin/env python

""" Advent of Code 2018 - Question 1

    Solution by John Tocher

"""

import os

INPUT_FILE = "aoc_q01_input.txt"

def solve_the_puzzle():
    """ Code for the Advent code qestion """
    input_file = os.path.join(INPUT_FILE)

    list_of_changes = list()
    with open(input_file, "r") as puzzle_input:
        for each_line in puzzle_input.readlines():
            number_to_add = int(each_line.strip())
            list_of_changes.append(number_to_add)

    print(f"Read {len(list_of_changes)} lines.")

    results_so_far = set()
    duplicate_found = False
    list_index = 0
    line_count = 0
    counter = 0
    while not duplicate_found:
        line_count += 1
        this_item = list_of_changes[list_index]
        counter += this_item
        if counter in results_so_far:
            print(f"We've hit {counter} twice after {line_count} lines")
            duplicate_found = True
        else:
            results_so_far.add(counter)
            #print(f"At line {line_count:04} number is {this_item:06} total is {counter} at index {list_index}")
        list_index = (list_index + 1) % len(list_of_changes)

if __name__ == "__main__":
    solve_the_puzzle()
