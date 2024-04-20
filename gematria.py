def mispar_gadol(letter):
    if letter == "א":
        return 1
    elif letter == "ב":
        return 2
    elif letter == "ג":
        return 3
    elif letter == "ד":
        return 4
    elif letter == "ה":
        return 5
    elif letter == "ו":
        return 6
    elif letter == "ז":
        return 7
    elif letter == "ח":
        return 8
    elif letter == "ט":
        return 9
    elif letter == "י":
        return 10
    elif letter == "כ" or letter == "ך":
        return 20
    elif letter == "ל":
        return 30
    elif letter == "מ" or letter == "ם":
        return 40
    elif letter == "נ" or letter == "ן":
        return 50
    elif letter == "ס":
        return 60
    elif letter == "ע":
        return 70
    elif letter == "פ" or letter == "ף":
        return 80
    elif letter == "צ" or letter == "ץ":
        return 90
    elif letter == "ק":
        return 100
    elif letter == "ר":
        return 200
    elif letter == "ש":
        return 300
    elif letter == "ת":
        return 400
    else:
        return 0.0
while True:
    word = input("Insert word without nikkud: ")
    total = 0
    for i in range(len(word)):
        print("total: ",total,"+",mispar_gadol(word[i]))

        total += mispar_gadol(word[i])

    print("Total for", word ,": ",total)
