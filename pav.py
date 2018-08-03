pa=int(input())
if(pa%400==0):
    print ("leapyear")
elif(pa%4==0):
    print ("leapyear")
elif(pa%100!=0):
    print ("leapyear")
else:
    print ("not leapyear")
