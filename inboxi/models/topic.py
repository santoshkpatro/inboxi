from django.db import models
from django.contrib.postgres.fields import ArrayField

from inboxi.models.base import BaseUUIDTimestampModel


class Topic(BaseUUIDTimestampModel):
    name = models.CharField(max_length=124, unique=True)
    tags = ArrayField(base_field=models.CharField(max_length=124), default=list)
    is_public = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    subscriber_count = models.BigIntegerField(default=0)
    
    subscribers = models.ManyToManyField(to="Subscriber", through="Subscription")

    class Meta:
        db_table = "topics"

    def __str__(self) -> str:
        return self.name
