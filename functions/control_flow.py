# Write a function that uses while, if and continue statements 
# to print all the even numbers between 0 and 50.
def even_numbers():
   num = 0
   while num<50:
      num+=1
      if num % 2!=0:
          continue
      print(num)
# Write a function that takes an integer argument and prints "Prime"
# if the number is prime, and "Not prime" if the number is not prime
def prime_number(nums):
   for i in nums:
      if i %1==0:
         print(f"{i} is prime number")
      else:
         print(f"{i} is not prime number")
         
        
 #   Write a function that takes a list of integers as input and 
 #   prints the sum of all the even numbers in the list.
def sum_even_numbers(int):
   sum = 0
   for i in int:
      if i%2==0:
         sum+=i
   print(sum)
 # Write a function that takes any two integers as input, and prints the sum of all
 # the numbers between the two integers (inclusive) that are divisible by 3.
def sum_divisible_by_three(num1, num2):
   output = 0
   for i in range(num1,num2+1):
      if i % 3 ==0:
         output+=i
         print(output)

 