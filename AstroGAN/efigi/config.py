'''
   1  T               - EFIGI morphological type
   4  Bulge_to_Total  - Bulge-to-total ratio
   7  Arm strength    - Strength of spiral arms
   10 Arm curvature   - Average curvature of the spiral arms
   13 Arm Rotation    - Direction of the winding of the spiral arms
   16 Bar length      - Length of the central bar
   19 Inner Ring      - Strength of the inner ring, lens or inner pseudo-ring
   22 Outer Ring      - Strength of outer ring
   25 Pseudo Ring     - Type and strength of outer pseudo-ring
   28 Perturbation    - Deviation from rotational symmetry
   31 Visible Dust    - Strength of dust features
   34 Dust Dispersion - Patchiness of dust features
   37 Flocculence     - Strength of scattered HII regions
   40 Hot Spots       - Strength of regions of strong star formation, active nuclei, or stellar nuclie
   43 Inclination     - Inclination of disks or elongation of spheroids
   46 Contamination   - Severity of contamination by stars, galaxies or artifacts
   49 Multiplicity    - Abundance of neighbouring galaxies
'''

import numpy as np

c1  = 0
c4  = 0
c7  = 1
c10 = 1
c13 = 0
c16 = 0
c19 = 0
c22 = 0
c25 = 0
c28 = 0
c31 = 1
c34 = 0
c37 = 0
c40 = 0
c43 = 0
c46 = 0
c49 = 1
redshift = 1

classes = np.asarray([c1, c4, c7, c10, c13, c16, c19, c22, c25, c28, c31, c34, c37, c40, c43, c46, c49, redshift])
