a = 'VASFHGAGFMBLCSFGZB\nVFSSCMINJUYSSSSHDS\nZPOXUIWSSSSFO'
b = a.split('\n')
max1 = [0,0]
kak = 0
for i in range(0,len(b)):
    for n in range(0,len(b[i])):
        if b[i][n] == 'S' and n != len(b[i]) - 1:
            kak += 1
        elif b[i][n] == 'S' and n == len(b[i]) - 1:
            kak += 1
            if kak > max1[0]:
                max1[0] = kak
                max1[1] = i
                kak = 0
            else:
                kak = 0
        elif b[i][n] != 'S':
            if kak > max1[0]:
                max1[0] = kak
                max1[1] = i
                kak = 0
            else:
                kak = 0
c = b[max1[1]].split('S')
while '' in c:
    c.remove('')
print(max(c , key=len))