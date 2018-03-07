from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'TASK'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = False
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'CMSCONFIG'
#config.JobType.maxMemoryMB = 2500

config.Data.inputDataset = 'DATASAMPLE'
config.Data.inputDBS = 'global'
#config.Data.splitting = 'FileBased'
config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 500000
#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.outLFNDirBase = '/store/user/OUTPUTDIR/'
config.Data.publication = False
config.Data.outputDatasetTag = 'TASK'

config.Site.storageSite = 'T2_CH_CERN'
