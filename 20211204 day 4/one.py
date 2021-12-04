#!/usr/bin/python3

INPUT_FILE = "input"


def main():
    numbers, bingocards = get_input()
    bingocard, pulled = calculate_winning_card(numbers, bingocards)
    print(calculate_aoc_answer(bingocard, pulled))


def get_input():
    with open(INPUT_FILE) as f:
        input_raw = f.readlines()

    numbers = input_raw[0].split("\n")[0].split(",")

    # Remove the pulled numbers from the file
    input_without_pulled = input_raw[2:]

    n_bingocard = 0
    bingocards = [[]]
    for i, row in enumerate(input_without_pulled):
        if row == '\n':
            n_bingocard = n_bingocard + 1
            bingocards.append([])
            continue
        bingocards[n_bingocard].append([])
        for val in row.split('\n')[0].split():
            bingocards[n_bingocard][i%6].append([val, 0])

    return numbers, bingocards


def calculate_winning_card(pulled_numbers, bingocards):
    for pulled in pulled_numbers:
        for bingocard in bingocards:
            for row in bingocard:
                for number in row:
                    if number[0] == pulled:
                        number[1] = 1
            if check_bingo(bingocard):
                return bingocard, pulled


def pretty_bingocard(bingocard):
    for row in bingocard:
        for column in row:
            print(str(column[1]) + ":" + column[0], end='')
            if len(column[0]) == 2:
                print(" ", end='')
            else:
                print("  ", end='')
        print()
    print()


def calculate_aoc_answer(bingocard, last_pulled):
    sum_unmarked_numbers = 0
    for row in bingocard:
        for column in row:
            if column[1] == 0:
                sum_unmarked_numbers = sum_unmarked_numbers + int(column[0])
    return sum_unmarked_numbers * int(last_pulled)


def check_bingo(bingocard):
    for row in bingocard:
        wins_in_row = 0
        for number in row:
            wins_in_row = wins_in_row + number[1]
        if wins_in_row >= 5:
            return True

    for column in range(len(bingocard)):
        wins_in_column = 0
        for row in range(len(bingocard[0])):
            wins_in_column = wins_in_column + bingocard[row][column][1]
        if wins_in_column >= 5:
            return True

    return False

if __name__ == "__main__":
    main()
