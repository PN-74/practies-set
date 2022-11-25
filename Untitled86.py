#!/usr/bin/env python
# coding: utf-8

# In[1]:


##You will be given a list. You have to print a list whose 1st element should be largest and 2nd should be the smallest then the 3rd should be 2nd largest and 4th should be 2nd smallest and so on.


# In[2]:


l = list(map(int, input().split()))
# Write your code here
new_list = []
for i in range(len(l)):
	if i % 2 == 0:
		new_list.append(max(l))
		l.remove(max(l))
	else:
		new_list.append(min(l))
		l.remove(min(l))
						
print(new_list)


# In[ ]:


Find nth fibonacci number. If it starts with 0,1,1,2.....

Also, Print Incorrect Input if n is less than or equal to 0.

Input Format:

Call the function with n

Output Format:

Print the nth fibonacci number

Sample Input 0:

4

Sample Output 0:

2

Sample Input 1:

 0

Sample Output 1:

Incorrect input


# In[4]:


n = int(input())
def Fibonacci(n):
# Write your code here
	if n == 0:
		return("Incorrect input")
	else:
		if n == 1:
			res = 0
			return(res)
		elif n == 2: 
			res = 1
			return(res)
		else:
			res = Fibonacci(n - 1) + Fibonacci(n -2)
			return(res)
			
print(Fibonacci(n))



# In[ ]:




