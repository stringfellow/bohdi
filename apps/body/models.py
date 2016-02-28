from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Body(models.Model):
    
    
    user = models.ForeignKey(User)
    
    def name(self):
        return self.user.username
    
    def __str__(self):
        return "%s's body"%self.user.username
    
    class Meta:
       verbose_name_plural = "Bodies"
    

###############################################################
############### TEMPLATE SYSTEMS ##############################
###############################################################
class BaseSystem(models.Model):
    #common bits
    cName = models.CharField(max_length=100)
    tName = models.CharField(max_length=100)
    
    #this field used for bones, veins, muscles... if appropriate?
    symmetry = models.CharField(max_length=1,choices=(("C","Central"),("R","Right"),("L","Left")))
    
    def __str__(self):
        if self.symmetry == "C":
            return "%s"%(self.tName)
        else:
            return "%s (%s)"%(self.tName,self.symmetry)
    
    class Meta():
        ordering= ('tName',)


class BaseOrgan(BaseSystem):
    
    def __str__(self):
        return "organ %s"%(self.tName)



class SkeletalSystem(BaseSystem):
    # skeletal system
    """
    There are 206 bones in the adult human body[1] and 270 in an infant.[2]
    """
    #regions = models.CharField(max_length=255,blank=True,null=True)
    type = models.CharField(max_length=25,choices=(("LONG","Long"),("SHORT","Short"),("FLAT","Flat"),("IRREGULAR","Irregular")))
    
    
    class Meta:
       verbose_name_plural = "Skeletal Template"
    

class BoneSurface(models.Model):
    
    bone = models.ForeignKey("SkeletalSystem")
    tName = models.CharField(max_length=100,blank=True,null=True)
    cName = models.CharField(max_length=100,blank=True,null=True)
    articular = models.BooleanField(blank=True,null=True)
    associations = models.ManyToManyField("BoneSurface",null=True,blank=True)
    type = models.CharField(max_length=25,choices=(("LINE/RIDGE","Line/Ridge"),("TUBERCULE","Tubercule"),("TUBEROSITY","Tuberosity"),("SPINE","Spine"),("REGION","Region")))
    formation = models.CharField(max_length=3,choices=(("EPI","Epiphysis"),("APO","Apophysis")),null=True,blank=True)
    
    
    def __str__(self):
        return "%s of %s"%(self.tName,self.bone)
        
    class Meta:
        ordering = ['bone','tName']

class Attachment(models.Model):
    
    bonesurfaces = models.ManyToManyField("BoneSurface")
    muscles = models.ManyToManyField("MuscularSystem",null=True,blank=True)
    connectives = models.ManyToManyField("ConnectiveSystem",null=True,blank=True)


class VascularSystem(BaseSystem):
    # vascular system
    
    class Meta:
       verbose_name_plural = "Vascular Template"

class MuscularSystem(BaseSystem):
    # muscular system
    origin = models.ManyToManyField("Attachment",null=True,blank=True,related_name="origin_for")
    insertion = models.ManyToManyField("Attachment",null=True,blank=True,related_name="insertion_for")
    antagonist = models.ManyToManyField("MuscularSystem",null=True,blank=True)
    
    artery = models.ManyToManyField("VascularSystem",null=True,blank=True)
    nerve = models.ManyToManyField("NervousSystem",null=True,blank=True)
    presence = models.IntegerField(default=100)
    
    class Meta:
       verbose_name_plural = "Muscular Template"


class ConnectiveSystem(BaseSystem):
    # musculoskeletal system that is not in either muscular or skeletal systems
    pass

class NervousSystem(BaseSystem):
    # nervous system
    
    class Meta:
       verbose_name_plural = "Nervous Template"

"""

class LymphSystem(BaseSystem):
    # lymph system
    
    class Meta:
       verbose_name_plural = "Lymphatic Template"

class EndocrineSystem(BaseSystem):
    # endocrine system
    pass


class DigestiveSystem(BaseOrgan):
    # digestive system
    pass

class IntegumentarySystem(BaseOrgan):
    # integumentary system
    pass

class ImmuneSystem(BaseOrgan):
    # Immune system
    pass

class ReproductiveSystem(BaseOrgan):
    # reproductive system
    pass

class UrinarySystem(BaseOrgan):
    # skeletal system
    pass
"""




###############################################################
############### ABSTRACT REGIONS ##############################
###############################################################


"""
class SuperficialAnatomy(models.Model):
    # skeletal system
    pass

class FunctionalGroup(models.Model):
    # e.g. sensory group or e.g. upper respiratory tract.
    pass


"""


class Region(models.Model): # is this the same as SuperficialAnatomy
    # self referencing e.g. knee->leg->legs->....
    
    parent = models.ForeignKey("Region",null=True,blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField(default="")
    
    def drilldown(self):
        hierarchy = []
        obj = self
        while obj.parent:
            hierarchy.append(obj)
            obj = obj.parent
        hierarchy.append(obj)
        reverse(hierarchy)
        return hierarchy
            
    
    def __str__(self):
        return str(self.drilldown())
    




###############################################################
############### NON-STATIC DBASE ##############################
###############################################################

class BasePart(models.Model):
    
    functional = models.BooleanField(default=True)
    exists = models.BooleanField(default=True)
    
    def __str__(self):
        return "%s's %s"%(self.body.name(),self.syspart)

class Bone(BasePart):
    body = models.ForeignKey(Body)
    syspart = models.ForeignKey(SkeletalSystem)
    


class Vessel(BasePart):
    # vasuclar system: which region it is in
    body = models.ForeignKey(Body)
    syspart = models.ForeignKey(VascularSystem)

"""
class Muscle(BasePart):
    # muscular system: which bone/connective it depends on, which nerve operates it, which region
    syspart = models.ForeignKey(MuscularSystem)

class Nerve(BasePart):
    # w'ev, and which regions it runs through, which it controls
    syspart = models.ForeignKey(NervousSystem)


class Organ(BasePart):
    #skin, heart, lung... generic based on one of various models
    def __init__(self):
        pass
        


class Fluid(BasePart):
    #blood, urine, ....
    def __init__(self):
        pass


class Connective(BasePart):
    #tendon etc
    def __init__(self):
        pass


class Cavity(BasePart):
    # a sinus, inside mouth, ... others? e.g. 'lesser sac' (omental bursa)
    pass





class Gene(BasePart):
    # a weird class that should be filled with known gene functions. 
    # i know i have spheroctosis as a result of a gene. what is it? 
    # include allele config? dominance? heriditary? epigeneticity?
    pass
    

class Expression(BasePart):
    # for the gene model - describes expression? maybe?
    pass

"""

###############################################################
############### INTERACTIVE RELATION ##########################
###############################################################


"""

class Joint(models.Model):
    # a specific linkage for bone,connective,muscle?
    pass


class Linkage(models.Model):
    # describes how 'connected' one part is to another
    # maybe using a scale of connectivity? when i move my little finger
    #   this affects everything up to my elbow? further? how much?
    #   perhaps a verb to describe linkage: attaches, pressures, produces for, consumes from?
    
    def __init__(self):
        pass

class Action(models.Model):
    # how muscles act on body
    
    pass

"""

###############################################################
############### TEMPORAL STATES ###############################
###############################################################

"""
class MetricAlteration(models.Model):
    # this is used to define the ratio difference from 'norm' for a given age/gender/race combo.
    age
    gender
    race
    
    equation
    special

class Stage(models.Model):
    # teen, pubescent, adult... there are probably biologically correct names for this
    pass

class State(models.Model):
    # an age-dependant representation of the body -includes height, weight...............
    pass
"""