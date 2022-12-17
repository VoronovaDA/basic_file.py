import os

files =  [x for x in os.listdir() if x.endswith('.txt')]

dict_f = {}

for file in files:
    with open(file, encoding='utf8') as f:
        counter = 0
        for line in f:
            counter += 1
        dict_f[file] = counter

res_file = open('res.txt', 'w', encoding='utf8')
for file in sorted(dict_f, key=lambda x: x[1]):
    info = f'{file}\n{dict_f[file]}\n'
    res_file.write(info)
    with open(file, 'r', encoding='utf8') as text:
        for line in text:
            res_file.write(line)
    res_file.write('\n\n')

# res_file.close()