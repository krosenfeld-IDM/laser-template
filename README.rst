========
Overview
========

Spatial models implemented with the LASER toolkit.

* Free software: MIT license

Installation
============

::

Nothing

Documentation
=============


https://laser-template.readthedocs.io/en/latest/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
