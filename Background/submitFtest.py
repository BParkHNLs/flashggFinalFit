import os


class window(object):
  def __init__(self,m,s,ns):
    self.m = m
    self.s = s
    self.ns = ns



if __name__ == "__main__":
  
  tag = "D1_v01" 
  doCopyEOS = True
  doCleanEOS = True
  doRun = True

  windows = [
  #window(1.00,0.009,5),
  window(2.75,0.025,5),
  window(3.00,0.025,5),
  #window(4.50,0.037,5),
  ]

  cats = [
  "lxy0to1_OS", 
  "lxy0to1_SS", 
  "lxy1to5_OS", 
  "lxy1to5_SS", 
  "lxygt5_OS", 
  "lxygt5_SS",
  ]
  
  #doBlind = False
  if doCopyEOS and doCleanEOS:
    # clean existing dir in eos
    os.system("rm -rf /eos/home-m/mratti/www/BHNL/recoAnalysis/fTest/{tag}/".format(tag=tag))
    os.system("mkdir /eos/home-m/mratti/www/BHNL/recoAnalysis/fTest/{tag}/".format(tag=tag))
    os.system("cp HTACCESS /eos/home-m/mratti/www/BHNL/recoAnalysis/fTest/{tag}/.htaccess".format(tag=tag))
 
  
  for w in windows:
    wtag = "m{:.2f}_s{:.3f}_ns{}".format(w.m,w.s,w.ns)
    for i,cat in enumerate(cats):
      inpath = "/work/mratti/BParkingNano/Oct_CMSSW_10_2_15/CMSSW_10_2_15/src/PhysicsTools/BHNLAnalysis/exampleWS/wsAnalysis/"
      inws = inpath + "allData_" + wtag + ".root"
      outws = "{tag}/window_{wtag}/ws/CMS-BHNL_multipdf_{cat}.root".format(tag=tag,wtag=wtag,cat=cat)
      outdir = "{tag}/window_{wtag}/".format(tag=tag,wtag=wtag)
      command = "./bin/fTest -i {inws} --saveMultiPdf {outws}  -D {outdir} -f {cat} --mN {m} --sigma {s} --nsigma {ns}  --isData 1 --year 2018 --catOffset {catoffset}".format(
                     inws=inws,
                     outws=outws,
                     outdir=outdir,
                     cat=cat,
                     m=w.m,
                     s=w.s,
                     ns=w.ns,
                     catoffset=i,
                   )

      if not os.path.exists(outdir+'ws'): 
        os.makedirs(outdir+'ws')

      print "\n\n\n\n"
      print "*********************************"
      print "===> F-test analysis:"
      print "         mass   : {:.2f}".format(w.m)
      print "         sigma  : {:.2f}".format(w.s)
      print "         nsigma : {:.2f}".format(w.ns)
      print "         cat    : {}".format(cat)
      print "*********************************"
      print command
      if doRun:
        os.system(command) 

    if doCopyEOS:
      print "===> Copying results to EOS" 
      os.system("cp -r {outdir} /eos/home-m/mratti/www/BHNL/recoAnalysis/fTest/{outdir}".format(outdir=outdir))
      os.system("cp HTACCESS_SUB /eos/home-m/mratti/www/BHNL/recoAnalysis/fTest/{outdir}/.htaccess".format(outdir=outdir))
      print "*********************************"





