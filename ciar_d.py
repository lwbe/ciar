# this module needs a .py file containing a class.

import ciar

import sys,os,importlib,inspect
import argparse
import redis


# creating the parser
parser = argparse.ArgumentParser(description="Start a python interpreter using the .py file supplied")
parser.add_argument('python_module',metavar='file')

args = parser.parse_args()


file_name=args.python_module


if os.path.isfile(file_name):
    sys.path.append(os.path.dirname(file_name))
    if file_name.endswith(".py"):
        module_name = file_name[:-3]
        mod = importlib.import_module(module_name)
    else:
        print("Error : expecting a file ending in .py")
        sys.exit(0)
else:
    parser.print_help()
    parser.print_usage()
    sys.exit(0)


# we now extract the class
classes = [i for i in dir(mod) if i.startswith("cmd")] #(not i.startswith("__")) and i != "ciar" ]
if len(classes) > 1:
    print("we can only have one class in the file found %d : (%s)" % (len(classes),", ".join(classes)))
    sys.exit(0)

# and we get one instance
cla = classes[0]

inst = mod.__dict__[cla]()

print("inspecting class:")
for m in inspect.getmembers(inst):
    if not m[0].startswith("__"):
        if inspect.isfunction(m[1]):
            print("%s is function with signature: %s" % (m[0],str(inspect.signature(m[1]))))






def treat_pubsub(channel):
    pass



# init readis listener
r=redis.StrictRedis()



l=r.listener(module_name)
while True:
    # wait for something to happen

    kw,arguments = treat_pubsub(l)
    # if we have a init
    if kw == "init":
        # we have to instantiate the class
        pass
        # perform the init function with parameters

