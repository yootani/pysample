from django.shortcuts import render
from doc.models import Document

# Create your views here.
def doc_list(request):
	documents = Document.objects.all()
	return render(request, 'doc/doc_list.html', {'docs': documents})
