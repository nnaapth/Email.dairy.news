import requests

API_Key = '17717aa986d44e12ba2d5fb69df05211'
url= 'https://newsapi.org/v2/everything?q=tesla&from' \
     '=2024-10-29&sortBy=publishedAt&apiKey=17717aa986d44e12ba2d5fb69df05211'
# make request
readurl = requests.get(url)

#make dictionary of data
findtool = readurl.json()

#Access the articles titles and descriptions
for article in findtool['articles']:
     print(article['title'])
     print(article['description'])