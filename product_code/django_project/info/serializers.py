# info/serializers.py

from rest_framework import serializers
from .models import Info


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = (
            "id",
            "first_name",
            "last_name",
            "created_at",
            "has_cough",
            "cough_amt_of_days",
            "cough_extra_info",
            "has_fever",
            "fever_last_temp",
            "fever_amt_of_days",
            "has_headache",
            "headache_severity",
            "headache_amt_of_days",
            "headache_extra_info",
            "has_sorethroat",
            "sorethroat_amt_of_days",
            "sorethroat_severity",
            "sorethroat_extra_info",
            "has_muscleaches",
            "muscleaches_severity",
            "muscleaches_amt_of_days",
            "muscleaches_extra_info",
            "has_nausea",
            "nausea_severity",
            "nausea_amt_of_days",
            "nausea_extra_info",
            "has_weightloss",
            "weightloss_amount",
            "weightloss_extra_info",
            "has_shortbreath",
            "shortbreath_severity",
            "shortbreath_amt_of_days",
            "shortbreath_extra_info",
            "has_chills",
            "chills_severity",
            "chills_amt_of_days",
            "chills_extra_info",
        )
