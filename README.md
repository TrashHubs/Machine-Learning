# Machine Learning

We use tensorflow as main library that we used to develop the CNN model. And used the another library as support the preprocessing the dataset.

> [!NOTE]
> This Link for .h5 model, json-model, and datasets that where it uses : [Link For Dataset,model.h5,and Converted model to JSON-MODEL](https://drive.google.com/drive/folders/1D155_PddvgVCwRZg4IIHKTHV7DFiSIdo?usp=sharing)

## Requirements

The model for this project using **python version 3.9.x** and requires importing libraries with appropriate versions :

```
tensorflow==2.13.0
numpy==1.24.3
pandas==2.0.3
scikit-learn==1.2.0
scipy==1.10.1
tensorflowjs==4.12.0 -> This Require For Convert
```

> [!WARNING]
> Please use the followin versions, using different version may can make it error.

## Detail Of Dataset

The following data set is used from Kaggle :

- [First Dataset](https://www.kaggle.com/datasets/mostafaabla/garbage-classification)
- [Second Dataset](https://www.kaggle.com/datasets/fatemehboloori/trash-type-detection)

  And it merge into a large Dataset :
  
### **First Dataset Detail**

![First Dataset Detail](https://github.com/TrashHubs/Machine-Learning/assets/33770553/8d433f64-b282-4d2e-860b-ba79991b9a76)

### **Second Dataset Detail**

![Second Dataset Detail](https://github.com/TrashHubs/Machine-Learning/assets/33770553/8fbf8eda-ddc2-46e4-8c4a-562e18e7081c)

### **And After Merge it**

![Used Dataset](https://github.com/TrashHubs/Machine-Learning/assets/33770553/910315a1-f468-4b0e-a50f-68d8e0a11a4d)



## **Model Architecture**

Choosing this model Architecture, after create and evaluate the model by model layer created. The final model Architecture that used :

![Model Architecture](https://github.com/TrashHubs/Machine-Learning/assets/33770553/835b7d08-9377-43ff-8b75-998620376ca0)


### **Train Model Chart Result**

![Train Chart Result](https://github.com/TrashHubs/Machine-Learning/assets/33770553/7fcc40fa-1a7f-4123-aaa6-e971c95f327e)


### **The Last Accuracy**

`Akurasi validasi: 95.55%`


> [!NOTE]
> Hope The Documentation can help understand the model. 
