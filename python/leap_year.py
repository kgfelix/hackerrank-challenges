

def is_leap(year):
    leap = False
    str_num = int(str(year)[-2:])
    print(str_num)
    if str_num != 0:
        last_digits = int(str_num)
        if last_digits % 4 == 0:
            leap = True
    elif year % 400 == 0:
        leap = True    
    return leap


if __name__ == '__main__':
    year = int(input())
    print(is_leap(year))
