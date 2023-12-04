with open('input.txt') as f:
    total = 0
    arr = [line.strip() for line in f]

    # Transformation 1: Remove The initial stuff
    arr = [line.split(': ')[1] for line in arr]

    # Trans 2: Split the two sections
    arr = [line.split(' | ') for line in arr]

    # print(arr)

    # Do computation
    cardmap = {}

    # Populate the cardmap
    for index in range(len(arr)):
        cardmap[index] = 1

    # print(cardmap)

    for index in range(len(arr)):
        count = 0
        keystring = arr[index][0]
        valstring = arr[index][1]

        keys = keystring.split(' ')

        keymap = {}

        for key in keys:
            if len(key) > 0:
                keymap[int(key)] = 1

        vals = valstring.split(' ')
        for val in vals:
            if len(val) <= 0:
                continue

            if int(val) in keymap:
                count += 1

        # print("card index: " + str(index) + " count: " + str(count))

        for i in range(1, count + 1):
            cardmap[index + i] += cardmap[index]


    print(cardmap)
    sum = 0

    for v in cardmap.values():
        sum += v

    print(sum)

