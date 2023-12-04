def check_adj(graph, row, col):
    if graph[row][col] != "*":
        return 0

    count = 0
    adj_map = [(row-1, col-1), (row-1, col), (row-1, col+1), (row, col-1), (row, col+1), (row+1, col-1), (row+1, col), (row+1, col+1)]
    rows = [row-1, row+1]
    cols = [col-1, col+1]

    for r in rows:
        count += count_num(graph, r, col)

    for c in cols:
        if graph[row][c] in "1234567890":
            count += 1

    if count != 2:
        return 0

    nums = set()
    result = 1

    for r, c in adj_map:
        if not isValid(graph, r, c):
            continue

        if graph[r][c] not in "1234567890":
            continue

        nums.add(get_num(graph, r, c))

    for number in nums:
        result *= number

    if len(nums) == 1:
        result *= result

    return result


def count_num(graph, row, col):
    first = graph[row][col - 1] if isValid(graph, row, col - 1) else "."
    second = graph[row][col] if isValid(graph, row, col) else "."
    third = graph[row][col + 1] if isValid(graph, row, col + 1) else "."

    if first in "1234567890" and second in "1234567890" and third in "1234567890":
        return 1

    if first in "1234567890" and second in "1234567890" and third not in "1234567890":
        return 1

    if first in "1234567890" and second not in "1234567890" and third in "1234567890":
        return 2

    if first in "1234567890" and second not in "1234567890" and third not in "1234567890":
        return 1

    if first not in "1234567890" and second in "1234567890" and third in "1234567890":
        return 1

    if first not in "1234567890" and second in "1234567890" and third not in "1234567890":
        return 1

    if first not in "1234567890" and second not in "1234567890" and third in "1234567890":
        return 1

    if first not in "1234567890" and second not in "1234567890" and third not in "1234567890":
        return 0


def isValid(graph, row, col):
    if row < 0 or row >= len(graph):
        return False
    if col < 0 or col >= len(graph[0]):
        return False
    return True

def get_num(graph, row, col):
    ## print("start is", col)
    left = col
    right = col + 1

    while isValid(graph, row, left - 1) and graph[row][left - 1] in "1234567890":
        left -= 1

    while isValid(graph, row, right) and graph[row][right] in "1234567890":
        right += 1

    ## print("left is " + str(left) + " and right is " + str(right))
    ## print(graph[row][left:right])
    val = int(graph[row][left:right])

    # graph[row] = graph[row][:left] + "." * (right - left) + graph[row][right:]
    return val



with open("input.txt") as f:
    arr = [line.rstrip() for line in f]
    result = 0
    ## print(arr)

    for rowie in range(len(arr)):
        for colie in range(len(arr[rowie])):
            result += check_adj(arr, rowie, colie)

    print(result)





