# Distance code for chemical shift calculation


## Binder (working example)
Link to Binder: 
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/steto123/dcode/06729e4831939ecd5ced530d9506835b1e713701?urlpath=lab%2Ftree%2Fcalc-shift-v.04.ipynb)



## Introduction

DCode stands for Distance Code, a distance based linear code for describing the atom environment

### Steps and Rules

​	1.Generating the 3D coordinates with MMFF (maximum of 20 runs with 200 iterations each).

​	2.Generating the DCode atom name

​		1.Hydrogens remain simply H

​		2.The first element is the atomic symbol (C, S, Br, etc.)

​		3.The second element is the number of neighbors (atom.GetNeighbors())

​		4.Ring: "r" for an atom in a ring and "n" for an atom not in a ring.

​		5.Chirality: Default is No

​			1.CHI_ALLENE = Al

​			2.CHI_OCTAHEDRAL = Ot

​			3.CHI_OTHER = Oh

​			4.CHI_SQUAREPLANAR = Sp

​			5.CHI_TETRAHEDRAL = Tt

​			6.CHI_TETRAHEDRAL_CCW = CC

​			7.CHI_TETRAHEDRAL_CW = CW

​			8.CHI_TRIGONALBIPYRAMIDAL = Bp

 	3. Build the final DCode



### Building the Code



![l-alanin](pictures/l-alanin.png)

The code starts with the DCodeName for the atom being considered and is separated from the rest by an @. All other atoms are then separated by a #. They are sorted by increasing distance. At 6 angstroms, the process stops.

<u>Example C-2 L-Alanin</u>
C4nCC@H#N3nNo#C4nNo#C3nNo#H#H#H#H#H#O2nNo#O1nNo#H#



### The finale DCode Collection

Origin: NMRShiftDB (all sdf- entries with only one 13C- assignment)
Number of generated code´s: 343625
Minimum number of neighbours: 2

![Verteilung](pictures/Verteilung.png)



The image above shows the distribution plot of the number of neighbors recorded in the DCode. The distance is limited to 6 Angstroms. The x-axis shows the number of recorded neighbors, and the y-axis shows the number of corresponding DCodes.

![Verteilung2](pictures/Verteilung2.png)

The second distribution plot shows the chemical shifts recorded in the codebase, in steps of 10 ppm.  The chemical shift is plotted on the x-axis, and the number of cases on the y-axis.



<u>The minimum an maximum entry:</u>

With a chemical shift of -45.8 ppm for C-Atom 1

![minimum](pictures/minimum.png)



With a chemical shift of 292.5 for C- Atom 5:

![maximum](pictures/maximum.png)
