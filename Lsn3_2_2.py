a = [str(i) for i in input().split()]
i = 0
out_dct = {}
# make  the  dict  of  words with count
for i in  range(len(a)):
    if a[i].lower() not in out_dct:
        out_dct[a[i].lower()] = 1
    else:
        out_dct[a[i].lower()] += 1
# Printing  results  in format:  'key'' ''value'
for key in out_dct:
    print(key, end=' ')
    print(out_dct[key])
