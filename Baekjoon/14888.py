OPS = [
    lambda x, y : x + y,
    lambda x, y : x - y,
    lambda x, y : x * y,
    lambda x, y : int(x / y),
]


n = int(input())
nums = list(map(int, input().split()))
ops_count = list(map(int, input().split()))

maximum = -1_000_000_000
minimum = 1_000_000_000

def calc(nums_index, remaining_ops_count, result):
    if nums_index == n:
        global maximum, minimum
        maximum = max(maximum, result)
        minimum = min(minimum, result)
        return

    for i in range(4):
        if remaining_ops_count[i] > 0:
            new_result = OPS[i](result, nums[nums_index])
            remaining_ops_count[i] -= 1
            calc(nums_index + 1, remaining_ops_count, new_result)
            remaining_ops_count[i] += 1

calc(1, ops_count, nums[0])

print(maximum)
print(minimum)
