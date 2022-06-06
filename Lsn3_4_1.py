'''
Напишите программу, которая считывает из файла строку, соответствующую тексту,
сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.
'''
# initials
i: int = 0
seq_res = ''
add_letter = ''
# open the  file and  get 'packed' sequence
with open('text.txt') as inf:
    seq = inf.readline().strip()
# 'unpack'  the sequence
if len(seq) > 1:
    while i < len(seq):
        j: int = 0
        mult = '0'
        # if  next  symbol of  sequense  is  an  letter then  save  it  to var - 'ass_letter'
        if seq[i] not in '0, 1, 2, 3, 4, 5, 6, 7, 8, 9':
            add_letter = seq[i]
            j = 1
        else:
            # counting the number  of similar  letters which  we should  add to the  sequence
            while seq[i+j] in '0, 1, 2, 3, 4, 5, 6, 7, 8, 9':
                mult += (seq[i + j])
                j= j + 1
                if (i + j) >= len(seq): # cheking  for  the  EOL
                    break
        seq_res = seq_res + (add_letter * int(mult))
        i += j
else:
    seq_res = seq[0]
# writing  result sequence to  file
with open('text_out.txt', 'w') as ouf:
    ouf.write(seq_res)
