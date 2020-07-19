from flask import Flask
from flask import jsonify
import whois
import datetime

app = Flask(__name__)


@app.route("/<domain_name>")
def hello(domain_name):
    # domain_name = request.args.get('domain_name')
    w = whois.whois(domain_name)
    w.expiration_date  # dates converted to datetime object
    datetime.datetime(2013, 6, 26, 0, 0)
    w.text  # the content downloaded from whois server u'\nWhois Server Version 2.0\n\nDomain names in the .com and .net'

    print(w)  # print values of all found attributes

    return jsonify(w)


if __name__ == '__main__':
    app.run()
