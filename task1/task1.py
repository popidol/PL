import sys

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

if len(sys.argv) != 5:
    print("Не все аргументы")
    sys.exit(1)

n1 = int(sys.argv[1])
m1 = int(sys.argv[2])
n2 = int(sys.argv[3])
m2 = int(sys.argv[4])
    
a = gen_arr(n1, m1)
b = gen_arr(n2, m2)
    
result = ''.join(str(x) for x in a + b)
print(result)
    