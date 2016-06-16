#to prevent eof error
try:
	#for input
	print "Enter numbers:",
	n=raw_input().split()
	flag=True #for printing answer
	n=[int(x) for x in n]
	s=len(n)-1
	#loop for swapping 
	for i in xrange(s):
		if n[i]>n[i+1]:
			j=i+1
			if j<s:
				for a in xrange(j,s):
					if n[a]>n[a+1]:
						flag=False
						break
			if flag==True :
				n[i],n[i+1]=n[i+1],n[i]
				break
			else:
				n[i],n[a+1]=n[a+1],n[i]
				break
	#for checking list is sorted or not
	flag=True
	for i in xrange(s):
		if n[i]>n[i+1]:
			flag=False
			break
	#for printing Answer
	print "Array can be sorted in one swap?"
	print "Answer: %r"% flag
except:
	print EOFError
