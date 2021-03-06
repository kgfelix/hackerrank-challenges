

def my_print(n):
    seq = range(n)
    for i in seq:
        print(i+1, end='')


if __name__ == '__main__':
    a = int(input())
    my_print(a)
