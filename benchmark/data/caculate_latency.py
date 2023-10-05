str_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

with open('compress_13b_4_32.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()

    s = 0

    for i in range(len(data)):
        if len(data[i] )> 9:
            if data[i][9] in str_list:
                print(float(data[i][9:]))
                s += float(data[i][9:])

    print(s)