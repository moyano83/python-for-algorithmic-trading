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

