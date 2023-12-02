def check_game(game):
    rb = 0
    gb = 0
    bb = 0

    game_num = game.split(":")[0].split(" ")[1]
    log = game.split(":")[1].strip().split("; ")

    for line in log:
        action = line.split(", ")

        for act in action:
            temp = act.split(" ")
            numbar = int(temp[0])
            color = temp[1]

            if "red" in color:
                rb = max(rb, numbar)

            if "green" in color:
                gb = max(gb, numbar)

            if "blue" in color:
                bb = max(bb, numbar)

    return rb * gb * bb


with open("input.txt") as f:
    arr = [l.rstrip() for l in f]
    sum = 0
    ## print(arr)

    for game in arr:
        sum += check_game(game)


    print(sum)
