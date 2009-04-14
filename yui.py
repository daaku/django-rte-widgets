from django.forms import Textarea
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.utils import simplejson as json


class YuiTextarea(Textarea):
    class Media:
        js = (
            'http://yui.yahooapis.com/combo?2.7.0/build/yahoo-dom-event/yahoo-dom-event.js&2.7.0/build/container/container_core-min.js&2.7.0/build/menu/menu-min.js&2.7.0/build/element/element-min.js&2.7.0/build/button/button-min.js&2.7.0/build/editor/editor-min.js',
        )
        css = {
            'all': ('http://yui.yahooapis.com/combo?2.7.0/build/assets/skins/sam/skin.css',)
        }

    def __init__(self, attrs=None, config={}):
        self.rte_config = {
            'handleSubmit': True
        }
        self.rte_config.update(config)
        super(YuiTextarea, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        rendered = super(YuiTextarea, self).render(name, value, attrs)
        context = {
            'id': mark_safe(json.dumps(attrs['id'])),
            'rte_config': mark_safe(json.dumps(self.rte_config)),
        }
        return rendered + mark_safe(render_to_string('rte_widgets/yui.html', context))
