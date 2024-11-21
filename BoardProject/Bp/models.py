from django.db import models
from django.utils.timezone import now
# Create your models here.
class Boardgame(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    #slug = models.SlugField(unique=True, blank=True)  # Slug for URL-friendly paths
    #description = models.TextField(blank=True)
    #subtitle = models.CharField(max_length=200, blank=True)
    #maker = models.ManyToManyField("Maker")
    #description = models.TextField(max_length=1000, null=True)
    pub_year = models.PositiveSmallIntegerField("Publish date", null=True)
    #type = models.ManyToManyField("Type")

    def __str__(self):
        return self.title
# (f" ({str(self.pub_year)})")
class Description(models.Model):
    title = models.ForeignKey(Boardgame, on_delete=models.CASCADE,related_name='descriptions')
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Descriptions"

    def __str__(self):
        return f"{self.description[:50]}..."