# CV_project

## part1 部署并运行tesseract-ocr

尝试在windows和mac os两个平台部署和运行tesseract

### windows平台部署

1. 安装cmake以及cppan、并将他们加入环境变量

2. 在tesseract源文件目录运行cppan

![](https://github.com/Fanglouhao/cv_project/blob/master/pngForMd/win1.png)

3. 运行cmake，如图存放source code的目录为“E:/cv/sources”，存放build的结果的目录为“E:/cv/build”，将（Name，Value）对中的CMAKE\_INSTALL\_PREFIX设置为“E：/cv/install”用以表示生成可执行文件的目录。

![](https://github.com/Fanglouhao/cv_project/blob/master/pngForMd/win2.png)

4. 打开build目录中的tesseract.sln，在vs2017打开项目，解决方案如图

![](https://github.com/Fanglouhao/cv_project/blob/master/pngForMd/win3.png)

![](https://github.com/Fanglouhao/cv_project/blob/master/pngForMd/win4.png)

5. 生成ALL_BUILD，编译生成debug版本库或release库本库。如图为“E:/cv/build/bin/Debug”目录下的内容。

![](https://github.com/Fanglouhao/cv_project/blob/master/pngForMd/win5.png)

![](https://github.com/Fanglouhao/cv_project/blob/master/pngForMd/win6.png)

6. 仅生成INSTALL。如图，在“E：/cv/install”中就会生成包装好的头文件，和可执行文件。

![](https://github.com/Fanglouhao/cv_project/blob/master/pngForMd/win7.png)

![](https://github.com/Fanglouhao/cv_project/blob/master/pngForMd/win8.png)

“include”文件夹中为各种头文件

![](https://github.com/Fanglouhao/cv_project/blob/master/pngForMd/win9.png)

“bin”文件夹中为各种dll库文件和可执行文件，包括“tesseract.exe”

![](https://github.com/Fanglouhao/cv_project/blob/master/pngForMd/win10.png)

7. 进行简单的测试，发现没有加入训练好的语言文件，从官网中下载并放入“E:/cv/install/bin/tessdata”

![](https://github.com/Fanglouhao/cv_project/blob/master/pngForMd/win11.png)

![](https://github.com/Fanglouhao/cv_project/blob/master/pngForMd/win12.png)

8. 测试结果如图

![](https://github.com/Fanglouhao/cv_project/blob/master/pngForMd/win13.png)

用于文字识别的图片

![](https://github.com/Fanglouhao/cv_project/blob/master/pngForMd/win14.png)

生成的txt文件

![](https://github.com/Fanglouhao/cv_project/blob/master/pngForMd/win15.png)

### mac os平台的部署

1. 在终端运行以下命令(已经事先安装homebrew)，完成各种依赖的安装

```
brew install automake autoconf libtool
brew install pkgconfig
brew install icu4c
brew install leptonica
brew install gcc
brew install pango
```

2. 在原文件目录下运行以下命令，完成编译以及安装过程

```
./autogen.sh
./configure CC=gcc-8 CXX=g++-8 CPPFLAGS=-I/usr/local/opt/icu4c/include LDFLAGS=-L/usr/local/opt/icu4c/lib
make -j
sudo make install 
```

3. 此时tesseract已经加入了系统环境变量，可直接运行，如图，同样需要加入语言文件。

![](https://github.com/Fanglouhao/cv_project/blob/master/pngForMd/mac1.png)

4. 测试结果如图

![](https://github.com/Fanglouhao/cv_project/blob/master/pngForMd/mac2.png)

### 遇到的困难、解决的方法及感想

1. windows中在设置环境变量后，如果无效，可以尝试退出cmd并以管理员身份打开，再次运行命令。

2. tesseract源文件以UTF-8编码，而系统语言为中文的win10下的vs编码格式为GB2312，则需要通过文本编辑其另存为的方法改变“E:/cv/sources/ccmain/equationdetect.cpp”的编码格式，这样才能通过编译。

3. mac os平台下的部署与安装较windows平台下的简单许多。

## part2 训练tesseract，识别老师提供的图片

1. 采用jTessBoxEditor来编辑训练用的.box文件，为满足jTessBoxEditor的要求，将提供的.bmp图像文件转化为.tif文件。

2. 编写Python脚本inverse_up_down.py, 实现对部分颠倒文件的倒置，代码如下：

```
import cv2
import numpy as np
import sys


def main():
    if len(sys.argv) == 1 or sys.argv[1][-3:-1] + sys.argv[1][-1] != "tif":
        print("require a tif file")
        return
    filename = sys.argv[1]
    bmp = cv2.imread(filename, 0)
    row, col = bmp.shape
    bmp_inverse = np.zeros_like(bmp)
    for r in range(row):
        for l in range(col):
            bmp_inverse[r, l] = bmp[row - r - 1, l]
    cv2.imwrite(filename[:-4] + "_inverse_up_down.tif", bmp_inverse)


if __name__ == '__main__':
    main()
```

3. 将5个.tif文件放大为640*480，方便tesseract-ocr的识别，以及jTessBoxEditor中对box的框选

4. 打开jTessBoxEditor，通过Tools>Merge TIFF将5个.tif文件merge为一个文件,将该文件命名为eng2.haha.exp0.tif，其中eng2为需要识别的语言（为与tesseract
中自带的eng做区分命名为eng2），haha表示字体。

5. 运行以下命令，通过初步识别，生成.box文件

```
tesseract eng2.haha.exp0.tif eng2.haha.exp0 batch.nochop makebox
```

6. 在jTessBoxEditor中打开eng2.haha.exp0.tif，eng2.haha.exp0.box会被自动打开

7. 编辑eng2.haha.exp0.box，使得一个box中的图像对应正确的value。

8. 定义字体配置文件font_properties.txt，内容为

```
haha 0 0 0 0 0  
```

9. 执行以下命令，将最后生成的eng2.traineddata复制到tessdata目录下，即完成了训练

```
tesseract.exe eng2.haha.exp0.tif eng2.haha.exp0 nobatch box.train
```

```
unicharset_extractor.exe eng2.haha.exp0.box
```

```
mftraining -F font_properties -U unicharset -O eng2.unicharset eng2.haha.exp0.tr
```

```
cntraining.exe eng2.haha.exp0.tr
```

```
rename normproto eng2.normproto 
rename inttemp eng2.inttemp 
rename pffmtable eng2.pffmtable 
rename shapetable eng2.shapetable 
```

```
combine_tessdata.exe eng2.
```

10. 测试结果



