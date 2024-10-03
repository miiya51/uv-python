import pytest

@pytest.fixture
def readable_file():
    print('\nopen file\n')
    f = open("test_file.txt")
    yield f
    print('\nclose file\n')
    f.close()
    
def test_read_file(readable_file):
    assert readable_file.read() == "test"