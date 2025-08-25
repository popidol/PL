def gen_arr(n, m):
    arr = [1]
    cur = 1
    while True:
        next_index = (cur + m - 1) % n
        if next_index == 0:
            next_index = n
        cur = next_index
        if cur == 1:
            break
        arr.append(cur)
    return arr


a = gen_arr((int(input("n1: "))), (int(input("m1: "))))
b = gen_arr((int(input("n2: "))), (int(input("m3: "))))
print(list(a + b))
