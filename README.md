# clip - URL Shortener Challenge
Python URL shortener on the command line with focus on code simplicity. Shortened URLs survive an application restart through the json data file _clip.db_. 

Shorten an url using _clip_:
```
$ ./clip http://www.extremeprogramming.org/rules/simple.html
http://cl.ip/KAROPTAnKo
```

To expand a previsously shorten url:
```
$ ./clip --expand http://cl.ip/KAROPTAnKo
http://www.extremeprogramming.org/rules/simple.html
```

Shorten  multiples URLs from a file with _--input_. (Can be combined with --expand to expand multiples short URLs.)
```
$ ./clip --input test.txt 
http://cl.ip/vpZgdTd8th
http://cl.ip/vpZgdTd8th
http://cl.ip/DA7CnPi4vp
http://cl.ip/fWebvNyPE1
http://cl.ip/9nCqRO6j5Y
```

Get information on more options:
```
$ ./clip --help
usage: clip [-h] [-e] [-p PERSISTFILENAME] [-i INPUTFILENAME] [URL [URL ...]]

Python URL shortener on the command line with focus on code simplicity.

positional arguments:
  URL                   URLs to shorten or expand.

optional arguments:
  -h, --help            show this help message and exit
  -e, --expand          expand URL from a previously generated short URL.
  -p PERSISTFILENAME, --persist PERSISTFILENAME
                        filename to use for persistance database. Default to
                        clip.db
  -i INPUTFILENAME, --input INPUTFILENAME
                        read URLs from an input file instead of the command
                        line. One url by line.
```


