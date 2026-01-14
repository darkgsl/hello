#!/usr/bin/env python3

import datetime
import socket

def do_magic():
  now = datetime.datetime.now()
  hostname = socket.gethostname()
  return "Hello  from ->  {0} <- ! {1}".format(hostname, now)

def application(env, start_response):
  start_response('200 OK', [('Content-Type', 'text/html')])
  return [do_magic().encode()]

if __name__ == "__main__":
  print(do_magic())
