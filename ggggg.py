code=input().split()
string=input()
chars=[]
ggg=[]
decoded=''
buffer=''
for i in range(0, len(code), 2):
    chars.append(code[i])
for i in range(1, len(code), 2):
    ggg.append(code[i])
del code
for i in range(len(string)):
    if string[i] not in 'gG':
        decoded+=string[i]
    else:
        buffer+=string[i]
        for x in range(len(ggg)):
            if buffer==ggg[x]:
                decoded+=chars[x]
                buffer=''
print(decoded)