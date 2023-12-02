# Python for Algorithmic Trading

## Table of contents:

1. [Chapter 1: Python and Algorithmic Trading](#Chapter1)
2. [Chapter 2: Python Infrastructure](#Chapter2)
3. [Chapter 3: Working with Financial Data](#Chapter3)
4. [Chapter 4: Mastering Vectorized Backtesting](#Chapter4)
5. [Chapter 5: Predicting Market Movements with Machine Learning](#Chapter5)
6. [Chapter 6: Building Classes for Event-Based Backtesting](#Chapter6)
7. [Chapter 7: Working with Real-Time Data and Sockets](#Chapter7)
8. [Chapter 8: CFD Trading with Oanda](#Chapter8)
9. [Chapter 9: FX Trading with FXCM](#Chapter9)
10. [Chapter 10: Automating Trading Operations](#Chapter10)

## Chapter 1: Python and Algorithmic Trading<a name="Chapter1"></a>

### Python for Finance

Numerical algorithms in general and financial algorithms in particular are quite often implemented based on (nested)
loop structures which python is generally slow doing so.

### Python Versus Pseudo-Code

With Python, the pseudo-code to explain a (financial) algorithm might not be necessary anymore.

### NumPy and Vectorization

NumPy stands for numerical Python, suggesting that it targets scenarios that are numerically demanding. The major class
of NumPy is the regular array object, called ndarray object for n-dimensional array. It is immutable and can only
accommodate a single data type, called _dtype_. One central approach in this context is vectorization. Basically,
this approach avoids looping on the Python level and delegates the looping to specialized _NumPy_ code, generally
implemented in C and therefore fast.

### pandas and the DataFrame Class

_pandas_ was created to support working with time series data.

### Algorithmic Trading

_Algorithmic trading_  refers to the trading of financial instruments based on some formal algorithm. Here is a
non-exhaustive list of financial trading motives of people and financial institutions managing money of their own or for
others:

    * Beta trading: Earning market risk premia by investing in, for instance, exchange traded funds (ETFs) that 
      replicate the performance of the S&P 500
    * Alpha generation: Earning risk premia independent of the market by, for example, selling short stocks listed in 
      the S&P 500 or ETFs on the S&P 500
    * Static hedging: Hedging against market risks by buying, for example, out-of-the-money put options on the S&P 500
    * Dynamic hedging: Hedging against market risks affecting options on the S&P 500 by, for example, dynamically 
      trading futures on the S&P 500 and appropriate cash, money market, or rate instruments
    * Asset-liability management: Trading S&P 500 stocks and ETFs to be able to cover liabilities resulting from, for 
      example, writing life insurance policies
    * Market making: Providing, for example, liquidity to options on the S&P 500 by buying and selling options at 
      different bid and ask prices

All these types of trades can be implemented by human traders making decisions as well as based on algorithms supporting
the human trader or even replacing them completely.
This book focuses on algorithmic trading in the context of alpha generating strategies. alpha is seen as the difference
between a trading strategy's return over some period of time and the return of the benchmark (single stock, index, etc).
For example, if the S&P 500 returns 10% in 2018 and an algorithmic strategy returns 12%, then alpha is +2% points.

### Python for Algorithmic Trading

Python is used in the financial industry and has become popular in the algorithmic trading space, mostly due to:

    * Data analytics capabilities: The ability to manage and process financial data efficiently
    * Handling of modern APIs: Python is well suited to interact with restful and socket APIs
    * Dedicated packages: There are multiple packages available that are dedicated to the algorithmic trading space
    * Vendor sponsored packages: Vendors release open source Python packages to facilitateaccess to their offerings
    * Dedicated platforms: There are dedicated platforms that offers standardized backtesting environments
    * Buy- and sell-side adoption: A lot of institutional players uses Python to streamline development efforts in 
      their trading departments
    * Education, training, and books: The Python ecosystem has seen a tremendous growth recently

### Trading Strategies

4 different algorithmic trading strategies are used as examples and are classified as mainly alpha seeking strategies:

    * Simple Moving Averages: The basic idea is that a shorter term SMA being higher in value than a longer term SMA 
      signals a long market position and the opposite scenario signals a neutral or short market position
    * Momentum: A financial instrument is assumed to perform in accordance with its recent performance for some 
      additional time
    * Mean Reversion: A financial instrument is assumed to revert to some mean or trend level if it is currently far 
      enough away from such a level
    * Machine and Deep Learning: With this strategy, one takes a more black box approach to predicting market movements

## Chapter 2: Python Infrastructure<a name="Chapter2"></a>

There are several reasons why deployment of python programs can prove difficult:

    * The standard interpreter (CPython) only comes with the so-called standard library
    * Optional Python packages need to be installed separately
    * Compiling such non-standard packages on your own can be tricky due to dependencies and OS requirements
    * It is difficult to manage such dependencies and of version consistency over time
    * Updates and upgrades for certain packages might cause the need for recompiling a multitude of other packages
    * Changing or replacing one package might cause trouble
    * Migrating from one Python version to another one at some later point might amplify all the preceding issues

Fortunately, there are tools and strategies available that help with the Python deployment issue:

    * Package manager: Like pip or conda help with the installing, updating, and removing of packages 
    * Virtual environment manager: Like venv, allows one to manage multiple Python installations in parallel 
    * Container: Like Docker, complete file systems containing all pieces of a system needed to run a certain software
    * Cloud instance: High availability, security, and performance can be achieved through professional compute and 
      storage infrastructure on the cloud

### Conda as a Package Manager

#### Installing Miniconda

Miniconda is a minimal Python distribution that includes _conda_ as a package and virtual environment manager. You can
download the latest distribution [here](https://docs.conda.io/projects/miniconda/en/latest).

#### Basic Operations with Conda

_conda_ can be used to efficiently handle, among others, the installation, updating, and removal of Python packages:

    * Installing Python x.x: conda install python=x.x
    * Updating Python: conda update python
    * Installing a package: conda install $PACKAGE_NAME
    * Updating a package: conda update $PACKAGE_NAME
    * Removing a package: conda remove $PACKAGE_NAME
    * Updating conda itself: conda update conda
    * Searching for packages: conda search $SEARCH_TERM
    * Listing installed packages: conda list

Some of the most important libraries for financial analytics are available in addition to the standard ones:

    * IPython: An improved interactive Python shell
    * matplotlib: The standard plotting library for Python
    * NumPy: Efficient handling of numerical arrays
    * pandas: Management of tabular data, like financial time series data
    * PyTables: A Python wrapper for the HDF5 library
    * scikit-learn: A package for machine learning and related tasks
    * SciPy : A collection of scientific classes and functions

### Conda as a Virtual Environment Manager

Having installed Miniconda with _conda_ included provides a default Python installation depending on what version of
Miniconda has been chosen. _conda_ offers the following functionality:

    * Creating a virtual environment: conda create --name $ENVIRONMENT_NAME
    * Activating an environment: conda activate $ENVIRONMENT_NAME
    * Deactivating an environment: conda deactivate $ENVIRONMENT_NAME
    * Removing an environment: conda env remove --name $ENVIRONMENT_NAME
    * Exporting to an environment file: conda env export > $FILE_NAME
    * Creating an environment from a file: conda env create -f $FILE_NAME
    * Listing all environments: conda info --envs

An example of how to create an environment named 'test' with IPython and python 2.7 can be seen below:

```shell
(base) root@root:~# conda create --name test python=2.7
(base) root@root:~# conda activate test
(py27) root@root:~# pip install ipython
```

All available environments can be shown via `conda info --envs`. To share environment information with others or to
use environment information on multiple machines use `conda env export`, which only works properly by default for the
same operating system since the build versions are specified in the resulting yaml file (add `--no-builds` flag to
only specify the package versions).

### Using Docker Containers

#### Docker Images and Containers

A docker image is an ordered collection of root filesystem changes and the corresponding execution parameters for use
within a container runtime. A container is a runtime instance of a Docker image.

#### Building a Ubuntu and Python Docker Image

You can build a docker image providing a docker file with the command `docker build -t <repository>:<tag> .`.
List the available images with `docker images`. Run the image with `docker run -ti <repository>:<tag>`, the `-ti` flag
is needed for interactive processes running within a Docker container, like a shell process of _IPython_. Detach
from a container via `Ctrl+p --> Ctrl+q`. `docker ps` shows the running containers. Attaching to the Docker with
`docker attach $CONTAINER_ID`, remove a container with `docker rm $CONTAINER_ID` (use `rmi` to remove the image too).

### Using Cloud Instances

Cloud instances can also be used to spin up a full-fledged Python environment. Check provider notes on how to do this.

## Chapter 3: Working with Financial Data<a name="Chapter3"></a>

In algorithmic trading, one generally has to deal with four types of data:

|            | Structured                | Unstructured            |
|------------|---------------------------|-------------------------|
| Historical | End-of-day closing prices | Financial news articles |
| Real-time  | Bid/ask prices for FX     | Posts on Twitter        |

An algorithmic trading project typically starts with a trading idea or hypothesis that needs to be (back)tested based on
historical financial data. 

### Reading Financial Data From Different Sources