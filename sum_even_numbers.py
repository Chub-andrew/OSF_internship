def sum_even_numbers():
    numbers = input('Enter your numbers, separated by space:')
    list = numbers.split()
    ints = []
    for number in list:
        only_numbers = int(number)
        if only_numbers % 2 ==0:
            ints.append(only_numbers)

    return(sum(ints))

result = sum_even_numbers()
print('The sum of the numbers that are divisible by 2 is equal:' + f"{result}")
