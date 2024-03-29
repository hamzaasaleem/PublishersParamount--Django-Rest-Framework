from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model

import journals
from journals.models import *
from accounts.models import *

User = get_user_model()


class Manuscript(models.Model):
    APPROVED = 'approved'
    REJECTED = 'rejected'
    MINOR = 'minor'
    MAJOR = 'major'
    NA = 'under process'

    STATUS = (
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
        (MINOR, 'Minor'),
        (MAJOR, 'Major'),
        (NA, 'under process'),
    )

    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='manuscripts', null=True)
    title = models.CharField(max_length=100)

    abstract = models.TextField(max_length=300)
    keywords = models.TextField(default='')
    article_type = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS, default=NA)
    saved = models.BooleanField(default=False)
    manuscript_file = models.FileField(upload_to='manuscripts/file/', null=True, blank=True)
    figure_file = models.FileField(upload_to='manuscripts/figures/', null=True, blank=True)
    cover_file = models.FileField(upload_to='manuscripts/cover/', null=True, blank=True)
    abstract_file = models.FileField(upload_to='manuscripts/abstract/', null=True, blank=True)
    comment = models.CharField(max_length=2000, null=True, blank=True, default='')
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE, related_name='manuscripts', null=True)
    mergedPdf = models.CharField(max_length=2000, null=True, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Figure(models.Model):
    manuscript = models.ForeignKey(Manuscript, on_delete=models.CASCADE, null=True, blank=True)
    file = models.FileField(upload_to='manuscripts/figures', null=True, blank=True)

    def __str__(self):
        return self.file.name


class ManuRev(models.Model):
    APPROVED = 'approved'
    REJECTED = 'rejected'
    MINOR = 'minor'
    MAJOR = 'major'
    NA = 'under process'

    STATUS = (
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
        (MINOR, 'Minor'),
        (MAJOR, 'Major'),
        (NA, 'under process'),
    )
    manuscript = models.ForeignKey(Manuscript, on_delete=models.CASCADE, null=True, blank=True)
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.CharField(max_length=2000, null=True, blank=True, default='')
    status = models.CharField(max_length=50, choices=STATUS, default=NA)


class ManuEditor(models.Model):
    APPROVED = 'approved'
    REJECTED = 'rejected'
    MINOR = 'minor'
    MAJOR = 'major'
    NA = 'under process'

    STATUS = (
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
        (MINOR, 'Minor'),
        (MAJOR, 'Major'),
        (NA, 'under process'),
    )
    manuscript = models.ForeignKey(Manuscript, on_delete=models.CASCADE)
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.CharField(max_length=2000, null=True, blank=True, default='')
    status = models.CharField(max_length=50, choices=STATUS, default=NA)


class CoAuthorModels(models.Model):
    manuscript = models.ForeignKey(Manuscript, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True, default='')
    email = models.CharField(max_length=200, null=True, blank=True, default='')


class ManuRevStringModel(models.Model):
    manuscript = models.ForeignKey(Manuscript, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE, null=True, blank=True)
    string=models.CharField(max_length=200)

