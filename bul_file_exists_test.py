import pytest
import os.path

@pytest.fixture
def bul_file(bul_file_name):
    bul_file_path = "C:\\Python_progs\\bul_tests\\" + bul_file_name
    return bul_file_path

def pytest_generate_tests(metafunc):
    metafunc.parametrize("bul_file_name", ['bul1.sdl','bul2.sdl','bul3.sdl'])

def test_file_exists(bul_file):
    assert os.path.isfile(bul_file)  

