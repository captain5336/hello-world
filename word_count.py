import functools
import re

# this program is to count the number of workd in a article
# read word into ls2, replace special charactor with space 
ls1=[]
f_obj=open('David.txt','r')
ls1=f_obj.read().lower()
for i in '!@#$^*()_+-;:`~\'"<>=./?,':
	ls1=ls1.replace(i,' ')
ls2=ls1.split()
print(len(ls2))

#count the number of all words
counts={}
for i in ls2:
	counts[i]=counts.get(i,0)+1
iteams = list(counts.items())
iteams.sort(key=lambda x:x[1],reverse=True)

#display word count
for i in iteams[300:400]:
    print(i)

# The pause is for looking screen
s=input("Press <enter> ")

