from bottle import route, run, template, static_file, get, post, request
import random
from sense_hat import SenseHat

MAX = 999
bad_guesses = 0
password = ''
pause = False


@get('/')
def get_index():
    return '/guess/{guess}/{message}  or /guess/{guess}'


@get('/guess/<guess>')
def get_guess(guess):
    get_guess_message(guess, 'Hacked!')


@get('/guess/<guess>/<message>')
def get_guess_message(guess, message):
    global bad_guesses
    global pause
    if not pause:
        try:
            if int(guess) > password:
                bad_guesses += 1
                result = {'result': 'too high'}
            elif int(guess) < password:
                bad_guesses += 1
                result = {'result': 'too low'}
            else:
                pause = True
                bad_guesses = 0
                result = {'result': 'correct'}
                message_scroll(message[:15])
                set_password()
                pause = False
        except:
            bad_guesses += 1
            result = {'result': 'wrong'}
        set_matrix()
    else:
        result = {'result': 'honoring the winner, please wait'}
    return result


def set_matrix():
    matrix = [(255, 0, 0) for i in range(bad_guesses % 64)]
    matrix += [(255, 255, 255) for i in range(64 - bad_guesses % 64)]
    sense.set_pixels(matrix)


def clear_matrix():
    matrix = [(255, 255, 255) for i in range(64)]
    sense.set_pixels(matrix)


def message_scroll(message):
    sense.show_message(message, .1, (255, 165, 0), (0, 255, 0))
    sense.show_message(message, .1, (255, 0, 0), (0, 255, 255))
    sense.show_message(message, .1, (0, 0, 255), (255, 255, 0))
    clear_matrix()


def set_password():
    global password
    password = random.randint(0, MAX)
    print password


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')


if __name__ == '__main__':
    sense = SenseHat()
    set_password()
    clear_matrix()
    run(host='0.0.0.0', port=8080)#, reloader=True)
