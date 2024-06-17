## Environment Setup
Python 3.12 with keyboard and tkinter packages installed

## Run
1. Python /path/occlusion_validation.py -t \<Occolusion time you want>:  
   This is to start visual occolusion from OS end with Occolusion time period you decide. Press space will show the creen for some time (Occolusion time period you decide) and turn it black
   afterwards. Python_occlusion_validation.txt stores the real time of Screen-On for a series of clicks. 
2. Python /path/python Python_occ_valid.py:  
   This will caculate the statistics of the results and store them in statistics.csv and make a bar plot of the data for visualization.

## Some Implement Detail
Using dynamic correction of Screen-On time:  
If the real real time of Screen-On of previous click is larger then we expect, next time the input to the .sleep() function will be downscaled for correction. On the contrary, if the real real time of Screen-On of previous click is less then we expect, next time the input to the .sleep() function will be upscaled. Using this approach, even on different computer and 
different computer usage environment, we can make sure that the real time of Screen-On is very close to what we expected.


## Example Results
Set script_out.txt and statistics.csv