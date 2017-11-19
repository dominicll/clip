

test: test1 test2 cover

test1: 
	# Test base api: get help, shorten and expand
	# Only check if execution succeed without errors or crash
	./clip --help
	./clip http://www.extremeprogramming.org/rules/simple.html
	./clip -e http://cl.ip/4u5jwS5lRD
	./clip --expand http://cl.ip/4u5jwS5lRD

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


readme4:
	./clip "../image/x.jpg"	
	./clip ftp://example.com/index.html

readme5:
	./clip "http://google.com"	
	./clip "http://google.com"	

readme6:
	./clip --short-url-prefix http://localhost:5000/ --key-length 4 --key-base 10 http://example.com

readme7:
	./clip "http://google.com"	
	./clip http://www.extremeprogramming.org/rules/simple.html
	echo 
	./clip --expand http://cl.ip/4u5jwS5lRD
	./clip -e http://cl.ip/2le961GJac

readme8:
	./clip --expand http://cl.ip/0000

readme-db1:
	./clip http://google.com/
	./clip --expand http://cl.ip/Ikb9uxtHru
	./clip --db-reset	
	./clip --expand http://cl.ip/Ikb9uxtHru

readme-algo1:
	./clip --db-reset	
	./clip --key-algo sha http://google.com/
	./clip --db-reset	
	./clip --key-algo sha http://google.com/

readme-algo2:
	./clip --db-reset	
	./clip --key-algo random http://google.com/
	./clip --db-reset	
	./clip --key-algo random http://google.com/



