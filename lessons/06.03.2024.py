from re import findall

from middleware import taskify


# taskify.config(timer=True)


@taskify.task
def task1_1():
    with open("Files/2024.03.04 - 24-181.txt", 'r') as file:
        data = file.readline()
    data = data.split('Y')
    max_len = 0
    for seq in data:
        if seq.count('.') <= 5:
            max_len = max(max_len, len(seq))
        else:
            dot_ids = [0] + [x for x in range(len(seq)) if seq[x] == '.'] + [len(seq)]
            for j in range(len(dot_ids) - 6):
                if dot_ids[j] == 0:
                    max_len = max(max_len, dot_ids[j + 6] - dot_ids[j])
                else:
                    max_len = max(max_len, dot_ids[j + 6] - dot_ids[j] - 1)
    print(f"{max_len = }")


@taskify.task
def task1_2():
    with open("Files/2024.03.04 - 24-181.txt", 'r') as file:
        data = file.readline()
    left = 0
    count_dot = 0
    max_len = 0
    for right in range(len(data)):
        if data[right] == 'Y':
            left = right + 1
            count_dot = 0
            max_len = max(max_len, right - left)
        if data[right] == '.':
            count_dot += 1
        while count_dot > 5:
            if data[left] == '.':
                count_dot -= 1
            max_len = max(max_len, right - left)
            left += 1
    print(f"{max_len = }")


@taskify.task
def task2():
    with open("Files/2024.03.04 - 24-181.txt", 'r') as file:
        data = file.readline()
    letters = ['A', 'E', 'I', 'O', 'U', 'Y']
    letters_count = 0
    left = 0
    max_len = 0
    for right in range(len(data)):
        if data[right] in letters:
            letters_count += 1
        if letters_count <= 7:
            max_len = max(max_len, right - left + 1)
        while letters_count > 7:
            if data[left] in letters:
                letters_count -= 1
            left += 1
        if data[right] == '.':
            left = right + 1
            letters_count = 0
    print(f"{max_len = }")


# CORRECT
@taskify.task
def task3():
    with open("Files/2024.03.04 - 24-181.txt", 'r') as file:
        data = file.readline()
    left = 0
    a_count = 0
    max_len = 0
    for right in range(len(data)):
        if data[right] == '.':
            left = right + 1
            a_count = 0
        if data[right] == 'A':
            a_count += 1
        if a_count >= 3:
            max_len = max(max_len, right - left + 1)
    print(f"{max_len = }")


# CORRECT
@taskify.task
def task4():
    with open("Files/2024.03.04 - 24-181.txt", 'r') as file:
        data = file.readline()
    letters = ['A', 'E', 'I', 'O', 'U', 'Y']
    left = 0
    dot_count = 0
    max_len = 0
    for right in range(len(data)):
        if data[right] in letters:
            left = right + 1
            dot_count = 0
        if data[right] == '.':
            dot_count += 1
        if dot_count >= 6:
            max_len = max(max_len, right - left + 1)
    print(f"{max_len = }")


# CORRECT
@taskify.task
def task5():
    with open("Files/2024.03.06 - 24-222.txt", 'r') as file:
        data = file.readline()
    matches = findall(r"A([BCDEF]+)A\1A\1A", data)
    print("max_len = %d" % (len(max(matches, key=len))*3 + 4))


taskify.run()