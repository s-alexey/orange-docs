from sphinx.ext.autodoc import ClassDocumenter
import os

widget_template = """
{widget.description}

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


def render_widget(widget):
    return widget_template.format(widget=widget, dots='=' * len(widget.name),
                                  inputs=render_channels(widget.inputs),
                                  outputs=render_channels(widget.outputs))


class WidgetDocument(ClassDocumenter):
    """ :class:`Orange.widgets.widget.OWWidget` documenter.

    """
    objtype = 'widget'
    content_indent = ''
    titles_allowed = True

    def get_doc(self, encoding=None, ignore=1):
        """Bypass superclass' get_doc with custom documentation."""
        return [render_widget(self.object).split('\n')]

    def add_directive_header(self, sig):
        """Add the directive header and options to the generated content."""
        domain = getattr(self, 'domain', 'py')
        directive = getattr(self, 'directivetype', self.objtype)

        sourcename = self.get_sourcename()
        self.add_line(u'.. %s:%s:: %s' % (domain, directive, self.object.name),
                      sourcename)
        if self.options.noindex:
            self.add_line(u'   :noindex:', sourcename)
