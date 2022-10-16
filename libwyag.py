import argparse
import collections
import configparser
import hashlib
import os
import re
import sys
import zlib

argparser = argparse.ArgumentParser(description="The stupid content tracker")

argsubparsers = argparser.add_subparsers(title="Commands", dest="command")
argsubparsers.required = True


def main(argv=sys.argv[1:]):
    args = (argparser.parse_args(argv))

    if   args.command == "add"              : cmd_add(args)
    elif args.command == "cat-file"         : cmd_cat_file(args)
    elif args.command == "checkout"         : cmd_checkout(args)
    elif args.command == "commit"           : cmd_commit(args)
    elif args.command == "hash-object"      : cmd_hash_object(args)
    elif args.command == "init"             : cmd_init(args)
