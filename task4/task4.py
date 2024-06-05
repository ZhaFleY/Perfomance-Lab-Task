import sys

def read_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers

def find_median(nums):
    nums.sort()
    length = len(nums)
    if length % 2 == 0:
        median = (nums[length // 2 - 1] + nums[length // 2]) / 2
    else:
        median = nums[length // 2]
    return median

def calculate_min_moves(nums, median):
    return int(sum(abs(num - median) for num in nums))

def main(file_path):
    nums = read_numbers_from_file(file_path)
    median = find_median(nums)
    min_moves = calculate_min_moves(nums, median)
    print(min_moves)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)
