import os, sys
from PIL import Image, ImageDraw
from tqdm import tqdm
import numpy as np
from time import perf_counter



main_board = Image.new('RGB', (1920*3, 1080*3))


end_folder = "end/"
if not os.path.exists(end_folder):
   os.makedirs(end_folder)

print("Rendering...")
#for k in tqdm(range(apple_num_frames)):
apple_num_frames = 2589

for k in tqdm(range(apple_num_frames+1)): 


    board = main_board


    b = len(str(k))-1 #1-9 returns 0, 10-99 returns 1, 100-999 returns 2...
    zero = "0"*(5-b) #Sony vegas image sequences are name_000000
    name = "a_"+zero + str(k) #an example of name is a_000123 (frame 123)

    source = Image.open("apple/"+name+".jpeg").convert('L') #the source image in black and white
    source = source.point(lambda x: 255 * (x > 128))
    source = source.resize((800,800), resample=Image.BILINEAR)
    source = source.convert('RGB')

    source.save('end/'+name+'.png')



    
    # board.paste(source, ( int((board.width - source.width)/2) , int((board.height - source.height)/2)  ))

    # board = board.convert('L')
    # board = board.resize((800,int(1080/1920 * 800)), resample=Image.BILINEAR)
    # board = board.resize((800,800), resample=Image.BILINEAR)


    # binarized_board = board.point(lambda x: 255 * (x > 128))
    # binarized_board = binarized_board.convert('RGB')
    # binarized_board.save('end/'+name+'.png')


print("Done!")
