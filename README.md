# CompressionQualityAnalysis
Computes MSR and PSNR after compression of an image to check the compression quality.

#Prerequisites
* [Numpy](http://www.numpy.org/)
* [Opencv](https://opencv.org/)

# To compute
Replace orignal_image.png and compressed_image.png with your own image files. 
Run python file PSNR.py
```
Python3 PSNR.py
```

![alt text](https://github.com/vasutomar/CompressionQualityAnalysis/blob/master/example_image.jpg "Example_image")

# Significance of PSNR value
PSNR values defines how well a compression algorithm functions, lower PSNR values (0-15db) measns that the quality of restored image is bad, higher PSNR values (approximately 30-40db) means the compression algorithm works well. 

#Credits
* **Mohd. Omama** - *Improvements in implementation* - [Mohd Omama](https://github.com/mohdomama)

# References
* [Measures of image quality](https://homepages.inf.ed.ac.uk/rbf/CVonline/LOCAL_COPIES/VELDHUIZEN/node18.html) 
* [Peak signal to noise ratio](https://en.wikipedia.org/wiki/Peak_signal-to-noise_ratio)
