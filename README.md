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

#### The Data Set

With pandas, you can support the three main tasks you usually do with data: reading, handling, and storing data.

#### Reading from a CSV File with Python

Python has a built-in module called csv that supports the reading of data from a CSV file:

```python
import csv

fn = '../data/AAPL.csv'
csv_reader = csv.reader(open(fn, 'r'))  # gets a csv iterator

first_5_lines_of_data = list(csv_reader)[:5]
```

Using a `csv.DictReader` iterator object instead of the standard csv.reader object makes such tasks a bit more
manageable. Every row of data in the CSV file (apart from the header row) is then imported as a dict object so that
single values can be accessed via the respective key (which is in the first row). You can calculate an average like
this: `sum([float(l['CLOSE']) for l in data]) / len(data)` where data is `data = list(csv.DictReader(open(fn, 'r')))`.

#### Reading from a CSV File with pandas

Pandas provide the functionality to read from files and perform lot of common operations on the data returned.

```python
import pandas as pd

# 'parse_dates' indicates that the entries in the index column should also be interpreted as date-time information
data = pd.read_csv(fn, index_col=0, parse_dates=True)
# You can inspect the data loaded with this:
data.info()
# Print information of the last rows
data.tail()
# This calculates the mean of the colum 'CLOSE'
data['CLOSE'].mean()
```

#### Exporting to Excel and JSON

Apart from being able to export to CSV files (_xlwings_ is more appropriate for this purpose), pandas also allows one
to do the export in the form of Excel spreadsheet files as well as JSON files.

```python
data.to_excel('data/aapl.xls', 'AAPL')
data.to_json('data/aapl.json')
```

#### Reading from Excel and JSON

Pandas can also read from json, use the `read_json` method and operate with the result in the same way than with the
`read_csv` method. _pandas_ generally provides the right set of parameter combinations to cope with situations like
using ';' instead of comma to separate tabular data.

### Working with Open Data Sources

_Quandl_ is a platform that aggregates a large number of open, as well as premium data sources. The data is provided via
a unified API for which a Python wrapper package is available. With Quandl, requests always expect a combination of the
database and the specific data set desired and returns a panda dataframe by default. You might need a key which can be
obtained by signing up for a free Quandl account.

```python
import configparser

config = configparser.ConfigParser()
config.read('../pyalgo.cfg')
import quandl as q

# Reads historical data for the BTC/USD exchange rate.
data = q.get('BCHAIN/MKPRU', api_key=config['quandl']['api_key'])
# Selects the Value column, resamples it—from the originally daily values to yearly values—and defines the last 
# available observation to be the relevant one.
data['Value'].resample('A').last()
```

The API key can also be configured permanently with the Python wrapper via the following:
`q.ApiConfig.api_key = 'YOUR_API_KEY'`

### Eikon Data API

Refinitiv is one of the biggest financial data and news providers, its current desktop flagship product is _Eikon_,
which is the equivalent to the Terminal by Bloomberg. Refinitiv has a python wrapper called _eikon_, but a technical
prerequisite is that a local desktop application is running that provides a desktop API session.
In order to use the Eikon Data API, the Eikon app_key needs to be set. You get it via the App Key Generator (APPKEY)
application in either Eikon or Workspace:

```python
import eikon as ek

ek.set_app_key(config['eikon']['app_key'])
```

#### Retrieving Historical Structured Data

An example of historical data retrieval is below:

```python
symbols = ['AAPL.O', 'MSFT.O', 'GOOG.O']

data = ek.get_timeseries(symbols, start_date='2020-01-01', end_date='2020-05-01', interval='daily', fields=['*'])
# The above returns a multi-index DataFrame object.
data.keys()
# This is a pandas.core.frame.DataFrame type, you can see information with data['AAPL.O'].info() and contents with tail 
type(data['AAPL.O'])
# loc access a group of rows and columns by label(s), in this case all columns within those two dates (included)
print(data['AAPL.O'].loc['2020-08-14 16:00:00': '2020-08-14 16:04:00'])
# data is resampled to a 30 second interval length (by taking the last value and the sum, respectively), which is 
# reflected in the DatetimeIndex of the new DataFrame object.
resampled = data.resample('30s', label='right').agg({'VALUE': 'last', 'VOLUME': 'sum'})
```

By default, the function `get_timeseries()` provides the following options for the interval parameter: _tick_, _minute_,
_hour_, _daily_, _weekly_, _monthly_, _quarterly_, and _yearly_.

#### Retrieving Historical Unstructured Data

A major strength of working with the Eikon API via Python is the easy retrieval of unstructured data, which can then be
parsed and analyzed with Python packages for natural language processing (NLP).

```python
# This retrieves news headlines for a fixed time interval that includes Apple Inc. as a company and "Macbook” as a word
headlines = ek.get_news_headlines(query='R:AAPL.O macbook', count=5, date_from='2020-4-1', date_to='2020-5-1')
# iloc retrieves columns by integer-location based indexing for selection by position
story = headlines.iloc[0]  # gets the story on the news

# gets the whole news text and displays it using the HTML module
news_text = ek.get_news_story(story['storyId'])  # This retrieves the news text as html code
IPython.display.HTML(news_text)  # renders the html
```

### Storing Financial Data Efficiently

One of the most important scenarios for the management of data sets is "retrieve once, use multiple times" or "write
once, read multiple times". We can generate a meaningful sample financial data in terms of size by the use of
pseudorandom numbers.

```python
# This function is in the chapter3_scripts.py file
from sample_data import generate_sample_data

data = generate_sample_data(rows=5, cols=4)
```

#### Storing DataFrame Objects

The storage of a pandas DataFrame object as a whole is made simple by the pandas _HDFStore_ wrapper functionality
for the _HDF5_ binary storage standard. To store the dataframe, you need to open a _HDFStore_ object and write the
dataframe to it like `h5 = dataframe.HDFStore('data_location/data.h5', 'w')`. Note that selecting an existing path
would cause the original file to be overwritten. Make sure to close the database file with `h5.close()`.
You can also load a an HDFStore file with `h5 = pd.HDFStore('data/data.h5', 'r')`. You can also call the `to_hdf`
method of a dataframe and set the format parameter to _table_. This allows the appending of new data to the table object
on disk and also searching over the data on disk, which is not possible with the first approach, althought it is slower:

```python
# data is a pandas dataframe
data.to_hdf('data/data.h5', 'data', format='table')
# Reading is also slower in this application scenario.
data_copy = pd.read_hdf('data/data.h5', 'data')
```

The above example has the advantage of one being able to work with the `table_frame` object on disk like with any other
table object of the _PyTables_ package that is used by pandas in this context. An example of this can be seen below:

```python
import tables as tb

# Opens the database file for reading.
h5 = tb.open_file('data/data.h5', 'r')
# Prints the first three rows in the table.
h5.root.data.table[:3]
h5.close()
```

These two approaches are convenient and efficient when you are working with more or less immutable data sets that fit
into memory.

#### Using TsTables

The _PyTable_s package is a wrapper for the HDF5 binary storage library that is also used by pandas for its _HDFStore_
implementation. It is effectively an enhancement of the _PyTables_ package and adds support for time series data. 
It implements a hierarchical storage approach that allows for a fast retrieval of data sub-sets selected by providing 
start and end dates and times respectively and used in the "write once, retrieve multiple times" scenario.

```python
import tstables
import tables as tb

data = generate_sample_data(rows=2.5e6, cols=5, freq='1s').round(4) # creates data every second
# The desc class provides the description for the table object’s data structure:
class desc(tb.IsDescription):
    ''' 
    Description of TsTables table structure.
    '''
    timestamp = tb.Int64Col(pos=0)
    No0 = tb.Float64Col(pos=1)
    No1 = tb.Float64Col(pos=2)
    No2 = tb.Float64Col(pos=3)
    No3 = tb.Float64Col(pos=4)
    No4 = tb.Float64Col(pos=5)

h5 = tb.open_file('data/data.h5ts', 'w')
# TsTables table is created at the root node, with name data and given the class-based description desc 
ts = h5.create_ts('/', 'data', desc)
# This writes the sample data stored in a DataFrame object to the table object on disk
ts.append(data)
```

With regard to the structure in the database, _TsTables_ chunks the data into sub-sets of a single day. You can read 
a subset of the data by calling the `ts.read_range(start, end)` where `start` and `end` are _datetime_ objects (remember
to close the hdf object always at the end of the processing)

#### Storing Data with SQLite3

Financial time series data can also be written directly from a DataFrame object to a relational database like _SQLite3_.
The DataFrame class provides the method `to_sql()` to write data to a table in a relational database. There is quite 
some overhead when using relational databases:
```python
import sqlite3 as sq3

con = sq3.connect('data/data.sql')  # A connection is opened to a new database file

dataframe.to_sql('financial_data', con)  # financial_data is the name of the table to write to

# checking the results and operate on them, this returns an array with the values (tuples)
rows = con.execute('SELECT * FROM data WHERE No1 > 105 and No2 < 108').fetchall()  
con.close() # Always close the connection
```

## Chapter 4: Mastering Vectorized Backtesting<a name="Chapter4"></a>
