import commands as cmd
import time

ListOfSamples=['/SingleMuon/Run2016B-23Sep2016-v3/MINIAOD',
               '/SingleMuon/Run2016C-23Sep2016-v1/MINIAOD',
               '/SingleMuon/Run2016D-23Sep2016-v1/MINIAOD',
               '/SingleMuon/Run2016E-23Sep2016-v1/MINIAOD',
               '/SingleMuon/Run2016F-23Sep2016-v1/MINIAOD',
               '/SingleMuon/Run2016G-23Sep2016-v1/MINIAOD']

ITime=time.localtime()
StringITime=str(ITime.tm_year)+'_'+str(ITime.tm_mon)+'_'+str(ITime.tm_mday)+'_'+str(ITime.tm_hour)+'_'+str(ITime.tm_min)
print "Submitting Jobs "+StringITime

WorkingFolder='CrabConfigs_'+StringITime
cmd.getoutput('mkdir '+WorkingFolder)

for i in ListOfSamples:
    UsefulString=i.split('/')[1]+"_"+i.split('/')[2]
    cmd.getoutput('cp Crab_Template_ReRecoRunBtoG.py '+WorkingFolder+'/Crab_'+UsefulString+'.py')
    cmd.getoutput('sed -i -- "s#OUTPUTDIR#jruizalv/VLF_ANA/SingleMuon_WjetsEstimation#g" '+WorkingFolder+'/Crab_'+UsefulString+'.py')
    cmd.getoutput('sed -i -- "s/CMSCONFIG/Wpjets_Estimation_cfg.py/g" '+WorkingFolder+'/Crab_'+UsefulString+'.py')
    cmd.getoutput('sed -i -- "s/TASK/'+UsefulString.split('Tune')[0]+i.split('/')[2].split("_")[-1]+'_'+StringITime+'/g" '+WorkingFolder+'/Crab_'+UsefulString+'.py')
    cmd.getoutput('sed -i -- "s#DATASAMPLE#'+i+'#g" '+WorkingFolder+'/Crab_'+UsefulString+'.py')
    print "Job being submitted: "+UsefulString
    CrabOutput=cmd.getoutput('crab submit -c '+WorkingFolder+'/Crab_'+UsefulString+'.py')
    print CrabOutput
    print "---------------------------------------------------------------------------------------"
