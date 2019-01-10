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

![](https://github.com/Fanglouhao/cv_project/blob/master/pngForMd/win14.png)

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
