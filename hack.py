import requests

MIN = 0
MAX = 9999


def binary_search():
    minimum = MIN
    maximum = MAX
    tries = 0
    while minimum <= maximum:
        tries += 1
        guess = minimum + (maximum - minimum) // 2
        response = requests.get('http://hardsense:8080/guess/%d/hi' % guess).json()
        print(tries, maximum, minimum, guess, response['result'])
        if response['result'] == 'correct':
            break
        elif response['result'] == 'too low':
            minimum = guess + 1
        elif response['result'] == 'too high':
            maximum = guess - 1
    print(tries, guess)


def linear_search():
    for i in range(MAX):
        response = requests.get('http://hardsense:8080/guess/%d/You Rock!' % i).json()
        if response['result'] == 'correct':
            print('code is: ', i)
            break


if __name__ == '__main__':
    linear_search()
    binary_search()