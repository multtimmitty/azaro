#!/usr/bin/python3
import random

azar = random.randint(100,254)
green="\033[1;32m"
red="\033[1;31m"
blue="\033[1;34m"
end="\033[00m"

print ("{}----------------------{}".format(red,end))
print ("{} azar: {}{}{}".format(blue,green,azar,end))
print ("{}----------------------{}".format(red,end))
