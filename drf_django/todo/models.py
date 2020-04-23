from django.db import models

# Create your models here.


class TodoContent(models.Model):
    contents = models.CharField(max_length=1000, verbose_name='内容')
    ischecked = models.BooleanField(default=False, verbose_name='选中状态')
    isActive = models.BooleanField(default=False, verbose_name='激活状态')
    isEditing = models.BooleanField(default=False, verbose_name='编辑状态')

    class Meta:
        db_table = 'todo_content'
