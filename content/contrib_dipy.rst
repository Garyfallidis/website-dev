:title: How to become a Dipy Master!
:date: 2015-03-15 20:20
:category: blog

This a question that I get very often. How can I contribute to `Dipy <http://dipy.org>`_ or how can I become a really good user of Dipy? 

In this post I am providing the necessary learning materials to master Python, code sharing and do diffusion MRI analysis with Dipy.

.. contents::


Start from the basics
=======================

Learn Python
~~~~~~~~~~~~~
I recommend taking one of the free online interactive courses. Look for example at learning Python from Codecademy. You should be able the learn the basics of programming with Python in 10-14 hours.

Learn how to do data analysis in Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Have a read at the ``Python for data analysis`` boook from Wes McKinney. Focus on chapters 3, 4, 8 and 12. This book explains how to use Numpy and IPython. You will find these tools
helpful in many areas of imaging beyond diffusion MRI.


Learn the basics of Diffusion MRI and Dipy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Learn the basics of Dipy and diffusion MRI by reading this `Frontiers paper <http://journal.frontiersin.org/article/10.3389/fninf.2014.00008/abstract>`_.

Read the `Dipy tutorials <http://dipy.org/examples_index.html>`_ and your expertize in analyzing dMRI data will grow very quickly. 


Learn Git/Github
=================

This information is useful mostly to those who want to contribute Dipy by sharing their code.

Git/Github
~~~~~~~~~~~
Use and learn git and github. Give a go to the interactive courses below 

https://try.github.io

http://pcottle.github.io/learnGitBranching/

Understand the concept of pull requests. Here is a nice tutorial.

http://dipy.org/devel/index.html


Quick guidelines
~~~~~~~~~~~~~~~~~~
`Dipy's code base <https://github.com/nipy/dipy/>`_ is available in `Github <https://github.com>`_. You will need to create an account in Github to be able to share code with Dipy.

Here we provide a quick summary of the process of sharing your code in Github.

1. Fork nipy/dipy from github
2. Clone your forked version (using git clone)
3. Start working on a new branch from your cloned forked version.
4. After your branch is finished. I mean you commited all changes.
5. Push your changes in your github account and make a pull request.
6. Then the Dipy  give you advice and you can make the suggested corrections
7. we merge your project.

In practice
~~~~~~~~~~~~
After forking nipy/dipy from github in your own github space (assuming your username in github is david) do:

.. code-block:: bash

    # clone your fork
    git clone https://github.com/david/dipy.git

    # add a tracking branch which can always have the last version of dipy
    git remote add nipy-dipy https://github.com/nipy/dipy.git
    git fetch nipy-dipy
    git branch nipy-dipy-master --track nipy-dipy/master
    git checkout nipy-dipy-master
    # you will only need to write the following command in to have the latest dipy dev version
    git pull

    # create a branch from the last dev version of the tracking branch above
    # let’s call this branch new_tracking_feature
    git branch new_tracking_feature
    git checkout new_tracking_feature

    # add and commit your changes
    git add …
    git commit …
    git push origin new_tracking_feature


Afte you have finished pushing all your changes you are ready to make a pull request from github. You just need to press the green button from your github repo and write a title and a small description of what you are sharing with us.

After the pull request has arrived, the Dipy developers will review it and give you comments
so you can improve your code. 


Coding Policies
===============

Coding style
~~~~~~~~~~~~~

Readability and reproducibility of code is very important in Dipy therefore we suggest to use the following coding style

https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt

https://www.python.org/dev/peps/pep-0008/

The Spyder python editor has some tools automated to check for PEP8 issues. I would recommend using such an editor until you get used to the style.

Coding philosophy
~~~~~~~~~~~~~~~~~~
https://www.python.org/dev/peps/pep-0020/

Tutorials
~~~~~~~~~
You will need to write a tutorial to communicate your contribution to the coders and the users of Dipy. See examples in doc/examples

Testing
~~~~~~~~
Dipy is a highly tested library and we plan to keep it this way and make it even better. Make sure you have individual tests for all your functions (test coverage should be close to 100%).

Look for inspiration in dipy/reconst/tests For example, see how the tests are written in the file dipy/reconst/test/test_csdeconv.py

More Questions?
~~~~~~~~~~~~~~~

Send an e-mail to `Neurostars <https://neurostars.org>`_ or subscribe to the `Nipy-devel list <http://mail.scipy.org/mailman/listinfo/nipy-devel>`_.