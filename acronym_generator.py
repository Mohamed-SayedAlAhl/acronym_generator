from time import time
start=time()
#python project to create acronyms
word=input("Write a phrase to get its acronym: ").lower()
text=word.split()
a=" "
for i in text:
    a=a+str(i[0]).upper()
print(a)
end=time()
execution_time=end-start
print(f"execution time is: {execution_time} seconds")
