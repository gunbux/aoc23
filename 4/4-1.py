with open('input.txt') as f:
    total = 0
    arr = [line.strip() for line in f]

    # Transformation 1: Remove The initial stuff
    arr = [line.split(': ')[1] for line in arr]

    # Trans 2: Split the two sections
    arr = [line.split(' | ') for line in arr]

    # print(arr)

    # Do computation

    for line in arr:
        points = 1
        keystring = line[0]
        valstring = line[1]

        keys = keystring.split(' ')
        # print(keys)

        keymap = {}

        for key in keys:
            if len(key) > 0:
                keymap[int(key)] = 1

        # print(keymap)

        vals = valstring.split(' ')
        for val in vals:
            if len(val) <= 0:
                continue

            if int(val) in keymap:
                points = points << 1
                # print("points updated", points)

        points = points >> 1
        total += points

    print(total)

