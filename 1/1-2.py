import re
with open("input.txt") as f:
    num = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
           '6': 6, '7': 7, '8': 8, '9': 9, '0': 0,
           'one': 1, 'two': 2, 'three': 3, 'four': 4,
           'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
           'nine': 9, 'zero': 0}
    arr = [string.rstrip() for string in f]
    sum = 0

    for item in arr:
        first = None
        second = None

        best = None
        for key in num:
            if key in item:
                ind = item.index(key)
                if best is None:
                    best = ind
                    first = num[key]
                    continue

                if best > ind:
                    best = ind
                    first = num[key]

        last = None
        for key in num:
            if key in item:
                lind = item.rindex(key)
                if last is None:
                    last = lind
                    second = num[key]
                    continue

                if last < lind:
                    last = lind
                    second = num[key]

        val = first * 10 + second
        sum += val
        print(val)


    print(sum)

