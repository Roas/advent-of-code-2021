#!/usr/bin/python3


INPUT_FILE = "input"


def main():
    input = get_input()
    oxigen = calculate_oxigen(input)
    co2 = calculate_co2(input)
    print(binary_to_int(oxigen) * binary_to_int(co2))
    # oxigen_generator = determine_answer(processed_output, input, False)
    # co2_scrubber = determine_answer(processed_output, input, True)
    # print(int(gamma_rate, 2) * int(epsilon_rate, 2))


def get_input():
    with open(INPUT_FILE) as f:
        input_raw = f.readlines()

    input = []
    for line_raw in input_raw:
        line = []
        for character in line_raw:
            if character == "\n":
                continue
            line.append(int(character))
        input.append(line)
    return input


def calculate_oxigen(input):
    for i, column in enumerate(range(len(input[0]))):
        most_common_char = calculate_most_common_char_in_input(input, i)
        input = remove_entries_from_input(input, i, most_common_char)
        if len(input) == 1:
            break
    return input[0]


def calculate_co2(input):
    for i, column in enumerate(range(len(input[0]))):
        most_common_char = calculate_least_common_char_in_input(input, i)
        input = remove_entries_from_input(input, i, most_common_char)
        if len(input) == 1:
            break
    return input[0]


def calculate_most_common_char_in_input(input, filter_column):
    zeros = 0
    ones = 0
    for row in input:
        for i, column in enumerate(row):
            if i == filter_column:
                if column == 0:
                    zeros = zeros + 1
                if column == 1:
                    ones = ones + 1
    if zeros > ones:
        return 0
    else:
        return 1


def calculate_least_common_char_in_input(input, filter_column):
    zeros = 0
    ones = 0
    for row in input:
        for i, column in enumerate(row):
            if i == filter_column:
                if column == 0:
                    zeros = zeros + 1
                if column == 1:
                    ones = ones + 1
    if zeros <= ones:
        return 0
    else:
        return 1


def binary_to_int(binary):
    binary_string = '0b'
    for char in binary:
        binary_string = binary_string + str(char)
    return int(binary_string, 2)


def remove_entries_from_input(input, filter_column, filter_bit):
    new_input = []
    for row in input:
        for i, column in enumerate(row):
            if i == filter_column:
                if column == filter_bit:
                    new_input.append(row)
    return new_input


if __name__ == "__main__":
    main()
