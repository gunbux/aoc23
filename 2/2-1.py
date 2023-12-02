with open("input.txt") as f:
    rc = 12
    gc = 13
    bc = 14
    arr = [l.rstrip() for l in f]
    ## print(arr)

    for string in arr:
        log = string.split(":")[1].strip().split("; ")
        ## print(log)

        for line in log:
            line.split(", ")
            print(line)


