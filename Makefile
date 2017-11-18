

test: test1 test2

test1: 
	# Check if all basic options are working without generating and error.
	./clip --help
	./clip htt://google.com
	./clip -e http://cl.ip/I8tDAsqAnP
	./clip --expand http://cl.ip/I8tDAsqAnP

test2: 
	# Shorten a list of urls, expand them back and check if they match
	./clip -i test.txt > test.out
	./clip --expand -i test.out > test.out2
	diff -u test.txt test.out2

clean: 
	rm clip.db test.out test.out2



