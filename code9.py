####count=0
####a=0
####b=1
####n=10
####
####while count < n :
####    count += 1
####    print(a)
####    c=a+b
####    a=b
####    b=c
####    
##
var=[4,40,5]

for x in var:
    if x > 1 :
        for i in range(2,x):
            if (x%i) == 0:
                print("{} is not a prime number.".format(x))
S                break
                
        else:
            print("{} is a prime number.".format(x))
        
                

##        

##import pandas
####import numpy
####var=numpy.array([10,20,30])
####var2=var/2
####print(var2)
####     
##
####var=[2,4,6]
#####var1=pandas.Series(var)
####var1=pandas.Series(var,index=['a','b','c'])
#####print(var1)
#####print(var1.sum())
#####print(var1.prod())
####print(var1.cumsum())
##
####dictio = "a", "b", "c", "d";
####var=pandas.Series(dictio)
####var1=pandas.Series(var.sum())
####print(var)
####print(var1)
##
##var= [1,2,3]
###var1=pandas.DataFrame(var,index=['a','b'],columns=['c','d'])
###var2=pandas.DataFrame.iloc(var.loc[1])
##var3=pandas.DataFrame(var)
##var4=var3.to_csv('Sample.csv')
###print(var4)
