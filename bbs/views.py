from django.views.generic.base import View
from django.shortcuts import render

from . import APP_LABEL

class BbsView(View):
    template_name = '%s/index.html' % APP_LABEL

    def get(self, request):
        return render(request, self.template_name)
