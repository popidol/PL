import sys

if len(sys.argv) != 2:
    print("Не все аргументы")
    sys.exit(1)

filename = sys.argv[1]

with open(filename, 'r') as file:
    nums = [int(line.strip()) for line in file if line.strip().isdigit()]
    nums.sort()
n = len(nums)
median = nums[n // 2]
total_moves = sum(abs(x - median) for x in nums)
if total_moves <= 20:
    print(total_moves)
else:
    print("Невозможно достичь за 20 ходов")
