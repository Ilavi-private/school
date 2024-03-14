from middleware import taskify

taskify.config(timer=True)


@taskify.task
def task1():
    counter = 0

    with open("../text_files/24-191.txt", 'r') as file:
        data = file.readline()

    data = data.split('A')

    for sym in data:
        if 'B' not in sym and len(sym) + 2 >= 17:
            counter += 1

    print(f"{counter = }")


@taskify.task
def task2():
    counter = 0

    with open("../text_files/24-191.txt", 'r') as file:
        data = file.readline()

    data = data.split('A')

    for sym in data:
        sym = sym.split('B')

        for line in sym:
            if len(line) >= 20:
                counter += 1

    print(f"{counter = }")


@taskify.task
def task3():
    counter = 0
    max_count = 0

    with open("../text_files/24-213.txt", 'r') as file:
        data = file.readline()

    i = 0

    while i <= len(data):
        if data[i-3: i] == 'NPO' or data[i-3: i] == 'PNO':
            counter += 1
            i += 3
        else:
            max_count = max(max_count, counter)
            counter = 0
            i += 1

    print(max_count)


@taskify.task
def task4():
    counter = 0
    max_count = 0

    with open("../text_files/24-213.txt", 'r') as file:
        data = file.readline()

    i = 0

    while i < len(data) - 1:
        if data[i] != 'O' or data[i+1] == 'O':
            counter += 1
            i += 2
        else:
            max_count = max(max_count, counter)
            counter = 0
            i += 1

    print(max_count)

@taskify.task
def task5():
    counter = 0
    max_count = 0

    with open("../text_files/24.txt", 'r') as file:
        data = file.readline()

    for i in range(1, len(data) - 1):
        if (data[i-1] in ['A', 'B', 'C']) and (data[i] not in ['A', 'B', 'C']) or data[i-1] not in ['A', 'B', 'C']:
            counter += 1
            max_count = max(max_count, counter)
        else:
            counter = 1

    print(max_count)


@taskify.task
def task6():
    max_count = 0

    with open("../text_files/24-173.txt", 'r') as file:
        data = file.readline()

    prev = ''
    sammw_count = 0

    for i in range(0, len(data) - 4, 3):
        if prev == data[i:i + 3]:
            sammw_count = 1
        else:
            max_count = max(sammw_count, max_count)
            sammw_count += 1
        prev = data[i:i + 3]

    print(max_count)


@taskify.task
def task7():
    max_count = 0

    with open("../text_files/171.txt", 'r') as file:
        data = file.readlines()

    sammw_count = 0
    big_count = 0
    i = 0

    for line in data:
        while i < len(line) - 1:
            if line[i:i + 3] == 'XYZ':
                sammw_count += 3
                max_count = max(sammw_count, max_count)
                i += 3
            else:
                sammw_count = 0
                i += 1
        big_count = max(big_count, max_count)

    print(big_count)


@taskify.task
def task7():
    max_count = 0

    with open("../text_files/171.txt", 'r') as file:
        data = file.readlines()

    sammw_count = 0
    big_count = 0
    i = 0

    for line in data:
        while i < len(line) - 1:
            if line[i:i + 3] == 'XYZ':
                sammw_count += 3
                max_count = max(sammw_count, max_count)
                i += 3
            else:
                sammw_count = 0
                i += 1
        big_count = max(big_count, max_count)

    print(big_count)