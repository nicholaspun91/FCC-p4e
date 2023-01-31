def arithmetic_arranger(problems, calculate=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    problemss = []
    for i in range(len(problems)):
        problemt = problems[i].split()
        problemss.append(problemt)
        
    print(problemss)
    a = []
    spacer = '    '
    line1=''
    line2=''
    line3=''
    line4=''
    def sp1(x, m):
        x=' '*(m-len(str(x))+2)+str(x)
        return x

    def sp2(x, m, y):
        x=y+' '*(m-len(x)+1)+x
        return x
        
    for i in range(len(problemss)):
        n1 = problemss[i][0]
        op = problemss[i][1]
        n2 = problemss[i][2]
        l = max(problemss[i], key=len)
        
        try:
            int(n1)
            int(n2)
        except:
            return "Error: Numbers must only contain digits."

        if len(n1) > 4 or len(n2) > 4:
            return "Error: Numbers cannot be more than four digits."
            
        if op == '+':
            a=int(n1) + int(n2)

        if op == '-':
            a=int(n1) - int(n2)

        if op == '*' or op == '/':
            return "Error: Operator must be '+' or '-'."

        t1=sp1(n1, len(l))
        t2=sp2(n2, len(l), op)
        t4=sp1(a, len(l))

        if i < len(problemss)-1:
            line3=line3+'-'*(len(l)+2)+spacer
            line1=line1+t1+spacer
            line2=line2+t2+spacer
            line4=line4+t4+spacer

        if i == len(problemss)-1:
            line3=line3+'-'*(len(l)+2)
            line1=line1+t1
            line2=line2+t2
            line4=line4+t4
            
    if calculate==True:
        return line1+'\n'+line2+'\n'+line3+'\n'+line4
    if calculate==False:
        return line1+'\n'+line2+'\n'+line3
