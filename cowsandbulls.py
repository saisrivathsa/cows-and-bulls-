from random import *
flag=0

def generator():
    random_number=randint(0123,9876)
    f=0
    s=str(random_number)
    if random_number < 1000:
        s='0'+s

    for i in range(4):
        for j in range (4):
            if i!=j:
                if s[i] == s[j]:
                    f=1
    if f==1 :
        s=generator()
        return s
    else :
        return s

def check(y,n):
    global flag
    cows,bulls=0,0
    n=str(n)
    if len(n)!=4:
        print "enter only a four digit number \n"
        game()
    a=[]
    for i in n :
        a.append(i)

    for i in range(4):
        for j in range (4):
            if i!=j :
                if a[i]==a[j]:
                    print "guess a number with no repeated digits\n"
                    game()

    for i in range(4):
        for j in range (4):
            if a[i] == y[j]:
                if i==j:
                    bulls=bulls+1
                else :
                    cows=cows+1

    print "you have got %d cows and %d bulls\n" % (cows,bulls)

    if bulls==4:
        flag=1
        print "Congo you won\n"
        quit()
def game():
    global flag
    global x
    y=[]
    for i in x:
        y.append(i)
    while flag==0:
        n=raw_input("Try guessing the 4 digit number:")
        try:
            int(n)
            check(y,n)
        except ValueError:
            print "Only enter numbers\n"
            game()

x=str(generator())

game()
