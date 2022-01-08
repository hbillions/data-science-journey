def count(lst, value):
    cnt = 0
    for element in lst:
        if element == value:
            cnt = cnt + 1
    return cnt