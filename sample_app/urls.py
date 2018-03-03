# -*- encoding: utf-8 -*-

import re

from django.conf.urls import url
try:
    # Django < 1.10
    from django.conf.urls import patterns
except ImportError:
    def patterns(prefix, *urls):
        return list(urls)

from . import views


urlpatterns = patterns('',
   url(r'', views.XEditableColumnsDatatableView.as_view()),
)
