def toBinary(num):
    return bin(int(num))[2:]
def toTrinary(num):
    num=str(num)
    d=[0, 1, 2, 10, 11, 12, 20, 21, 22, 100]
    a=0
    m=1
    for i in range(len(num)):
        t=d[int(num[int(len(num)-i-1)])]*m
        a=int(a)+t
        a=str(a)
        while(badchars(a)):
            if '9' in str(a):
                a=correct(a, '9')
            elif '8' in str(a):
                a=correct(a, '8')
            elif '7' in str(a):
                a=correct(a, '7')
            elif '6' in str(a):
                a=correct(a, '6')
            elif '5' in str(a):
                a=correct(a, '5')
            elif '4' in str(a):
                a=correct(a, '4')
            elif '3' in str(a):
                a=correct(a, '3')
        m*=101
    return str(a)
def badchars(a, bad='3456789'):
    for i in bad:
        if i in str(a):
            return True
    return False
def correct(a, x):
    i=a.find(x)
    if i==0:
        return '1'+a[i].replace(x,str(int(x)-3))+a[i+1:]
    elif a[i-1]=='9':
       return a[:i-2]+a[i-2].replace(a[i-2], str(int(a[i-2])+1))+a[i-1].replace('9','0')+a[i].replace(x,str(int(x)-3))+a[i+1:]
    else:
        return a[:i-1]+a[i-1].replace(a[i-1],str(int(a[i-1])+1))+a[i].replace(x,str(int(x)-3))+a[i+1:]