import os
from argparse import ArgumentParser

from lib import Collection, Directory


# primary execution
if __name__ == '__main__':

    here = os.path.abspath(os.getcwd())
    parser = ArgumentParser()
    parser.add_argument(
        '-p',
        '--path',
        default=here
    )
    args = parser.parse_args()
    collection = Collection(top_path=args.path)
    import pdb; pdb.set_trace()
    pass