import src.lib.keys as key

keys = key.keys
test = 'testtt'

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
while z < int(len(eto) / 8):
    for x, y in keys.items():
        # print(eto[one:two])
        if y == str(eto[one:two]):
            dto += x
    one += 8
    two += 8
    z += 1

for x, y in keys.items():
    # print(eto[one:two])
    if y == str(eto[0:7]):
        print(x)

print(dto)