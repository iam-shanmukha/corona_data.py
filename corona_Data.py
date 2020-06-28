from covid import Covid
import time
covid = Covid()
India_cases = covid.get_status_by_country_id(27)
#print(India_cases)
print('''
 ___ _   _ ____ ___    _    
|_ _| \ | |  _ \_ _|  / \   
 | ||  \| | | | | |  / _ \  
 | || |\  | |_| | | / ___ \ 
|___|_| \_|____/___/_/   \_\
                            

	''')
for param,val in India_cases.items():
	print("{} : {}".format(param,val))
	#print(val)
val = str(val)
print("Last Updated : {}".format(time.ctime(int(val[:10]))))