with open('input.txt') as f:
    arr = [string.rstrip() for string in f]
    sum = 0

    for item in arr:
        first = -1
        second = -1
        for char in item:
            if char in "1234567890":
                if first == -1:
                    first = int(char)

                second = int(char)

        val = first * 10 + second
        sum += val
        print(val)


    print(sum)

