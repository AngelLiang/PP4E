"""一个共享栈模块

>>> import stack1
>>> stack1.push('spam')
>>> stack1.push(123)
>>> stack1.top()
123
>>> stack1.stack
[123, 'spam']
>>> stack1.pop()
123
>>> stack1.dump()
<Stack:['spam']>
>>> stack1.pop()
'spam'
>>> stack1.empty()
True
>>> for c in 'spam': stack1.push(c)
...
>>> while not stack1.empty():
...     print(stack1.pop(), end=' ')
...
m a p s 
>>> stack1.pop()
Traceback (most recent call last):
    ...
stack1.error: stack underflow
"""  # noqa

stack = []                                   # on first import


class error(Exception):
    """local excs, stack1.error"""
    pass


def push(obj):
    global stack                             # use 'global' to change
    stack = [obj] + stack                    # add item to the front


def pop():
    global stack
    if not stack:
        raise error('stack underflow')       # raise local error
    top, *stack = stack                      # remove item at front
    return top


def top():
    if not stack:                            # raise local error
        raise error('stack underflow')       # or let IndexError occur
    return stack[0]


def empty(): return not stack           # is the stack []?


def member(obj): return obj in stack        # item in stack?


def item(offset): return stack[offset]       # index the stack


def length(): return len(stack)          # number entries


def dump(): print('<Stack:%s>' % stack)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
