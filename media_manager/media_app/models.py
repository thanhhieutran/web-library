from django.db import models

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # related_name => Dùng để get all chill của category đó.
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return self.name

    def get_full_path(self):
        """Return the full path of the category by traversing its parents."""
        if self.parent:
            return f"{self.parent.get_full_path()}/{self.name}"
        return self.name


# Tag Model
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


# MediaFile Model
class MediaFile(models.Model):
    MEDIA_TYPES = [
        ('photo', 'Photo'),
        ('video', 'Video'),
        ('gif', 'GIF'),
    ]

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='media_files')
    tags = models.ManyToManyField(Tag, related_name='media_files', blank=True)
    # Mặc định file sẽ lưu theo ngày tháng năm
    file = models.FileField(upload_to='media/%Y/%m/%d/')  # Updated dynamically below
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)

    def __str__(self):
        return f"{self.media_type}: {self.file.name}"

    def save(self, *args, **kwargs):
        """Override save to adjust upload path dynamically based on category."""
        self.file.field.upload_to = self.dynamic_upload_path
        super().save(*args, **kwargs)
    # Tuy nhiên sẽ lưu theo cấu trúc như vậy.
    def dynamic_upload_path(self, filename):
        """Dynamically generate the upload path using the category path."""
        category_path = self.category.get_full_path()
        return f"media/{category_path}/{filename}"
