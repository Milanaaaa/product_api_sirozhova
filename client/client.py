import urllib.request

fp = urllib.request.urlopen("http://0.0.0.0:5050/")

encodedContent = fp.read()
decodedContent = encodedContent.decode("utf8")

print(decodedContent)

fp.close()
