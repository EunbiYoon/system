from django.forms import ModelForm
from report.models import Comment

class CommentForm(ModelForm):
    class Meta:
        model=Comment
        fields=['body','id']