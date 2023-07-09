def find_second_largest():
    numbers = [5, 2, 7, 3, 9, 1]
    x = sorted(numbers)
    x.reverse()
    print(x)
    return("The second largest number from this list is:"+f"{x[1]}")

result = find_second_largest()
print(result) 