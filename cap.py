import re
with open('captcha.txt','r') as ca:
	read_data = ca.read()
	mletter=[""]
	completem=[""]
	'''
	#Program to find a matching list item 
	def search(b):
 		try:
  			k=mletter.index(b)
  			return mletter[k] 
 		except ValueError:
    			return 'not found'
	#Ends here
	'''
	#Line By Line Code	
	for line in read_data.splitlines():
    		mletter.append(line)
		print line
	# Code to print each line
	for each_line in mletter:
		completem.append(each_line[24:35])	
	#completem.remove(".___  ___.")	
	#completem.remove("|   \/   |")	
	#completem.remove("|  \  /  |")	
	#completem.remove("|  |\/|  |")	
	#completem.remove("|  |  |  |")	
	#completem.remove("|__|  |__|")
	for each_Linem in completem:
		print each_Linem	
	print mletter[1].find(completem[2],29)
	print mletter[2].find(completem[3],29)
	print mletter[3].find(completem[4],29)
	print mletter[4].find(completem[5],29)
	print mletter[5].find(completem[6],29)
	
	f=open("u.txt",'w')
	for item in completem:
		f.write("%s\n" % item)
			
'''
#Using it 
	print(search(".___  ___.      ___       __    __   __    __  ___   ___ "))
'''

	
