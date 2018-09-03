from __future__ import print_function
from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should be started in global layout
app = Flask(__name__)



@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") != "intro.intro-custom.intro-custom-custom":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    name = parameters.get("names")

    pswrd = {'Ramesh':'ram123','Suresh':'sur345','Akash':'akki8','Deepak':'dpk00'}

    speech = "your password for name " + name + " is " + str(pswrd[name])
    print("Response:")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "FirstBot"
    }

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5050))

    print("Starting app on port %d" % port)

    app.run(debug=True, port=port, host='0.0.0.0')
