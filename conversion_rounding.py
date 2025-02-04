def round_ans(val):
    """
    rounds temperatures to nearest degree
    :param val:  number to be rounded
    :return: Number rounded to nearest degree
    """

    var_rounded = (val * 2 +1) // 2
    return "{:.0f}".format(var_rounded)


def to_celsius(to_convert):
    """
    Converts from Fahrenheit ot Celsius
    :param to_convert: Temperature to be converted in f
    :return: Converted temperature in Celsius
    """
    answer = (to_convert - 32) * 5 /9
    return round_ans(answer)


def to_fahrenheit(to_convert):
    """
    Converts from c to f
    :param to_convert: temperature to be converted in c
    :return: converted temperature in f
    """
    answer = to_convert *1.8 +32
    return round_ans(answer)


# Main Routine / Testing starts here
to_c_test = [0, 100, -459]
to_f_test = [0, 100, 40, -273]

for item in to_f_test:
    ans = to_fahrenheit(item)
    print(f"{item} c is {ans}f")

print()

for item in to_c_test:
    ans = to_celsius(item)
    print(f"{item} f is {ans}c")

print()