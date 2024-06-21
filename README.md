# Occlusion from OS end Using python

## Environment Setup
Python 3.12 with keyboard and tkinter packages installed

## Run
1. Python occlusion\.py -t \<Occolusion time> -s \<Stackable or not> -a \<adaptive or not>:  
   This is to start visual occolusion from OS end with Occolusion time period you decide. Press space will show the creen for some time (Occolusion time period you decide) and turn it black
   afterwards. Python_occlusion_validation.txt stores the real time of Screen-On for a series of clicks. For arguments, 1 means stackable and 0 means non-stackable. 1 means adaptive and 0 means non-adaptive.  
   Example command: Python occlusion.py -t 0.500 -s 1 -a 1  
2. Python /path/python Python_occ_valid.py:  
   This will caculate the statistics of the results and store them in statistics.csv and make a bar plot of the data for visualization.

## What's adaptive mode?
Using dynamic correction of Screen-On time:  
If the real real time of Screen-On of previous click is larger then we expect, next time the input to the .sleep() function will be downscaled for correction. On the contrary, if the real real time of Screen-On of previous click is less then we expect, next time the input to the .sleep() function will be upscaled. Using this approach, even on different computer and 
different computer usage environment, we can make sure that the real time of Screen-On is very close to what we expected.

## What's difference between stackable and non-stackable mode
The difference shows in the case when you press key many times in a short time (shorter than the occlusion time you set). If you choose non-stackable mode, the screen will turn black \<Occolusion time> pass your last key press. If you choose stackable mode instead, the time the screen turn black depends on how many times you press the key. Each key press will extend the sceen visible time by \<Occolusion time>.  
These two mode are for different preference and purpose of use.


## Example Results
See text files and csv files attached in this folder.