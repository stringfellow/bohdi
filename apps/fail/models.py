from django.db import models
from body.models import *
# Create your models here.









class BaseFail(models.Model):
    
    body = models.ForeignKey(Body)
    date = models.DateTimeField()
    report_state = models.CharField(max_length=25,choices=(("SURGERY","Surgically Treated"),("MEDICAL","Medically Treated"),("REPORTED","On Record"),("OFF RECORD","Off Record")))
    
    def __str__(self):
        return "%s failed @%s; %s"%(self.body,self.date,self.report_state)


class Break(BaseFail):
    
    severity = models.CharField(max_length=25,choices=(("GREEN STICK","Green stick"),("SPLINTER","Splinter")))
    bone = models.ForeignKey(Bone)
    region = models.ForeignKey(Region,null=True,blank=True)
    section = models.CharField(max_length=25,choices=(("UPPER","Upper"),("MIDDLE","Middle"),("LOWER","Lower")),null=True,blank=True)
    
    def __str__(self):
        if self.region:
            return "@%s: <%s> BROKE %s(<%s>) -- %s:%s"%(self.date,self.body.name(),self.region.name,self.bone.syspart,self.severity,self.report_state)
        return "@%s: <%s> BROKE <%s> -- %s:%s"%(self.date,self.body.name(),self.bone.syspart,self.severity,self.report_state)
