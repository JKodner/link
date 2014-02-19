def gethost():
	import urllib2
	host = "http://" + raw_input("Type in Domain Name\nhttp://")
	return host
def extractlink():
	import urllib2, re
	host = gethost()
	# pattern = r"<a +.*href *= *(\"|\')(.*)\1>"
	pattern = r"href *= *(\"|\')(.*)\1"
	try:
		url = urllib2.urlopen(host)
	except urllib2.URLError:
		raise urllib2.URLError("Host-Name not Existing")
		links = None
	finally:
		results = re.findall(pattern, url.read())
	return results

