import argparse
from models.director import Director

parser = argparse.ArgumentParser(description="Movie store")
parser.add_argument("-ad", "-adddr", help="Add director")
parser.add_argument("-ld", "-listdr", help="List all directors")
parser.add_movie("-am", "-addmv", help="Add movie")
args = parser.parse_args()

if args.adddr:
    Director(args.adddr)
elif args.listdr:
    print(Director.all())
elif args.addmv:
    Director.add_movie(args.addmv)
else:
    print("Invalid command!")
