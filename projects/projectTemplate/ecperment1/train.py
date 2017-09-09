# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from lib import *
import sys,os
import lib
from lib import dicto, glob, getArgvDic,filename
from lib import show, loga, logl, imread, imsave
from configManager import (getImgGtNames, indexOf, readgt, readimg, 
                           setMod, togt, toimg, makeTrainEnv)

from config import c, cf

setMod('train')

from configManager import args
args.names = getImgGtNames(c.names)[:]
args.prefix = c.weightsPrefix
args.classn = 2
args.step = 64*7
# =============================================================================
# config BEGIN
# =============================================================================
args.update(
        batch=5,
        epoch=10,
        resume=0,
        )
# =============================================================================
# config END
# =============================================================================




argListt, argsFromSys = getArgvDic()
args.update(argsFromSys)

makeTrainEnv(args)

if __name__ == '__main__':
    import trainInterface as train
    train.train()
    pass

