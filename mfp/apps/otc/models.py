from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid

class OtcBase(models.Model):

    otc = models.UUIDField(verbose_name="UUID code", default=uuid.uuid4)
    created_in = models.DateTimeField(verbose_name="created in", auto_now_add=True)
    used_in = models.DateTimeField(verbose_name="used in", null = True, blank = True)
    is_used = models.BooleanField(verbose_name="is used", default = False)
    user = models.ForeignKey(User, related_name = 'otc', null=True, blank=True)

    def __str__(self):
        return "ID: %s, Time: %s, Used: %s" % (self.id, self.created_in, self.is_used)

    # utilization
    def apply_this(self):
        self.is_used = True
        self.used_in = timezone.now()
        self.save()