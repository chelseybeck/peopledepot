from django import forms
from models import RecurringEvent


class RecurringEventForm(forms.ModelForm):
    class Meta:
        model = RecurringEvent
        fields = (
            "name",
            "start",
            "duration_in_min",
            "video_conference_url",
            "additional_info",
            "recurrences",
        )
