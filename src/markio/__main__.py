import argparse
import markio


# Create an argument parser.
parser = argparse.ArgumentParser('markio')
parser.add_argument(
    '--validate', '-v',
    action='store_true',
    help='validate input file'
)
parser.add_argument(
    '--debug', '-d',
    action='store_true',
    help='enable debugging mode'
)

parser.add_argument('input', help='input Markio file')


def main(args=None):
    args = parser.parse_args(args)

    try:
        ast = markio.parse(args.input)
    except SyntaxError as ex:
        if args.debug:
            raise
        print('Error: ' + str(ex))
        raise SystemExit(not bool(args.validate))

    if args.validate:
        print('Your markio source is valid!')
        return

if __name__ == '__main__':
    main(['-h'])