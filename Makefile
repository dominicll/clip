

test: test1 test2 cover

test1: 
	# Test base api: get help, shorten and expand
	# Only check if execution succeed without errors or crash
	./clip --help
	./clip http://google.com
	./clip -e http://cl.ip/2le961GJac
	./clip --expand http://cl.ip/2le961GJac

test2:
	# Test if shortened urls are reexpanded to same urls 
	./clip -i test.txt > test.out
	./clip --expand -i test.out > test.out2
	diff -u test.txt test.out2

cover:
	# Run 
	pytest --cov=clip
	coverage html

clean: 
	-rm clip.db test.out test.out2 *.pyc


test3: 
	-rm clip.db
	./clip --key-base 4 --key-length 1 --key-algo random http://google.com/1
	./clip --key-base 4 --key-length 1 --key-algo random http://google.com/2
	./clip --key-base 4 --key-length 1 --key-algo random http://google.com/3
	./clip --key-base 4 --key-length 1 --key-algo random http://google.com/4
	./clip --key-base 4 --key-length 1 --key-algo random http://google.com/5
	cat clip.db

test4: 
	-rm clip.db
	./clip --key-base 4 --key-length 1 --key-algo sha http://google.com/1
	./clip --key-base 4 --key-length 1 --key-algo sha http://google.com/2
	./clip --key-base 4 --key-length 1 --key-algo sha http://google.com/3
	./clip --key-base 4 --key-length 1 --key-algo sha http://google.com/4
	./clip --key-base 4 --key-length 1 --key-algo sha http://google.com/5
	cat clip.db

