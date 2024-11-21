from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
#class Boardgame(models.Model):
    #title = models.CharField(max_length=200, db_index=True)
    #slug = models.SlugField(unique=True, blank=True)  # Slug for URL-friendly paths
    #description = models.TextField(blank=True)
    #subtitle = models.CharField(max_length=200, blank=True)
    #maker = models.ManyToManyField("Maker")
    #description = models.TextField(max_length=1000, null=True)

    #type = models.ManyToManyField("Type")

class Boardgame(models.Model):
    title = models.CharField(max_length=100)
    pub_year = models.PositiveSmallIntegerField("Publication Year", null=True)
    available_copies = models.IntegerField(default=0)
    def __str__(self):
        return self.title

    def is_available(self):
        return self.available_copies > 0
    #def __str__(self):
       # return self.title
# (f" ({str(self.pub_year)})")
class Description(models.Model):
    title = models.ForeignKey(Boardgame, on_delete=models.CASCADE,related_name='descriptions')
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Descriptions"

    def __str__(self):
        return f"{self.description[:50]}..."

class Loan(models.Model):
    boardgame = models.ForeignKey(Boardgame, on_delete=models.CASCADE, related_name='loans')
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    date_borrowed = models.DateTimeField(auto_now_add=True)
    date_due = models.DateTimeField()
    returned = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_borrowed']

    def __str__(self):
        return f"{self.borrower.username} borrowed {self.boardgame.title}"

    def is_overdue(self):
        return self.date_due < timezone.now() and not self.returned

