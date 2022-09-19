import torch
import cv2
import matplotlib.pyplot as plt

import replicate
model = replicate.models.get("pixray/text2image")
output = model.predict(prompts="Cairo skyline at sunset.")

# plt.imshow(img)