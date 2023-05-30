from django.shortcuts import render, redirect
from .models import FileUpload

def upload_file(request):
    if request.method == 'POST':
        file = request.FILES['file']
        column_to_predict = request.POST['column_to_predict']
        upload = FileUpload(file=file, column_to_predict=column_to_predict)
        upload.save()
        return redirect('prediction:result', upload_id=upload.id)
    return redirect('prediction:result')  # Redirect to the result view

def result(request, upload_id=None):
    if upload_id is not None:
        upload = FileUpload.objects.get(id=upload_id)
        # Perform the prediction and obtain the encrypted result
        encrypted_result = perform_prediction(upload.file.path, upload.column_to_predict)
    else:
        encrypted_result = None  # Default result value when no upload ID is provided

    return render(request, 'prediction/result.html', {'result': encrypted_result})
