

test: test1 test2

test1: 
	# Check is all major command are working without generating and error
	./clip --help
	./clip google.com
	./clip -e http://cl.ip/vpZgdTd8th
	./clip --expand http://cl.ip/vpZgdTd8th	

test2: 
	# Shorten a list of urls, expand them back and check if they match
	./clip -i test.txt > test.out
	./clip --expand -i test.out > test.out2
	diff -u test.txt test.out2

clean: 
	rm clip.db test.out test.out2



