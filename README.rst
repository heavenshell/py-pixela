Pixela
======

.. image:: https://travis-ci.com/heavenshell/py-pixela.svg?branch=master
    :target: https://travis-ci.com/heavenshell/py-pixela
.. image:: https://pyup.io/repos/github/heavenshell/py-pixela/shield.svg
     :target: https://pyup.io/repos/github/heavenshell/py-pixela/
     :alt: Updates
.. image:: https://pyup.io/repos/github/heavenshell/py-pixela/python-3-shield.svg
     :target: https://pyup.io/repos/github/heavenshell/py-pixela/
     :alt: Python 3

`Pixela <https://pixe.la/>`_ API client for Python.

Installation
------------

::

  $ virtualenv --distribute pixela_sample
  $ source pixela_sample/bin/activate
  $ cd pixela_sample
  $ pip install pixela

Usage
-----

::

  from pixela import Pixela

  client = Pixela(username='YOUR_NAME', token='YOUR_NAME')

  # register
  client.create_user(agree_terms_of_service=True, not_minor=True)

  # create graph
  client.create_graph(
      graph_id='test-graph',
      name='graph-name',
      unit='commit',
      type='int',
      color='shibafu',
      timezone='Asia/Tokyo',
  )

  # register value
  from datetime import datetime

  date = datetime.strptime('2018-10-21', '%Y-%m-%d')
  res = self.client.create_pixel(graph_id='py-pixela', quantity=5, date=date)

LICENSE
=======
NEW BSD LICENSE.
