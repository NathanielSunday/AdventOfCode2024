import re


def multiply(nums):
    return [a * b for a, b in nums]


def format_and_split(contents):
    # Remove unnecessary characters and format into numbers for calculation
    return [[int(num) for num in formula.strip('mul()').split(',')] for formula in contents]


def find_muls(string):
    return re.findall(r'mul\(\d{1,3},\d{1,3}\)', string)


def get_file_string(filename):
    return open(filename, 'r').read()


def get_dos(filename):
    # Grab all valid commands
    commands = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", get_file_string(filename))
    dos = []
    active = True

    # I was really hoping to figure out a better way to write this
    for command in commands:
        if command == "don't()":
            active = False
            continue
        if command == "do()":
            active = True
            continue
        if not active:
            continue
        dos.append(command)

    return dos


def get_contents(filename):
    # Find all references to anything that matches mul(num, num) to strip later
    return find_muls(get_file_string(filename))


def main():
    # Part One
    contents = get_contents('day3.input')
    contents = format_and_split(contents)
    print(sum(multiply(contents)))

    # Part Two
    contents = get_dos('day3.input')
    contents = format_and_split(contents)
    print(sum(multiply(contents)))


if __name__ == '__main__':
    main()
