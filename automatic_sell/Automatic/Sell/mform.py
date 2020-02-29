from django import forms

class MessageForm(forms.Form):
    
    content =forms.CharField(widget=forms.Textarea,label="发送内容")
    