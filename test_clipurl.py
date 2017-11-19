import pytest

import clip
from clipurl import *



def test_generateKey():
	# generateKey(longUrl, key_algo, key_base, key_length)
	(key,iter)= generateKey("http://example.com/", "http://cl.ip/", "sha", 64, 2)
	assert(key== "lQ")

	(key,iter)= generateKey("http://example.com/",  "http://cl.ip/", "random", 64, 10)
	assert(len(key) == 10)

	with pytest.raises(KeyError):
		generateKey("http://example.com/",  "http://cl.ip/", "xyz", 64, 10)


def test_shortenUrl():
	# Test invalid urls
	for u in ("www.example.com", "www.example.com/", "ftp://www.example.com/"):
		res = shortenUrl(u, "http://cl.ip/", "sha", 64, 10)
		assert(res=="")	


	# Use a key alphabet of 4 character with a key size of 1 giving a key space of 4. 
	# Try to insert more ulrs than there is space expecting a KeyErrror on the fith insertion.
	shortenUrl("http://example.com/1", "http://cl.ip/", "sha", 4, 1)
	shortenUrl("http://example.com/2", "http://cl.ip/", "sha", 4, 1)
	shortenUrl("http://example.com/3", "http://cl.ip/", "sha", 4, 1)
	shortenUrl("http://example.com/4", "http://cl.ip/", "sha", 4, 1) 
	with pytest.raises(KeyError):
		shortenUrl("http://example.com/5", "http://cl.ip/", "sha", 4, 1)


	# Use a key alphabet of 4 character with a key size of 1 giving a key space of 4. 
	# Try to insert more ulrs than there is space expecting a KeyErrror on the fith insertion.
	shortenUrl("http://example.com/1", "http://cl.ip/", "random", 4, 1)
	shortenUrl("http://example.com/2", "http://cl.ip/", "random", 4, 1)
	shortenUrl("http://example.com/3", "http://cl.ip/", "random", 4, 1)
	shortenUrl("http://example.com/4", "http://cl.ip/", "random", 4, 1) 
	with pytest.raises(KeyError):
		shortenUrl("http://example.com/5", "http://cl.ip/", "random", 4, 1)		

def test_originalUrl(): 
 	u = expandUrl("http://notthere.com/x")
 	assert(u=="")

def test_shorten_expand():
	u = shortenUrl("http://www.google.com/", "http://cl.ip/" , "sha", 64, 10)
	assert(u=="http://cl.ip/QeqGeYywHS")

	u = expandUrl("http://cl.ip/QeqGeYywHS")
	assert(u=="http://www.google.com/")


def test_validateFullAbsoluteUrl():
	# validateFullAbsoluteUrl(longUrl)
	b = validateFullAbsoluteUrl("http://example.com/x")
	assert(b)
	b = validateFullAbsoluteUrl("www.example.com")
	assert(not b)
	b = validateFullAbsoluteUrl("../index.html")
	assert(not b)


	