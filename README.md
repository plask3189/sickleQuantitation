# sickleQuantitation
# sickleQuantitation with iteration over files  # Takes data from a single image and returns the percent sickle for that one image. # Super inefficient but it works.

Input: A directory with images with blood cells
Output: Percentage of sickle cells for each image.

sickleCounter3.ijm is opened in Fiji ImageJ which prompts for an input directory of images and
an output directory for resulting .csv files for each image. 

The output directory is then run through batchSickleQuantitation.py which returns the percentage of 
sickle cells for each .csv file passed through. 
