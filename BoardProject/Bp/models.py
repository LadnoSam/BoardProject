from django.db import models
from django.utils.timezone import now

# Existing Boardgame model
class Boardgame(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    pub_year = models.PositiveSmallIntegerField("Publish date", null=True)

    def __str__(self):
        return self.title

# Existing Description model
class Description(models.Model):
    title = models.ForeignKey(Boardgame, on_delete=models.CASCADE, related_name='descriptions')
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Descriptions"

    def __str__(self):
        return f"{self.description[:50]}..."

# New BorrowedGame model
class BorrowedGame(models.Model):
    boardgame = models.ForeignKey(Boardgame, on_delete=models.CASCADE)
    borrower = models.CharField(max_length=200)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.borrower} borrowed {self.boardgame.title}"
