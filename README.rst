Logger: Setup log default config
========================================================

Build
====

How to build this module:

.. code-block:: console
    
    python setup.py sdist

Usage on apps
====

Install:

.. code-block:: console

    pip install git+git://github.com/aeciovc/logger.git

    or, after a local build:

.. code-block:: console

    pip install logger-0.0.1.tar.gz


Import:

.. code-block:: python
    
    from logger import logger

Set a different level:

.. code-block:: python
    
    logger.setLevel(logging.DEBUG)

