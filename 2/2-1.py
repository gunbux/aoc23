def check_game(game):
    game_num = game.split(":")[0].split(" ")[1]
    log = game.split(":")[1].strip().split("; ")

    for line in log:
        action = line.split(", ")

        for act in action:
            temp = act.split(" ")
            numbar = int(temp[0])
            color = temp[1]
            # print(color)
            # print(numbar)
            if "red" in color and numbar > rc:
                return 0

            if "green" in color and numbar > gc:
                return 0

            if "blue" in color and numbar > bc:
                return 0

    return int(game_num)


with open("input.txt") as f:
    arr = [l.rstrip() for l in f]
    sum = 0
    ## print(arr)

    for game in arr:
        sum += check_game(game)


    print(sum)
