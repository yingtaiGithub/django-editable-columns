# -*- encoding: utf-8 -*-
from datatableview.views import XEditableDatatableView
from datatableview import Datatable
from datatableview import helpers

from .models import BatchException

class XEditableColumnsDatatableView(XEditableDatatableView):
    template_name = "sample.html"
    model = BatchException
    class datatable_class(Datatable):
        class Meta:
            columns = ['batchExceptionID', 'batchID', 'createdBy', 'createdOn', 'modifiedBy', 'modifiedOn', 'fileName', 'exceptionReason']
            processors = {
                'batchExceptionID': helpers.make_xeditable,
                'batchID': helpers.make_xeditable,
                'createdBy': helpers.make_xeditable,
                'createdOn': helpers.make_xeditable,
                'modifiedBy': helpers.make_xeditable,
                'modifiedOn': helpers.make_xeditable,
                'fileName': helpers.make_xeditable,
                'exceptionReason': helpers.make_xeditable,
            }


