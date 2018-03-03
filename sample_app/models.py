# -*- encoding: utf-8 -*-

from django.db import models

class BatchException(models.Model):

    class Meta:
        db_table = "batchException"
#        db_tablespace = "web"

    batchExceptionID = models.IntegerField(primary_key=True)
    batchID = models.IntegerField()
    createdBy = models.CharField(max_length=500)
    createdOn= models.DateField()
    modifiedBy = models.CharField(max_length=500)
    modifiedOn= models.DateField()
    fileName = models.CharField(max_length=500)
    exceptionReason = models.CharField(max_length=5000)