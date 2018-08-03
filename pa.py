pa=int(input("enter leap year"))
if(pa%400==0):
    print ("yes")
elif(pa%4==0):
    print ("yes")
elif(pa%100!=0):
    print ("yes")
else:
    print ("no")
