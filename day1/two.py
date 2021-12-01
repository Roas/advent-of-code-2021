#!/usr/bin/python3

def main():
    lines = get_input()
    counter = check_lines(lines)
    print(counter)


def get_input():
    with open('input') as f:
        lines_raw = f.readlines()

    lines = []
    for line in lines_raw:
        lines.append(int(line))

    return lines


def check_lines(lines):
    counter = 0
    for i, line in enumerate(lines):
        if i + 3 == len(lines):
            break
        if lines[i] + lines[i+1] + lines[i+2] < lines[i+1] + lines[i+2] + lines[i+3]:
            counter = counter + 1
    return counter


if __name__ == "__main__":
    main()
