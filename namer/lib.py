import os, re


class Directory:

    HEXLIKE = re.compile(r'^([a-f0-9]{10,})\.(.{3,4})$')
    PARENTPATH = re.compile(r'.*\/(?P<parent>[^/]+)$')

    entry = ('', [], [''])

    def __init__(self, os_walk_entry):
        self.entry = os_walk_entry  # ('path', [], ['list of filenames'...])

    @property
    def path(self) -> str:
        return self.entry[0]

    @property
    def parent(self) -> str:
        matches = self.PARENTPATH.fullmatch(self.path)
        return matches.groupdict().get('parent') if matches else None

    @property
    def filename(self) -> str:
        return self.entry[2][0]

    @staticmethod
    def is_candidate(entry: tuple) -> str:
        if len(entry[2]) == 1 and Directory._filename_is_candidate(entry[2][0]):
            return entry[2][0]

    @staticmethod
    def _filename_is_candidate(filename: str) -> bool:
        return bool(Directory.HEXLIKE.fullmatch(filename))


class Collection:

    top_path = ''
    entries = None

    def __init__(self, top_path=''):
        self.top_path = top_path
        self.load_entries()

    def load_entries(self, path=''):
        target_path = path or self.top_path
        candidates = tuple(
            Directory(d) for d in os.walk(target_path)
            if Directory.is_candidate(d)
        )
