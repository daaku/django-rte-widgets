from django.conf import settings
from django.forms import Textarea
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from os.path import join
import json


class WmdTextarea(Textarea):
    class Media:
        js = [join(settings.RTE_MEDIA_URL, path) for path in (
            'wmd-disable-autostart.js',
            'wmd/wmd.js',
        )]

    def __init__(self, attrs=None, config={}):
        self.rte_config = {
            'height': config.pop('height', '200px'),
            'width': config.pop('width', '700px'),
        }
        self.rte_config.update(config)
        super(WmdTextarea, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        rendered = super(WmdTextarea, self).render(name, value, attrs)
        context = {
            'id': mark_safe(json.dumps(attrs['id'])),
            'rte_config': mark_safe(json.dumps(self.rte_config)),
        }
        return rendered + mark_safe(render_to_string('rte_widgets/wmd.html', context))
