#!/usr/bin/python3
import random
import itertools
import sys, re, os, inspect, importlib

# Globals
prompt = ""
default_prompt = "ftech"
welcome_message = "Welcome to the {0} shell. Type 'help' after the ({0}) prompt to see a list of commands".format(default_prompt)
loaded_modules = []
context = None
commands = ['list', 'home', 'quit', 'exit', 'show', 'set', 'run', 'use', 'help']

# Commands

def help():
    """ For now, just list commands """

    print("Commands")
    print("--------")
    for command in commands:
        print(command)


def list():
    """ List available modules """

    # Dynamically find modules from the "modules" package. 
    # A python package called "modules" should be in the 
    # same folder as this script.
    files = os.listdir("modules")
    print("Modules")
    print("-------")
    for module in files:
        if module[0].isupper() and module != "Module.py":
            print(module[:module.index(".py")])


def home():
    """ Reset to default promp and no loaded modules """

    global context
    set_prompt(default_prompt)
    context = None


def quit():
    """ Exit the custom shell """

    sys.exit()


def exit():
    """ Exit the custom shell """

    sys.exit()


def show():
    """ Show the options for the currently loaded module """

    dashes = ""
    print(context.name)
    for i in range(0,len(context.name)):
        dashes += "-"
    print(dashes)
    print(context.info)
    print("----------")
    print("Options")
    print("-------")
    for k, v in context.options.items():
        print("{0} = {1}".format(k, v))


def set(args):
    """ Set an option for the currently loaded module """

    global context
    if context == None:
        print("You must load a module before you can set options.")
    else:
        context.options[args[0]] = args[1]


def run():
    """ Run the current module  """
    global context
    if context == None:
        output = "No module loaded."
    else:
        output = context.run()
    print(output)


def use(args):
    """ Set a module to be the current active module """

    global context
    global loaded_modules
    module_name = args[0]
    print("Using module {0}".format(module_name))
    set_prompt(module_name)
    module = importlib.import_module("modules.{0}".format(module_name))
    class_ = getattr(module, module_name) # Because the only class is the same
    instance = class_()
    loaded_modules.append(instance)
    context = instance

# Utility Functions

def set_prompt(arg):
    global prompt
    prompt = "({0}) ".format(arg)

# Main

def main():
    print(welcome_message)
    set_prompt(default_prompt)

    random.seed()

    while(True):
        #draw prompt
        sys.stdout.write("\033[1;36m")
        print(prompt, end='')
        sys.stdout.write("\033[0;0m")
        command = input().strip().split()
        if len(command) == 0:
            continue
        if command[0] not in commands:
            print("Not a command: {0}".format(command))
            continue
        try:
            if len(command) == 1:
                globals()[command[0].strip()]()
            else:
                globals()[command[0]](command[1:])
        except TypeError:
            print("Invalid command, probably bad args: {0}".format(command))

main()

