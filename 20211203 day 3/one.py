#!/usr/bin/python3


INPUT_FILE = "input"


def main():
    input = get_input()
    processed_output = process_input(input)
    gamma_rate = determine_answer(processed_output, False)
    epsilon_rate = determine_answer(processed_output, True)
    print(int(gamma_rate, 2) * int(epsilon_rate, 2))


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


def process_input(input):
    output = []

    for column in range(len(input[0])):
        output.append([0, 0])

    for i, row in enumerate(input):
        for j, column in enumerate(row):
            output[j][column] = output[j][column] + 1

    return output


def determine_answer(processed_output, inverted):
    zero = "0"
    one = "1"
    if inverted:
        zero = "1"
        one = "0"

    final_answer = "0b"
    for column in processed_output:
        if column[0] > column[1]:
            final_answer = final_answer + zero
        else:
            final_answer = final_answer + one
    return final_answer


if __name__ == "__main__":
    main()
