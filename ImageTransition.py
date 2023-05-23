import numpy as np
from PIL import Image

# Reading Images
image1_path = "stock1.jpg"
image2_path = "stock2.jpg"
im1 = Image.open(image1_path)
im2 = Image.open(image2_path)

# Bringing Both Image to same resolution
width1, height1 = im1.size
width2, height2 = im2.size
width, height = (width1+width2)//2, (height1+height2)//2
im1 = im1.resize((width, height))
im2 = im2.resize((width, height))

# Creating Frames of the Transition
steps = 20
transition_frames = [Image.blend(im1, im2, i)
                     for i in np.linspace(0, 1, steps)]
# transition_frames = transition_frames + transition_frames[::-1]

# Creatong GIF from transition frames
transition_frames[0].save("out.gif", save_all=True,
                          append_images=transition_frames[1:],
                          duration=1000/steps,
                          loop=0)
