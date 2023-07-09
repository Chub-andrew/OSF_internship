def max_difference():
    numbers = input('Enter your numbers, separated by space:')
    list = numbers.split()
    ints = []
    for number in list:
        ints.append(int(number))

    print(ints)

    x = sorted(ints)
    x.reverse()

    difference = x[0] - x[-1]
    return(difference)
result = max_difference()
print(result)



