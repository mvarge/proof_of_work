import sys
import random
import string
import hashlib
import argparse

def proof_of_work(prototype, level=1, verbose=False):
    if not prototype:
        prototype = random_prototype()
        print prototype
    count = 0
    while True:
        for y in range(0, 256):
            for x in range(0, 256):
                h = hashlib.sha256(b'{0}{1}'.format(prototype, chr(x))).hexdigest()
                count += 1
                if verbose:
                    print("Try: {0} - {1}".format(count, h))
                if h[0:level] == ('0' * level):
                    print("Coin costed {0} tests.".format(count))
                    return
            prototype = "{0}{1}".format(prototype, chr(y))

def random_prototype():
    return ''.join([random.choice(string.ascii_letters) for n in xrange(16)])

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--prototype", help="Prototype string to test")
    parser.add_argument("-l", "--level", help="Level of difficulty", type=int, default=1)
    parser.add_argument("-v", "--verbose", action="store_true")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse()
    proof_of_work(args.prototype, args.level, args.verbose)
