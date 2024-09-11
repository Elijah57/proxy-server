with open('req.txt', "r+") as file:
    lines = file.readlines()

    for line in lines:
        nline = line.rstrip("\n")
        print(nline.rstrip(","))
    processed_lines = [line.rstrip("\n").rstrip(",") + "\n" for line in lines]

    file.seek(0)
    file.writelines(processed_lines)

    file.truncate()
    file.close()

