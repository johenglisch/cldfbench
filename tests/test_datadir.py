import shutil

import pytest

from cldfbench.datadir import *


@pytest.fixture
def datadir(tmpdir, fixtures_dir):
    for p in fixtures_dir.iterdir():
        if p.is_file():
            shutil.copy(str(p), str(tmpdir.join(p.name)))
    return DataDir(str(tmpdir))


def test_get_url(mocker):
    mocker.patch('cldfbench.datadir.requests', mocker.Mock(get=mocker.Mock()))
    get_url(None, log=mocker.Mock(warn=mocker.Mock()))


def test_datadir(datadir):
    datadir.write('fname', '{"a": 2}')
    assert datadir.read('fname')
    assert datadir.read_json('fname')['a'] == 2
    datadir.write('sources.bib', '@article{id,\ntitle={the title}\n}')
    assert len(datadir.read_bib()) == 1


def test_datadir_xml(datadir):
    assert datadir.read_xml('test.xml').find('b').text == 'b'


def test_datadir_excel(datadir):
    res = datadir.xls2csv(datadir / 'test.xls')
    assert res['Sheet2'].stem == 'test.Sheet2'

    datadir.xlsx2csv(datadir / 'test.xlsx')
    data = datadir.read_csv('test.Sheet2.csv')
    assert data[1] == ['1']


def test_datadir_download_and_unpack(datadir, mocker):
    mocker.patch(
        'cldfbench.datadir.get_url',
        mocker.Mock(
            return_value=mocker.Mock(
                iter_content=mocker.Mock(
                    return_value=[datadir.joinpath('test.zip').open('rb').read()]))))
    datadir.download_and_unpack(None)
    assert datadir.joinpath('setup.py').exists()
    datadir.download(None, 'fname')
    datadir.download(None, 'fname', skip_if_exists=True)
