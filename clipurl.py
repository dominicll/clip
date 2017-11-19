#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Python URL shortener on the command line with focus on code simplicity."""

import hashlib
import random
import string
import urlparse


from clipdb import *

# Build base64 url safe list of characters
keyAlphabet64 =  string.digits + string.ascii_uppercase + string.ascii_lowercase + "-_"


def validateFullAbsoluteUrl(longUrl):
	o = urlparse.urlparse(longUrl)

	# Not an absolute URL without a hostname
	if not o.netloc:
		return False

	# Not a full URL without a scheme. 
	if o.scheme != "http":
		return False

	return True


def generateKeyRandom(allowedKeyChars, key_length):	
	# Randomly pick key_length characters from the list of allowed characters
	key = ""
	for _ in range(key_length):
		key += random.choice(allowedKeyChars)

	return key


def generateKeySha(longUrl, allowedKeyChars, key_length, iteration):
	# Use  an hash of the longUrl and iteration number as key. In case the 
	# key is already use iteration number can be incremented to generate 
	# a different key. 

	# Create hash
	m = hashlib.sha224()
	m.update(longUrl)
	m.update(str(iteration))
	digest = m.digest() 
	digest = digest[0:key_length]

	# Encode hash has with allowed alphabet.
	allowedlen = len(allowedKeyChars)
	key = ""
	for d in digest:
		# Todo: ord(d) is a char between 0-255. 
		# Using "modulo allowedlen" is not always giving the best spread of keys. 
		# Use only base64 for key or more arithmetic with bignum instead to fix.
		key +=  allowedKeyChars[ ord(d) % allowedlen ]

	return key


def generateKey(longUrl, url_prefix, key_algo, key_base, key_length):
	# Build the list of allowed characters to use in the key. Create maximum list 
	# of 64 url safe characters than reduce it to specified size. 

	allowedKeyChars = keyAlphabet64[0:key_base]

	# Iterate as long as we do not have a shortUrl (only fist iteration) and
	# as long as this key is not already associated with another longUrl.
	key = None
	iteration = 0
	while( key == None or lookupDbByShortUrlIndex(url_prefix + key) != None):
		if key_algo == 'random':
			key = generateKeyRandom(allowedKeyChars, key_length)
		elif key_algo == 'sha':
			key = generateKeySha(longUrl, allowedKeyChars, key_length, iteration)
		else:
			raise KeyError("Unknow algorhith for key generation: " + key_algo)	

		iteration += 1
		if iteration > 50:
			# Prevent infinite loop if key space is getting full. 50 is arbitrary
			# as any more than two iteration is already showing crowding.
			raise KeyError("Cannot find unused key (tried 50 times) for " + longUrl)

	return (key, iteration)



def shortenUrl(longUrl, url_prefix, key_algo, key_base, key_length):
	if not validateFullAbsoluteUrl(longUrl):
		sys.stderr.write("Error: Not full absolute url. Urls must start with http://\n")
		return ""

	# If this longUrl exist in db return already created  shortUrl
	shortUrl = lookupDbByLongUrlIndex(longUrl)
	if shortUrl:
		return shortUrl

	#  Create a new key for this longUrl
	(key, iteration) = generateKey(longUrl, url_prefix, key_algo, key_base, key_length)

	# Add short and long url association in DB.
	# If more than one iteration was needed add this info in db to help debugging.
	shortUrl = url_prefix + key
	if iteration <= 1:
		insertDb(longUrl, shortUrl)
	else:
		insertDb(longUrl, shortUrl, iteration)

	return shortUrl


def expandUrl(u):
	longUrl = lookupDbByShortUrlIndex(u)
	if not longUrl:
		sys.stderr.write("Error: URL not found.\n")
		return ""

	return longUrl

