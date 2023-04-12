Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> dates1=pd.date_range('20230719',periods=10)
>>> series1=pd.Series([1,2,3,4,5,6,7,8,9,10])
>>> series1.index=dates1
>>> series1
2023-07-19     1
2023-07-20     2
2023-07-21     3
2023-07-22     4
2023-07-23     5
2023-07-24     6
2023-07-25     7
2023-07-26     8
2023-07-27     9
2023-07-28    10
Freq: D, dtype: int64
>>> series1['20230727]
	
SyntaxError: EOL while scanning string literal
>>> series1['20230727']
9
>>> series1['20230720']
2
>>> series1['20230719']
1
>>> pd.read_csv(r'C:\HI_Course\python_file\Lib\site-packages\sklearn\datasets\data\test.csv')
     150    4  setosa  versicolor  virginica
0    5.1  3.5     1.4         0.2          0
1    4.9  3.0     1.4         0.2          0
2    4.7  3.2     1.3         0.2          0
3    4.6  3.1     1.5         0.2          0
4    5.0  3.6     1.4         0.2          0
..   ...  ...     ...         ...        ...
145  6.7  3.0     5.2         2.3          2
146  6.3  2.5     5.0         1.9          2
147  6.5  3.0     5.2         2.0          2
148  6.2  3.4     5.4         2.3          2
149  5.9  3.0     5.1         1.8          2

[150 rows x 5 columns]
>>> df_test = pd.read_csv(r'C:\HI_Course\python_file\Lib\site-packages\sklearn\datasets\data\test.csv')
>>> df_test.describe()
              150           4      setosa  versicolor   virginica
count  150.000000  150.000000  150.000000  150.000000  150.000000
mean     5.843333    3.057333    3.758000    1.199333    1.000000
std      0.828066    0.435866    1.765298    0.762238    0.819232
min      4.300000    2.000000    1.000000    0.100000    0.000000
25%      5.100000    2.800000    1.600000    0.300000    0.000000
50%      5.800000    3.000000    4.350000    1.300000    1.000000
75%      6.400000    3.300000    5.100000    1.800000    2.000000
max      7.900000    4.400000    6.900000    2.500000    2.000000
>>> 