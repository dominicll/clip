from flask import Flask, abort, redirect
import json
from urlparse import urlparse

app = Flask(__name__)

keyToLong = {}


@app.route('/<shortUrl>')
def redirect_short_url(shortUrl):

    longUrl = keyToLong.get("/"+shortUrl, None)
    if  longUrl:
        return redirect(longUrl)
    
    # Return "404 Not Found"
    abort(404)


if __name__ == '__main__':

    # Read shorturls data
    # Strip "http://cl.ip and only keep key as index
    shortToLong = json.loads(open("clip.db").read())
    for shortUrl in shortToLong.keys():
        o = urlparse(shortUrl)
        keyToLong[o.path] = shortToLong[shortUrl]['longUrl'] 


    # Start web server listening on localhost:5000 by default  
    print " # Starting app with {:d} short urls".format(len(keyToLong)) 
    app.run(debug=True)
