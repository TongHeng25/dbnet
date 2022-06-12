
## 环境
* pytorch 1.4+
* torchvision 0.5+
* gcc 4.9+



## 数据预处理

训练数据: 准备一个以下格式的文本“ train. txt”，使用’\t’作为分隔符
```
./datasets/train/img/001.jpg	./datasets/train/gt/001.txt
```

验证数据: 准备一个以下格式的文本“ test. txt”，使用’\t’作为分隔符
```
./datasets/test/img/001.jpg	./datasets/test/gt/001.txt
```
- 图片放在img文件夹中
- 标注放在gt文件夹中

标注可以是‘ . txt’文件，格式如下
```
x1, y1, x2, y2, x3, y3, x4, y4, annotation
```


## 训练
1. 修改config/icdar2015_resnet18_fpn_DBhead_polyLR.yaml，注意train.txt和test.txt的路径
* . single gpu train
```bash
bash singlel_gpu_train.sh
```
* . Multi-gpu training
```bash
bash multi_gpu_train.sh
```

2.运行train.py

## 测试

(tools/eval.py)用于测试模型
需修改模型路径和测试集路径

