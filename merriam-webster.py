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
    for w in sys.argv[1:]:
        word += w
    return word

response = getPageContent("https://www.merriam-webster.com/dictionary/" + word())

print "[looking for the meaning...]"
for r in response:
    if '<meta name="description"' in r:
        try:
            print "Meaning of", word(), ":", r.split(':')[1][1:]
        except:
            print "Couldn't find your word on the website"
