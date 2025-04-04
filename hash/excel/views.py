import pandas as pd
from django.shortcuts import render
from .forms import UploadFileForm
from django.core.files.storage import FileSystemStorage

def upload_csv(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES["file"]
            fs = FileSystemStorage()
            filename = fs.save(uploaded_file.name, uploaded_file)
            file_url = fs.url(filename)
            file_path = fs.path(filename)
            df = pd.read_csv(file_path)
            table_html = df.to_html(classes="sortable table table-striped", index=False)
            table_html = table_html.replace('<th>', '<th onclick="sortTable(event)">')

            return render(request, "display.html", {"table": table_html, "file_url": file_url})
    else:
        form = UploadFileForm()
    
    return render(request, "home.html", {"form": form})
