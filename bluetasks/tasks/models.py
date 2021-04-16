import uuid

from django.conf import settings
from django.db import IntegrityError, models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


"""
Task, Project, Tag, Comment, Epic.
"""

class Project(models.Model):
    """
    """

    # General fields
    # IDENTIFIERS
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # FECHAS
    created = models.DateTimeField(_('date joined'), default=timezone.now)
    updated = models.DateTimeField(_('last update'), auto_now=True)

    # TEXT
    title = models.CharField(
        _('title'), max_length=40,
        blank=False, null=False
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        related_name='projects',
        blank=True, null=True
    )


class Epic(models.Model):
    """
    """

    # General fields
    # IDENTIFIERS
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # FECHAS
    created = models.DateTimeField(_('date joined'), default=timezone.now)
    updated = models.DateTimeField(_('last update'), auto_now=True)

    # TEXT
    title = models.CharField(
        _('title'), max_length=40,
        blank=False, null=False
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        related_name='epics',
        blank=True, null=True
    )


class Tag(models.Model):
    """
    """

    # General fields
    # IDENTIFIERS
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # FECHAS
    created = models.DateTimeField(_('date joined'), default=timezone.now)
    updated = models.DateTimeField(_('last update'), auto_now=True)

    # TEXT
    name = models.CharField(
        _('title'), max_length=40,
        blank=False, null=False
    )


class Comment(models.Model):
    """
    """

    # General fields
    # IDENTIFIERS
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # FECHAS
    created = models.DateTimeField(_('date joined'), default=timezone.now)
    updated = models.DateTimeField(_('last update'), auto_now=True)

    # TEXT
    text = models.TextField(blank=False, null=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        related_name='comments',
        blank=True, null=True
    )


class Task(models.Model):
    """
    Model to store Certificate Orders.
    """
    TYPE_FEATURE = 1
    TYPE_BUG = 2
    TYPE_CHOICES = (
        (TYPE_FEATURE, 'feature'),
        (TYPE_BUG, 'bug'),
    )

    STATUS_CREATED = 1
    STATUS_ACTIVE = 2
    STATUS_COMPLETED = 3
    STATUS_REJECTED = 4
    STATUS_VOID = 5
    STATUS_CHOICES = (
        (STATUS_CREATED, 'created'),
        (STATUS_ACTIVE, 'active'),
        (STATUS_COMPLETED, 'completed'),
        (STATUS_REJECTED, 'rejected'),
        (STATUS_VOID, 'void'),
    )

    PRIORITY_LOW = 1
    PRIORITY_MEDIUM = 2
    PRIORITY_HIGH = 3
    PRIORITIES_CHOICES = (
        (PRIORITY_LOW, 'low'),
        (PRIORITY_MEDIUM, 'medium'),
        (PRIORITY_HIGH, 'high'),
    )

    # General fields
    # IDENTIFIERS
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # FECHAS
    created = models.DateTimeField(_('date joined'), default=timezone.now)
    updated = models.DateTimeField(_('last update'), auto_now=True)

    # TEXT
    title = models.CharField(
        _('title'), max_length=40,
        blank=False, null=False
    )
    description = models.TextField(
        blank=True, null=False
    )

    # ENUMS
    type = models.PositiveSmallIntegerField(
        _('type'), choices=TYPE_CHOICES,
        blank=True, null=True
    )
    status = models.PositiveSmallIntegerField(
        _('status'), choices=STATUS_CHOICES,
        blank=True, null=True
    )
    priority = models.PositiveSmallIntegerField(
        _('priority'), choices=PRIORITIES_CHOICES,
        blank=True, null=True
    )

    # FK
    project = models.ForeignKey(
        'Project', on_delete=models.CASCADE,
        related_name='tasks',
        blank=True, null=True
    )
    epic = models.ForeignKey(
        'Epic', on_delete=models.CASCADE,
        related_name='tasks',
        blank=True, null=True
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        related_name='tasks',
        blank=True, null=True
    )

    # MAny to many
    owners = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, null=True)
    tags = models.ManyToManyField('Tag', blank=True, null=True)
    comments = models.ManyToManyField('Comment', blank=True, null=True)
    linked_tasks = models.ManyToManyField('self', blank=True, null=True)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        related_name='certificate_orders',
        blank=True, null=True
    )
