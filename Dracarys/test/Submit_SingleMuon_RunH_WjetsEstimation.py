import commands as cmd
import time

ListOfSamples=[#'/SingleMuon/Run2016H-PromptReco-v1/MINIAOD',
               '/SingleMuon/Run2016H-PromptReco-v2/MINIAOD',
               '/SingleMuon/Run2016H-PromptReco-v3/MINIAOD']

ITime=time.localtime()
StringITime=str(ITime.tm_year)+'_'+str(ITime.tm_mon)+'_'+str(ITime.tm_mday)+'_'+str(ITime.tm_hour)+'_'+str(ITime.tm_min)
print "Submitting Jobs "+StringITime

WorkingFolder='CrabConfigs_'+StringITime
cmd.getoutput('mkdir '+WorkingFolder)

for i in ListOfSamples:
    UsefulString=i.split('/')[1]+"_"+i.split('/')[2]
    cmd.getoutput('cp Crab_Template_PromptRecoRunH.py '+WorkingFolder+'/Crab_'+UsefulString+'.py')
    cmd.getoutput('sed -i -- "s#OUTPUTDIR#jruizalv/VLF_ANA/SingleMuon_WjetsEstimation#g" '+WorkingFolder+'/Crab_'+UsefulString+'.py')
    cmd.getoutput('sed -i -- "s/CMSCONFIG/Wpjets_Estimation_cfg.py/g" '+WorkingFolder+'/Crab_'+UsefulString+'.py')
    cmd.getoutput('sed -i -- "s/TASK/'+UsefulString.split('Tune')[0]+i.split('/')[2].split("_")[-1]+'_'+StringITime+'/g" '+WorkingFolder+'/Crab_'+UsefulString+'.py')
    cmd.getoutput('sed -i -- "s#DATASAMPLE#'+i+'#g" '+WorkingFolder+'/Crab_'+UsefulString+'.py')
    print "Job being submitted: "+UsefulString
    CrabOutput=cmd.getoutput('crab submit -c '+WorkingFolder+'/Crab_'+UsefulString+'.py')
    print CrabOutput
    print "---------------------------------------------------------------------------------------"
