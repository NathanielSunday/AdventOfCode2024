def get_dampened_safe_count(contents):
    # count = 0
    # for row in contents:
    #     for i in range(len(row)):
    #         if is_safe(row[:i] + row[i + 1:]):
    #             count += 1
    #             break
    #
    # return count

    # One true if any 'is_safe' call returns true while remove any one value from the data
    return sum(any([is_safe(row[:i] + row[i + 1:]) for i in range(len(row))]) for row in contents)


def get_safe_count(contents):
    return sum(is_safe(row) for row in contents)


def is_safe(row):
    # Subset check to see if diff contains safe distances in either direction, but not both
    diff = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    return set(diff) <= {1, 2, 3} or set(diff) <= {-1, -2, -3}


# Returns a list of lists
def get_contents(filename):
    # Using list comprehension, read the file using its iterator
    # then read each num with ' ' delimiter and cast as a num
    return [[int(num) for num in row.split(' ')] for row in open(filename)]


def main():
    contents = get_contents('day2.input')

    # Part One
    print(get_safe_count(contents))

    # Part Two
    print(get_dampened_safe_count(contents))


if __name__ == '__main__':
    main()
