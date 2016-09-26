from sphinx import addnodes
from sphinx.directives.other import TocTree
from sphinx.ext.autodoc import ClassDocumenter, bool_option
import os

widget_template = """
{widget.name}
{dots}

{widget.description}

.. figure:: {icon}


Signals
-------

**Inputs**

{inputs}

**Outputs**

{outputs}
"""

chanel_template = "- **{chanel.name}** {doc}"
no_channels = "  (None)"


def render_channels(channels):
    return '\n'.join(chanel_template.format(chanel=c, doc=c.doc or '') for c in channels) or no_channels


def render_widget(widget, icon):
    return widget_template.format(widget=widget, dots='=' * len(widget.name),
                                  inputs=render_channels(widget.inputs),
                                  outputs=render_channels(widget.outputs), icon=icon)


class WidgetDocumenter(ClassDocumenter):
    """ :class:`Orange.widgets.widget.OWWidget` documenter.

    """
    objtype = 'widget'
    content_indent = ''
    titles_allowed = True
    option_spec = {
        'icon': lambda x: x,
        'noindex': bool_option,
    }

    def get_doc(self, encoding=None, ignore=1):
        """Bypass superclass' get_doc with custom documentation."""
        if not hasattr(self.env, 'orange_all_widget'):
            self.env.orange_all_widget = {}

        self.env.orange_all_widget[self.env.docname] = {
            'name': self.object.name,
            'module': self.modname,
            'priority': self.object.priority,
            'document': self.env.docname,
        }

        if self.options.get('icon', None):
            icon = self.options['icon']
        else:
            icon = '/' + os.path.join(
                os.path.abspath(os.path.join(self.module.__file__, '..')), self.object.icon)
        return [render_widget(self.object, icon=icon).split('\n')]

    def add_directive_header(self, sig):
        """Add the directive header and options to the generated content."""
        domain = getattr(self, 'domain', 'py')
        directive = getattr(self, 'directivetype', self.objtype)

        sourcename = self.get_sourcename()
        self.add_line(u'.. %s:%s:: %s' % (domain, directive, self.object.name),
                      sourcename)
        if self.options.noindex:
            self.add_line(u'   :noindex:', sourcename)


class TowTree(TocTree):
    def run(self):
        res = super().run()
        # Mark widgets toctree nodes.
        for compound in res:
            for node in compound:
                node.attributes['widget'] = True
        return res


def process_widgets(app, doctree, fromdocname):
    env = app.builder.env
    if not hasattr(env, 'orange_all_widget'):
        return

    for node in doctree.traverse(addnodes.toctree):
        if node.attributes.get('widget', False):
            node.attributes['entries'] = sorted(node.attributes['entries'],
                                                key=lambda x: env.orange_all_widget[x[1]].get('priority', -1))
