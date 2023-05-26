from django.db import models


class StateStats(models.Model):
    state_code = models.CharField(primary_key=True, max_length=6, verbose_name='State Code', unique=True, null=False,
                                  blank=False)
    state_name = models.CharField(max_length=45, verbose_name='State Name', null=False, blank=False)
    rigid = models.FloatField(verbose_name='Rigid', default=0, null=False, blank=False)
    flexible = models.FloatField(verbose_name='Flexible', default=0, null=False, blank=False)
    mlp = models.FloatField(verbose_name='MLP', default=0, null=False, blank=False)

    class Meta:
        db_table = "state_statistics"

    def total_waste(self):
        return self.rigid + self.flexible + self.mlp
