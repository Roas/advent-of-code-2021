#!/usr/bin/python3

def main():
    lines = get_input()
    counter = compare_values(lines)
    print(counter)


def get_input():
    with open('input') as f:
        lines_raw = f.readlines()

    lines = []
    for line in lines_raw:
        lines.append(int(line))

    return lines


def compare_values(lines):
    counter = 0
    for i, line in enumerate(lines):
        if i == 0:
            continue
        if lines[i] > lines[i-1]:
            counter = counter + 1
    return counter


if __name__ == "__main__":
    main()
