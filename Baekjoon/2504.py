def sum_pop_to(stack, bracket):
    sum = 0
    while True:
        if len(stack) == 0:
            return None
        elem = stack.pop()
        if isinstance(elem, str):
            if elem == bracket:
                return sum
            else:
                return None
        else:
            sum += elem


brackets = input()

def solve():
    stack = []

    for b in brackets:
        if b == '(' or b == '[':
            stack.append(b)
        else:
            sum_to = sum_pop_to(stack, '(' if b == ')' else '[')
            if sum_to is None:
                return 0
            elif sum_to == 0:
                sum_to = 1
            stack.append((2 if b == ')' else 3) * sum_to)

    ans = 0
    for e in stack:
        if isinstance(e, str):
            return 0
        else:
            ans += e
    return ans

print(solve())
