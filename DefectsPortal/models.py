from django.db import models

# Create your models here.

DEFECTS_TYPES = [
    ('PRIMARY','primary'),
    ('SECONDARY','secondary')
]

DEFECTS_PRIORITY = [
    ('HIGH','high'),
    ('MEDIUM','medium'),
    ('LOW','low')
]

DEFECTS_STATUS = [
    ('COMPLETED','completed'),
    ('NOT COMPLETED','not completed')
]

class DefectsList(models.Model):
    defect_id = models.CharField(max_length=100)
    defect_name = models.CharField(max_length=100)
    defect_type= models.CharField(max_length=100,choices=DEFECTS_TYPES,default='primary')
    assigned_by = models.CharField(max_length=100)
    assigned_to = models.CharField(max_length=100)
    description = models.TextField()
    defect_status = models.CharField(max_length=100,choices=DEFECTS_STATUS)
    priority = models.CharField(max_length=100,choices=DEFECTS_PRIORITY,default='high')
    
    def __str__(self):
        return self.defect_name
    
class Defects_screen_shots(models.Model):
    defect = models.ForeignKey(DefectsList,related_name='defectslists',on_delete=models.CASCADE)
    defect_img = models.ImageField(upload_to='defect_ss',blank=True,null='True')