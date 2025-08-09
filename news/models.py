from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                               related_name="projects", null=True,
                               blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "project"
        verbose_name_plural = "projects"


class FileModel(models.Model):
    media = models.FileField(upload_to="projects/")
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                related_name="files")

    def get_filename(self):
        return self.media.name.split("/")[-1]

    def get_image(self):
        format_to_image = {
            "pdf": static("img/pdf.png"),
            "mp4": static("img/video.png"),
            "webm": static("img/video.png"),
            "mp3": static("img/audio.png"),
            "wav": static("img/audio.png"),
            "ogg": static("img/audio.png"),
            "jpg": static("img/photo.jpg"),
            "jpeg": static("img/photo.jpg"),
            "png": static("img/photo.jpg"),
            "gif": static("img/photo.jpg"),
            "webp": static("img/photo.jpg"),
            "txt": static("img/txt.png"),
        }
        filetype = self.media.name.split(".")[-1].lower()
        try:
            return format_to_image[filetype]
        except:
            return static("img/code.png")

    def __str__(self):
        return f"{self.media}"

    class Meta:
        verbose_name = "file"
        verbose_name_plural = "files"
