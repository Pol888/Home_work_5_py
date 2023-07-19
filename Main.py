# task_home_1
def file_info(path:str) -> tuple[str, int]:
    return path, path.split('\\')[-1], path.split('\\')[-1].split('.')[1]

print(file_info(r'C:\Users\pollove\AppData\Roaming\Zoom\bin\Zoom.exe'))

# task_home_2
a, b, c = ['Pol', 'Fox', 'Bill'], [10000, 5000, 3000], ['10.25%', '25.65%', '100%']

gen_3 = {i: j * float(k.split('%')[0]) for i, j, k in zip(a, b, c)}
print(*gen_3.items())

# task_home_3
def gen_4(n_fib):
    if n_fib == 1:
        yield 1
        return
    elif n_fib == 2:
        yield 1
        yield 1
        return
    yield 1
    yield 1
    a = 'str'
    b = 1
    c = 1
    for i in range(n_fib - 2):
        yield b + c
        a = b + c
        b = c
        c = a
print(*gen_4(10))