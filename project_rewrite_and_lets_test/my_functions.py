def min(digit_a, digit_b):
    if digit_a < digit_b:
        return digit_a
    return digit_a

def max(list_of_numbers):
    max_number = list_of_numbers[0]
    for number in list_of_numbers:
        if number > max_number:
            max_number = number
    return max_number

def len(list_of_things):
    sum = 0
    for x in list_of_things:
        sum += 1
    return sum

def pow(digit_a, digit_b):
    result = 1
    for x in range(digit_b):
        result *= digit_a
    return result

def divmod(digit_a, digit_b):
    result = str(digit_a / digit_b).split('.')
    return result[0], digit_a - (int(result[0]) * digit_b)


if __name__ == '__main__':
    a = int(input('Enter number: '))
    b = int(input('Enter number: '))
    print(min(a, b))
    my_list = [19, 72, 0, -89, 78, 3, 6]
    print(max(my_list))
    print(len(my_list))
    print(pow(a, b))
    print(a ** b)
    print(divmod(a, b))
    print(a // b, a % b)