from bottle import route, run, template, static_file, get, post, request
import random

PASSWORD_LENGTH = 8

bad_guesses = 0
key = '01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
password = ''

@get('/')
def get_index():
    return template('index')


@get('/hack/<guess>')
def get_hack(guess):
    global bad_guesses
    if guess != password:
        bad_guesses += 1
        result = 'go away'
        print('bad guess '+str(bad_guesses))
        print build_matrix()
    else:
        bad_guesses = 0
        result = 'welcome'
        print winner_matrix()
        
    return result

def build_matrix():
    matrix = [ (255,0,0) for i in range(bad_guesses%64) ]
    matrix += [ (0,0,0) for i in range(64-bad_guesses%64) ]
    return matrix

def winner_matrix():
    matrix = [ (0,255,0) for i in range(64) ]
    return matrix
                  
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

if __name__=='__main__':
    password = ''.join([ random.choice(key) for i in range(PASSWORD_LENGTH) ] )
    print(password)
    run(host='0.0.0.0', port=8080)#, reloader=True)
