# closure

def gen():
    idx = 0

    def next_item():
        nonlocal idx
        result = idx
        idx = idx + 1
        return result

    return next_item


g = gen()


# print(g())
# print(g())
# print(g())


def gen_1():
    print('1')
    yield 2
    print('3')
    yield 4
    print('5')


g_1 = gen_1()


# print(next(g_1))
# print(next(g_1))
# print(next(g_1))


def gen_2():
    idx = 0
    while True:
        yield idx
        idx += 1
        if idx > 3:
            return 'dupa'


# g_2 = gen_2()
# print(next(g_2))
# print(next(g_2))
# print(next(g_2))
# print(next(g_2))
# print(next(g_2))

# for item in gen_2():
#     print(item)

print([x * 2 for x in gen_2()])
