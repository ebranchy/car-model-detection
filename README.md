# car-model-detection

Download the source dataset from https://www.kaggle.com/datasets/jessicali9530/stanford-cars-dataset/data and extract to the stanford-cars-dataset folders

CSV Lable Data sourced from https://github.com/BotechEngineering/StanfordCarsDatasetCSV
Format for these lables is x1,y1,x2,y2 (creating a rectangle inside the image with top left to bottom right position)
The training dataset contains a class and then the image name
The test dataset contains no class information

Top 2 rows from cardatasettrain.csv:
,x1,y1,x2,y2,Class,image
0,39,116,569,375,14,00001.jpg

Top 2 rows from cardatasettest.csv:
,x1,y1,x2,y2,image
0,30,52,246,147,00001.jpg 

Ultralytics expects a format of:
class x_center y_center width height
it expects a .txt format output, with one txt file per image
Finally, you have to normalise the values on a scale of 0-1

Objective:

I want to create a new csv file that takes the original 'cardatasettrain.csv'
as an input and then opens each image in turn to find the height and width of 
the original image so that I can create a normalised xywh format from 0-1 for 
the box coordinates of each lable.