bones = {
# CRANIAL (8)
    'cranial:frontal':      {'tcName':'cranial:frontal',    'symmetry':"C"},
    'cranial:parietal':     {'tcName':'cranial:parietal',   'symmetry':"LR"},
    'cranial:temporal':     {'tcName':'cranial:temporal',   'symmetry':"LR"},
    'cranial:occipital':    {'tcName':'cranial:occipital',  'symmetry':"C"},
    'cranial:sphenoid':     {'tcName':'cranial:sphenoid',   'symmetry':"C"},
    'cranial:ethmoid':      {'tcName':'cranial:ethmoid',    'symmetry':"C"},
    
#Facial bones: (14) 
    'facial:mandible':      {'tcName':'facial:mandible',     'symmetry':"C"},
    'facial:maxilla':       {'tcName':'facial:maxilla',     'symmetry':"LR"},
    'facial:palatine':      {'tcName':'facial:palatine',    'symmetry':"LR"},
    'facial:zygomatic':     {'tcName':'facial:zygomatic',  'symmetry':"LR"},
    'facial:nasal':         {'tcName':'facial:nasal',       'symmetry':"LR"},
    'facial:lacrimal':      {'tcName':'facial:lacrimal',    'symmetry':"LR"},
    'facial:vomer':         {'tcName':'facial:vomer',       'symmetry':"C"},
    'facial:inferior-nasal-conchae':{'tcName':'facial:inferior-nasal-conchae','symmetry':"LR"},

#Ears (6)
    'middle-ear:malleus':   {'tcName':'middle-ear:malleus', 'symmetry':"LR"},
    'middle-ear:incus':     {'tcName':'middle-ear:incus',   'symmetry':"LR"},
    'middle-ear:stapes':    {'tcName':'middle-ear:stapes',  'symmetry':"LR"},
    
# Throat (1)
    
    'throat:hyoid':         {'tcName':'throat:hyoid',       'symmetry':"C"},

# Shoulder (4)

    'shoulder:clavicle':    {'tName':'shoulder:clavicle','cName':'collar bone','symmetry':"LR"},
    'shoulder:scapula':     {'tName':'shoulder:scapula','cName':'shoulder blade','symmetry':"LR"},


# Spine

    'spinal:cervical1':       {'tcName':'spinal:cervical-vertebra1',    'symmetry':"C"},
    'spinal:cervical2':       {'tcName':'spinal:cervical-vertebra2',    'symmetry':"C"},
    'spinal:cervical3':       {'tcName':'spinal:cervical-vertebra3',    'symmetry':"C"},
    'spinal:cervical4':       {'tcName':'spinal:cervical-vertebra4',    'symmetry':"C"},
    'spinal:cervical5':       {'tcName':'spinal:cervical-vertebra5',    'symmetry':"C"},
    'spinal:cervical6':       {'tcName':'spinal:cervical-vertebra6',    'symmetry':"C"},
    'spinal:cervical7':       {'tcName':'spinal:cervical-vertebra7',    'symmetry':"C"},
    
    'spinal:thoracic1':       {'tcName':'spinal:thoracic-vertebra1',    'symmetry':"C"},
    'spinal:thoracic2':       {'tcName':'spinal:thoracic-vertebra2',    'symmetry':"C"},
    'spinal:thoracic3':       {'tcName':'spinal:thoracic-vertebra3',    'symmetry':"C"},
    'spinal:thoracic4':       {'tcName':'spinal:thoracic-vertebra4',    'symmetry':"C"},
    'spinal:thoracic5':       {'tcName':'spinal:thoracic-vertebra5',    'symmetry':"C"},
    'spinal:thoracic6':       {'tcName':'spinal:thoracic-vertebra6',    'symmetry':"C"},
    'spinal:thoracic7':       {'tcName':'spinal:thoracic-vertebra7',    'symmetry':"C"},
    'spinal:thoracic8':       {'tcName':'spinal:thoracic-vertebra8',    'symmetry':"C"},
    'spinal:thoracic9':       {'tcName':'spinal:thoracic-vertebra9',    'symmetry':"C"},
    'spinal:thoracic10':      {'tcName':'spinal:thoracic-vertebra10',   'symmetry':"C"},
    'spinal:thoracic11':      {'tcName':'spinal:thoracic-vertebra11',   'symmetry':"C"},
    'spinal:thoracic12':      {'tcName':'spinal:thoracic-vertebra12',   'symmetry':"C"},
    
    'spinal:lumbar1':         {'tcName':'spinal:lumbar-vertebra1',      'symmetry':"C"},
    'spinal:lumbar2':         {'tcName':'spinal:lumbar-vertebra2',      'symmetry':"C"},
    'spinal:lumbar3':         {'tcName':'spinal:lumbar-vertebra3',      'symmetry':"C"},
    'spinal:lumbar4':         {'tcName':'spinal:lumbar-vertebra4',      'symmetry':"C"},
    'spinal:lumbar5':         {'tcName':'spinal:lumbar-vertebra5',      'symmetry':"C"},
    
    'sacral:1':              {'tcName':'sacral:1',       'symmetry':"C"},
    'sacral:2':              {'tcName':'sacral:2',       'symmetry':"C"},
    'sacral:3':              {'tcName':'sacral:3',       'symmetry':"C"},
    'sacral:4':              {'tcName':'sacral:4',       'symmetry':"C"},
    'sacral:5':              {'tcName':'sacral:5',       'symmetry':"C"},
    
    'coccyx:1':              {'tcName':'coccyx:1',       'symmetry':"C"},
    'coccyx:2':              {'tcName':'coccyx:2',       'symmetry':"C"},
    'coccyx:3':              {'tcName':'coccyx:3',       'symmetry':"C"},
    'coccyx:4':              {'tcName':'coccyx:4',       'symmetry':"C"},
    

#Thorax...
    
    'true-rib:I':                {'tName':'vertebrosternal:I','cName':'true-rib:I','symmetry':"LR"},
    'true-rib:II':               {'tName':'vertebrosternal:II','cName':'true-rib:II','symmetry':"LR"},
    'true-rib:III':              {'tName':'vertebrosternal:III','cName':'true-rib:III','symmetry':"LR"},
    'true-rib:IV':               {'tName':'vertebrosternal:V','cName':'true-rib:IV','symmetry':"LR"},
    'true-rib:V':                {'tName':'vertebrosternal:VI','cName':'true-rib:V','symmetry':"LR"},
    'true-rib:VI':               {'tName':'vertebrosternal:VII','cName':'true-rib:VI','symmetry':"LR"},
    'true-rib:VII':              {'tName':'vertebrosternal:VIII','cName':'true-rib:VII','symmetry':"LR"},
    'false-rib:VIII':            {'tName':'vertebrochondral:VIII','cName':'false-rib:VIII','symmetry':"LR"},
    'false-rib:IX':              {'tName':'vertebrochondral:IX','cName':'false-rib:IX','symmetry':"LR"},
    'false-rib:X':               {'tName':'vertebrochondral:X','cName':'false-rib:X','symmetry':"LR"},
    'floating-rib:XI':           {'tName':'vertebral:XI','cName':'floating-rib:XI','symmetry':"LR"},
    'floating-rib:XII':          {'tName':'vertebral:XII','cName':'floating-rib:XII','symmetry':"LR"},
    
    'sternum:manubrium':         {'tName':'sternum:manubrium','symmetry':"C"},
    'sternum:gladiolus':         {'tName':'sternum:gladiolus','symmetry':"C"},
    'sternum:xiphoid-process':   {'tName':'sternum:xiphoid-process','symmetry':"C"},

# Hands 

    'hand:navicular':                   {'tcName':'hand:navicular', 'symmetry':"LR"},
    'hand:lunate':                      {'tcName':'hand:lunate', 'symmetry':"LR"},
    'hand:pisiform':                    {'tcName':'hand:pisiform', 'symmetry':"LR"},
    'hand:triangular':                  {'tcName':'hand:triangular', 'symmetry':"LR"},
    'hand:hamate':                      {'tcName':'hand:hamate', 'symmetry':"LR"},
    'hand:capitate':                    {'tcName':'hand:capitate', 'symmetry':"LR"},
    'hand:lesser-multangular':           {'tcName':'hand:lesser-multangular', 'symmetry':"LR"},
    'hand:greater-multangular':         {'tcName':'hand:greater-multangular', 'symmetry':"LR"},
    
    'hand:metacarpus1':     {'tcName':'hand:metacarpus1',           'symmetry':"LR"},
    'hand:metacarpus2':     {'tcName':'hand:metacarpus2',           'symmetry':"LR"},
    'hand:metacarpus3':     {'tcName':'hand:metacarpus3',           'symmetry':"LR"},
    'hand:metacarpus4':     {'tcName':'hand:metacarpus4',           'symmetry':"LR"},
    'hand:metacarpus5':     {'tcName':'hand:metacarpus5',           'symmetry':"LR"},
    
    'hand:proximal-phalanx1':      {'tcName':'hand:proximal-phalanx1',            'symmetry':"LR"},
    'hand:proximal-phalanx2':      {'tcName':'hand:proximal-phalanx2',            'symmetry':"LR"},
    'hand:proximal-phalanx3':      {'tcName':'hand:proximal-phalanx3',            'symmetry':"LR"},
    'hand:proximal-phalanx4':      {'tcName':'hand:proximal-phalanx4',            'symmetry':"LR"},
    'hand:proximal-phalanx5':      {'tcName':'hand:proximal-phalanx5',            'symmetry':"LR"},
    
    'hand:intermediate-phalanx2':      {'tcName':'hand:intermediate-phalanx2',            'symmetry':"LR"},
    'hand:intermediate-phalanx3':      {'tcName':'hand:intermediate-phalanx3',            'symmetry':"LR"},
    'hand:intermediate-phalanx4':      {'tcName':'hand:intermediate-phalanx4',            'symmetry':"LR"},
    'hand:intermediate-phalanx5':      {'tcName':'hand:intermediate-phalanx5',            'symmetry':"LR"},
    
    'hand:distal-phalanx2':      {'tcName':'hand:distal-phalanx2',            'symmetry':"LR"},
    'hand:distal-phalanx3':      {'tcName':'hand:distal-phalanx3',            'symmetry':"LR"},
    'hand:distal-phalanx4':      {'tcName':'hand:distal-phalanx4',            'symmetry':"LR"},
    'hand:distal-phalanx5':      {'tcName':'hand:distal-phalanx5',            'symmetry':"LR"},

# Feet 

    'ankle:calcaneus':      {'tcName':'ankle:calcaneus',            'symmetry':"LR"},
    'ankle:talus':          {'tcName':'ankle:talus',                'symmetry':"LR"},
    
    'foot:cuboid':          {'tcName':'foot:cuboid',                'symmetry':"LR"},
    'foot:navicular':       {'tcName':'foot:navicular',             'symmetry':"LR"},
    'foot:cuneiform1':      {'tcName':'foot:cuneiform1',            'symmetry':"LR"},
    'foot:cuneiform2':      {'tcName':'foot:cuneiform2',            'symmetry':"LR"},
    'foot:cuneiform3':      {'tcName':'foot:cuneiform3',            'symmetry':"LR"},
    
    'foot:metatarsus1':     {'tcName':'foot:metatarsus1',           'symmetry':"LR"},
    'foot:metatarsus2':     {'tcName':'foot:metatarsus2',           'symmetry':"LR"},
    'foot:metatarsus3':     {'tcName':'foot:metatarsus3',           'symmetry':"LR"},
    'foot:metatarsus4':     {'tcName':'foot:metatarsus4',           'symmetry':"LR"},
    'foot:metatarsus5':     {'tcName':'foot:metatarsus5',           'symmetry':"LR"},
    
    'foot:proximal-phalanx1':      {'tcName':'foot:proximal-phalanx1',            'symmetry':"LR"},
    'foot:proximal-phalanx2':      {'tcName':'foot:proximal-phalanx2',            'symmetry':"LR"},
    'foot:proximal-phalanx3':      {'tcName':'foot:proximal-phalanx3',            'symmetry':"LR"},
    'foot:proximal-phalanx4':      {'tcName':'foot:proximal-phalanx4',            'symmetry':"LR"},
    'foot:proximal-phalanx5':      {'tcName':'foot:proximal-phalanx5',            'symmetry':"LR"},
    
    'foot:intermediate-phalanx2':      {'tcName':'foot:intermediate-phalanx2',            'symmetry':"LR"},
    'foot:intermediate-phalanx3':      {'tcName':'foot:intermediate-phalanx3',            'symmetry':"LR"},
    'foot:intermediate-phalanx4':      {'tcName':'foot:intermediate-phalanx4',            'symmetry':"LR"},
    'foot:intermediate-phalanx5':      {'tcName':'foot:intermediate-phalanx5',            'symmetry':"LR"},
    
    'foot:distal-phalanx2':      {'tcName':'foot:distal-phalanx2',            'symmetry':"LR"},
    'foot:distal-phalanx3':      {'tcName':'foot:distal-phalanx3',            'symmetry':"LR"},
    'foot:distal-phalanx4':      {'tcName':'foot:distal-phalanx4',            'symmetry':"LR"},
    'foot:distal-phalanx5':      {'tcName':'foot:distal-phalanx5',            'symmetry':"LR"},
    
    




#Arms (6)
    
    'arm:humerus':          {'tcName':'arm:humerus',        'symmetry':"LR"},
    'arm:ulna':             {'tcName':'arm:ulna',           'symmetry':"LR"},
    'arm:radius':           {'tcName':'arm:radius',         'symmetry':"LR"},
    

#Pelvis (4):
    
   # 'pelvic:coccyx':        {'tcName':'pelvis:coccyx',      'symmetry':"C"},
   # 'pelvic:sacrum':        {'tcName':'pelvis:sacrum',      'symmetry':"C"},
    #'pelvic:coxal':         {'tName':'pelvis:coxal','cName':'pelvis:hip','symmetry':"LR"},
    'pelvic:ilium':         {'tName':'pelvis:ilium','cName':'pelvis:hip','symmetry':"LR"},
    'pelvic:pubis':         {'tcName':'pelvis:pubis','symmetry':"LR"},
    'pelvic:ischium':       {'tcName':'pelvis:ischium','symmetry':"LR"},

#Legs (8)
    
    'leg:patella':  {'tName':'leg:patella','cName':'leg:knee',    'symmetry':"LR"},
    'leg:femur':    {'tName':'leg:femur','cName':'leg:thigh',      'symmetry':"LR"},
    'leg:tibia':    {'tcName':'leg:tibia',    'symmetry':"LR"},
    'leg:fibula':   {'tcName':'leg:fibula',    'symmetry':"LR"},

}




bonesurfaces = {

# Pelvis
    '*ilium:iliac-crest':       {'fk_bone':'*ilium','tName':'iliac-crest','type':'REGION','m2m_delay_asoc':['S|anterior-superior-iliac-spine','S|posterior-superior-iliac-spine']},
    '*ilium:ASIS':              {'fk_bone':'*ilium','tName':'anterior-superior-iliac-spine','type':"SPINE"},
    '*ilium:PSIS':              {'fk_bone':'*ilium','tName':'posterior-superior-iliac-spine','type':"SPINE"},
    '*ilium:AIIS':              {'fk_bone':'*ilium','tName':'anterior-inferior-iliac-spine','type':"SPINE"},
    '*ilium:PIIS':              {'fk_bone':'*ilium','tName':'posterior-inferior-iliac-spine','type':"SPINE"},
    '*ilium:inf-glut-line':     {'fk_bone':'*ilium','tName':'inferior-glutaeal-line','type':"LINE/RIDGE"},
    '*ilium:ant-glut-line':     {'fk_bone':'*ilium','tName':'anterior-glutaeal-line','type':"LINE/RIDGE"},
    '*ilium:pos-glut-line':     {'fk_bone':'*ilium','tName':'posterior-glutaeal-line','type':"LINE/RIDGE"},
    '*ilium:iliac-tubercle':    {'fk_bone':'*ilium','tName':'iliac-tubercle','type':"TUBERCLE",'m2m_delay_asoc':['S|iliac-crest']},
    '*ilium:arcuate-line':      {'fk_bone':'*ilium','tName':'arcuate-line','type':"LINE/RIDGE"},
    '*ilium:iliac-fossa':       {'fk_bone':'*ilium','tName':'iliac-fossa','type':"REGION",'m2m_delay_asoc':['S|arcuate-line','S|iliac-crest']},
    '*ilium:iliac-tuberosity':  {'fk_bone':'*ilium','tName':'iliac-tuberosity','type':"TUBEROSITY"},
    
    '*ischium:ischial-spine':       {'fk_bone':'*ischium','tName':'ischial-spine','type':"SPINE"},
    '*ischium:les-sci-notch':       {'fk_bone':'*ischium','tName':'lesser-sciatic-notch','type':"NOTCH",'m2m_delay_asoc':['S|ischial-spine']},
    '*ischium:gre-sci-notch':       {'fk_bone':'*ischium','tName':'greater-sciatic-notch','type':"NOTCH",'m2m_delay_asoc':['S|ischial-spine']},
    '*ischium:ischial-tuberosity':  {'fk_bone':'*ischium','tName':'ischial-tuberosity','type':"TUBEROSITY"},
    '*ischium:ischial-sup-ramus':   {'fk_bone':'*ischium','tName':'ischial-superior-ramus','type':"REGION",'m2m_delay_asoc':['S|ischial-tuberosity']},
    '*ischium:ischial-inf-ramus':   {'fk_bone':'*ischium','tName':'ischial-inferior-ramus','type':"REGION"},
    '*ischium|pubis:isc-pub-ramus': {'fk_bone':'*ischium|*pubis','tName':'ischiopubic-ramus','type':"REGION",'m2m_delay_asoc':['S|ischial-inferior-ramus','S|pubic-inferior-ramus']},
    
    '*pubis:pubic-crest':       {'fk_bone':'*pubis','tName':'pubic-crest','type':"REGION",'m2m_delay_asoc':['S|pubic-tubercle']},
    '*pubis:pubic-sup-ramus':   {'fk_bone':'*pubis','tName':'pubic-superior-ramus','type':"REGION",'m2m_delay_asoc':['S|pubic-tubercle']},
    '*pubis:pubic-tubercle':    {'fk_bone':'*pubis','tName':'pubic-tubercle','type':"TUBERCLE"},
    '*pubis:obturator-crest':   {'fk_bone':'*pubis','tName':'obturator-crest','type':"REGION",'m2m_delay_asoc':['S|pubic-superior-ramus','S|pubic-tubercle']}, #acetabular notch?
    '*pubis:pubic-inf-ramus':   {'fk_bone':'*pubis','tName':'pubic-inferior-ramus','type':"REGION",'m2m_delay_asoc':['S|pubic-superior-ramus','S|ischial-inferior-ramus']},
    '*pubis:pecten-pubis':      {'fk_bone':'*pubis','tName':'pecten-pubis','type':"LINE/RIDGE",'m2m_delay_asoc':['S|pubic-superior-ramus']},
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


}