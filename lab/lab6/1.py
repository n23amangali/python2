def multiple(list):
    sum = 1
    for i in list:
        sum*=i
    return sum

numbers = [1, 2, 3, 4]
result = multiple(numbers)

print (result)
