===============================
Nummifier
===============================


.. image:: https://img.shields.io/pypi/v/nummifier.svg
        :target: https://pypi.python.org/pypi/nummifier

.. image:: https://img.shields.io/travis/etscrivner/nummifier.svg
        :target: https://travis-ci.org/etscrivner/nummifier

.. image:: https://readthedocs.org/projects/nummifier/badge/?version=latest
        :target: https://nummifier.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/etscrivner/nummifier/shield.svg
     :target: https://pyup.io/repos/github/etscrivner/nummifier/
     :alt: Updates


Abymal Nummification of the Signifier or fun with numerical coincidence. Based
on https://www.urbanomic.com/gematrix.html


* Free software: BSD license
* Documentation: https://nummifier.readthedocs.io.


Features
--------

* Compute the Qabbalistic nummification of any arbitrary string using the
  English alpha.
* Maintain a database of nummifications for finding synchronicities.

Usage
-----

To find the nummification of a given string AND commit that string to your
database type the following:

.. code::

    $ nummifier nummify --commit "discipline"
    [13, 18, 28, 12, 18, 25, 21, 18, 23, 14]
    190
    10
    1
    
    190=LIBERALISM
    190=NIETZSCHE
    190=DISCIPLINE
    
    10=SPINOZA
    10=LIBERALISM
    10=PLATO
    10=NIETZSCHE
    10=HEGEL

    1=SPINOZA
    1=LIBERALISM
    1=PLATO
    1=NIETZSCHE
    1=HEGEL
    1=SIGNIFIED
    1=FREE ENTERPRISE
    1=PREDICTION MARKET
    1=RUSSIAN ROULETTE
    1=DISCIPLINE


Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

