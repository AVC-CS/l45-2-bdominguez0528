import random


def main():
    total = 0
    numbers = []
    last_number = 0
    while total < 100:
        number = random.randint(1, 10)
        numbers.append(number)
        total += number
        last_number = number
        
    total -= last_number
        

        
    

    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
