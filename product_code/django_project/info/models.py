from django.db import models

# Create your models here.
class Info(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    # Symptoms

    # Cough
    has_cough = models.BooleanField(default=False)
    cough_amt_of_days = models.IntegerField(null=True, blank=True)
    cough_extra_info = models.TextField(null=True, blank=True)

    # Fever
    has_fever = models.BooleanField(default=False)
    fever_last_temp = models.FloatField(null=True, blank=True)
    fever_amt_of_days = models.IntegerField(null=True, blank=True)

    # Headache
    has_headache = models.BooleanField(default=False)
    headache_severity = models.IntegerField(null=True, blank=True)
    headache_amt_of_days = models.IntegerField(null=True, blank=True)
    headache_extra_info = models.TextField(null=True, blank=True)

    # Sore Throat
    has_sorethroat = models.BooleanField(default=False)
    sorethroat_severity = models.IntegerField(null=True, blank=True)
    sorethroat_amt_of_days = models.IntegerField(null=True, blank=True)
    sorethroat_extra_info = models.TextField(null=True, blank=True)

    # Muscle Aches
    has_muscleaches = models.BooleanField(default=False)
    muscleaches_severity = models.IntegerField(null=True, blank=True)
    muscleaches_amt_of_days = models.IntegerField(null=True, blank=True)
    muscleaches_extra_info = models.TextField(null=True, blank=True)

    # Nausea
    has_nausea = models.BooleanField(default=False)
    nausea_severity = models.IntegerField(null=True, blank=True)
    nausea_amt_of_days = models.IntegerField(null=True, blank=True)
    nausea_extra_info = models.TextField(null=True, blank=True)

    # Unexplained Weight Loss
    has_weightloss = models.BooleanField(default=False)
    weightloss_amount = models.IntegerField(null=True, blank=True)
    weightloss_extra_info = models.TextField(null=True, blank=True)

    # Shortness of Breath
    has_shortbreath = models.BooleanField(default=False)
    shortbreath_severity = models.IntegerField(null=True, blank=True)
    shortbreath_amt_of_days = models.IntegerField(null=True, blank=True)
    shortbreath_extra_info = models.TextField(null=True, blank=True)

    # Chills
    has_chills = models.BooleanField(default=False)
    chills_severity = models.IntegerField(null=True, blank=True)
    chills_amt_of_days = models.IntegerField(null=True, blank=True)
    chills_extra_info = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
