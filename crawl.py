import urllib2

# get source code
url = raw_input("> URL: ")
opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]

source = opener.open(url).read()

f = open("source.txt", "r+")
f.seek(0)
f.write(source)
f.truncate()
data = f.read()
print data

f = open("data.csv", "w")
