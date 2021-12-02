#!/usr/bin/python3

def main():
    directions = get_input()
    horpos, depth = follow_directions(directions)
    print(horpos * depth)


def get_input():
    with open('input') as f:
        directions_raw = f.readlines()

    directions = []
    for direction in directions_raw:
        directions.append([direction.split()[0], int(direction.split()[1])])

    return directions


def follow_directions(directions):
    horpos = 0
    depth = 0
    aim = 0
    for direction in directions:
        if direction[0] == "forward":
            horpos = horpos + direction[1]
            depth = depth + (aim * direction[1])
        elif direction[0] == "down":
            aim = aim + direction[1]
        elif direction[0] == "up":
            aim = aim - direction[1]
    return horpos, depth


if __name__ == "__main__":
    main()
