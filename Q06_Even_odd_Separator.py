def separate_even_odd(numbers):
    even = []
    odd = []

    for num in numbers:
        if num % 2 == 0:
            even.append(num) 
        else:
            odd.append(num) 

    return (even, odd)

print(separate_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) 
