from django.db import models


class EFiscalParams(models.Model):
    query = models.URLField(blank=False)

    def __str__(self):
        return self.query
