# Detect_Skin_Color_Using_yCrCb

Human Skin Color

- Encoded nonlinear RGB signal, commonly used in video coding and image compression work.
- constructed as a weighted sum of the RGB values, and two color difference values Cr and Cb that are formed by subtracting luma from RGB red and blue components
  16 to 235 for Y, 16 to 240 for Cb and Cr
- Skin pixels form a compact cluster in the Cb-Cr plane.
  Y = 0.299R + 0.587G + 0.114BY=0.299R+0.587G+0.114B
  C_r = R - Y
  C_b = B- Y
- Transformation simplicity and explicit separation of luminance and chrominance components makes this colorspace attractive for skin color modelling
