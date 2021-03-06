===================================
Passa: Toolset for Pipfile projects
===================================

.. image:: https://img.shields.io/pypi/v/passa.svg
    :target: https://pypi.org/project/passa

.. image:: https://img.shields.io/pypi/l/passa.svg
    :target: https://pypi.org/project/passa

.. image:: https://api.travis-ci.com/sarugaku/passa.svg?branch=master
    :target: https://travis-ci.com/sarugaku/passa

.. image:: https://ci.appveyor.com/api/projects/status/y9kpdaqy4di5nhyk/branch/master?svg=true
    :target: https://ci.appveyor.com/project/sarugaku/passa

.. image:: https://img.shields.io/pypi/pyversions/passa.svg
    :target: https://pypi.org/project/passa

.. image:: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg
    :target: https://saythanks.io/to/techalchemy

.. image:: https://readthedocs.org/projects/passa/badge/?version=latest
    :target: https://passa.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status


Summary
=======

Passa_ is a toolset for performing tasks in a Pipfile project, designed to be
used as a backing component of Pipenv_. It contains several components:

* A resolver designed for performing dependency resolution using a stateful
  look-forward algorithm to resolve dependencies (backed by ResolveLib_).
* Interface to interact with individual requirement specifications inside
  Pipfile and Pipfile.lock (backed by RequirementsLib_).
* A command line interface to invoke the above operations.

.. _Passa: https://github.com/sarugaku/passa
.. _Pipenv: https://github.com/pypa/pipenv
.. _ResolveLib: https://github.com/sarugaku/resolvelib
.. _RequirementsLib: https://github.com/sarugaku/requirementslib


`Read the documentation <https://passa.readthedocs.io/>`__.
