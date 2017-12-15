# HEU_Deep_Learning_Group
## 第一次研讨会
> 于2017年11月24日下午6:00开始
### 朱磊

DeepLearning基本的概念
深度学习中搜索算法的应用

### 李昕达

CNN图像分类

K近邻分类器

选用L范数的问题

线性分类器的损失函数

regularization的作用是防止过拟合
### 朱元微

基础知识

对神经网络的理解，如何模拟一个函数。

问题：克服高阶多项式的缺点，防止过拟合。

### 朱鸿林

CS229是推荐课程

CNN改变了传统的端到端的做法，通过提取特征到pool层来得出最后的结果。

卷积层对每一格子进行卷积，得到一张带有某种特征的模糊图像

### 吴哲远
安装python 讨论卷积问题，
某软件可对pdf文件进行加解密，找文献上SCI-HUB
>海洋deep learning 论文
>安装python跑程序

### 苏敏利
用matlab做神经网络可以不借助工具箱

视频资源请看deep learning。

书推荐《机器学习》《统计学习方法》

### 付岳霖
可使用Kaggle上的数据集进行处理

### 王志航
学习CS229和选用TensorFlow

## 第二次研讨会
> 于2017年12月1日下午6:00开始
### 朱磊：SGD的学习率太慢，所以要加momentum项

保存了前一项信息，不只是遵循梯度进行下降。Nestow很牛，一般加Nestow momentum项。

SGD+momntum

再一个就是Adagra

> Adagrad [8] is an algorithm for gradient-based optimization that does just this: It adapts the learning rate to the parameters, performing larger updates for infrequent and smaller updates for frequent parameters. For this reason, it is well-suited for dealing with sparse data. Dean et al. [6] have found that Adagrad greatly improved the robustness of SGD and used it for training large-scale neural nets at Google, which – among other things – learned to recognize cats in Youtube videos10. Moreover, Pennington et al. [16] used Adagrad to train GloVe word embeddings, as infrequent words require much larger updates than frequent ones.

adaptive就是适应学习率。

Ada delta改进Adagra不使用G而使用E[g^2]。这个期望非单调增加，改进了G单调增加的缺点。这个方法不需要全局learning rate，这个learning rate不需要给出。

Hinton 提出了Ada delta的一个特例。取lamda=0.9,这个方法呃大概是hinton牛逼吧。

Adam（Adaptive Moment Estimation）矩估计。m是一阶矩,然后修正了一下，变成无偏估计，把矩替换了梯度。除的那一项变成标准化。
我们想要算法收敛，我们想要算法收敛的又快又准。所谓的所有的优化收敛算法，主要纠结方向和在方向上走的大小。(momentum方向是修正方向)理解负梯度方向是最速下降方向是有问题的。我们现在大多数是研究D1L，D2NL主要有算Hessian Matrix，Fisher Matrix的逆（这里优化计算逆是一种方向）。很多神经网络的论文都是在 lost function 上面动手脚的加了一项正则（2范数1范数自身相乘）。

计算能力和算法性能优先算法性能,选择合适的算法是很重要的，可以加速思维的迭代速度。

### 朱元威

SVM：处理交叉的分类算法。与其寻找复杂的线，不如解决超平面的问题。升维与降维的问题来解决分类不好分的文题。SVM善于处理小样本。PCA是一个维度下降的算法。
机器学习是一个老词，因为深度学习，机器学习火了。

介绍决策树算法，首先介绍训练集。

特征空间是训练集X的特征向量的集合，决策树就是用2叉或n叉树对训练集空间分块
# 第三次研讨会
> 于2017年12月8日下午6:00开始

主要讨论了python写作的相关内容

# 第四次研讨会
> 于2017年12月15日下午6:00开始

与会者：李昕达、谢佳昕

###李昕达
CART生成树
###谢佳昕
遗传算法初步
