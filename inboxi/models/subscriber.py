from django.db import models

from inboxi.models.base import BaseUUIDTimestampModel


class Subscriber(BaseUUIDTimestampModel):
    identifier = models.CharField(max_length=225, unique=True, blank=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    notes = models.JSONField(blank=True, null=True)

    topics = models.ManyToManyField(to="Topic", through="Subscription")

    class Meta:
        db_table = "subscribers"

    def __str__(self) -> str:
        return self.identifier

    def save(self, *args, **kwargs):
        if self._state.adding:
            if not self.identifier:
                self.identifier = self.email
        return super().save(*args, **kwargs)