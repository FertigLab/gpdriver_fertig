GenePattern Driver Package for the Fertig Lab
=============================================

There are four repositories that form the core infrastructure used on genepattern.org for the Fertig lab.

`gpdriver_fertig`_ This python package manages the infrastructure and pulls updates from the other three

`fertigaws`_ This python package provides an interface to the specific AWS resources managed by the Fertig lab

`CondaEnvironments`_ This is a collection of conda environments with installation procedure that installs a kernel from the environment into the local Jupyter notebook server

`GenePatternWorkflows`_ This is a collection of example notebooks that shows how to use the Gene Pattern infrastructure

.. _gpdriver_fertig: https://github.com/FertigLab/gpdriver_fertig 
.. _fertigaws: https://github.com/FertigLab/fertigaws 
.. _CondaEnvironments: https://github.com/FertigLab/CondaEnvironments
.. _GenePatternWorkflows: https://github.com/FertigLab/GenePatternWorkflows


Installation on GenePattern
===========================

Open a new terminal and run these two commands:

::

  $ /opt/conda/envs/python3.6/bin/pip install git+https://github.com/FertigLab/gpdriver_fertig.git
  $ /opt/conda/envs/python3.7/bin/pip install git+https://github.com/FertigLab/gpdriver_fertig.git
