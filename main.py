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
# def factorial(X):
#     fact =1
#     for i in range(2, X+1):
#         fact *= i
#     return fact

# X= int(input("enter a number:"))
# print("Factorial of", X, "is:", factorial(X))


# Count frequency
# I/P: arr[] = {10,5,10,15,10,5};
# O/P:  10 3
#        5 2
#       15 1
# ----CODE----
# from collections import Counter
# arr = [1,2,1,5,4,2,2,1,4,5]
# frequency = Counter(arr)
# for key, value in frequency.items():
#     print(f"{key} -> {value}")


# Leap year check
# I/P: 1996
# O/P: TRUE
# ----CODE----
# def leap_year(N):
#     year = N
#     if(year%400 == 0):
#         return True
#     elif(year%100 == 0):
#         return False
#     elif(year%4 == 0):
#         return True
#     else:
#         return False
# N=int(input("enter the year: "))
# print(f"The {N} year is {leap_year(N)} leap year")


# Sorting Algorithms
# -bubble sort
# -insertion sort
# -selection sort **(interview)
# -quick sort **(interview)
# -merge sort

# swap two numbers without using third variable
# I/P: a=5, b=10
# O/P: a=10, b=5
# ----CODE----
# a =int(input("enter the number a: "))
# b =int(input("enter the number b: "))

# a= a+b
# b= a-b
# a= a-b
# or use this a = a+b-(b=a)
# print(f"after swapping: a={a}, b={b}")

# Largest an smallest elelmebts in an array
# I/P: arr = {2,3,6,7,8,9}
# O/P: 9 2
# ----CODE----
# def largest_num (N):
#         minimum = min(N)
#         maximum = max(N)
#         return minimum, maximum

# N= {2,3,4,5,7,8,9}
# minimum_value, maximum = largest_num(N)
# print(f"minimum value: {minimum_value}, maximum value: {maximum}")
    
# Given an AP Series, we need to find the sum of the series.
# I/P: 
# n=4
# a=2
# d=2
# O/P: 20    
# Sn = n*(2*a+(n-1)*d)/2)
# ----Code----
# def sum_of_ap(a,d,n):
#     return (n*(2*a+(n-1)*d)/2)

# a= int(input("enter first term a:"))
# d= int(input("enter second term d: "))
# n= int(input("enter no of terms n: "))
# print(f"sum of the AP: ",sum_of_ap(a,d,n))


# second smallest and second largest element in an array 
# ----Code----
# def second_smallest_largest(arr):
#     e = list(set(arr))
#     e.sort()
#     return e[1], e[-2] if len(e) >= 2 else (None, None)

# arr = [3, 1, 7, 5, 9, 1]
# print("Second Smallest & Largest:", second_smallest_largest(arr))


# reverse an given array
# ----Code----
# def reverse_array(arr):
#     return arr[::-1]

# arr= [1,2,3,4]
# print(f"reversed array: ", reverse_array(arr))
# O/P: [4,3,2,1]


# Rearrange array in increasing-decreasing order
# ----Code----
# def rearrange(arr):
#     arr.sort()
#     mid =len(arr) // 2
#     return arr[:mid] + arr[mid:][::-1]

# arr = [5,2,8,1,3]
# print("rearrange: ", rearrange(arr))

# sum of the elements in array
# ----Code----
# def array_sum(arr):
#     return sum(arr)

# arr = [1,2,3,4,5]
# print("Sum:", array_sum(arr))

# rotate array by K elements-block swap algorithm (left rotation)
# ----Code----
# def left_rotate(arr, k):
#     n =len(arr)
#     k %=n
#     return arr[k:]+ arr[:k]

# arr = [1,2,3,4,5]
# k =2
# print("rotated", left_rotate(arr, k))


# avg of all elements in array 
# ----Code----
# def average(arr):
#     return sum(arr) / len(arr) if arr else 0

# arr = [2, 4, 6, 8]
# print("Average:", average(arr))


# finding the median
# ----Code----
# def median(arr):
#     arr.sort()
#     n = len(arr)
#     mid = n // 2
#     return (arr[mid] + arr[mid - 1]) / 2 if n % 2 == 0 else arr[mid]

# arr = [5, 3, 1, 2, 4]
# print("Median:", median(arr))



# odd and even positions difference
# I/P: 4567
# O/P: 2
# ----Code---- 
# def oddlyeven(n):
#     oddsum= 0
#     evensum= 0
#     for i in range(len(n)):
#         digit = int(n[i])
#         if(i+1)%2 == 1 :
#             oddsum += digit
#         else:
#             evensum += digit
#     return abs(oddsum - evensum)

# num = input(" ")
# print(oddlyeven(num))

# product of digits
# ----Code----
# def product_of_digits(n):
#     prod = 1
#     while n > 0:
#         prod *= n % 10
#         n = n // 10
#     return prod

# n = int(input())
# print(product_of_digits(n))

# palindrome string/ number
# ----Code----
# def palindrome(s):
#     rev = s[::-1]
#     print (rev)
#     return s == rev

# s = input()
# print(palindrome(s))

# missing number from array 1 to n
# ----Code----
# def missing(arr ,n):
#     total = n * (n+1) // 2
#     return total - sum(arr)

# n = int(input())
# arr = list(map(int,input().split()))
# print(missing(arr, n))

# sweet seventeen
# I/P: 1a
# O/P: 27
# ----Code----
# def base17_to_decimal(num):
#     return int(num, 17)

# num = input("Enter base-17 number: ").upper()
# print("Decimal:", base17_to_decimal(num))

# second largest number
# I/P: 456 456 882 600
# O/P: 600
# ----Code----
# def sec(arr):
#     arr = list(set(arr))
#     arr.sort()
#     return arr[-2]

# arr = list(map(int,input().split()))
# print(sec(arr))

# bubble sort
# I/P: 5 1 4 2 3
# O/P: 1 2 3 4 5
# ----Code----

def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = list(map(int,input().split()))
print(bubblesort(arr))