from body.models import *



SkelF = open("apps/body/exp_skel_template.py","w")

SkelF.writeline("bones = {")

for part in SkeletalSystem.objects.all():
    
    s = "%s:\t\t\t"%(part.tName)
    kvs = ""
    for field in part.__class__._meta.fields:
        if field.name not in ['id','basesystem_ptr'] and not field.rel:
            kvs += "'%s':'%s',"%(field.name,getattr(part,field.name))
        elif field.name not in ['id','basesystem_ptr'] and field.rel.multiple:
            kvs += "'m2m_delay_%s':%s"%(field.name,[o.tName for o in getattr(part,field.name)])
        elif field.name not in ['id','basesystem_ptr'] and not field.rel.multiple:
            kvs += "'fk_%s':%s"%(field.name,getattr(part,field.name).tName)
            
     