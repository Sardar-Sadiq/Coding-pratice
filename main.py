#TCS practing

# give a no of N find out the sum of the first N natural numbers
# i/p: N =5
# O/P : 15
# explanation: 1+2+3+4+5
# -----CODE-----
# N= int(input("enter a number:"))
# sum = N*(N+1)//2
# print(f"sum of {N} natural number is: {sum}")

# Palindrome check
# I/P: N =121
# O/P: Palindrome
# ----CODE----
# def is_palindrome(N):
#     OG, rev_num = N,0
#     while N>0:
#         digit = N%10
#         rev_num = rev_num*10+ digit
#         N //= 10
#     return OG == rev_num

# N= int(input("enter a number:"))
# print("is palindrome:", is_palindrome(N) )

# For the reversing just remove the OG from the code and return only rev_num for optional add the print("reversed number:", rev_num ) like that it will show you the reversed integer

# Factorial
# I/P: 5
# O/P: 120
# ----CODE----
def factorial(X):
    fact =1
    for i in range(2, X+1):
        fact *= i
    return fact

X= int(input("enter a number:"))
print("Factorial of", X, "is:", factorial(X))
