from django.db import models

from inboxi.models.base import BaseUUIDTimestampModel


class Subscription(BaseUUIDTimestampModel):
    subscriber = models.ForeignKey(
        "Subscriber", on_delete=models.CASCADE, related_name="subscriber_subscriptions"
    )
    topic = models.ForeignKey(
        "Topic", on_delete=models.CASCADE, related_name="topic_subscriptions"
    )
    meta = models.JSONField(blank=True, null=True)

    class Meta:
        db_table = "subscriptions"

    def __str__(self) -> str:
        return str(self.id)
