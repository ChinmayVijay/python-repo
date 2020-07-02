# Closure in Python
def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func


hi_func = outer_func('Hi!')
hey_func = outer_func('Hey!')
# print(my_func.__name__)

hi_func()
hey_func()

# __closure__
# print(hi_func.__closure__)
