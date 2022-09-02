
library(tidyverse)
# take mouseInfoOutput.csv, calc avgs, make graph.
mouseInfoDF <- read.csv(file = "/Users/kateplas/Documents/Lab/ImageJproject/sickCellCountPrgrm/batchAnalysisOutput/mouseInfoOutput.csv")
# mouseInfoDF[1, ] # Prints data frame where a mouseID and %sick 

# if first five characters of mosue id are the same, add them to new data frame?
# retval <- subset(mouseInfoDF, )
# for(i in 1:nrow(mouseInfoDF)){
 # mouseInfoElement <- mouseInfoDF[i, ]
 # print(mouseInfoElement)
#}

mouseID <- data.frame(mouseInfoDF[0, i]) # increment along the top columns of the row
print(mouseID)
print(mouseInfoDF[0, ])


