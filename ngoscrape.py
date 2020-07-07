# a=[4,4,5,1,25,5,5,4,3,3,4,3]
# b=[]
# for i in a:
# 	if i not in b:
# 		b.append(i)
# count1={}
# for j in b:
# 	count=0
# 	for i in a:
# 		if j==i:
# 			count+=1
# 	count1[j]=count
# same=0
# for k in count1.values():
# 	if k>same:
# 		same=k
# 		demo=k
# c=demo
# empty=[]
# for i in count1.keys():
# 	if count1[i]==c:
# 		empty.append(i)
# print(min(empty))
	

		
# import requests,os,json
# from bs4 import BeautifulSoup
# if os.path.exists('ngo.json'):
# 	with open('ngo.json','r') as file:
# 		c=json.load(file)
# 		c=json.loads(c)
# 	ask=input('enter state  ').lower()
# 	for i in c:
# 		if ask==i['state'].lower():
# 			print(i['name'])
# else:
# 	url='https://www.giveindia.org/certified-indian-ngos'
# 	r=requests.get(url)
# 	soup=BeautifulSoup(r.text,('html.parser'))
# 	table=soup.find('table',class_="jsx-697282504 certified-ngo-table")
# 	tr=table.find_all('tr',class_="jsx-697282504")
# 	# print(len(tr))
# 	final=[]
# 	for i in range(1,len(tr)):
# 		dic={'name':'','cause':[],'state':[]}
# 		td=tr[i].find_all('td',class_="jsx-697282504")
# 		a=[]
# 		for i in (td):
# 			a.append(i.text)
# 		dic['name']=a[0]
# 		dic['cause']=a[1]
# 		dic['state']=a[2]
# 		# print(dic)
# 		final.append(dic)
# 	with open('ngo.json','w+') as file:
# 		c=json.dumps(final)
# 		c=json.dump(c,file)


		
		



# puri tamanna bhala meri kab hui
# jab hui pta na chala tum meri kab hui


