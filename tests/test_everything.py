import pytest

from namer.lib import Directory


@pytest.fixture
def datasample():
    return [
        ('/path/to/files/firstset',
            [],
            ['63a0eb269458451c957cfec02d40de01.log']
        ),
        ('/path/to/files/secondset',
            [],
            ['1b43e3aac15849d19c88621021c3cd4a.log']
        ),
        ('/path/to/files/thirdset',
            [],
            ['c11a8ea16f0f4878b7dc07d5ae050d0a.log']
        ),
        ('/path/to/files/fourthset',
            [],
            ['ca640cf4b07a4a5591f09523614bb4b9.log',
            '._ca640cf4b07a4a5591f09523614bb4b9.log']
        ),
        ('/path/to/files/fifthset',
            [],
            ['fifthset.log']
        ),
        ('/mnt/pool0/downloads/sixthset',
            [],
            ['sixthset.log']
        ),
    ]


def test_parent_path(datasample):
    for testcase, expected in zip(
        datasample,
        [
            'firstset', 'secondset', 'thirdset', 'fourthset', 'fifthset', 'sixthset'
        ]
    ):
        assert Directory(testcase).parent == expected


@pytest.mark.parametrize('pattern, expected', (
    ('1b43e3aac15849d19c88621021c3cd4a.log', True),
    ('ca640cf4b07a4a5591f09523614bb4b9.log', True),
    ('ca640cf4b07a4a5_591f09523614bb4b9.log', False),
    ('c11a8ea16f0f4878b7dc07d5ae050d0a', False),
    ('c11a8ea1.123', False),
    ('sixthset.log', False)
))
def test_name_pattern(pattern, expected):
    assert Directory._filename_is_candidate(pattern) is expected
