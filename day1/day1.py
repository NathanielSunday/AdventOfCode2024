def get_frequency(left, right):
    frequency = []
    for left_num in left:
        count = 0
        for right_num in right:
            if left_num == right_num:
                count += 1
        frequency.append(left_num * count)
    return frequency


def get_distances(left, right):
    distances = []
    for i in range(len(left)):
        distances.append(abs(left[i] - right[i]))
    return distances


def get_contents(filepath):
    left, right = [], []
    file = open(filepath, 'r')
    for line in file.readlines():
        line = line.replace('\n', '').split('   ')
        left.append(int(line[0]))
        right.append(int(line[1]))
    return left, right

def main():
    left, right = get_contents('day1.input')
    left.sort()
    right.sort()

    # Part 1
    distance_list = get_distances(left, right)

    print(sum(distance_list))

    # Part 2
    frequency_list = get_frequency(left, right)

    print(sum(frequency_list))


if __name__ == '__main__':
    main()