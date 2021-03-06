'''

   Collecting stats on the efigi dataset

'''

import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--DATA_DIR',   required=True, help='Directory where data is', type=str,default='./')

a = parser.parse_args()
DATA_DIR = a.DATA_DIR

f1 = DATA_DIR+'EFIGI_attributes.txt'
f2 = DATA_DIR+'EFIGI_coord_redshift.txt'

redict = {}
d=0
with open(f2,'r') as f:
   for line in f:
      if d==0:
         d=1
         continue
      line = line.rstrip().split()
      galaxy_id = line[0]
      redshift  = float(line[9])
      if redshift < 0: continue
      redict[galaxy_id] = redshift

'''
   7  Arm strength    - Strength of spiral arms
   10 Arm curvature   - Average curvature of the spiral arms
   31 Visible Dust    - Strength of dust features
   49 Multiplicity    - Abundance of neighbouring galaxies
'''
arm_s = []
arm_c = []
vd    = []
mult  = []
red   = []
idx = np.asarray([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49])

with open(f1,'r') as f:
   #idx = np.array([7, 10, 31, 49])
   for line in f:
      line = line.rstrip().split()
      galaxy_id = line[0]
      line = np.asarray(line[1:])
      line = line[idx].astype('float32')
      line = np.asarray([float(x) for x in line])
      try: line = np.append(line, redict[galaxy_id]) # if using redshift, add it to the attributes
      except: continue

      for x in line:
         if float(x) == float(-99.0): print galaxy_id
         if float(x) == float(-99): print galaxy_id
      #arm_s.append(line[0])
      #arm_c.append(line[1])
      #vd.append(line[2])
      #mult.append(line[3])
      #red.append(line[4])


exit()
arm_s = np.asarray(arm_s)
arm_c = np.asarray(arm_c)
vd = np.asarray(vd)
mult = np.asarray(mult)
red = np.asarray(red)

print 'min,max,mean,std\n'
print 'Arm Strength\n---------------------------\n',np.min(arm_s),',',np.max(arm_s),',',np.mean(arm_s),',',np.std(arm_s),'\n'
print 'Arm Curvature\n---------------------------\n',np.min(arm_c),',',np.max(arm_c),',',np.mean(arm_c),',',np.std(arm_c),'\n'
print 'Visible Dust\n---------------------------\n',np.min(vd),',',np.max(vd),',',np.mean(vd),',',np.std(vd),'\n'
print 'Multiplicity\n---------------------------\n',np.min(mult),',',np.max(mult),',',np.mean(mult),',',np.std(mult),'\n'
print 'Redshift\n---------------------------\n',np.min(red),',',np.max(red),',',np.mean(red),',',np.std(red),'\n'


