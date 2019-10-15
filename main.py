import json
import src.lib.keys as key

keys = key.keys
test = 'testtt'


def findKey(value, string):
    for x, y in keys.items():
        if y == value:
            print(x, y)


# def changeSlice(ne, wo):
#     ne = ne + 8
#     wo = wo + 8


# FINDS A VALUE USING A KEY
# print(keys['!']))

# FINDS A KEY USING A VALUE!
# for x, y in keys.items():
#     if y == "1(oM^Zh+":
#         print(x,y)

eto = ''
for t in test:
    eto += keys[t]

# print(eto)

dto = ''
z = 0
one = 0
two = 7
o = slice(one, two)
b = int(len(eto) / 8)
# print(b)
while z < b:
    # print(z)
    # print(one)
    # print(two)
    # print(eto[o])
    # print(o)
    # print(eto[o])
    print(findKey(eto[o], dto))
    one = one + 8
    two = two + 8
    o = slice(one, two)
    z += 1

v = "1(oM^Zh+"

for x, y in keys.items():
    if y == v:
        print(x, y)

# print(dto)

# a = "fdasfdsa"

# x = slice(2, 4)

# print(a[x])
