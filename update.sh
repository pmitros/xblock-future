# This script will update an edx-platform installation to have a more complete set of XBlocks for development. 

mkdir xblocks
cd xblocks

for x in \
https://github.com/pmitros/DisqusXBlock.git \
https://github.com/pmitros/XBadger.git \
https://github.com/pmitros/ImageXBlock.git \
https://github.com/pmitros/AudioXBlock.git \
https://github.com/pmitros/DoneXBlock.git \
https://github.com/pmitros/AnimationXBlock.git 
do git clone $x
done

for x in `ls` ; do cd $x; python setup.py develop; cd .. ; done

pip install ipython