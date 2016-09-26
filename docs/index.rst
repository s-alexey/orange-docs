Welcome to Orange Docs documentation!
=====================================


==========
audowidget
==========


To generate documentation for a widget use ``autowidget`` directive.
For instance:

.. code-block:: rst

   .. autowidget:: Orange.widgets.visualize.owboxplot.OWBoxPlot


Result:

.. autowidget:: Orange.widgets.visualize.owboxplot.OWBoxPlot



===
ref
===


Use ``:ref:widget:`Name``` to refer a widget (for instance :ref:widget:`File`).



=======
towtree
=======

To generate a list of widget ordered by priority use ``towtree`` directive:

.. code-block:: rst

   .. towtree::
      :maxdepth: 1
      :glob:

      widgets/*


That outputs:

.. towtree::
   :maxdepth: 1
   :glob:

   widgets/*


