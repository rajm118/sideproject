def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
nterms = input()
if nterms <= 0:
   print("Enter a positive number ")
else:
   print("The following is the Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
