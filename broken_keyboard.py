def check_chars(word, chars):
    for i in range(len(word)):
        if word[i] not in chars:
            return False
    return True

f=open("enable1.txt", "r")
strokes=[]; words=[]; goodwords=[]; final=[]
for i in range(int(input())):
    strokes.append(input())
for line in f:
    words.append(line)
for x in range(len(strokes)):
    best=0
    for i in range(len(words)):
        if check_chars(words[i].rstrip(), strokes[x]):
            goodwords.append(words[i].rstrip())
    for i in range(len(goodwords)):
        if len(goodwords[i])>len(goodwords[best]):
            best=i
    try:
        final.append(goodwords[best])
    except IndexError:
        final.append("NONE")
    goodwords.clear()
for i in range(len(strokes)):
    print(strokes[i]+" = "+final[i])