# Exercise website: https://www.complexityexplorer.org/courses/100-nonlinear-dynamics-mathematical-and-computational-approaches/segments/9034
# Problem No.: 1,2

n = int(input("Enter n: "))
x0 = float(input("Enter x0: "))
r = float(input("Enter r: "))

def logistic(r, x):
    return r * x * (1 - x)

x = x0
for i in range(n):
    x = (logistic(r,x))
    print("X"+str(int(i+1))+" = "+str(x))
