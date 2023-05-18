# Muscle Ultrasound Image Segmentation using Deep Learning: A Comparative 057 058 Study of FCN, U-Net and its variations
Python notebook for the implementation of deep learning algorithm for the segmentation of muscles ultra sound images.

Advised by professor Bryan Ranger, we identified the space for a research that connects the growth pace of the children with the thickness of their muscles.
In order to achieve our purposes, we will be working with different pre-existing Deep Learning models for seg- mentation. We will implement minor changes to reach the highest scores on the specific task of muscle measurements.

The dataset we were given from the lab of professor 194 Bryan ranger, is composed of 300 images of size 415 x 195 287. Each image has its own mask, namely a binary im- 196 age, highlighting the segmentation task we need to com- 197 plete. Due to privacy reasons the data are not uploaded 

When training deep learning models for image segmentation tasks, we started with the U-Net architecture and
gradually progressed to more advanced models such as U-Net++, U-Net 3+. We finished by implementing FCN. For
each of these models, we initially used implementations that were available from other researchers and adapted them to
suit our specific task and dataset. We decided to utilize the Binary Cross Entropy as the loss function and the stochastic gradient descent as the optimizer.

In the notebook _Project.ipynb_ is possible to find the pre-processing of the data, the training and testing of the models.
In the python files it is possible to find the model implementation.

UNET from https://github.com/nikhilroxtomar/Semantic-Segmentation-Architecture/blob/main/PyTorch/unet.p \\
UNET3plus from https://github.com/avBuffer/UNet3plus_pth

Finally, we have developed a simple algorithm that measures the thickness of the muscle. It first measure for each column of the image the longest consecutive list of white 
pixels and, then, it takes its average. The decided to implement this instead of just computing the average of white 
pixels per column, to minimize the possibility of mistake.

Thanks to our experiments we observed, as expected, that U-net models and its variations, perform way better
than FCNN. As mentioned above, these models were born as an improvement of FCNN.
U-net ++ is the model we decided to retain for our further analysis, since it is faster than U-net 3-plus and slightly better than U-net. 
Our next step in the project is the employment of this trained model on real clinical data, as soon as they will be given to the lab.
