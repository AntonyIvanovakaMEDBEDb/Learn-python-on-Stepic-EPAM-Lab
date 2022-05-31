def update_dictionary(d, key, value):
    add_v = []
    if key in d:
        add_v= (d[key])
        add_v.append(value)
        d[key] = add_v
    elif (2 * key) in d:
        add_v= (d.get(2*key))
        add_v.append(value)
        d[(2 * key)]= add_v
    else:
        add_v.append(value)
        d[(2 * key)] = add_v
    #eturn d

#x = float(input())
# print(update_dictionary({10: 10, 11: 0}, 11, 20))
d = {}
update_dictionary(d, 1, -1)
print(d)
update_dictionary(d, 2, -2)
print(d)
update_dictionary(d, 1, -3)
print(d)