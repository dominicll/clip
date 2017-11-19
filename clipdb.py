#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Python URL shortener on the command line with focus on code simplicity."""

import argparse
import base64
import hashlib
import json
import os.path
import random
import string
import sys
import urlparse



#  shortToLong and longToShort are used as global database to store shorten URLs.
shortToLong = {}
longToShort = {}





def importDb(filename):
	global shortToLong, longToShort

	# Check if file exist before opening it. If file not found it will be created 
	# during exportDB().
	if (os.path.isfile(filename)):
		shortToLong = json.loads(open(filename).read())

	# Recreate inverse dict 
	for shortUrl, entry in shortToLong.items():
		longToShort[entry['longUrl']] = shortUrl

	return 


def exportDb(filename):
	# Export database in sorted json format to help inspection and tests.
	with open(filename, 'w') as file:
		file.write(json.dumps(shortToLong, sort_keys=True, indent=4))
		file.write("\n")
	return 



def lookupDbByShortUrlIndex(shortUrl):
	record = shortToLong.get(shortUrl, None)
	if record:
		return record['longUrl']
	else:
		return None

def lookupDbByLongUrlIndex(longUrl):	
	return longToShort.get(longUrl, None)


def insertDb(longUrl, shortUrl, iteration=None):
	global shortToLong, longToShort

	# Store short and long url verions in global storage. 
	if iteration:
		shortToLong[shortUrl] = {'longUrl':longUrl,'iter':iteration}
	else:
		shortToLong[shortUrl] = {'longUrl':longUrl}

	longToShort[longUrl] = shortUrl	
