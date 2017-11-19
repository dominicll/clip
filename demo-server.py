from flask import Flask, abort, redirect
import json

app = Flask(__name__)

shortToLong = {}

@app.route('/<shortUrl>')
def redirect_short_url(shortUrl):
    url = "http://www.bing.com/"
    print ("shortUrl", shortUrl)
    print shortToLong
    entry = shortToLong.get(shortUrl, None)
    if not entry:
        print "abort"
        abort(404)

    longUrl = entry["longUrl"]  
    print ("longUrl", longUrl)
    return redirect(longUrl)

if __name__ == '__main__':
    shortToLong = json.loads(open("clip.db").read())
    app.run(debug=True)
