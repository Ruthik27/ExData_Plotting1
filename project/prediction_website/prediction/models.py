from django.db import models

class FileUpload(models.Model):
    file = models.FileField(upload_to='uploads/')
    column_to_predict = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)