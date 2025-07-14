#tcs practing

# give a no of N find out the sum of the first N natural numbers
# i/p: N =5
# O/P : 15
# explanation: 1+2+3+4+5
#code
N= int(input("enter a number:"))
sum = N*(N+1)//2
print(f"sum of {N} natural number is: {sum}")