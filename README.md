# Mini_Project2

1. This is a project for building a CNN model to predict a photo if it is a car or a bus. By using python3 and tensorflow, dataset from MIO-TCD dataset: http://podoce.dinf.usherbrooke.ca/challenge/dataset/. 

2. The photos of training set is 1328 and testing set is 332. The batch size is 32, image size is 64x64x3 by pre-processing from the photos. The validation rate is 0.2 and the drop-out rate is 0.3 in the model.

3. The sturcture of the model is shown below:
https://github.com/ZhibinHuang/Mini_Project2/issues/1#issue-374173005

4. Compare between two different systems: 
   Generlly speaking, different systems have different module with different structure. How to evaluate a system it's usually based on some simensions such as the stability, accuracy, speed and so on. Base on the literature reviewed, I found the following aspects about comparing two different systems. 
   The first one is the structure of the system, which is also the most important one. Because different sturcture of system could have various performance. Let's take the AlexNet CNN Network Architecture acknowledged since 2012, has 5 convolutional layers, 3 max pool layers and 3 full connection layers. Which performs more better than LeNet (1 convolution,1 pool and 3 full connections). 
   The second factor is the arguments in the system. ZFNet is a better network than AlexNet is mainly because the former improve some arguments in the latter while the structure is almost the same.
   The other factors such as input, energy comsumtion and resources required is also related with the performance of different systems. I don't disscuss further here since they are not the main reason.
   
5. If you have questions, please contact me: hzhibin@bu.edu



References:

Marcus, G. (2018). Deep learning: A critical appraisal. arXiv preprint arXiv:1801.00631.

Besold, T. R., Garcez, A. D., Bader, S., Bowman, H., Domingos, P., Hitzler, P. et al. (2017).Neural-Symbolic Learning and Reasoning: A Survey and Interpretation. arXiv, cs.AI. 

Bošnjak, M., Rocktäschel, T., Naradowsky, J., & Riedel, S. (2016). Programming with a Differentiable Forth Interpreter. arXiv.
Bottou, L. (2015). Two big challenges in machine learning. Proceedings from 32nd InternationalConference on Machine Learning.

Bowman, S. R., Angeli, G., Potts, C., & Manning, C. D. (2015). A large annotated corpus for learning natural language inference. arXiv, cs.
