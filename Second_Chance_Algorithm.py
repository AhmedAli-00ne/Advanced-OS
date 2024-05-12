def Second_Chance(reference_string, frames):
    page_faults = 0
    pointer = 0
    page_table = [-1] * frames
    second_chance = [False] * frames
    reference_pages = reference_string
    history = []

    for page in reference_pages:
        if page not in page_table:
            if -1 in page_table:
                page_table[pointer] = page
                pointer = (pointer + 1) % frames
            else:
                while True:
                    if second_chance[pointer]:
                        second_chance[pointer] = False
                        pointer = (pointer + 1) % frames
                    else:
                        page_table[pointer] = page
                        pointer = (pointer + 1) % frames
                        break
            page_faults += 1
        else:
            second_chance[page_table.index(page)] = True

        print("Page Table:", page_table)
        history.append(page_table.copy())

    print("Total page faults:", page_faults)
    return history, page_faults


frames = 3
print(Second_Chance([10,20,30,50], frames))
