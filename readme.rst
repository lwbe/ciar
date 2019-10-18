Ciar
====

Introduction
------------
This software is to test some ideas about communication between multiple python instance through
redis. The basic idea is that each instances of python runs a class that can be called through
string passed by redis pubsub mechanism. This is done through class introspection.


redis
-----
Redis is a NoSQL database (in fact it only holds **key** **value** pairs with values being *strings*, *list*, *sets* or
*hashmaps*). It is reachable by network and thus can communicate between computers and can use password to protect
communication.

One of the features of redis is that it can do pub/sub and thus permits to communicate between
process that have subscribe to channel.

To install the redis server I used https://realpython.com/python-redis/.


class instrospection
--------------------
The advantage of python is that one can use specials method of a class to call a method.


the basic idea
--------------
This work is inspired by pyrame in the idea of transforming all the modules (that can be written in
python, C, Lua and R in the case of pyrame) in standalone processes.

I keep the idea of the mandatory sequence

- init
- config
- inval or deconfigration
- deinit

The idea is to push further the idea of having a simple set of function that can be translated
directly into a GUI or web based interface. And thus the configuration string should be
defined somewhere.

For now (October 2019 ) this is a toy.



To daemonize the module

- introspection of the class in the module
    - only one class per file
    - we should find the 4 functions mentionned above
    - check that we have an attribute called confstring
    - we get all the methods and get their signature.
- create an entry in redis with the name of the module as key and put inside
    - signatures.
- create a channel
- wait for actions to do from the channel.
    - the fist is to instantiate the class with an id
    - the actions should be done by

Tests
-----
On pyrame we should see if we can talk to the same module with two different ids. For example
with  thorlabs we set connect to both LTS300 set a very low speed and check that from two
different terminals we can move both stages at the same time. In this case we should probably
use the mutiprocessing module of python

We should also see if we can use C module with ctypes.