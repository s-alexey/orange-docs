from docutils import nodes

__version__ = '0.1'


def setup(app):
    app.setup_extension('sphinx.ext.autodoc')
    app.setup_extension('sphinx.ext.napoleon')
    app.add_object_type('widget', 'widget', indextemplate='%s Widget',
                        ref_nodeclass=nodes.Invisible)
