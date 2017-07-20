from __future__ import print_function

from leappto.actor_support.portannotation import PortAnnotation, DstPortAnnotation, FinalPortAnnotation, All
from leappto.msgtypes.msgtypes import ShellCommandStatus

inports_annotations = {'allstat': DstPortAnnotation(ShellCommandStatus, All)}
outports_annotations = {'msg': FinalPortAnnotation}

def func(allstat):
    msg = '{'
    for m in allstat.values():
        if m.errorinfo == None:
            msg += m.srcname + ':' + str(m.payload) + ',\n'
        else:
            msg += m.srcname + ':' + str(m.errorinfo) + ',\n'

    msg += '}'
    return msg

outports=('msg')
