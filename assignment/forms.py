from django import forms
from .models import *


class IncidentForm(forms.ModelForm):
    incident_CHOICES = (
        (1, "Environmental Incident"),
        (2, "Injury/Illness"),
        (3, "Property Damage"),
        (4, "Vehicle"),
    )

    location_choices = (
        ("Corporate Headoffice", "Corporate Headoffice"),
        ("Operations Department", "Operations Department"),
        ("Work Station", "Work Station"),
        ("Marketing Division", "Marketing Division"),
    )

    severity_choices = (
        ("Mild", "Mild"),
        ("Moderate", "Moderate"),
        ("Severe", "Severe"),
        ("Fatal", "Fatal"),
    )

    location = forms.ChoiceField(
        choices=location_choices,
        widget=forms.Select(attrs={"class": "form-control", "style": "width:50%"}),
    )
    initial_severity = forms.ChoiceField(
        choices=severity_choices,
        widget=forms.Select(attrs={"class": "form-control", "style": "width:50%"}),
    )
    sub_incident_type = forms.MultipleChoiceField(
        choices=incident_CHOICES, widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Incident
        fields = "__all__"
        exclude = [
            "type_env",
            "type_inju",
            "type_property",
            "type_vehicle",
            "reported_by",
        ]
        widgets = {
            "incident_department": forms.Textarea(
                attrs={"class": "form-control", "rows": 3, "style": "width:50%"}
            ),
            "incident_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date", "style": "width:50%"}
            ),
            "incident_time": forms.TimeInput(
                attrs={"class": "form-control", "type": "time", "style": "width:50%"}
            ),
            "incident_location": forms.TextInput(
                attrs={"class": "form-control", "style": "width:25%"}
            ),
            "suspected_cause": forms.Textarea(
                attrs={"class": "form-control", "rows": 3, "style": "width:50%"}
            ),
            "immediate_action_taken": forms.Textarea(
                attrs={"class": "form-control", "rows": 3, "style": "width:50%"}
            ),
        }
