import sys, pytest
from dlx_datasets.scripts import eth_extract

def test_script():
    sys.argv[1:] = ['--connect=mongomock://localhost', '--database=test', '--output=out.json']
    eth_extract.run()