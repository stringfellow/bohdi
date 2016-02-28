from models import *

from bone_template import bones, bonesurfaces

from muscle_template import muscles, connectives, attachments



def expandShortcuts(partdict):
    
    result = {}
    
    for key in partdict.keys():
        
        part = partdict[key]
        result[key] = part
        
        result[key]['m2m'] = {}
        result[key]['m2m_delay'] = {}
        result[key]['fk'] = {}
        
        #print part
        if part.has_key('tcName'):
            tName = part['tcName']
            cName = tName
            part.pop('tcName')
        if part.has_key('tName'):
            tName = part['tName']
        if part.has_key('cName'):
            cName = part['cName']
        else:
            cName = tName
        
        result[key]['cName']=cName
        result[key]['tName']=tName
        
        
        if result[key].has_key('m2m_o'):
            result[key]['m2m']['skeletal_origin'] = (SkeletalSystem,result[key]['m2m_o'])
            result[key].pop('m2m_o')
        if result[key].has_key('m2m_i'):
            result[key]['m2m']['skeletal_insertion'] = (SkeletalSystem,result[key]['m2m_i'])
            result[key].pop('m2m_i')
        if result[key].has_key('m2m_a'):
            result[key]['m2m']['artery'] = (VascularSystem,result[key]['m2m_a'])
            result[key].pop('m2m_a')
        if result[key].has_key('m2m_n'):
            result[key]['m2m']['nerve'] = (NervousSystem,result[key]['m2m_n'])
            result[key].pop('m2m_n')
        if result[key].has_key('m2m_delay_ant'):
            result[key]['m2m_delay']['antagonist'] = (MuscularSystem,result[key]['m2m_delay_ant'])
            result[key].pop('m2m_delay_ant')
        if result[key].has_key('m2m_delay_asoc'):
            result[key]['m2m_delay']['associations'] = (BoneSurface,result[key]['m2m_delay_asoc'])
            result[key].pop('m2m_delay_asoc')
        if result[key].has_key('fk_bone'):
            result[key]['fk']['bone'] = (SkeletalSystem,result[key]['fk_bone'])
            result[key].pop('fk_bone')
        
        
        if result[key].has_key('symmetry') and result[key]['symmetry'] == "LR":
            result["%s_L"%key] = dict(result[key])
            result["%s_L"%key]['symmetry'] = "L"
            result["%s_R"%key] = dict(result[key])
            result["%s_R"%key]['symmetry'] = "R"
            result.pop(key)
    
    return result


def addBones():
    
    the_bones = expandShortcuts(bones)
    print len(the_bones)
    addParts(SkeletalSystem,the_bones)
    

def addMuscles():
    
    the_muscles = expandShortcuts(muscles)
    
    addParts(MuscularSystem,the_muscles)
    

def addBoneSurfaces():
    
    the_bs = expandShortcuts(bonesurfaces)
    
    addParts(BoneSurface,the_bs)

def oppose(side):
    if side == "L":
        return "R"
    if side == "R":
        return "L"

def m2mPostAdder(m2m,syspart,fk_field=''):
    print "Post-Adding to ",syspart
    m2mAdder(m2m,syspart,fk_field)

def m2mAdder(m2m,syspart,fk_field=''):
    for key,val in m2m.items():
        (m2m_classtype,m2m_objectnames) = val
        objects = list(getattr(syspart,key).all())
        print objects
        for name in m2m_objectnames:
            symside,oname = name.split("|")
            try:
                symmetry = syspart.symmetry
            except:
                symmetry = getattr(syspart,fk_field).symmetry
                
            print name,symmetry
            if symside == "S":
                try:
                    objects += [obj for obj in m2m_classtype.objects.filter(tName=oname,symmetry=symmetry)]
                except:
                    try:
                        print "using %s__symmetry to get part"%fk_field
                        kwargs = {'tName':oname,"%s__symmetry"%fk_field:symmetry}
                        objects += [obj for obj in m2m_classtype.objects.filter(**kwargs)]
                    except Exception,e:
                        print "\t couldn't add %s\r\t%s"%(oname,e)
            if symside == "O":
                try:
                    objects += [obj for obj in m2m_classtype.objects.filter(tName=oname,symmetry=oppose(symmetry))]
                except:
                    print "\t couldn't add %s"%oname
            if symside == "C":
                try:
                    objects += [obj for obj in m2m_classtype.objects.filter(tName=oname,symmetry="C")]
                except:
                    print "\t couldn't add %s"%oname
            if symside == "B":
                try:
                    objects += [obj for obj in m2m_classtype.objects.filter(tName=oname,symmetry=symmetry)]
                    objects += [obj for obj in m2m_classtype.objects.filter(tName=oname,symmetry=oppose(symmetry))]
                except:
                    print "\t couldn't add %s"%oname
        print key,objects
        print "got:",getattr(syspart,key).all()
        setattr(syspart,key,objects)
        #syspart.save()
        print "\tadded m2m %s %s"%(key,m2m_objectnames)
        print getattr(syspart,key).all()
    syspart.save()



def addParts(classtype, partdict):
        #print partdict
        post_add_set = []
        count = 0
        for partname,kwargs in partdict.items():
            m2m = None
            delay = None
            print partname,kwargs
            try:
                m2m = kwargs.pop('m2m')
            except:
                pass
            try:
                delay = kwargs.pop('m2m_delay')
            except:
                pass
            try:
                fk = kwargs.pop('fk')
            except:
                fk = None
            if not fk:
                syspart,created = classtype.objects.get_or_create(**kwargs)
                syspart.save()
                if not created:
                    print syspart
                else:
                    count+=1
                if m2m:
                    m2mAdder(m2m,syspart)
                if delay and len(delay)>0:
                    post_add_set.append((syspart,delay))
                fk_field = None
            else:
                for fkk,fkv in [fk.items()[0]]: #there should only be one really... MESS MESS MESS
                    fk_field = fkk
                    fk_classtype,fko_names = fkv
                    fko_names = fko_names.split("|")
                    fk_objects = []
                    for fko_name in fko_names:
                        if fko_name.startswith("*"):
                            fk_objects += fk_classtype.objects.filter(tName__contains=fko_name[1:])
                        else:
                            fk_objects += fk_classtype.objects.get(tName=fko_name)
                    kwargs[fkk] = None
                    # add partname for each objects... preserve symmetry from objects, m2ms from above
                    for o in fk_objects:
                        kwargs[fkk] = o
                        #kwargs['symmetry'] = o.symmetry
                        syspart,created = classtype.objects.get_or_create(**kwargs)
                        syspart.save()
                        if not created:
                            print "Exists ",syspart
                        else:
                            count += 1
                        if m2m:
                            m2mAdder(m2m,syspart)
                        if delay and len(delay)>0:
                            post_add_set.append((syspart,delay))
        
        for syspart,delay in post_add_set:
            m2mPostAdder(delay,syspart,fk_field)
            #print getattr(syspart,"associations").all()
            try:
                print "*****",BoneSurface.objects.get(pk=6).associations.all()
            except:
                pass




