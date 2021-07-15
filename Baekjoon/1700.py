def get_elem_max_first(lst, start, elems):
    max_first, elem_max_first = -1, None
    for elem in elems:
        try:
            first = lst.index(elem, start)
        except ValueError:
            return elem
        if first > max_first:
            max_first, elem_max_first = first, elem
    return elem_max_first


n, k = map(int, input().split())
uses = list(map(int, input().split()))

in_use = set()
num_remove = 0
for i in range(k):
    if uses[i] in in_use:
        continue

    if len(in_use) < n:
        in_use.add(uses[i])
    else:
        elem_max_first = get_elem_max_first(uses, i + 1, in_use)
        in_use.remove(elem_max_first)
        num_remove += 1
        in_use.add(uses[i])

print(num_remove)
