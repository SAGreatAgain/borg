import ConfigParser
import os
import urllib
import getpass
import socket


#log signature
#the log signature is an md5 hash of the username + passcode
def logSecure(logRepo):
	print "ayyy"

#create signature and the log file
def cSign(logRepo):
	print "ayyy"

#function to write to log file
def log(a,d, logFile):
	currentTime = urllib.urlopen("http://just-the-time.appspot.com/")
	currentTime = currentTime.read()
	#print currentTime

	user = getpass.getuser()
	#print user

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("gmail.com",80))
	ipaddr = (s.getsockname()[0])
	s.close()
	#print ipaddr

	#print action

	#print destination

	logLine = "[{0}]\t[{1}]\t[{2}]\t[{3}]\t[{4}]\n".format(currentTime,user,ipaddr,a,d)
	logFile.write(logLine)


def main():

	action = "backup"
	destination = "\home\steal\Desktop\\backups"
	config = ConfigParser.RawConfigParser()
	config.read('logging.cfg')

	logScope = config.get('borglog', 'logScope')
	logRepo = config.get('borglog', 'logRepo')
	isRemote = config.getboolean('borglog', 'isRemote')

	if not os.path.exists(logRepo) or not os.path.getsize(logRepo) > 0:
		cSign(logRepo)

	if not logSecure:
		print "The log file has been tampered with, terminating logging"
		exit(0)
	
	if isRemote:
		#mount the filesystem then use it
		print "Mounting %s"%logRepo

	try:
	    lf = open(logRepo, 'a+')

	except OSError:
	    # handle error here
	    print "Cannot open log file for editing"
	    exit(1)

	if logScope == "all":
		log(action,destination,lf)
	elif logScope == "none":
		exit(0)
	elif logScope == "back":
		if action == "backup":
			log(action,destination,lf)
		else:
			exit(0)
	elif logScope == "rest":
		if action == "restore":
			log(action,destination,lf)
		else:
			exit(0)
	elif logScope == "bare":
		if action == "backup" or action == "restore":
			log(action,destination,lf)
		else:
			exit(0)
	else:
		print "Incorrect log configuration for logScope"
		exit(1)

if __name__ == '__main__':
	main()