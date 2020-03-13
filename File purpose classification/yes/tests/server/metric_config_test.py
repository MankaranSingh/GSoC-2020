import re
from unittest import mock

import pytest

from git_code_debt.server.metric_config import _get_commit_links_from_yaml
from git_code_debt.server.metric_config import _get_groups_from_yaml
from git_code_debt.server.metric_config import Group


def test_Group_from_yaml():
    # Simulate a call we would get from yaml
    group = Group.from_yaml(
        'BazGroup',
        metrics=['Foo', 'Bar'],
        metric_expressions=['^.*Baz.*$'],
    )

    assert group == Group(
        'BazGroup',
        frozenset(('Foo', 'Bar')),
        (re.compile('^.*Baz.*$'),),
    )


def test_Group_from_yaml_complains_if_nothing_useful_specified():
    with pytest.raises(TypeError) as excinfo:
        Group.from_yaml('G1', [], [])
    msg, = excinfo.value.args
    assert msg == (
        'Group G1 must define at least one of `metrics` or '
        '`metric_expressions`'
    )


def test_Group_contains_does_not_contain():
    group = Group('G', frozenset(('Foo', 'Bar')), (re.compile('^.*Baz.*$'),))
    assert not group.contains('buz')


def test_Group_contains_contains_by_name():
    group = Group('G', frozenset(('Foo', 'Bar')), (re.compile('^.*Baz.*$'),))
    assert group.contains('Foo')


def test_Group_contains_by_regex():
    group = Group('G', frozenset(('Foo', 'Bar')), (re.compile('^.*Baz.*$'),))
    assert group.contains('FooBaz')


def test_get_groups_from_yaml_smoke():
    # Grapped from sample run
    groups_yaml = [
        {
            'Cheetah': {
                'metrics': [],
                'metric_expressions': ['^.*Cheetah.*$'],
            },
        },
        {
            'Python': {
                'metrics': [],
                'metric_expressions': ['^.*Python.*$'],
            },
        },
        {
            'CurseWords': {
                'metrics': [],
                'metric_expressions': ['^TotalCurseWords.*$'],
            },
        },
        {
            'LinesOfCode': {
                'metrics': [],
                'metric_expressions': ['^TotalLinesOfCode.*$'],
            },
        },
    ]

    groups = _get_groups_from_yaml(groups_yaml)
    assert (
        groups ==
        (
            # Regexes tested below
            Group('Cheetah', frozenset(), (mock.ANY,)),
            Group('Python', frozenset(), (mock.ANY,)),
            Group('CurseWords', frozenset(), (mock.ANY,)),
            Group('LinesOfCode', frozenset(), (mock.ANY,)),
        )
    )

    regexes = [group.metric_expressions[0].pattern for group in groups]
    assert (
        regexes ==
        [
            '^.*Cheetah.*$',
            '^.*Python.*$',
            '^TotalCurseWords.*$',
            '^TotalLinesOfCode.*$',
        ]
    )


def test_get_groups_from_yaml_no_metrics_provided():
    groups_yaml = [{'G1': {'metric_expressions': ['^Foo.*$']}}]
    groups = _get_groups_from_yaml(groups_yaml)
    # Regex tested below
    assert groups == (Group('G1', frozenset(), (mock.ANY,)),)
    assert groups[0].metric_expressions[0].pattern == '^Foo.*$'


def test_get_groups_from_yaml_no_metric_expressions_provided():
    groups_yaml = [{'G1': {'metrics': ['Foo']}}]
    groups = _get_groups_from_yaml(groups_yaml)
    assert groups == (Group('G1', frozenset(('Foo',)), ()),)


def test_get_commit_links_from_yaml_empty():
    assert _get_commit_links_from_yaml({}) == ()


def test_get_commit_links_from_yaml_one_entry():
    assert _get_commit_links_from_yaml({'foo': 'bar'}) == (('foo', 'bar'),)


def test_get_commit_links_from_yaml_is_sorted():
    ret = _get_commit_links_from_yaml({'a': '1', 'b': '2', 'c': '3', 'd': '4'})
    assert ret == (('a', '1'), ('b', '2'), ('c', '3'), ('d', '4'))
