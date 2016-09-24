import urllib.robotparser

rp = urllib.robotparser.RobotFileParser()
# as plain english set your URL you want to crawl
rp.set_url("http://www.bdjobs.com/robots.txt")
print(rp.read())
print(rp.can_fetch("*", "http://www.bdjobs.com"))


