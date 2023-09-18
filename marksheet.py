def entry():
    global math,hindi,english,physics,chemistry
    math=int(input("enter the marks of math"))
    hindi=int(input("enter the marks of math"))
    english=int(input("enter the marks of math"))
    physics=int(input("enter the marks of math"))
    chemistry=int(input("enter the marks of math"))
    
def calculate():
   global per,total
   total=math+hindi+english+physics+chemistry
   per=total*100/500
def results():
    if(per>=60):
        print("we have found the first positio")
    elif(per>=50) and (per<60):
        print("we have find the second position")
    elif(per>=33) and (per<50):
        print("we have find the third position")
    else:
        (per<33)
        print("the result of five subject is fail")
def display():
    print("the math marks is",math)
    print("the hindi marks is",hindi)
    print("the physics marks is",physics)
    print("the english marks is",english)
    print("the total is",total)
    print("the percentage is",per)
entry()
calculate()
results()
display()
    