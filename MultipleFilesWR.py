import re
'''
CHECKINGAIM : PROGRAM TO SOLVE CAPTCHAS PROVIDED BY ZEND FRAMEWORK
VARIABLES USED :avg,upper,lower,caprange,
LISTS USED ARE :testcases,alphalist

'''
matchinglist=[]
matchingcount=[]
### TEST CASES ARRAY ###
testcases=["BYDYR","COQIF","FYQYM","GUNEJ","QYROG","QOQEC","FEXAK","GOXOH","HYUOV","JAFED","REJOT","SEVEU","TANYV","XEHAG","MADOK","PUWYM","UEFYT","WOJUS"]

#################FUNCTIONS#####################
#### CREATING CUSTOM FUNCTION TO SEE RANGE ####
def checkrange(avg,lower,upper):
	if (upper>avg>lower):
		str(lower)
		str(upper)
		print "Between Lower",lower,"Upper",upper
		print alphalist[al]	
#############END OF FUNCTIONS###################

for caprange in range(len(testcases)):
	#### OPENING A TEST FILE AND READING####
	with open('CAPTCHATESTCASES/'+testcases[caprange]+'.txt','r') as ca:
		##SAVING ALL THE READ DATA TO A VARIABLE##
		read_data = ca.read()
		##INITIALIZING A ARRAY BY NAME CAP##
		cap=[]
		## SAVING INDIVIDUAL LINE OF CAPTCHA AS SEPERATE LIST ITEM IN CAP ##	
		for line in read_data.splitlines():
	    		cap.append(line)

		##READING EACH LIST ITEM IN CAP AND PRINTING IT ##
		for each_line in cap:
			print each_line

		## CREATING A LIST OF ALPHABETS ##
		alphalist=["a","b","c","d","e","f","g","h","i","j","k","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
		## READING A LETTER FROM DICTIONARY AND SAVING IT TO LIST##
		for al in range(25):
			with open('dict/'+alphalist[al]+'.txt','r') as alpha:
				read_alpha=alpha.read()
				## INITIALIZING ARRAY BY NAME U##
				alpha=[]
				## SAVING INDIVIDUAL LINE OF LETTER U AS SEPERATE LIST ITEM IN U ##	
				for line in read_alpha.splitlines():
					alpha.append(line)	
				## PRINTING READ OUTPUT##
				##    for each_alpha_line in alpha:
				##	print each_alpha_line
	
	
	
			##INITIALIZING Z
			z=0
			q=0
			avg=0
			count=0.0
			calpha= ""
			percentage=0.0
			##SEARCHING ALOGORITHM FOR 1ST ALPHABET##
			for x in range(6):
				## USED TO CHECK THE POSITION OF STRING IS IN 1ST POSITION ONLY##	
				y= cap[x].find(alpha[x],0,22)
				if (y==0):
					count=count+1	
					calpha=calpha +alphalist[al]
														
			str(count)		
			if(calpha!=""):		
				percentage=(count/6)*100
				str(percentage)		
				matchinglist.append(alphalist[al])	 
				matchingcount.append(count)
			
					
		for i in range(len(matchingcount)):
			maximum=max(matchingcount)
			if(matchingcount[i]==maximum):
				print "The First Letter is" 
				print matchinglist[i]			
		matchingcount=[]	
	        matchinglist=[]	
		
		

	
	'''## GIVING Z VALUE TO Y ##
			z=y
			## CHECK WHETHER Z == Y OR Z >= 0 ## 
			if (z==y) and (z>=0):
				print alphalist[al]
				x=x+1			 							
				q = q+y
				avg = q/x
				## TEST CONDITION or (15>avg>10) or (25>avg>18) or (35>avg>28) or (45>avg>38)
				if (avg ==0) :
					count=count+1
					print alphalist[al]
				checkrange(avg,10,15)
				checkrange(avg,18,25)
				checkrange(avg,28,35)
				checkrange(avg,38,45)
				x=0'''
	
				
			


	
