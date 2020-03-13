import pytest

from git_code_debt.file_diff_stat import FileDiffStat
from git_code_debt.file_diff_stat import Status
from git_code_debt.metric import Metric
from git_code_debt.metrics.imports import CheetahTemplateImportCount
from git_code_debt.metrics.imports import is_python_import
from git_code_debt.metrics.imports import is_template_import
from git_code_debt.metrics.imports import PythonImportCount
from git_code_debt.repo_parser import BLANK_COMMIT


@pytest.mark.parametrize(
    ('line', 'expected'), (
        (b'import collections', True),
        (b'from collections import defaultdict', True),
        (b'from foo import bar as baz', True),
        (b'import bar as baz', True),
        (b'#import foo as bar', False),
        (b'from with nothing', False),
        (b'    import foo', True),
        (b'herpderp', False),
    ),
)
def test_python_imports(line, expected):
    assert is_python_import(line) == expected


@pytest.mark.parametrize(
    ('line', 'expected'), (
        (b'#import foo', True),
        (b'#from foo import bar', True),
        (b'#from foo import bar as baz', True),
        (b'#import bar as baz', True),
        (b'    #import foo', True),
        (b'## Nothing to import from here', False),
        (b'herpderp', False),
    ),
)
def test_template_imports(line, expected):
    assert is_template_import(line) == expected


def test_python_import_parser():
    parser = PythonImportCount()
    input_stats = (
        FileDiffStat(
            b'test.py',
            [b'import collections', b'from os import path'],
            [b'import os.path', b'nothing'],
            Status.ALREADY_EXISTING,
        ),
    )

    metric, = parser.get_metrics_from_stat(BLANK_COMMIT, input_stats)
    assert metric == Metric('PythonImportCount', 1)


def test_template_import_parser():
    parser = CheetahTemplateImportCount()
    input_stats = (
        FileDiffStat(
            b'test.tmpl',
            [b'#import collections', b'#from os import path'],
            [b'#import os.path', b'nothing'],
            Status.ALREADY_EXISTING,
        ),
    )

    metric, = parser.get_metrics_from_stat(BLANK_COMMIT, input_stats)
    assert metric == Metric('CheetahTemplateImportCount', 1)
