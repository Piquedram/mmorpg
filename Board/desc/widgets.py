from ckeditor_uploader.widgets import CKEditorUploadingWidget


class MyCustomCKEditorWidget(CKEditorUploadingWidget):
    template_name = 'media_display.html'
