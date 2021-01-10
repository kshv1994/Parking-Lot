import sys

from project_controller import route


def main(filename):
    """Main driver function for execution of the code"""
    infile = open(filename, 'r')

    for line in infile:
        route(line)


if __name__ == '__main__':
    main(sys.argv[1])
