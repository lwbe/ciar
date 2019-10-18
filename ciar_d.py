# this module needs a .py file containing a class.

import ciar

import sys,os,importlib,inspect
import argparse


# creating the parser
parser = argparse.ArgumentParser(description="Start a python interpreter using the .py file supplied")
parser.add_argument('python_module',metavar='file')

args = parser.parse_args()

filename=args.python_module
if os.path.isfile(filename):
    sys.path.append(os.path.dirname(filename))
    if filename.endswith(".py"):
        mod=importlib.import_module(filename[:-3])
    else:
        print("Error : expecting a file ending in .py")
        sys.exit(0)
else:
    parser.print_help()
    parser.print_usage()
    sys.exit(0)


# we now extract the class
classes = [i for i in dir(mod) if (not i.startswith("__")) and i != "ciar" ]
if len(classes) > 1:
    print("we can only have one class in the file found %d : (%s)" % (len(classes),", ".join(classes)))
    sys.exit(0)

# and we get one instance
cla = classes[0]

inst = mod.__dict__[cla]

print("inspecting class:")
for m in inspect.getmembers(inst):
    if not m[0].startswith("__"):
        if inspect.isfunction(m[1]):
            print("%s is function with signature: %s" % (m[0],str(inspect.signature(m[1]))))



all_instance=[]
for i in range(2):
    # we create an instance
    inst = mod.__dict__['A']()
    all_instance.append(inst)
    print("before ",inst.a)
    
    # we get the method
    met = getattr(inst,"set_a")
    
    # a list of args
    list_arg = [3+i]
    
    # calling the method with args
    met(*list_arg)

    print("after ",inst.a)

for i in range(2):
    print(i," value",all_instance[i].a)
    
