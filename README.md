# HEU_Deep_Learning_Group
## 第二次研讨会
> 于2017年12月1日下午6:00开始
>朱磊：SGD的学习率太慢，所以要加momentum项

保存了前一项信息，不只是遵循梯度进行下降。Nestow很牛，一般加Nestow momentum项。

SGD+momntum

再一个就是Adagra
>Adagrad [8] is an algorithm for gradient-based optimization that does just this: It adapts the learning rate to the parameters, performing larger updates for infrequent and smaller updates for frequent parameters. For this reason, it is well-suited for dealing with sparse data. Dean et al. [6] have found that Adagrad greatly improved the robustness of SGD and used it for training large-scale neural nets at Google, which – among other things – learned to recognize cats in Youtube videos10. Moreover, Pennington et al. [16] used Adagrad to train GloVe word embeddings, as infrequent words require much larger updates than frequent ones.

adaptive就是适应学习率。
Ada delta改进Adagra不使用G而使用E[g^2]。这个期望非单调增加，改进了G单调增加的缺点。这个方法不需要全局learning rate，这个learning rate不需要给出。
Hinton 提出了Ada delta的一个特例。取lamda=0.9,这个方法呃大概是hinton牛逼吧。
Adam（Adaptive Moment Estimation）矩估计。m是一阶矩,然后修正了一下，变成无偏估计，把矩替换了梯度。除的那一项变成标准化。
我们想要算法收敛，我们想要算法收敛的又快又准。所谓的所有的优化收敛算法，主要纠结方向和在方向上走的大小。(momentum方向是修正方向)理解负梯度方向是最速下降方向是有问题的。我们现在大多数是研究D1L，D2NL主要有算Hessian Matrix，Fisher Matrix的逆（这里优化计算逆是一种方向）。很多神经网络的论文都是在 lost function 上面动手脚的加了一项正则（2范数1范数自身相乘）。

计算能力和算法性能优先算法性能,选择合适的算法是很重要的，可以加速思维的迭代速度。
