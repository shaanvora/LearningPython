
def hypervolume(length, *lengths):
    print(lengths)
    print(type(lengths))
    volume = length
    for length in lengths:
        volume *= length
    return volume

a = hypervolume(3,4)

print(a)

def tag(name, **kwargs):
    print(name)
    print(kwargs)
    HTMLLine = '<' + name
    for key, value in kwargs.items():
        HTMLLine += f'{key}="{value}"'
    HTMLLine += '>'
    return HTMLLine

print(tag('img', src='picture.jpg', alt="A picture", border=1))


def addUp(arg1, arg2, *args):
    value = arg1+arg2
    for number in args:
        value += number
    return value

a = (10,10)
b = (1,2,3,4,5,6,8)
print(addUp(*a))
print(addUp(*b))




