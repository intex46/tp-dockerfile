import argparse


def factorielle(n):
    if n == 0:
        return 1
    else:
        return n  * factorielle(n-1)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--number", help="le nombre factoriel",
                    default="0", required=False)
    args = parser.parse_args()
    if args.number:
        print(f"{args.number} factorial equal to : {factorielle(int(args.number))}")