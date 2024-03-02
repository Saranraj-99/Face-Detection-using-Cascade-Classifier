**Introduction**

Face detection has much significance in different fields of today’s world. It is a significant step in several applications, face recognition (also used as biometrics), photography (for auto-focus on the face), face analysis (age, gender, emotion recognition), video surveillance, etc.One of the popular algorithms for facial detection is “haarcascade”. It is computationally less expensive, a fast algorithm, and gives high accuracy.

**Haarcascade file has been uploaded for reference**

It works in four stages:

**1.Haar-feature selection** 
A Haar-like feature consists of dark regions and light regions. It produces a single value by taking the difference of the sum of the intensities of the dark regions and the sum of the intensities of light regions. It is done to extract useful elements necessary for identifying an object.

**2.Creation of Integral Images**

A given pixel in the integral image is the sum of all the pixels on the left and all the pixels above it. Since the process of extracting Haar-like features involves calculating the difference of dark and light rectangular regions, the introduction of Integral Images reduces the time needed to complete this task significantly.

**3.AdaBoost Training**

This algorithm selects the best features from all features. It combines multiple “weak classifiers” (best features) into one “strong classifier”. The generated “strong classifier” is basically the linear combination of all “weak classifiers”.

**4.Cascade Classifier**

It is a method for combining increasingly more complex classifiers like AdaBoost in a cascade which allows negative input (non-face) to be quickly discarded while spending more computation on promising or positive face-like regions. It significantly reduces the computation time and makes the process more efficient.
