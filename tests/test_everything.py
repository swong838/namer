import pytest

from namer.lib.utils import HEXLIKE



@pytest.fixture
def datasample():
    return [
        ('/path/to/files/firstset',
            [],
            ['63a0eb269458451c957cfec02d40de01.mp4']
        ),
        ('/path/to/files/secondset',
            [],
            ['1b43e3aac15849d19c88621021c3cd4a.mp4']
        ),
        ('/path/to/files/thirdset',
            [],
            ['c11a8ea16f0f4878b7dc07d5ae050d0a.mp4']
        ),
        ('/path/to/files/fourthset',
            [],
            ['ca640cf4b07a4a5591f09523614bb4b9.mp4',
            '._ca640cf4b07a4a5591f09523614bb4b9.mp4']
        ),
        ('/path/to/files/fifthset',
            [],
            ['fifthset.mp4']
        ),
        ('/mnt/pool0/downloads/sixthset',
            [],
            ['sixthset.mp4']
        ),
    ]


def test_scan_for_items(datasample):
    assert len(datasample) == 0


@pytest.mark.parametrize
