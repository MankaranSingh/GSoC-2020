**Basic Information**
=====================

**Name:** Mankaran Singh

**Major:** Computer Science And Engineering

**Institute:** Thapar Institute of Engineering and Technology, Patiala.

**Github:** @MankaranSingh

**Email:** [*mankaran32@gmail.com*](mailto:mankaran32@gmail.com)

**Phone:** (+91) 9872901791

**Postal Address:** 2206, Krishna Nagar, Civil Lines, Ludhiana, Punjab,, India

**Timezone:** Indian Standard Time (UTC +5:30)

Technical Knowledge
--------
I am a sophomore pursuing Computer Engineering at Thapar Institute, Patiala. My specialization is in the field of Machine Learning and Back-end Web/API Development. 
I have done an internship in a company named *Hustlerpad Tech* for developing production ready back-end API. Most of the knowledge I have gained through is by reading quality books. I have been doing machine learning since past 2 years and am able to solve real-life problems using machine learning on my own experience. 

Some of my Machine Learning Projects are:
- Gesture replicating Robotic Arm using Deep Learning Approach.
- Worked with machine learning based text-to-speech and speech-to-text systems.
- Worked on building machine learning based chat-bots.
- Secured good rank in some machine learning competitions.
- Image compression using Deep Learning Techniques
- Generative Deep Learning 
- Currently leading my University Self Driving Car project.

In all these years, the most valuable skill i have gained is to develop solutions and solve problems of machine learning on my own even if very less resources are available on the internet using the experience gained over the time.

I am skilled at following languages/frameworks: Python, C++/C, Tensorflow, Keras, Flask, Pandas, Numpy.

**Programming Language Detection Using Machine Learning**
==================

Abstract
--------
The current methods of programming language classification (like linguists, pygments) rely heavily on custom handcrafted rules for many of it's classification tasks. Although handcrafted rules do a good job making file-level language predictions, its performance declines considerably when files use unexpected naming conventions and, crucially, when a file extension is not provided. Handcrafting rules brings along some major problems with it :

-  Less accuracy.
-  Easily fails on edge cases.
-  Requires fair amount of time in manually thinking and implementing rules.
-  Adding a new language in database for classification not so easy.

File names and extensions, while providing a good indication of what the coding language is likely to be, do not offer the full picture. Machine learning algorithms are widely used for automating the process of handcrafting rules and may surpass the performance and accuracy for a given task. A machine learning model would rather learn the **vocabulary** of various languages (like humans do) to classify the programming language. Deep neural networks are widely used in Language Processing tasks and have surpassed the performance of conventional approaches  in good amount of cases . This approach can work from file level or snippet level to potentially line-level language detection and classification.

Why is this needed ? 
--------
Accurate classification of programming language is an important task as :
- It would be easier to extract information about which other libraries and frameworks are imported, as our search has been narrowed down to a specific programming language.  
- Easier security vulnerability alerting 
- Accurate picture about the % ages of programming languages used for a project. 
- More relevant information extraction from text file in context of programming language.
- More accurately determining the purpose of a file. 
- And possibly, many others.

Even  GitHub has agreed to the fact that their current solution of programming language detection *'Linguist'* isn't that accurate and fails miserably  when files use unexpected naming conventions and, crucially, when a file extension is not provided.

Technical Details
--------
Machine learning is replacing conventional methods of solving a specific problem but one cannot 'just replace' the conventional methods with some fancy machine learning algorithms the reason being:
 
- Machine learning may be computationally expensive.
- Inference time of machine learning algorithms may be larger than conventional algorithms.
- The size of a machine learning model may be huge, ultimately increasing the size of the project.

Now, using machine learning instead of existing conventional approaches is viable only if:

- There are large gains upon accuracy over conventional approaches.
- The developed machine learning solution is not very computationally expensive and runs fast.
- The solution is easy to integrate into the existing workflow.
- The solution is easy to distribute, maintain and is flexible.

From my research, i have found that using machine learning for this use case is a viable option.

GitHub is moving from it's existing solution 'Linguist' to a machine learning based solution named as 'OctoLingua' - [source](https://github.blog/2019-07-02-c-or-java-typescript-or-javascript-machine-learning-based-classification-of-programming-languages/)
The following results were obtained using OctoLingua. We can see that OctoLingua maintains a good performance under various conditions, suggesting that the model learns primarily from the vocabulary of the code, rather than from meta information (i.e. file extension), whereas Linguist fails as soon as the information on file extensions is altered.

![Figure 1](https://i0.wp.com/user-images.githubusercontent.com/7935808/60456070-7abcd800-9bf5-11e9-8bd8-18eed09b3612.png?ssl=1)

The above results seem very impressive. But are they worth it considering the impact on performance and integration into the scancode workflow ?

Well, here are some tests that I performed over different text classification models for a particular text classification task:

**Huge Models (Transformers):**

- BERT: Accuracy - 93 %, Inference Time - 120 ms
- XLNet: Accuracy - 95.6 %, Inference Time - 155 ms
Average - High accuracy, large model sizes (200 MB - 2 GB), High Inference times.

**Normal Sized Models (RNNs):**

- LSTM Based: Accuracy - 91 %, Inference time - 1.2 ms (100 times faster than BERT)
- GRU Based: Accuracy - 90.2 %, Inference time - 0.5 ms
Average - High-Medium accuracy, small model sizes (3 MB - 50 MB), Low Inference times.

**Smaller Models (Non RNNs):**
- Simple DNN with few hidden layers - Accuracy 88 %, Inference time - 0.02 ms 
Average - Lower accuracy, lowest model sizes (1MB - 10 MB), lowest Inference times.

*Note: The accuracy may vary according to the given task. The inference times were calculated on CPU*

We can see that larger models have greater accuracy, whereas smaller models have lesser accuracy but the twist is that, there are huge performance gains.

The final conclusions about which models to use for classification can only be made after training many models of different architectures on the dataset of text files of programming languages and choose the one which have the best combination of model size, computation requirement, inference time, etc.

**Tech Stack:**

- Python
- Machine Learning Libraries: Keras, XGBoost, Scikit Learn (Final library would be selected based upon the best performing model)
- Beautiful Soup: For scraping data from web

Timeline
--------
**Pre GSoC :**
I'd focus on collecting the dataset required for training the model by scraping data from the internet. I'd also have make sure that the collected data is well balanced by analysing it though various data analytic techniques and would have to clean the dataset as required. This also makes my task easier in those 12 weeks and helps me concentrate on shipping professional code.

 **Community Bonding :**
Getting acquainted with the code base and the procedure that needs to be followed to submit code and get it reviewed. Discussing with the team on what exactly needs to be the problem statement (minute details, like kind of dataset we want to use, what parameters should be user choices, like parameters such as for training a newer model, adding a new programming language to the model, specifying a custom model prior to the scan, etc).

**Week 1**
Understand the relevant parts of the code base and try to figure out how the final product should look like, how this classifier would be integrated into the existing workflow and what standards we need to follow,

**Week 2**
This week would be spent upon analyzing and collection of data from the internet. Data cleaning would also be done. Finally, a fully cleaned and structured data-set, that is ready to be fed to machine learning algorithms would be prepared by the end of this week.

**Week 3-4**
This week would be spent on training various types of models. A full report upon the performance of all the models (like inference times, model size, accuracy, ease of integration, etc) would be documented for future reference.

**Week 5-6**
Once the final model is selected, this week would be spent upon integration of this classifier into the existing workflow.

**Week 7**
After the model integration, this week would be sent on writing various test cases based upon all the features that were integrated into the codebase in previous weeks.

**Week 8-10**
Take feedback from the community and iterate on the designs and improvise on use cases. Ensure code quality by adding more test cases

**Week 10-11**
Streamlining and standardizing  the ways of training our own custom model if needed

**Week 12**
Documentation

**Week 13** 
Spare week in case of some work getting delayed, in case of any emergency or otherwise.