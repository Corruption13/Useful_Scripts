import wikipedia
query=input()
alphabets=[]
b=[]
result=wikipedia.WikipediaPage(query)
no_of_letters=0
a=result.content
for i in range(0,26):
    alphabets+=chr(65+i)
for i in a:
    if(i in alphabets):
        no_of_letters+=1
        b+=i.upper()
index={k: 0 for k in alphabets}
for i in b:
   index[i]+=1
percentages=[]
for key,value in index.items():
    percentages.append(float(value/no_of_letters))
index1=dict(zip(alphabets,percentages))
print(index1)
