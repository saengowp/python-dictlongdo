# -*- coding: utf-8 -*-

'''
Author: Pongsakorn Sommalai (bongtrop@gmail.com)
Date: 08/03/2016
Description: Server to translate en2thai and return it by json
'''

# Default
import json
import api

# Web Server
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor

class en2th(Resource):
    isLeaf = True

    def render_GET(self, request):
        request.responseHeaders.addRawHeader(b"content-type", b"application/json")
        if "word" not in request.args:
            return json.dumps({"status": "fail", "data": "Please define args word."})

        return json.dumps({"status": "success", "data": api.en2thai(request.args["word"][0])})


resource = en2th()
factory = Site(resource)
reactor.listenTCP(10001, factory)
reactor.run()
