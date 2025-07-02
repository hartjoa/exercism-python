def egg_count(display_value):
    remaining = display_value
    i = 0
    result = 0
    while remaining > 0:
        result += display_value % (2 ** (i + 1)) // 2 ** i
        remaining -= display_value % (2 ** (i + 1))
        i += 1
    return result



print(egg_count(89))           # 4
print(egg_count(16))           # 1
print(egg_count(0))            # 0
print(egg_count(2000000000))   # 13   


#89 : 01011001