import sys, os
query = ''
if len(sys.argv) <2:
     print("Pls enter what you want to search on google")
     sys.exit(0)
words=((sys.argv[1].split("\\")[-1]).split('.')[0]).split()
for word in words:
     if word == words[-1]:
          query+=word
     else:
          query+= word + '+'
link = "http://www.youtube.com/results?search_query="
os.system("start " + link + query)
