from .autowidget import WidgetDocument, process_widgets, TowTree

__version__ = '0.1'


def setup(app):
    app.setup_extension('sphinx.ext.autodoc')
    app.setup_extension('sphinx.ext.napoleon')

    app.add_object_type('widget', 'widget', indextemplate='%s Widget')

    app.add_crossref_type('widget', 'widget', indextemplate='', ref_nodeclass=None,
                          objname='widget')

    app.add_autodocumenter(WidgetDocument)

    app.add_directive('towtree', TowTree)
    app.connect('doctree-resolved', process_widgets)
