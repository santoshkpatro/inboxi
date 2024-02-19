from django.db import models

from inboxi.models.base import BaseUUIDTimestampModel


class Campaign(BaseUUIDTimestampModel):
    class Meta:
        db_table = "campaigns"