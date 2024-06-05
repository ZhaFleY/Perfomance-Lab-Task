import sys


def circular_array_path(n, m):
    result = []
    array = list(range(1, n + 1))
    current_index = 0

    while True:
        result.append(array[current_index])
        current_index = (current_index + m) % n
        if current_index == 0:
            break

    return ''.join(map(str, result))


if __name__ == "__main__":

    if len(sys.argv) != 3:
        sys.exit(1)

    n = int(sys.argv[1])
    m = int(sys.argv[2])

    path = circular_array_path(n, m)
    print(path)
