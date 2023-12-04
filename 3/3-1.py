def check_adj(graph, row, col):
    if graph[row][col] == ".":
        return False

    adj_map = [(row-1, col-1), (row-1, col), (row-1, col+1), (row, col-1), (row, col+1), (row+1, col-1), (row+1, col), (row+1, col+1)]

    for pair in adj_map:
        r = pair[0]
        c = pair[1]

        if not isValid(graph, r, c):
            continue

        if graph[r][c] in "@#$%&*+-&=/?":
            return True



def isValid(graph, row, col):
    if row < 0 or row >= len(graph):
        return False
    if col < 0 or col >= len(graph[0]):
        return False
    return True

def get_num(graph, row, col):
    # print("start is", col)
    left = col
    right = col + 1

    while isValid(graph, row, left - 1) and graph[row][left - 1] in "1234567890":
        left -= 1

    while isValid(graph, row, right) and graph[row][right] in "1234567890":
        right += 1

    ## print("left is " + str(left) + " and right is " + str(right))
    ## print(graph[row][left:right])
    val = int(graph[row][left:right])

    graph[row] = graph[row][:left] + "." * (right - left) + graph[row][right:]
    return val



with open("input.txt") as f:
    arr = [line.rstrip() for line in f]
    ## print(arr)
    sum = 0

    for rowie in range(len(arr)):
        for colie in range(len(arr[rowie])):
            if check_adj(arr, rowie, colie):
                sum += get_num(arr, rowie, colie)
                ## print(arr)

    print(sum)



