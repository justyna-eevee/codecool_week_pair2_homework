def get_user_name():
    name = input('What is your name? ')
    return name.upper()


def get_hello_message():
    name = get_user_name()
    if name:
        return f'Hello, {name}!'
    else:
        return 'Hello World!'

def say_hello():
        print(get_hello_message())


if __name__ == "__main__":
    say_hello()
    