# -*- coding=utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

import resolvelib


def print_title(text):
    print('\n{:=^84}\n'.format(text))


def print_requirement(r, end='\n'):
    print('{:>40}'.format(r.as_line().split('--hash')[0]), end=end)


def print_dependency(state, key):
    print_requirement(state.mapping[key], end='')
    parents = sorted(
        state.graph.iter_parents(key),
        key=lambda n: (-1, '') if n is None else (ord(n[0].lower()), n),
    )
    for i, p in enumerate(parents):
        if p is None:
            line = '(user)'
        else:
            line = state.mapping[p].as_line().split('--hash')[0]
        if i == 0:
            padding = ' <= '
        else:
            padding = ' ' * 44
        print('{pad}{line}'.format(pad=padding, line=line))


class StdOutReporter(resolvelib.BaseReporter):
    """Simple reporter that prints things to stdout.
    """
    def __init__(self, requirements):
        super(StdOutReporter, self).__init__()
        self.requirements = requirements

    def starting(self):
        self._prev = None
        print_title(' User requirements ')
        for r in self.requirements:
            print_requirement(r)

    def ending_round(self, index, state):
        print_title(' Round {} '.format(index))
        mapping = state.mapping
        if self._prev is None:
            difference = set(mapping.keys())
            changed = set()
        else:
            difference = set(mapping.keys()) - set(self._prev.keys())
            changed = set(
                k for k, v in mapping.items()
                if k in self._prev and self._prev[k] != v
            )
        self._prev = mapping

        if difference:
            print('New pins: ')
            for k in difference:
                print_dependency(state, k)
        print()

        if changed:
            print('Changed pins:')
            for k in changed:
                print_dependency(state, k)
        print()