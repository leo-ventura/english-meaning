import sys
import urllib

def getPageContent(url):
    try:
        print "[trying to get the content...]"
        return urllib.urlopen(url).readlines()
    except:
        return ""

def word():
    word = ""
    i = 1
    while(i <= len(sys.argv)-2):
        word += sys.argv[i] +"-"
        i+=1
    word += sys.argv[i]
    return word

response = getPageContent("https://www.merriam-webster.com/dictionary/" + word())

print "[looking for the meaning...]"
for i in range(len(response)):
    if '<meta name="description"' in response[i]:
        try:
            print "Meaning of", word(), ":", response[i].split(':')[1][1:]
        except:
            print "Couldn't find your word on the website"