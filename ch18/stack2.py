"""一个多实例栈类

>>> from stack2 import Stack
>>> x = Stack()
>>> x.push('spam')
>>> x.push(123)
>>> x
[Stack:[123, 'spam']]

>>> y = Stack()
>>> y.push(3.1415)
>>> y.push(x.pop())
>>> x, y
([Stack:['spam']], [Stack:[123, 3.1415]])

>>> z = Stack()
>>> for c in 'spam': z.push(c)
...
>>> while z:
...     print(z.pop(), end=' ')
...
m a p s 
>>> z = x + y
>>> z
[Stack:['spam', 123, 3.1415]]
"""  # noqa


class error(Exception):
    pass                 # when imported: local exception


class Stack:
    def __init__(self, start=[]):            # self is the instance object
        self.stack = []                      # start is any sequence: stack..
        for x in start:
            self.push(x)
        self.reverse()                       # undo push's order reversal

    def push(self, obj):                     # methods: like module + self
        self.stack = [obj] + self.stack      # top is front of list
        # 也可以使用下面语句
        # self.stack.insert(0, obj)

    def pop(self):
        if not self.stack:
            raise error('underflow')
        top, *self.stack = self.stack
        return top

    def top(self):
        if not self.stack:
            raise error('underflow')
        return self.stack[0]

    def empty(self):
        return not self.stack                     # instance.empty()

    def __repr__(self):
        """overloads"""
        return '[Stack:%s]' % self.stack          # print, repr(),..

    def __eq__(self, other):
        return self.stack == other.stack          # '==', '!='?

    def __len__(self):
        return len(self.stack)                    # len(instance), not instance

    def __add__(self, other):
        """创建新的Stack并返回"""
        return Stack(self.stack + other.stack)    # instance1 + instance2

    def __mul__(self, reps):
        """创建新的Stack并返回"""
        return Stack(self.stack * reps)           # instance * reps

    def __getitem__(self, offset):                # see also __iter__
        return self.stack[offset]                 # instance[i], [i:j], in, for

    def __getattr__(self, name):
        """instance.sort()/reverse()/.."""
        return getattr(self.stack, name)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
