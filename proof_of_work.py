import sys
import hashlib
import argparse

def proof_of_work(string, level=1, verbose=False):
    count = 0
    while True:
        for x in range(0, 256):
            string += chr(x)
            h = hashlib.sha256(b'{0}'.format(string)).hexdigest()
            count += 1
            if verbose:
                print("Try: {0} - {1}".format(count, h))
            if h[0:level] == ('0' * level):
                print("Coin costed {0} tests.".format(count))
                return

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--string", help="String to test", required=True)
    parser.add_argument("-l", "--level", help="Level of difficulty", type=int, default=1)
    parser.add_argument("-v", "--verbose", action="store_true")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse()
    proof_of_work(args.string, args.level, args.verbose)
