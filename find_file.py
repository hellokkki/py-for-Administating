#!/usr/bin/python3

import subprocess
import sys
import os

for i in range(1, len(sys.argv)):
   print("arg:", i, "value:", sys.argv[i])


def find_files(file_name, **kwargs):
  path = kwargs.get('path', None)

  if path:
      output = subprocess.Popen(["find " + path + " -name " + file_name], stdout=subprocess.PIPE, shell=True).communicate()[0]
  else:
      output = subprocess.Popen(["find / -name " + file_name], stdout=subprocess.PIPE, shell=True).communicate()[0]
       
  output = output.decode()
  search_results = output.split('\n')
  print("results", search_results)
  return search_results


if len(sys.argv) == 3 & len(sys.argv) > 3:
    find_files(sys.argv[1], path=sys.argv[2])
else: 
    find_files(sys.argv[1])
