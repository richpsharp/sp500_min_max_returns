import heapq
from datetime import datetime

# got this from https://shillerdata.com/
data = [
  {
    "month": "1871-01-01",
    "price": 4.44,
    "nominalPricePlusDividend": 4.44,
    "realPrice": 112.1118,
    "realPricePlusDividend": 112.1118
  },
  {
    "month": "1871-02-01",
    "price": 4.5,
    "nominalPricePlusDividend": 4.5217,
    "realPrice": 110.2601,
    "realPricePlusDividend": 110.7902
  },
  {
    "month": "1871-03-01",
    "price": 4.61,
    "nominalPricePlusDividend": 4.654,
    "realPrice": 111.306,
    "realPricePlusDividend": 112.366
  },
  {
    "month": "1871-04-01",
    "price": 4.74,
    "nominalPricePlusDividend": 4.8071,
    "realPrice": 118.78,
    "realPricePlusDividend": 120.4584
  },
  {
    "month": "1871-05-01",
    "price": 4.86,
    "nominalPricePlusDividend": 4.9508,
    "realPrice": 124.6191,
    "realPricePlusDividend": 126.9427
  },
  {
    "month": "1871-06-01",
    "price": 4.82,
    "nominalPricePlusDividend": 4.9321,
    "realPrice": 125.5402,
    "realPricePlusDividend": 128.4549
  },
  {
    "month": "1871-07-01",
    "price": 4.73,
    "nominalPricePlusDividend": 4.8622,
    "realPrice": 123.1961,
    "realPricePlusDividend": 126.6329
  },
  {
    "month": "1871-08-01",
    "price": 4.79,
    "nominalPricePlusDividend": 4.9461,
    "realPrice": 126.7545,
    "realPricePlusDividend": 130.8791
  },
  {
    "month": "1871-09-01",
    "price": 4.84,
    "nominalPricePlusDividend": 5.0201,
    "realPrice": 125.076,
    "realPricePlusDividend": 129.7233
  },
  {
    "month": "1871-10-01",
    "price": 4.59,
    "nominalPricePlusDividend": 4.7833,
    "realPrice": 116.791,
    "realPricePlusDividend": 121.7014
  },
  {
    "month": "1871-11-01",
    "price": 4.64,
    "nominalPricePlusDividend": 4.858,
    "realPrice": 118.0633,
    "realPricePlusDividend": 123.6008
  },
  {
    "month": "1871-12-01",
    "price": 4.74,
    "nominalPricePlusDividend": 4.9853,
    "realPrice": 117.8867,
    "realPricePlusDividend": 123.9792
  },
  {
    "month": "1872-01-01",
    "price": 4.86,
    "nominalPricePlusDividend": 5.1343,
    "realPrice": 120.8712,
    "realPricePlusDividend": 127.691
  },
  {
    "month": "1872-02-01",
    "price": 4.88,
    "nominalPricePlusDividend": 5.1786,
    "realPrice": 121.3686,
    "realPricePlusDividend": 128.7995
  },
  {
    "month": "1872-03-01",
    "price": 5.04,
    "nominalPricePlusDividend": 5.372,
    "realPrice": 123.4913,
    "realPricePlusDividend": 131.6364
  },
  {
    "month": "1872-04-01",
    "price": 5.18,
    "nominalPricePlusDividend": 5.5452,
    "realPrice": 124.1619,
    "realPricePlusDividend": 132.9322
  },
  {
    "month": "1872-05-01",
    "price": 5.18,
    "nominalPricePlusDividend": 5.5696,
    "realPrice": 124.1619,
    "realPricePlusDividend": 133.5231
  },
  {
    "month": "1872-06-01",
    "price": 5.13,
    "nominalPricePlusDividend": 5.5406,
    "realPrice": 123.8611,
    "realPricePlusDividend": 133.8046
  },
  {
    "month": "1872-07-01",
    "price": 5.1,
    "nominalPricePlusDividend": 5.5334,
    "realPrice": 124.9614,
    "realPricePlusDividend": 135.6172
  },
  {
    "month": "1872-08-01",
    "price": 5.04,
    "nominalPricePlusDividend": 5.494,
    "realPrice": 122.5831,
    "realPricePlusDividend": 133.6658
  },
  {
    "month": "1872-09-01",
    "price": 4.95,
    "nominalPricePlusDividend": 5.4219,
    "realPrice": 119.5151,
    "realPricePlusDividend": 130.9557
  },
  {
    "month": "1872-10-01",
    "price": 4.97,
    "nominalPricePlusDividend": 5.4703,
    "realPrice": 122.6851,
    "realPricePlusDividend": 135.0893
  },
  {
    "month": "1872-11-01",
    "price": 4.95,
    "nominalPricePlusDividend": 5.4752,
    "realPrice": 118.6489,
    "realPricePlusDividend": 131.2966
  },
  {
    "month": "1872-12-01",
    "price": 5.07,
    "nominalPricePlusDividend": 5.6352,
    "realPrice": 123.3127,
    "realPricePlusDividend": 137.1294
  },
  {
    "month": "1873-01-01",
    "price": 5.11,
    "nominalPricePlusDividend": 5.7075,
    "realPrice": 124.2856,
    "realPricePlusDividend": 138.8921
  },
  {
    "month": "1873-02-01",
    "price": 5.15,
    "nominalPricePlusDividend": 5.7803,
    "realPrice": 122.5553,
    "realPricePlusDividend": 137.6334
  },
  {
    "month": "1873-03-01",
    "price": 5.11,
    "nominalPricePlusDividend": 5.764,
    "realPrice": 121.6034,
    "realPricePlusDividend": 137.2482
  },
  {
    "month": "1873-04-01",
    "price": 5.04,
    "nominalPricePlusDividend": 5.7139,
    "realPrice": 119.9376,
    "realPricePlusDividend": 136.0609
  },
  {
    "month": "1873-05-01",
    "price": 5.05,
    "nominalPricePlusDividend": 5.7545,
    "realPrice": 122.8263,
    "realPricePlusDividend": 140.0554
  },
  {
    "month": "1873-06-01",
    "price": 4.98,
    "nominalPricePlusDividend": 5.7044,
    "realPrice": 124.7942,
    "realPricePlusDividend": 143.0482
  },
  {
    "month": "1873-07-01",
    "price": 4.97,
    "nominalPricePlusDividend": 5.723,
    "realPrice": 124.5436,
    "realPricePlusDividend": 143.5198
  },
  {
    "month": "1873-08-01",
    "price": 4.97,
    "nominalPricePlusDividend": 5.7535,
    "realPrice": 124.5436,
    "realPricePlusDividend": 144.2888
  },
  {
    "month": "1873-09-01",
    "price": 4.59,
    "nominalPricePlusDividend": 5.3445,
    "realPrice": 115.0211,
    "realPricePlusDividend": 134.0357
  },
  {
    "month": "1873-10-01",
    "price": 4.19,
    "nominalPricePlusDividend": 4.91,
    "realPrice": 107.4391,
    "realPricePlusDividend": 126.0083
  },
  {
    "month": "1873-11-01",
    "price": 4.04,
    "nominalPricePlusDividend": 4.766,
    "realPrice": 106.9078,
    "realPricePlusDividend": 126.2309
  },
  {
    "month": "1873-12-01",
    "price": 4.42,
    "nominalPricePlusDividend": 5.2465,
    "realPrice": 114.2223,
    "realPricePlusDividend": 135.7054
  },
  {
    "month": "1874-01-01",
    "price": 4.66,
    "nominalPricePlusDividend": 5.564,
    "realPrice": 118.5722,
    "realPricePlusDividend": 141.7035
  },
  {
    "month": "1874-02-01",
    "price": 4.8,
    "nominalPricePlusDividend": 5.764,
    "realPrice": 122.1344,
    "realPricePlusDividend": 146.7957
  },
  {
    "month": "1874-03-01",
    "price": 4.73,
    "nominalPricePlusDividend": 5.7129,
    "realPrice": 120.3533,
    "realPricePlusDividend": 145.4947
  },
  {
    "month": "1874-04-01",
    "price": 4.6,
    "nominalPricePlusDividend": 5.5891,
    "realPrice": 118.8739,
    "realPricePlusDividend": 144.5641
  },
  {
    "month": "1874-05-01",
    "price": 4.48,
    "nominalPricePlusDividend": 5.4767,
    "realPrice": 116.6847,
    "realPricePlusDividend": 142.7714
  },
  {
    "month": "1874-06-01",
    "price": 4.46,
    "nominalPricePlusDividend": 5.4859,
    "realPrice": 118.9739,
    "realPricePlusDividend": 146.4688
  },
  {
    "month": "1874-07-01",
    "price": 4.46,
    "nominalPricePlusDividend": 5.5197,
    "realPrice": 118.0219,
    "realPricePlusDividend": 146.1913
  },
  {
    "month": "1874-08-01",
    "price": 4.47,
    "nominalPricePlusDividend": 5.5662,
    "realPrice": 119.2407,
    "realPricePlusDividend": 148.6083
  },
  {
    "month": "1874-09-01",
    "price": 4.54,
    "nominalPricePlusDividend": 5.6876,
    "realPrice": 121.108,
    "realPricePlusDividend": 151.8484
  },
  {
    "month": "1874-10-01",
    "price": 4.53,
    "nominalPricePlusDividend": 5.7095,
    "realPrice": 122.8227,
    "realPricePlusDividend": 154.9318
  },
  {
    "month": "1874-11-01",
    "price": 4.57,
    "nominalPricePlusDividend": 5.7946,
    "realPrice": 124.9305,
    "realPricePlusDividend": 158.5376
  },
  {
    "month": "1874-12-01",
    "price": 4.54,
    "nominalPricePlusDividend": 5.7914,
    "realPrice": 124.1104,
    "realPricePlusDividend": 158.4495
  },
  {
    "month": "1875-01-01",
    "price": 4.54,
    "nominalPricePlusDividend": 5.8265,
    "realPrice": 124.1104,
    "realPricePlusDividend": 159.4005
  },
  {
    "month": "1875-02-01",
    "price": 4.53,
    "nominalPricePlusDividend": 5.8487,
    "realPrice": 123.8371,
    "realPricePlusDividend": 159.9989
  },
  {
    "month": "1875-03-01",
    "price": 4.59,
    "nominalPricePlusDividend": 5.9611,
    "realPrice": 125.4773,
    "realPricePlusDividend": 163.0659
  },
  {
    "month": "1875-04-01",
    "price": 4.65,
    "nominalPricePlusDividend": 6.0739,
    "realPrice": 126.0762,
    "realPricePlusDividend": 164.7825
  },
  {
    "month": "1875-05-01",
    "price": 4.47,
    "nominalPricePlusDividend": 5.8736,
    "realPrice": 124.251,
    "realPricePlusDividend": 163.3567
  },
  {
    "month": "1875-06-01",
    "price": 4.38,
    "nominalPricePlusDividend": 5.7901,
    "realPrice": 123.83,
    "realPricePlusDividend": 163.7775
  },
  {
    "month": "1875-07-01",
    "price": 4.39,
    "nominalPricePlusDividend": 5.8381,
    "realPrice": 124.1127,
    "realPricePlusDividend": 165.1237
  },
  {
    "month": "1875-08-01",
    "price": 4.41,
    "nominalPricePlusDividend": 5.8993,
    "realPrice": 123.6223,
    "realPricePlusDividend": 165.4332
  },
  {
    "month": "1875-09-01",
    "price": 4.37,
    "nominalPricePlusDividend": 5.8803,
    "realPrice": 123.5473,
    "realPricePlusDividend": 166.3009
  },
  {
    "month": "1875-10-01",
    "price": 4.3,
    "nominalPricePlusDividend": 5.8206,
    "realPrice": 121.5683,
    "realPricePlusDividend": 164.6029
  },
  {
    "month": "1875-11-01",
    "price": 4.37,
    "nominalPricePlusDividend": 5.9498,
    "realPrice": 124.6126,
    "realPricePlusDividend": 169.6967
  },
  {
    "month": "1875-12-01",
    "price": 4.37,
    "nominalPricePlusDividend": 5.9841,
    "realPrice": 125.6964,
    "realPricePlusDividend": 172.1504
  },
  {
    "month": "1876-01-01",
    "price": 4.46,
    "nominalPricePlusDividend": 6.1416,
    "realPrice": 129.4107,
    "realPricePlusDividend": 178.2294
  },
  {
    "month": "1876-02-01",
    "price": 4.52,
    "nominalPricePlusDividend": 6.2586,
    "realPrice": 131.1516,
    "realPricePlusDividend": 181.6246
  },
  {
    "month": "1876-03-01",
    "price": 4.51,
    "nominalPricePlusDividend": 6.2794,
    "realPrice": 130.8614,
    "realPricePlusDividend": 182.2259
  },
  {
    "month": "1876-04-01",
    "price": 4.34,
    "nominalPricePlusDividend": 6.0775,
    "realPrice": 127.0424,
    "realPricePlusDividend": 177.9254
  },
  {
    "month": "1876-05-01",
    "price": 4.18,
    "nominalPricePlusDividend": 5.8885,
    "realPrice": 126.849,
    "realPricePlusDividend": 178.7155
  },
  {
    "month": "1876-06-01",
    "price": 4.15,
    "nominalPricePlusDividend": 5.8814,
    "realPrice": 129.5037,
    "realPricePlusDividend": 183.5531
  },
  {
    "month": "1876-07-01",
    "price": 4.1,
    "nominalPricePlusDividend": 5.846,
    "realPrice": 127.9434,
    "realPricePlusDividend": 182.4457
  },
  {
    "month": "1876-08-01",
    "price": 3.93,
    "nominalPricePlusDividend": 5.6392,
    "realPrice": 121.492,
    "realPricePlusDividend": 174.3466
  },
  {
    "month": "1876-09-01",
    "price": 3.69,
    "nominalPricePlusDividend": 5.3307,
    "realPrice": 113.0162,
    "realPricePlusDividend": 163.2806
  },
  {
    "month": "1876-10-01",
    "price": 3.67,
    "nominalPricePlusDividend": 5.338,
    "realPrice": 110.3604,
    "realPricePlusDividend": 160.5281
  },
  {
    "month": "1876-11-01",
    "price": 3.6,
    "nominalPricePlusDividend": 5.2725,
    "realPrice": 107.28,
    "realPricePlusDividend": 157.1294
  },
  {
    "month": "1876-12-01",
    "price": 3.58,
    "nominalPricePlusDividend": 5.2798,
    "realPrice": 104.7954,
    "realPricePlusDividend": 154.5605
  },
  {
    "month": "1877-01-01",
    "price": 3.55,
    "nominalPricePlusDividend": 5.2725,
    "realPrice": 102.1103,
    "realPricePlusDividend": 151.627
  },
  {
    "month": "1877-02-01",
    "price": 3.34,
    "nominalPricePlusDividend": 4.9966,
    "realPrice": 98.6431,
    "realPricePlusDividend": 147.5063
  },
  {
    "month": "1877-03-01",
    "price": 3.17,
    "nominalPricePlusDividend": 4.7774,
    "realPrice": 97.9974,
    "realPricePlusDividend": 147.5889
  },
  {
    "month": "1877-04-01",
    "price": 2.94,
    "nominalPricePlusDividend": 4.465,
    "realPrice": 88.4086,
    "realPricePlusDividend": 134.14
  },
  {
    "month": "1877-05-01",
    "price": 2.94,
    "nominalPricePlusDividend": 4.4983,
    "realPrice": 86.8296,
    "realPricePlusDividend": 132.692
  },
  {
    "month": "1877-06-01",
    "price": 2.73,
    "nominalPricePlusDividend": 4.2094,
    "realPrice": 85.1916,
    "realPricePlusDividend": 131.161
  },
  {
    "month": "1877-07-01",
    "price": 2.85,
    "nominalPricePlusDividend": 4.4259,
    "realPrice": 88.1049,
    "realPricePlusDividend": 136.5802
  },
  {
    "month": "1877-08-01",
    "price": 3.05,
    "nominalPricePlusDividend": 4.767,
    "realPrice": 97.9493,
    "realPricePlusDividend": 152.7802
  },
  {
    "month": "1877-09-01",
    "price": 3.24,
    "nominalPricePlusDividend": 5.0935,
    "realPrice": 105.0714,
    "realPricePlusDividend": 164.8046
  },
  {
    "month": "1877-10-01",
    "price": 3.31,
    "nominalPricePlusDividend": 5.232,
    "realPrice": 107.3415,
    "realPricePlusDividend": 169.2468
  },
  {
    "month": "1877-11-01",
    "price": 3.26,
    "nominalPricePlusDividend": 5.1804,
    "realPrice": 107.834,
    "realPricePlusDividend": 170.8877
  },
  {
    "month": "1877-12-01",
    "price": 3.25,
    "nominalPricePlusDividend": 5.1909,
    "realPrice": 107.5032,
    "realPricePlusDividend": 171.1923
  },
  {
    "month": "1878-01-01",
    "price": 3.25,
    "nominalPricePlusDividend": 5.2162,
    "realPrice": 110.8287,
    "realPricePlusDividend": 177.3429
  },
  {
    "month": "1878-02-01",
    "price": 3.18,
    "nominalPricePlusDividend": 5.1292,
    "realPrice": 109.5705,
    "realPricePlusDividend": 176.1935
  },
  {
    "month": "1878-03-01",
    "price": 3.24,
    "nominalPricePlusDividend": 5.2512,
    "realPrice": 114.0136,
    "realPricePlusDividend": 184.221
  },
  {
    "month": "1878-04-01",
    "price": 3.33,
    "nominalPricePlusDividend": 5.4224,
    "realPrice": 118.441,
    "realPricePlusDividend": 192.2674
  },
  {
    "month": "1878-05-01",
    "price": 3.34,
    "nominalPricePlusDividend": 5.4641,
    "realPrice": 122.7562,
    "realPricePlusDividend": 200.1949
  },
  {
    "month": "1878-06-01",
    "price": 3.41,
    "nominalPricePlusDividend": 5.6039,
    "realPrice": 128.1767,
    "realPricePlusDividend": 209.9784
  },
  {
    "month": "1878-07-01",
    "price": 3.48,
    "nominalPricePlusDividend": 5.7443,
    "realPrice": 129.3391,
    "realPricePlusDividend": 212.8158
  },
  {
    "month": "1878-08-01",
    "price": 3.45,
    "nominalPricePlusDividend": 5.7201,
    "realPrice": 126.7991,
    "realPricePlusDividend": 209.5589
  },
  {
    "month": "1878-09-01",
    "price": 3.52,
    "nominalPricePlusDividend": 5.8615,
    "realPrice": 129.3718,
    "realPricePlusDividend": 214.7332
  },
  {
    "month": "1878-10-01",
    "price": 3.48,
    "nominalPricePlusDividend": 5.8202,
    "realPrice": 129.3391,
    "realPricePlusDividend": 215.6116
  },
  {
    "month": "1878-11-01",
    "price": 3.47,
    "nominalPricePlusDividend": 5.8288,
    "realPrice": 130.432,
    "realPricePlusDividend": 218.3762
  },
  {
    "month": "1878-12-01",
    "price": 3.45,
    "nominalPricePlusDividend": 5.8205,
    "realPrice": 132.6967,
    "realPricePlusDividend": 223.1323
  },
  {
    "month": "1879-01-01",
    "price": 3.58,
    "nominalPricePlusDividend": 6.0651,
    "realPrice": 136.1138,
    "realPricePlusDividend": 229.8449
  },
  {
    "month": "1879-02-01",
    "price": 3.71,
    "nominalPricePlusDividend": 6.311,
    "realPrice": 139.4533,
    "realPricePlusDividend": 236.4521
  },
  {
    "month": "1879-03-01",
    "price": 3.65,
    "nominalPricePlusDividend": 6.235,
    "realPrice": 138.7753,
    "realPricePlusDividend": 236.2948
  },
  {
    "month": "1879-04-01",
    "price": 3.77,
    "nominalPricePlusDividend": 6.4663,
    "realPrice": 145.0048,
    "realPricePlusDividend": 247.9194
  },
  {
    "month": "1879-05-01",
    "price": 3.94,
    "nominalPricePlusDividend": 6.7845,
    "realPrice": 151.5435,
    "realPricePlusDividend": 260.1292
  },
  {
    "month": "1879-06-01",
    "price": 3.96,
    "nominalPricePlusDividend": 6.846,
    "realPrice": 154.1044,
    "realPricePlusDividend": 265.5812
  },
  {
    "month": "1879-07-01",
    "price": 4.04,
    "nominalPricePlusDividend": 7.0117,
    "realPrice": 155.3898,
    "realPricePlusDividend": 268.8537
  },
  {
    "month": "1879-08-01",
    "price": 4.07,
    "nominalPricePlusDividend": 7.0915,
    "realPrice": 156.5436,
    "realPricePlusDividend": 271.9205
  },
  {
    "month": "1879-09-01",
    "price": 4.22,
    "nominalPricePlusDividend": 7.3809,
    "realPrice": 156.8422,
    "realPricePlusDividend": 273.4867
  },
  {
    "month": "1879-10-01",
    "price": 4.68,
    "nominalPricePlusDividend": 8.2139,
    "realPrice": 164.6864,
    "realPricePlusDividend": 288.1688
  },
  {
    "month": "1879-11-01",
    "price": 4.93,
    "nominalPricePlusDividend": 8.6814,
    "realPrice": 164.7216,
    "realPricePlusDividend": 289.1952
  },
  {
    "month": "1879-12-01",
    "price": 4.92,
    "nominalPricePlusDividend": 8.6929,
    "realPrice": 159.5529,
    "realPricePlusDividend": 281.0682
  },
  {
    "month": "1880-01-01",
    "price": 5.11,
    "nominalPricePlusDividend": 9.0581,
    "realPrice": 160.9789,
    "realPricePlusDividend": 284.5268
  },
  {
    "month": "1880-02-01",
    "price": 5.2,
    "nominalPricePlusDividend": 9.2479,
    "realPrice": 163.8141,
    "realPricePlusDividend": 290.511
  },
  {
    "month": "1880-03-01",
    "price": 5.3,
    "nominalPricePlusDividend": 9.4568,
    "realPrice": 165.3902,
    "realPricePlusDividend": 294.2962
  },
  {
    "month": "1880-04-01",
    "price": 5.18,
    "nominalPricePlusDividend": 9.2747,
    "realPrice": 167.9846,
    "realPricePlusDividend": 299.9689
  },
  {
    "month": "1880-05-01",
    "price": 4.77,
    "nominalPricePlusDividend": 8.5734,
    "realPrice": 159.3757,
    "realPricePlusDividend": 285.7131
  },
  {
    "month": "1880-06-01",
    "price": 4.79,
    "nominalPricePlusDividend": 8.6431,
    "realPrice": 163.3445,
    "realPricePlusDividend": 293.9979
  },
  {
    "month": "1880-07-01",
    "price": 5.01,
    "nominalPricePlusDividend": 9.0746,
    "realPrice": 170.8467,
    "realPricePlusDividend": 308.7012
  },
  {
    "month": "1880-08-01",
    "price": 5.19,
    "nominalPricePlusDividend": 9.4361,
    "realPrice": 176.9849,
    "realPricePlusDividend": 321.0227
  },
  {
    "month": "1880-09-01",
    "price": 5.18,
    "nominalPricePlusDividend": 9.4543,
    "realPrice": 174.8411,
    "realPricePlusDividend": 318.3822
  },
  {
    "month": "1880-10-01",
    "price": 5.33,
    "nominalPricePlusDividend": 9.7653,
    "realPrice": 179.904,
    "realPricePlusDividend": 328.8803
  },
  {
    "month": "1880-11-01",
    "price": 5.61,
    "nominalPricePlusDividend": 10.3165,
    "realPrice": 187.4418,
    "realPricePlusDividend": 343.9561
  },
  {
    "month": "1880-12-01",
    "price": 5.84,
    "nominalPricePlusDividend": 10.7785,
    "realPrice": 193.1749,
    "realPricePlusDividend": 355.7896
  },
  {
    "month": "1881-01-01",
    "price": 6.19,
    "nominalPricePlusDividend": 11.4645,
    "realPrice": 206.8208,
    "realPricePlusDividend": 382.2795
  },
  {
    "month": "1881-02-01",
    "price": 6.17,
    "nominalPricePlusDividend": 11.4684,
    "realPrice": 204.0906,
    "realPricePlusDividend": 378.6068
  },
  {
    "month": "1881-03-01",
    "price": 6.24,
    "nominalPricePlusDividend": 11.6403,
    "realPrice": 206.4061,
    "realPricePlusDividend": 384.3063
  },
  {
    "month": "1881-04-01",
    "price": 6.22,
    "nominalPricePlusDividend": 11.6457,
    "realPrice": 203.7088,
    "realPricePlusDividend": 380.7048
  },
  {
    "month": "1881-05-01",
    "price": 6.5,
    "nominalPricePlusDividend": 12.2137,
    "realPrice": 215.0064,
    "realPricePlusDividend": 403.2845
  },
  {
    "month": "1881-06-01",
    "price": 6.58,
    "nominalPricePlusDividend": 12.4086,
    "realPrice": 217.6526,
    "realPricePlusDividend": 409.7452
  },
  {
    "month": "1881-07-01",
    "price": 6.35,
    "nominalPricePlusDividend": 12.0205,
    "realPrice": 207.9664,
    "realPricePlusDividend": 393.0236
  },
  {
    "month": "1881-08-01",
    "price": 6.2,
    "nominalPricePlusDividend": 11.783,
    "realPrice": 199.1102,
    "realPricePlusDividend": 377.8019
  },
  {
    "month": "1881-09-01",
    "price": 6.25,
    "nominalPricePlusDividend": 11.9256,
    "realPrice": 193.2125,
    "realPricePlusDividend": 368.1001
  },
  {
    "month": "1881-10-01",
    "price": 6.15,
    "nominalPricePlusDividend": 11.7833,
    "realPrice": 188.3604,
    "realPricePlusDividend": 360.3611
  },
  {
    "month": "1881-11-01",
    "price": 6.19,
    "nominalPricePlusDividend": 11.9094,
    "realPrice": 191.3577,
    "realPricePlusDividend": 367.6456
  },
  {
    "month": "1881-12-01",
    "price": 6.01,
    "nominalPricePlusDividend": 11.6136,
    "realPrice": 185.7932,
    "realPricePlusDividend": 358.5363
  },
  {
    "month": "1882-01-01",
    "price": 5.92,
    "nominalPricePlusDividend": 11.4912,
    "realPrice": 183.0109,
    "realPricePlusDividend": 354.7556
  },
  {
    "month": "1882-02-01",
    "price": 5.79,
    "nominalPricePlusDividend": 11.2906,
    "realPrice": 177.3344,
    "realPricePlusDividend": 345.3329
  },
  {
    "month": "1882-03-01",
    "price": 5.78,
    "nominalPricePlusDividend": 11.3231,
    "realPrice": 177.0281,
    "realPricePlusDividend": 346.3246
  },
  {
    "month": "1882-04-01",
    "price": 5.78,
    "nominalPricePlusDividend": 11.3754,
    "realPrice": 175.4037,
    "realPricePlusDividend": 344.7275
  },
  {
    "month": "1882-05-01",
    "price": 5.71,
    "nominalPricePlusDividend": 11.2901,
    "realPrice": 171.7052,
    "realPricePlusDividend": 339.0323
  },
  {
    "month": "1882-06-01",
    "price": 5.68,
    "nominalPricePlusDividend": 11.2835,
    "realPrice": 169.264,
    "realPricePlusDividend": 335.7788
  },
  {
    "month": "1882-07-01",
    "price": 6,
    "nominalPricePlusDividend": 11.9722,
    "realPrice": 180.4257,
    "realPricePlusDividend": 359.5095
  },
  {
    "month": "1882-08-01",
    "price": 6.18,
    "nominalPricePlusDividend": 12.3845,
    "realPrice": 184.164,
    "realPricePlusDividend": 368.5392
  },
  {
    "month": "1882-09-01",
    "price": 6.24,
    "nominalPricePlusDividend": 12.5582,
    "realPrice": 191.1169,
    "realPricePlusDividend": 384.085
  },
  {
    "month": "1882-10-01",
    "price": 6.07,
    "nominalPricePlusDividend": 12.2698,
    "realPrice": 187.648,
    "realPricePlusDividend": 378.7679
  },
  {
    "month": "1882-11-01",
    "price": 5.81,
    "nominalPricePlusDividend": 11.7981,
    "realPrice": 181.3052,
    "realPricePlusDividend": 367.6421
  },
  {
    "month": "1882-12-01",
    "price": 5.84,
    "nominalPricePlusDividend": 11.9132,
    "realPrice": 183.9758,
    "realPricePlusDividend": 374.7585
  },
  {
    "month": "1883-01-01",
    "price": 5.81,
    "nominalPricePlusDividend": 11.9064,
    "realPrice": 183.0308,
    "realPricePlusDividend": 374.5463
  },
  {
    "month": "1883-02-01",
    "price": 5.68,
    "nominalPricePlusDividend": 11.6947,
    "realPrice": 177.2484,
    "realPricePlusDividend": 364.423
  },
  {
    "month": "1883-03-01",
    "price": 5.75,
    "nominalPricePlusDividend": 11.8941,
    "realPrice": 181.1406,
    "realPricePlusDividend": 374.1634
  },
  {
    "month": "1883-04-01",
    "price": 5.87,
    "nominalPricePlusDividend": 12.1979,
    "realPrice": 186.6994,
    "realPricePlusDividend": 387.4129
  },
  {
    "month": "1883-05-01",
    "price": 5.77,
    "nominalPricePlusDividend": 12.0461,
    "realPrice": 185.3009,
    "realPricePlusDividend": 386.3087
  },
  {
    "month": "1883-06-01",
    "price": 5.82,
    "nominalPricePlusDividend": 12.2069,
    "realPrice": 192.5134,
    "realPricePlusDividend": 403.2099
  },
  {
    "month": "1883-07-01",
    "price": 5.73,
    "nominalPricePlusDividend": 12.0749,
    "realPrice": 193.4053,
    "realPricePlusDividend": 406.9944
  },
  {
    "month": "1883-08-01",
    "price": 5.47,
    "nominalPricePlusDividend": 11.5842,
    "realPrice": 184.6295,
    "realPricePlusDividend": 390.4579
  },
  {
    "month": "1883-09-01",
    "price": 5.53,
    "nominalPricePlusDividend": 11.7689,
    "realPrice": 188.5793,
    "realPricePlusDividend": 400.7764
  },
  {
    "month": "1883-10-01",
    "price": 5.38,
    "nominalPricePlusDividend": 11.5078,
    "realPrice": 183.4642,
    "realPricePlusDividend": 391.8852
  },
  {
    "month": "1883-11-01",
    "price": 5.46,
    "nominalPricePlusDividend": 11.7374,
    "realPrice": 188.1305,
    "realPricePlusDividend": 403.8687
  },
  {
    "month": "1883-12-01",
    "price": 5.34,
    "nominalPricePlusDividend": 11.5384,
    "realPrice": 182.1001,
    "realPricePlusDividend": 392.9332
  },
  {
    "month": "1884-01-01",
    "price": 5.18,
    "nominalPricePlusDividend": 11.2521,
    "realPrice": 176.6439,
    "realPricePlusDividend": 383.17
  },
  {
    "month": "1884-02-01",
    "price": 5.32,
    "nominalPricePlusDividend": 11.6157,
    "realPrice": 181.4181,
    "realPricePlusDividend": 395.5369
  },
  {
    "month": "1884-03-01",
    "price": 5.3,
    "nominalPricePlusDividend": 11.6314,
    "realPrice": 180.7361,
    "realPricePlusDividend": 396.0605
  },
  {
    "month": "1884-04-01",
    "price": 5.06,
    "nominalPricePlusDividend": 11.1642,
    "realPrice": 176.1837,
    "realPricePlusDividend": 388.1371
  },
  {
    "month": "1884-05-01",
    "price": 4.65,
    "nominalPricePlusDividend": 10.319,
    "realPrice": 165.3905,
    "realPricePlusDividend": 366.4571
  },
  {
    "month": "1884-06-01",
    "price": 4.46,
    "nominalPricePlusDividend": 9.9569,
    "realPrice": 158.6326,
    "realPricePlusDividend": 353.582
  },
  {
    "month": "1884-07-01",
    "price": 4.46,
    "nominalPricePlusDividend": 10.0164,
    "realPrice": 160.3558,
    "realPricePlusDividend": 359.5453
  },
  {
    "month": "1884-08-01",
    "price": 4.74,
    "nominalPricePlusDividend": 10.7048,
    "realPrice": 170.423,
    "realPricePlusDividend": 384.2421
  },
  {
    "month": "1884-09-01",
    "price": 4.59,
    "nominalPricePlusDividend": 10.4256,
    "realPrice": 166.8437,
    "realPricePlusDividend": 378.3203
  },
  {
    "month": "1884-10-01",
    "price": 4.44,
    "nominalPricePlusDividend": 10.1446,
    "realPrice": 163.1849,
    "realPricePlusDividend": 372.1965
  },
  {
    "month": "1884-11-01",
    "price": 4.35,
    "nominalPricePlusDividend": 9.9986,
    "realPrice": 163.5099,
    "realPricePlusDividend": 375.1613
  },
  {
    "month": "1884-12-01",
    "price": 4.34,
    "nominalPricePlusDividend": 10.0353,
    "realPrice": 165.0095,
    "realPricePlusDividend": 380.8523
  },
  {
    "month": "1885-01-01",
    "price": 4.24,
    "nominalPricePlusDividend": 9.8638,
    "realPrice": 161.2074,
    "realPricePlusDividend": 374.2981
  },
  {
    "month": "1885-02-01",
    "price": 4.37,
    "nominalPricePlusDividend": 10.2252,
    "realPrice": 164.2617,
    "realPricePlusDividend": 383.5558
  },
  {
    "month": "1885-03-01",
    "price": 4.38,
    "nominalPricePlusDividend": 10.3068,
    "realPrice": 168.4671,
    "realPricePlusDividend": 395.5616
  },
  {
    "month": "1885-04-01",
    "price": 4.37,
    "nominalPricePlusDividend": 10.3406,
    "realPrice": 166.1501,
    "realPricePlusDividend": 392.251
  },
  {
    "month": "1885-05-01",
    "price": 4.32,
    "nominalPricePlusDividend": 10.2788,
    "realPrice": 168.1139,
    "realPricePlusDividend": 399.0337
  },
  {
    "month": "1885-06-01",
    "price": 4.3,
    "nominalPricePlusDividend": 10.2869,
    "realPrice": 171.3678,
    "realPricePlusDividend": 408.9216
  },
  {
    "month": "1885-07-01",
    "price": 4.46,
    "nominalPricePlusDividend": 10.7245,
    "realPrice": 175.6283,
    "realPricePlusDividend": 421.1931
  },
  {
    "month": "1885-08-01",
    "price": 4.71,
    "nominalPricePlusDividend": 11.3796,
    "realPrice": 185.473,
    "realPricePlusDividend": 446.8717
  },
  {
    "month": "1885-09-01",
    "price": 4.65,
    "nominalPricePlusDividend": 11.2876,
    "realPrice": 185.3163,
    "realPricePlusDividend": 448.5515
  },
  {
    "month": "1885-10-01",
    "price": 4.92,
    "nominalPricePlusDividend": 11.9951,
    "realPrice": 196.0766,
    "realPricePlusDividend": 476.6168
  },
  {
    "month": "1885-11-01",
    "price": 5.24,
    "nominalPricePlusDividend": 12.8265,
    "realPrice": 206.3436,
    "realPricePlusDividend": 503.5312
  },
  {
    "month": "1885-12-01",
    "price": 5.2,
    "nominalPricePlusDividend": 12.7787,
    "realPrice": 200.0066,
    "realPricePlusDividend": 489.9418
  },
  {
    "month": "1886-01-01",
    "price": 5.2,
    "nominalPricePlusDividend": 12.8278,
    "realPrice": 204.7685,
    "realPricePlusDividend": 503.5192
  },
  {
    "month": "1886-02-01",
    "price": 5.3,
    "nominalPricePlusDividend": 13.1235,
    "realPrice": 208.7063,
    "realPricePlusDividend": 515.1094
  },
  {
    "month": "1886-03-01",
    "price": 5.19,
    "nominalPricePlusDividend": 12.9,
    "realPrice": 206.8369,
    "realPricePlusDividend": 512.4189
  },
  {
    "month": "1886-04-01",
    "price": 5.12,
    "nominalPricePlusDividend": 12.7747,
    "realPrice": 206.5357,
    "realPricePlusDividend": 513.6126
  },
  {
    "month": "1886-05-01",
    "price": 5.02,
    "nominalPricePlusDividend": 12.5737,
    "realPrice": 207.5643,
    "realPricePlusDividend": 518.153
  },
  {
    "month": "1886-06-01",
    "price": 5.25,
    "nominalPricePlusDividend": 13.1981,
    "realPrice": 219.8221,
    "realPricePlusDividend": 550.7531
  },
  {
    "month": "1886-07-01",
    "price": 5.33,
    "nominalPricePlusDividend": 13.4474,
    "realPrice": 220.382,
    "realPricePlusDividend": 554.1239
  },
  {
    "month": "1886-08-01",
    "price": 5.37,
    "nominalPricePlusDividend": 13.5963,
    "realPrice": 219.2948,
    "realPricePlusDividend": 553.3273
  },
  {
    "month": "1886-09-01",
    "price": 5.51,
    "nominalPricePlusDividend": 13.9986,
    "realPrice": 225.012,
    "realPricePlusDividend": 569.6821
  },
  {
    "month": "1886-10-01",
    "price": 5.65,
    "nominalPricePlusDividend": 14.4019,
    "realPrice": 230.7292,
    "realPricePlusDividend": 586.0779
  },
  {
    "month": "1886-11-01",
    "price": 5.79,
    "nominalPricePlusDividend": 14.8062,
    "realPrice": 236.4464,
    "realPricePlusDividend": 602.5137
  },
  {
    "month": "1886-12-01",
    "price": 5.64,
    "nominalPricePlusDividend": 14.4699,
    "realPrice": 227.5119,
    "realPricePlusDividend": 581.6286
  },
  {
    "month": "1887-01-01",
    "price": 5.58,
    "nominalPricePlusDividend": 14.363,
    "realPrice": 219.7323,
    "realPricePlusDividend": 563.604
  },
  {
    "month": "1887-02-01",
    "price": 5.54,
    "nominalPricePlusDividend": 14.3078,
    "realPrice": 215.5905,
    "realPricePlusDividend": 554.8493
  },
  {
    "month": "1887-03-01",
    "price": 5.67,
    "nominalPricePlusDividend": 14.6919,
    "realPrice": 220.6495,
    "realPricePlusDividend": 569.7651
  },
  {
    "month": "1887-04-01",
    "price": 5.8,
    "nominalPricePlusDividend": 15.0779,
    "realPrice": 225.7085,
    "realPricePlusDividend": 584.7517
  },
  {
    "month": "1887-05-01",
    "price": 5.9,
    "nominalPricePlusDividend": 15.3877,
    "realPrice": 229.6,
    "realPricePlusDividend": 596.7841
  },
  {
    "month": "1887-06-01",
    "price": 5.73,
    "nominalPricePlusDividend": 14.9949,
    "realPrice": 225.6391,
    "realPricePlusDividend": 588.4902
  },
  {
    "month": "1887-07-01",
    "price": 5.59,
    "nominalPricePlusDividend": 14.6797,
    "realPrice": 222.7781,
    "realPricePlusDividend": 583.0825
  },
  {
    "month": "1887-08-01",
    "price": 5.45,
    "nominalPricePlusDividend": 14.3641,
    "realPrice": 214.6131,
    "realPricePlusDividend": 563.7703
  },
  {
    "month": "1887-09-01",
    "price": 5.38,
    "nominalPricePlusDividend": 14.2323,
    "realPrice": 214.409,
    "realPricePlusDividend": 565.3465
  },
  {
    "month": "1887-10-01",
    "price": 5.2,
    "nominalPricePlusDividend": 13.8096,
    "realPrice": 204.7685,
    "realPricePlusDividend": 542.0435
  },
  {
    "month": "1887-11-01",
    "price": 5.3,
    "nominalPricePlusDividend": 14.1294,
    "realPrice": 206.2509,
    "realPricePlusDividend": 548.0891
  },
  {
    "month": "1887-12-01",
    "price": 5.27,
    "nominalPricePlusDividend": 14.1044,
    "realPrice": 200.3687,
    "realPricePlusDividend": 534.5596
  },
  {
    "month": "1888-01-01",
    "price": 5.31,
    "nominalPricePlusDividend": 14.2672,
    "realPrice": 199.5948,
    "realPricePlusDividend": 534.567
  },
  {
    "month": "1888-02-01",
    "price": 5.28,
    "nominalPricePlusDividend": 14.2422,
    "realPrice": 200.7489,
    "realPricePlusDividend": 539.7481
  },
  {
    "month": "1888-03-01",
    "price": 5.08,
    "nominalPricePlusDividend": 13.7581,
    "realPrice": 193.1447,
    "realPricePlusDividend": 521.3871
  },
  {
    "month": "1888-04-01",
    "price": 5.1,
    "nominalPricePlusDividend": 13.8676,
    "realPrice": 196.1603,
    "realPricePlusDividend": 531.6296
  },
  {
    "month": "1888-05-01",
    "price": 5.17,
    "nominalPricePlusDividend": 14.1131,
    "realPrice": 201.1919,
    "realPricePlusDividend": 547.3871
  },
  {
    "month": "1888-06-01",
    "price": 5.01,
    "nominalPricePlusDividend": 13.7313,
    "realPrice": 197.2865,
    "realPricePlusDividend": 538.9013
  },
  {
    "month": "1888-07-01",
    "price": 5.14,
    "nominalPricePlusDividend": 14.1424,
    "realPrice": 200.0244,
    "realPricePlusDividend": 548.4878
  },
  {
    "month": "1888-08-01",
    "price": 5.25,
    "nominalPricePlusDividend": 14.4997,
    "realPrice": 204.3051,
    "realPricePlusDividend": 562.3276
  },
  {
    "month": "1888-09-01",
    "price": 5.38,
    "nominalPricePlusDividend": 14.9132,
    "realPrice": 209.3641,
    "realPricePlusDividend": 578.3463
  },
  {
    "month": "1888-10-01",
    "price": 5.35,
    "nominalPricePlusDividend": 14.8843,
    "realPrice": 205.776,
    "realPricePlusDividend": 570.4974
  },
  {
    "month": "1888-11-01",
    "price": 5.24,
    "nominalPricePlusDividend": 14.6324,
    "realPrice": 199.228,
    "realPricePlusDividend": 554.3758
  },
  {
    "month": "1888-12-01",
    "price": 5.14,
    "nominalPricePlusDividend": 14.4071,
    "realPrice": 195.426,
    "realPricePlusDividend": 545.8209
  },
  {
    "month": "1889-01-01",
    "price": 5.24,
    "nominalPricePlusDividend": 14.7411,
    "realPrice": 206.3436,
    "realPricePlusDividend": 578.4111
  },
  {
    "month": "1889-02-01",
    "price": 5.3,
    "nominalPricePlusDividend": 14.9636,
    "realPrice": 211.2207,
    "realPricePlusDividend": 594.2046
  },
  {
    "month": "1889-03-01",
    "price": 5.19,
    "nominalPricePlusDividend": 14.7068,
    "realPrice": 209.3594,
    "realPricePlusDividend": 591.1165
  },
  {
    "month": "1889-04-01",
    "price": 5.18,
    "nominalPricePlusDividend": 14.7321,
    "realPrice": 208.956,
    "realPricePlusDividend": 592.1261
  },
  {
    "month": "1889-05-01",
    "price": 5.32,
    "nominalPricePlusDividend": 15.184,
    "realPrice": 219.9685,
    "realPricePlusDividend": 625.534
  },
  {
    "month": "1889-06-01",
    "price": 5.41,
    "nominalPricePlusDividend": 15.4946,
    "realPrice": 223.6898,
    "realPricePlusDividend": 638.3178
  },
  {
    "month": "1889-07-01",
    "price": 5.3,
    "nominalPricePlusDividend": 15.2333,
    "realPrice": 219.1416,
    "realPricePlusDividend": 627.5402
  },
  {
    "month": "1889-08-01",
    "price": 5.37,
    "nominalPricePlusDividend": 15.4882,
    "realPrice": 222.0359,
    "realPricePlusDividend": 638.0285
  },
  {
    "month": "1889-09-01",
    "price": 5.5,
    "nominalPricePlusDividend": 15.9168,
    "realPrice": 224.6036,
    "realPricePlusDividend": 647.5796
  },
  {
    "month": "1889-10-01",
    "price": 5.4,
    "nominalPricePlusDividend": 15.681,
    "realPrice": 220.5199,
    "realPricePlusDividend": 637.9775
  },
  {
    "month": "1889-11-01",
    "price": 5.35,
    "nominalPricePlusDividend": 15.5895,
    "realPrice": 218.4781,
    "realPricePlusDividend": 634.2409
  },
  {
    "month": "1889-12-01",
    "price": 5.32,
    "nominalPricePlusDividend": 15.5557,
    "realPrice": 214.6035,
    "realPricePlusDividend": 625.1365
  },
  {
    "month": "1890-01-01",
    "price": 5.38,
    "nominalPricePlusDividend": 15.7847,
    "realPrice": 222.4494,
    "realPricePlusDividend": 650.1964
  },
  {
    "month": "1890-02-01",
    "price": 5.32,
    "nominalPricePlusDividend": 15.6625,
    "realPrice": 219.9685,
    "realPricePlusDividend": 645.1575
  },
  {
    "month": "1890-03-01",
    "price": 5.28,
    "nominalPricePlusDividend": 15.5987,
    "realPrice": 218.3146,
    "realPricePlusDividend": 642.5267
  },
  {
    "month": "1890-04-01",
    "price": 5.39,
    "nominalPricePlusDividend": 15.9778,
    "realPrice": 222.8628,
    "realPricePlusDividend": 658.1403
  },
  {
    "month": "1890-05-01",
    "price": 5.62,
    "nominalPricePlusDividend": 16.714,
    "realPrice": 229.5041,
    "realPricePlusDividend": 679.9604
  },
  {
    "month": "1890-06-01",
    "price": 5.58,
    "nominalPricePlusDividend": 16.6496,
    "realPrice": 227.8706,
    "realPricePlusDividend": 677.3357
  },
  {
    "month": "1890-07-01",
    "price": 5.54,
    "nominalPricePlusDividend": 16.5849,
    "realPrice": 226.2371,
    "realPricePlusDividend": 674.7023
  },
  {
    "month": "1890-08-01",
    "price": 5.41,
    "nominalPricePlusDividend": 16.2506,
    "realPrice": 213.0379,
    "realPricePlusDividend": 637.4885
  },
  {
    "month": "1890-09-01",
    "price": 5.32,
    "nominalPricePlusDividend": 16.0353,
    "realPrice": 207.0292,
    "realPricePlusDividend": 621.6397
  },
  {
    "month": "1890-10-01",
    "price": 5.08,
    "nominalPricePlusDividend": 15.3672,
    "realPrice": 197.6895,
    "realPricePlusDividend": 595.7349
  },
  {
    "month": "1890-11-01",
    "price": 4.71,
    "nominalPricePlusDividend": 14.3034,
    "realPrice": 187.7075,
    "realPricePlusDividend": 567.8526
  },
  {
    "month": "1890-12-01",
    "price": 4.6,
    "nominalPricePlusDividend": 14.025,
    "realPrice": 183.3236,
    "realPricePlusDividend": 556.7977
  },
  {
    "month": "1891-01-01",
    "price": 4.84,
    "nominalPricePlusDividend": 14.8127,
    "realPrice": 195.2407,
    "realPricePlusDividend": 595.2356
  },
  {
    "month": "1891-02-01",
    "price": 4.9,
    "nominalPricePlusDividend": 15.0524,
    "realPrice": 195.2795,
    "realPricePlusDividend": 597.5781
  },
  {
    "month": "1891-03-01",
    "price": 4.81,
    "nominalPricePlusDividend": 14.8322,
    "realPrice": 189.4108,
    "realPricePlusDividend": 581.8251
  },
  {
    "month": "1891-04-01",
    "price": 4.97,
    "nominalPricePlusDividend": 15.3822,
    "realPrice": 193.4088,
    "realPricePlusDividend": 596.2943
  },
  {
    "month": "1891-05-01",
    "price": 4.95,
    "nominalPricePlusDividend": 15.377,
    "realPrice": 194.9238,
    "realPricePlusDividend": 603.1876
  },
  {
    "month": "1891-06-01",
    "price": 4.85,
    "nominalPricePlusDividend": 15.1233,
    "realPrice": 195.6441,
    "realPricePlusDividend": 607.7017
  },
  {
    "month": "1891-07-01",
    "price": 4.77,
    "nominalPricePlusDividend": 14.931,
    "realPrice": 194.7926,
    "realPricePlusDividend": 607.3788
  },
  {
    "month": "1891-08-01",
    "price": 4.93,
    "nominalPricePlusDividend": 15.4892,
    "realPrice": 201.3265,
    "realPricePlusDividend": 630.0831
  },
  {
    "month": "1891-09-01",
    "price": 5.33,
    "nominalPricePlusDividend": 16.8036,
    "realPrice": 220.382,
    "realPricePlusDividend": 692.089
  },
  {
    "month": "1891-10-01",
    "price": 5.33,
    "nominalPricePlusDividend": 16.8614,
    "realPrice": 220.382,
    "realPricePlusDividend": 694.466
  },
  {
    "month": "1891-11-01",
    "price": 5.25,
    "nominalPricePlusDividend": 16.6663,
    "realPrice": 219.8221,
    "realPricePlusDividend": 695.1169
  },
  {
    "month": "1891-12-01",
    "price": 5.41,
    "nominalPricePlusDividend": 17.2324,
    "realPrice": 226.5214,
    "realPricePlusDividend": 718.7252
  },
  {
    "month": "1892-01-01",
    "price": 5.51,
    "nominalPricePlusDividend": 17.6093,
    "realPrice": 236.7009,
    "realPricePlusDividend": 753.5379
  },
  {
    "month": "1892-02-01",
    "price": 5.52,
    "nominalPricePlusDividend": 17.7003,
    "realPrice": 237.1305,
    "realPricePlusDividend": 757.4466
  },
  {
    "month": "1892-03-01",
    "price": 5.58,
    "nominalPricePlusDividend": 17.9524,
    "realPrice": 246.1001,
    "realPricePlusDividend": 788.7352
  },
  {
    "month": "1892-04-01",
    "price": 5.57,
    "nominalPricePlusDividend": 17.9805,
    "realPrice": 248.9789,
    "realPricePlusDividend": 800.664
  },
  {
    "month": "1892-05-01",
    "price": 5.57,
    "nominalPricePlusDividend": 18.0415,
    "realPrice": 248.9789,
    "realPricePlusDividend": 803.3947
  },
  {
    "month": "1892-06-01",
    "price": 5.54,
    "nominalPricePlusDividend": 18.006,
    "realPrice": 247.6379,
    "realPricePlusDividend": 801.828
  },
  {
    "month": "1892-07-01",
    "price": 5.54,
    "nominalPricePlusDividend": 18.0683,
    "realPrice": 241.1209,
    "realPricePlusDividend": 783.4435
  },
  {
    "month": "1892-08-01",
    "price": 5.62,
    "nominalPricePlusDividend": 18.3922,
    "realPrice": 241.4263,
    "realPricePlusDividend": 787.1454
  },
  {
    "month": "1892-09-01",
    "price": 5.48,
    "nominalPricePlusDividend": 17.9976,
    "realPrice": 235.4121,
    "realPricePlusDividend": 770.2756
  },
  {
    "month": "1892-10-01",
    "price": 5.59,
    "nominalPricePlusDividend": 18.4232,
    "realPrice": 240.1375,
    "realPricePlusDividend": 788.5058
  },
  {
    "month": "1892-11-01",
    "price": 5.57,
    "nominalPricePlusDividend": 18.4223,
    "realPrice": 233.2207,
    "realPricePlusDividend": 768.5202
  },
  {
    "month": "1892-12-01",
    "price": 5.51,
    "nominalPricePlusDividend": 18.2895,
    "realPrice": 227.8245,
    "realPricePlusDividend": 753.4593
  },
  {
    "month": "1893-01-01",
    "price": 5.61,
    "nominalPricePlusDividend": 18.6879,
    "realPrice": 223.5751,
    "realPricePlusDividend": 742.0466
  },
  {
    "month": "1893-02-01",
    "price": 5.51,
    "nominalPricePlusDividend": 18.4216,
    "realPrice": 216.9758,
    "realPricePlusDividend": 722.7719
  },
  {
    "month": "1893-03-01",
    "price": 5.31,
    "nominalPricePlusDividend": 17.8203,
    "realPrice": 214.2001,
    "realPricePlusDividend": 716.2371
  },
  {
    "month": "1893-04-01",
    "price": 5.31,
    "nominalPricePlusDividend": 17.8881,
    "realPrice": 216.8446,
    "realPricePlusDividend": 727.8443
  },
  {
    "month": "1893-05-01",
    "price": 4.84,
    "nominalPricePlusDividend": 16.3731,
    "realPrice": 200.1217,
    "realPricePlusDividend": 674.5335
  },
  {
    "month": "1893-06-01",
    "price": 4.61,
    "nominalPricePlusDividend": 15.6638,
    "realPrice": 195.4993,
    "realPricePlusDividend": 661.867
  },
  {
    "month": "1893-07-01",
    "price": 4.18,
    "nominalPricePlusDividend": 14.2722,
    "realPrice": 181.9288,
    "realPricePlusDividend": 618.9376
  },
  {
    "month": "1893-08-01",
    "price": 4.08,
    "nominalPricePlusDividend": 14.0007,
    "realPrice": 184.8741,
    "realPricePlusDividend": 632.1224
  },
  {
    "month": "1893-09-01",
    "price": 4.37,
    "nominalPricePlusDividend": 15.0664,
    "realPrice": 190.1983,
    "realPricePlusDividend": 653.3915
  },
  {
    "month": "1893-10-01",
    "price": 4.5,
    "nominalPricePlusDividend": 15.5857,
    "realPrice": 193.3129,
    "realPricePlusDividend": 667.1402
  },
  {
    "month": "1893-11-01",
    "price": 4.57,
    "nominalPricePlusDividend": 15.8998,
    "realPrice": 201.5551,
    "realPricePlusDividend": 698.7411
  },
  {
    "month": "1893-12-01",
    "price": 4.41,
    "nominalPricePlusDividend": 15.4154,
    "realPrice": 197.127,
    "realPricePlusDividend": 686.6133
  },
  {
    "month": "1894-01-01",
    "price": 4.32,
    "nominalPricePlusDividend": 15.1736,
    "realPrice": 198.4679,
    "realPricePlusDividend": 694.5689
  },
  {
    "month": "1894-02-01",
    "price": 4.38,
    "nominalPricePlusDividend": 15.4565,
    "realPrice": 204.0584,
    "realPricePlusDividend": 717.4345
  },
  {
    "month": "1894-03-01",
    "price": 4.51,
    "nominalPricePlusDividend": 15.9868,
    "realPrice": 216.2052,
    "realPricePlusDividend": 763.5064
  },
  {
    "month": "1894-04-01",
    "price": 4.57,
    "nominalPricePlusDividend": 16.2704,
    "realPrice": 219.0815,
    "realPricePlusDividend": 776.9982
  },
  {
    "month": "1894-05-01",
    "price": 4.4,
    "nominalPricePlusDividend": 15.7354,
    "realPrice": 210.9319,
    "realPricePlusDividend": 751.3952
  },
  {
    "month": "1894-06-01",
    "price": 4.34,
    "nominalPricePlusDividend": 15.5904,
    "realPrice": 208.0556,
    "realPricePlusDividend": 744.4171
  },
  {
    "month": "1894-07-01",
    "price": 4.25,
    "nominalPricePlusDividend": 15.3359,
    "realPrice": 203.741,
    "realPricePlusDividend": 732.2155
  },
  {
    "month": "1894-08-01",
    "price": 4.41,
    "nominalPricePlusDividend": 15.9814,
    "realPrice": 205.4561,
    "realPricePlusDividend": 741.4901
  },
  {
    "month": "1894-09-01",
    "price": 4.48,
    "nominalPricePlusDividend": 16.3025,
    "realPrice": 205.8186,
    "realPricePlusDividend": 745.8336
  },
  {
    "month": "1894-10-01",
    "price": 4.34,
    "nominalPricePlusDividend": 15.8598,
    "realPrice": 205.0835,
    "realPricePlusDividend": 746.2574
  },
  {
    "month": "1894-11-01",
    "price": 4.34,
    "nominalPricePlusDividend": 15.9258,
    "realPrice": 205.0835,
    "realPricePlusDividend": 749.3092
  },
  {
    "month": "1894-12-01",
    "price": 4.3,
    "nominalPricePlusDividend": 15.8442,
    "realPrice": 206.138,
    "realPricePlusDividend": 756.2227
  },
  {
    "month": "1895-01-01",
    "price": 4.25,
    "nominalPricePlusDividend": 15.7245,
    "realPrice": 203.741,
    "realPricePlusDividend": 750.4777
  },
  {
    "month": "1895-02-01",
    "price": 4.19,
    "nominalPricePlusDividend": 15.5667,
    "realPrice": 200.8647,
    "realPricePlusDividend": 742.9198
  },
  {
    "month": "1895-03-01",
    "price": 4.19,
    "nominalPricePlusDividend": 15.6307,
    "realPrice": 200.8647,
    "realPricePlusDividend": 745.9443
  },
  {
    "month": "1895-04-01",
    "price": 4.37,
    "nominalPricePlusDividend": 16.3659,
    "realPrice": 200.765,
    "realPricePlusDividend": 748.4602
  },
  {
    "month": "1895-05-01",
    "price": 4.61,
    "nominalPricePlusDividend": 17.3282,
    "realPrice": 208.8896,
    "realPricePlusDividend": 781.5844
  },
  {
    "month": "1895-06-01",
    "price": 4.7,
    "nominalPricePlusDividend": 17.7297,
    "realPrice": 210.0899,
    "realPricePlusDividend": 788.8588
  },
  {
    "month": "1895-07-01",
    "price": 4.72,
    "nominalPricePlusDividend": 17.868,
    "realPrice": 213.874,
    "realPricePlusDividend": 805.8748
  },
  {
    "month": "1895-08-01",
    "price": 4.79,
    "nominalPricePlusDividend": 18.1955,
    "realPrice": 220.0605,
    "realPricePlusDividend": 832.0187
  },
  {
    "month": "1895-09-01",
    "price": 4.82,
    "nominalPricePlusDividend": 18.3717,
    "realPrice": 221.4387,
    "realPricePlusDividend": 840.0481
  },
  {
    "month": "1895-10-01",
    "price": 4.75,
    "nominalPricePlusDividend": 18.1669,
    "realPrice": 218.2228,
    "realPricePlusDividend": 830.6515
  },
  {
    "month": "1895-11-01",
    "price": 4.59,
    "nominalPricePlusDividend": 17.6165,
    "realPrice": 210.8722,
    "realPricePlusDividend": 805.4611
  },
  {
    "month": "1895-12-01",
    "price": 4.32,
    "nominalPricePlusDividend": 16.6416,
    "realPrice": 201.2631,
    "realPricePlusDividend": 771.5711
  },
  {
    "month": "1896-01-01",
    "price": 4.27,
    "nominalPricePlusDividend": 16.51,
    "realPrice": 201.7757,
    "realPricePlusDividend": 776.3881
  },
  {
    "month": "1896-02-01",
    "price": 4.45,
    "nominalPricePlusDividend": 17.2669,
    "realPrice": 213.3289,
    "realPricePlusDividend": 823.7324
  },
  {
    "month": "1896-03-01",
    "price": 4.38,
    "nominalPricePlusDividend": 17.0562,
    "realPrice": 209.9731,
    "realPricePlusDividend": 813.6628
  },
  {
    "month": "1896-04-01",
    "price": 4.42,
    "nominalPricePlusDividend": 17.2728,
    "realPrice": 215.0068,
    "realPricePlusDividend": 836.0972
  },
  {
    "month": "1896-05-01",
    "price": 4.4,
    "nominalPricePlusDividend": 17.2554,
    "realPrice": 217.2286,
    "realPricePlusDividend": 847.7052
  },
  {
    "month": "1896-06-01",
    "price": 4.32,
    "nominalPricePlusDividend": 17.0024,
    "realPrice": 216.5103,
    "realPricePlusDividend": 847.9129
  },
  {
    "month": "1896-07-01",
    "price": 4.04,
    "nominalPricePlusDividend": 15.9611,
    "realPrice": 202.4773,
    "realPricePlusDividend": 795.964
  },
  {
    "month": "1896-08-01",
    "price": 3.81,
    "nominalPricePlusDividend": 15.113,
    "realPrice": 190.9501,
    "realPricePlusDividend": 753.6542
  },
  {
    "month": "1896-09-01",
    "price": 4.01,
    "nominalPricePlusDividend": 15.967,
    "realPrice": 200.9737,
    "realPricePlusDividend": 796.22
  },
  {
    "month": "1896-10-01",
    "price": 4.1,
    "nominalPricePlusDividend": 16.3859,
    "realPrice": 199.4407,
    "realPricePlusDividend": 793.0603
  },
  {
    "month": "1896-11-01",
    "price": 4.38,
    "nominalPricePlusDividend": 17.5654,
    "realPrice": 206.9737,
    "realPricePlusDividend": 825.8412
  },
  {
    "month": "1896-12-01",
    "price": 4.22,
    "nominalPricePlusDividend": 16.9842,
    "realPrice": 199.413,
    "realPricePlusDividend": 798.4975
  },
  {
    "month": "1897-01-01",
    "price": 4.22,
    "nominalPricePlusDividend": 17.0446,
    "realPrice": 205.278,
    "realPricePlusDividend": 824.9
  },
  {
    "month": "1897-02-01",
    "price": 4.18,
    "nominalPricePlusDividend": 16.9436,
    "realPrice": 203.3323,
    "realPricePlusDividend": 820.0088
  },
  {
    "month": "1897-03-01",
    "price": 4.19,
    "nominalPricePlusDividend": 17.0449,
    "realPrice": 203.8187,
    "realPricePlusDividend": 824.9088
  },
  {
    "month": "1897-04-01",
    "price": 4.06,
    "nominalPricePlusDividend": 16.5771,
    "realPrice": 200.4428,
    "realPricePlusDividend": 814.2382
  },
  {
    "month": "1897-05-01",
    "price": 4.08,
    "nominalPricePlusDividend": 16.72,
    "realPrice": 204.482,
    "realPricePlusDividend": 833.6957
  },
  {
    "month": "1897-06-01",
    "price": 4.27,
    "nominalPricePlusDividend": 17.5601,
    "realPrice": 214.0044,
    "realPricePlusDividend": 875.5802
  },
  {
    "month": "1897-07-01",
    "price": 4.46,
    "nominalPricePlusDividend": 18.4032,
    "realPrice": 223.5269,
    "realPricePlusDividend": 917.6117
  },
  {
    "month": "1897-08-01",
    "price": 4.75,
    "nominalPricePlusDividend": 19.6617,
    "realPrice": 227.7106,
    "realPricePlusDividend": 937.734
  },
  {
    "month": "1897-09-01",
    "price": 4.98,
    "nominalPricePlusDividend": 20.6758,
    "realPrice": 232.0116,
    "realPricePlusDividend": 958.3197
  },
  {
    "month": "1897-10-01",
    "price": 4.82,
    "nominalPricePlusDividend": 20.0738,
    "realPrice": 227.7655,
    "realPricePlusDividend": 943.7046
  },
  {
    "month": "1897-11-01",
    "price": 4.65,
    "nominalPricePlusDividend": 19.4283,
    "realPrice": 219.7323,
    "realPricePlusDividend": 913.3529
  },
  {
    "month": "1897-12-01",
    "price": 4.75,
    "nominalPricePlusDividend": 19.9088,
    "realPrice": 224.4577,
    "realPricePlusDividend": 935.9369
  },
  {
    "month": "1898-01-01",
    "price": 4.88,
    "nominalPricePlusDividend": 20.5165,
    "realPrice": 230.6008,
    "realPricePlusDividend": 964.531
  },
  {
    "month": "1898-02-01",
    "price": 4.87,
    "nominalPricePlusDividend": 20.5381,
    "realPrice": 226.8869,
    "realPricePlusDividend": 951.9691
  },
  {
    "month": "1898-03-01",
    "price": 4.65,
    "nominalPricePlusDividend": 19.6747,
    "realPrice": 216.6374,
    "realPricePlusDividend": 911.9734
  },
  {
    "month": "1898-04-01",
    "price": 4.57,
    "nominalPricePlusDividend": 19.4015,
    "realPrice": 212.9103,
    "realPricePlusDividend": 899.3304
  },
  {
    "month": "1898-05-01",
    "price": 4.87,
    "nominalPricePlusDividend": 20.7412,
    "realPrice": 211.9601,
    "realPricePlusDividend": 898.1973
  },
  {
    "month": "1898-06-01",
    "price": 5.06,
    "nominalPricePlusDividend": 21.6172,
    "realPrice": 235.7387,
    "realPricePlusDividend": 1002.0824
  },
  {
    "month": "1898-07-01",
    "price": 5.08,
    "nominalPricePlusDividend": 21.7703,
    "realPrice": 240.0516,
    "realPricePlusDividend": 1023.6199
  },
  {
    "month": "1898-08-01",
    "price": 5.27,
    "nominalPricePlusDividend": 22.653,
    "realPrice": 249.0299,
    "realPricePlusDividend": 1065.1459
  },
  {
    "month": "1898-09-01",
    "price": 5.26,
    "nominalPricePlusDividend": 22.6792,
    "realPrice": 248.5574,
    "realPricePlusDividend": 1066.4042
  },
  {
    "month": "1898-10-01",
    "price": 5.15,
    "nominalPricePlusDividend": 22.275,
    "realPrice": 243.3594,
    "realPricePlusDividend": 1047.4212
  },
  {
    "month": "1898-11-01",
    "price": 5.32,
    "nominalPricePlusDividend": 23.0812,
    "realPrice": 251.3927,
    "realPricePlusDividend": 1085.3522
  },
  {
    "month": "1898-12-01",
    "price": 5.65,
    "nominalPricePlusDividend": 24.5846,
    "realPrice": 263.2261,
    "realPricePlusDividend": 1139.7886
  },
  {
    "month": "1899-01-01",
    "price": 6.08,
    "nominalPricePlusDividend": 26.5282,
    "realPrice": 283.2592,
    "realPricePlusDividend": 1229.9042
  },
  {
    "month": "1899-02-01",
    "price": 6.31,
    "nominalPricePlusDividend": 27.6047,
    "realPrice": 285.9205,
    "realPricePlusDividend": 1244.7617
  },
  {
    "month": "1899-03-01",
    "price": 6.4,
    "nominalPricePlusDividend": 28.072,
    "realPrice": 289.9986,
    "realPricePlusDividend": 1265.8398
  },
  {
    "month": "1899-04-01",
    "price": 6.48,
    "nominalPricePlusDividend": 28.4969,
    "realPrice": 289.6559,
    "realPricePlusDividend": 1267.6445
  },
  {
    "month": "1899-05-01",
    "price": 6.21,
    "nominalPricePlusDividend": 27.3841,
    "realPrice": 277.5869,
    "realPricePlusDividend": 1218.1499
  },
  {
    "month": "1899-06-01",
    "price": 6.07,
    "nominalPricePlusDividend": 26.8417,
    "realPrice": 267.7111,
    "realPricePlusDividend": 1178.1127
  },
  {
    "month": "1899-07-01",
    "price": 6.28,
    "nominalPricePlusDividend": 27.8459,
    "realPrice": 273.3284,
    "realPricePlusDividend": 1206.1127
  },
  {
    "month": "1899-08-01",
    "price": 6.44,
    "nominalPricePlusDividend": 28.6314,
    "realPrice": 276.6522,
    "realPricePlusDividend": 1224.0399
  },
  {
    "month": "1899-09-01",
    "price": 6.37,
    "nominalPricePlusDividend": 28.3968,
    "realPrice": 263.3833,
    "realPricePlusDividend": 1168.4908
  },
  {
    "month": "1899-10-01",
    "price": 6.34,
    "nominalPricePlusDividend": 28.3401,
    "realPrice": 258.9067,
    "realPricePlusDividend": 1151.7707
  },
  {
    "month": "1899-11-01",
    "price": 6.46,
    "nominalPricePlusDividend": 28.9541,
    "realPrice": 260.5899,
    "realPricePlusDividend": 1162.3822
  },
  {
    "month": "1899-12-01",
    "price": 6.02,
    "nominalPricePlusDividend": 27.0601,
    "realPrice": 239.9149,
    "realPricePlusDividend": 1073.2658
  },
  {
    "month": "1900-01-01",
    "price": 6.1,
    "nominalPricePlusDividend": 27.4984,
    "realPrice": 243.1031,
    "realPricePlusDividend": 1090.7551
  },
  {
    "month": "1900-02-01",
    "price": 6.21,
    "nominalPricePlusDividend": 28.076,
    "realPrice": 244.5408,
    "realPricePlusDividend": 1100.5136
  },
  {
    "month": "1900-03-01",
    "price": 6.26,
    "nominalPricePlusDividend": 28.3868,
    "realPrice": 246.5097,
    "realPricePlusDividend": 1112.8029
  },
  {
    "month": "1900-04-01",
    "price": 6.34,
    "nominalPricePlusDividend": 28.8374,
    "realPrice": 249.66,
    "realPricePlusDividend": 1130.574
  },
  {
    "month": "1900-05-01",
    "price": 6.04,
    "nominalPricePlusDividend": 27.5639,
    "realPrice": 243.6475,
    "realPricePlusDividend": 1107.1088
  },
  {
    "month": "1900-06-01",
    "price": 5.86,
    "nominalPricePlusDividend": 26.8366,
    "realPrice": 239.305,
    "realPricePlusDividend": 1091.314
  },
  {
    "month": "1900-07-01",
    "price": 5.86,
    "nominalPricePlusDividend": 26.9339,
    "realPrice": 236.3865,
    "realPricePlusDividend": 1082.0229
  },
  {
    "month": "1900-08-01",
    "price": 5.94,
    "nominalPricePlusDividend": 27.4021,
    "realPrice": 242.5719,
    "realPricePlusDividend": 1114.5353
  },
  {
    "month": "1900-09-01",
    "price": 5.8,
    "nominalPricePlusDividend": 26.8601,
    "realPrice": 233.9662,
    "realPricePlusDividend": 1079.2745
  },
  {
    "month": "1900-10-01",
    "price": 6.01,
    "nominalPricePlusDividend": 27.9397,
    "realPrice": 245.4305,
    "realPricePlusDividend": 1136.6263
  },
  {
    "month": "1900-11-01",
    "price": 6.48,
    "nominalPricePlusDividend": 30.2351,
    "realPrice": 264.6239,
    "realPricePlusDividend": 1230.1169
  },
  {
    "month": "1900-12-01",
    "price": 6.87,
    "nominalPricePlusDividend": 32.1685,
    "realPrice": 284.0571,
    "realPricePlusDividend": 1325.2508
  },
  {
    "month": "1901-01-01",
    "price": 7.07,
    "nominalPricePlusDividend": 33.222,
    "realPrice": 288.7178,
    "realPricePlusDividend": 1351.7779
  },
  {
    "month": "1901-02-01",
    "price": 7.25,
    "nominalPricePlusDividend": 34.186,
    "realPrice": 299.7691,
    "realPricePlusDividend": 1408.4061
  },
  {
    "month": "1901-03-01",
    "price": 7.51,
    "nominalPricePlusDividend": 35.5312,
    "realPrice": 310.5195,
    "realPricePlusDividend": 1463.8446
  },
  {
    "month": "1901-04-01",
    "price": 8.14,
    "nominalPricePlusDividend": 38.6321,
    "realPrice": 340.8289,
    "realPricePlusDividend": 1611.766
  },
  {
    "month": "1901-05-01",
    "price": 7.73,
    "nominalPricePlusDividend": 36.8075,
    "realPrice": 323.6618,
    "realPricePlusDividend": 1535.6632
  },
  {
    "month": "1901-06-01",
    "price": 8.5,
    "nominalPricePlusDividend": 40.5963,
    "realPrice": 355.9024,
    "realPricePlusDividend": 1693.758
  },
  {
    "month": "1901-07-01",
    "price": 7.93,
    "nominalPricePlusDividend": 37.9974,
    "realPrice": 327.8854,
    "realPricePlusDividend": 1565.5273
  },
  {
    "month": "1901-08-01",
    "price": 8.04,
    "nominalPricePlusDividend": 38.6489,
    "realPrice": 328.3297,
    "realPricePlusDividend": 1572.7318
  },
  {
    "month": "1901-09-01",
    "price": 8,
    "nominalPricePlusDividend": 38.5821,
    "realPrice": 322.712,
    "realPricePlusDividend": 1550.887
  },
  {
    "month": "1901-10-01",
    "price": 7.91,
    "nominalPricePlusDividend": 38.2747,
    "realPrice": 319.0815,
    "realPricePlusDividend": 1538.5482
  },
  {
    "month": "1901-11-01",
    "price": 8.08,
    "nominalPricePlusDividend": 39.225,
    "realPrice": 322.012,
    "realPricePlusDividend": 1557.7681
  },
  {
    "month": "1901-12-01",
    "price": 7.95,
    "nominalPricePlusDividend": 38.7226,
    "realPrice": 313.0595,
    "realPricePlusDividend": 1519.5318
  },
  {
    "month": "1902-01-01",
    "price": 8.12,
    "nominalPricePlusDividend": 39.6806,
    "realPrice": 323.6061,
    "realPricePlusDividend": 1575.8867
  },
  {
    "month": "1902-02-01",
    "price": 8.19,
    "nominalPricePlusDividend": 40.1533,
    "realPrice": 326.3958,
    "realPricePlusDividend": 1594.667
  },
  {
    "month": "1902-03-01",
    "price": 8.2,
    "nominalPricePlusDividend": 40.3337,
    "realPrice": 326.7943,
    "realPricePlusDividend": 1601.8391
  },
  {
    "month": "1902-04-01",
    "price": 8.48,
    "nominalPricePlusDividend": 41.8432,
    "realPrice": 333.9301,
    "realPricePlusDividend": 1642.0089
  },
  {
    "month": "1902-05-01",
    "price": 8.46,
    "nominalPricePlusDividend": 41.8774,
    "realPrice": 329.2231,
    "realPricePlusDividend": 1624.0254
  },
  {
    "month": "1902-06-01",
    "price": 8.41,
    "nominalPricePlusDividend": 41.7637,
    "realPrice": 323.4722,
    "realPricePlusDividend": 1600.7882
  },
  {
    "month": "1902-07-01",
    "price": 8.6,
    "nominalPricePlusDividend": 42.8417,
    "realPrice": 330.7802,
    "realPricePlusDividend": 1642.1136
  },
  {
    "month": "1902-08-01",
    "price": 8.83,
    "nominalPricePlusDividend": 44.1227,
    "realPrice": 343.6217,
    "realPricePlusDividend": 1711.1154
  },
  {
    "month": "1902-09-01",
    "price": 8.85,
    "nominalPricePlusDividend": 44.3587,
    "realPrice": 340.3959,
    "realPricePlusDividend": 1700.2714
  },
  {
    "month": "1902-10-01",
    "price": 8.57,
    "nominalPricePlusDividend": 43.092,
    "realPrice": 308.1276,
    "realPricePlusDividend": 1543.9979
  },
  {
    "month": "1902-11-01",
    "price": 8.24,
    "nominalPricePlusDividend": 41.5703,
    "realPrice": 306.2512,
    "realPricePlusDividend": 1539.6969
  },
  {
    "month": "1902-12-01",
    "price": 8.05,
    "nominalPricePlusDividend": 40.7501,
    "realPrice": 295.8646,
    "realPricePlusDividend": 1492.5513
  },
  {
    "month": "1903-01-01",
    "price": 8.46,
    "nominalPricePlusDividend": 42.9648,
    "realPrice": 307.5159,
    "realPricePlusDividend": 1556.3901
  },
  {
    "month": "1903-02-01",
    "price": 8.41,
    "nominalPricePlusDividend": 42.8513,
    "realPrice": 305.6984,
    "realPricePlusDividend": 1552.2937
  },
  {
    "month": "1903-03-01",
    "price": 8.08,
    "nominalPricePlusDividend": 41.3113,
    "realPrice": 303.7149,
    "realPricePlusDividend": 1547.5423
  },
  {
    "month": "1903-04-01",
    "price": 7.75,
    "nominalPricePlusDividend": 39.7669,
    "realPrice": 291.3107,
    "realPricePlusDividend": 1489.7042
  },
  {
    "month": "1903-05-01",
    "price": 7.6,
    "nominalPricePlusDividend": 39.1411,
    "realPrice": 292.3174,
    "realPricePlusDividend": 1500.3888
  },
  {
    "month": "1903-06-01",
    "price": 7.18,
    "nominalPricePlusDividend": 37.1233,
    "realPrice": 276.163,
    "realPricePlusDividend": 1423.0578
  },
  {
    "month": "1903-07-01",
    "price": 6.85,
    "nominalPricePlusDividend": 35.5635,
    "realPrice": 263.4703,
    "realPricePlusDividend": 1363.2879
  },
  {
    "month": "1903-08-01",
    "price": 6.63,
    "nominalPricePlusDividend": 34.5692,
    "realPrice": 255.0084,
    "realPricePlusDividend": 1325.1887
  },
  {
    "month": "1903-09-01",
    "price": 6.47,
    "nominalPricePlusDividend": 33.8841,
    "realPrice": 245.9934,
    "realPricePlusDividend": 1284.0127
  },
  {
    "month": "1903-10-01",
    "price": 6.26,
    "nominalPricePlusDividend": 32.9349,
    "realPrice": 240.7772,
    "realPricePlusDividend": 1262.5774
  },
  {
    "month": "1903-11-01",
    "price": 6.28,
    "nominalPricePlusDividend": 33.1921,
    "realPrice": 244.3878,
    "realPricePlusDividend": 1287.4246
  },
  {
    "month": "1903-12-01",
    "price": 6.57,
    "nominalPricePlusDividend": 34.8783,
    "realPrice": 255.6732,
    "realPricePlusDividend": 1352.8462
  },
  {
    "month": "1904-01-01",
    "price": 6.68,
    "nominalPricePlusDividend": 35.6171,
    "realPrice": 253.9777,
    "realPricePlusDividend": 1349.6786
  },
  {
    "month": "1904-02-01",
    "price": 6.5,
    "nominalPricePlusDividend": 34.8114,
    "realPrice": 241.5817,
    "realPricePlusDividend": 1289.4458
  },
  {
    "month": "1904-03-01",
    "price": 6.48,
    "nominalPricePlusDividend": 34.8575,
    "realPrice": 243.5733,
    "realPricePlusDividend": 1305.7525
  },
  {
    "month": "1904-04-01",
    "price": 6.64,
    "nominalPricePlusDividend": 35.8706,
    "realPrice": 252.4569,
    "realPricePlusDividend": 1359.0861
  },
  {
    "month": "1904-05-01",
    "price": 6.5,
    "nominalPricePlusDividend": 35.2658,
    "realPrice": 252.9492,
    "realPricePlusDividend": 1367.5462
  },
  {
    "month": "1904-06-01",
    "price": 6.51,
    "nominalPricePlusDividend": 35.4708,
    "realPrice": 253.3383,
    "realPricePlusDividend": 1375.4273
  },
  {
    "month": "1904-07-01",
    "price": 6.78,
    "nominalPricePlusDividend": 37.0918,
    "realPrice": 263.8454,
    "realPricePlusDividend": 1438.2162
  },
  {
    "month": "1904-08-01",
    "price": 7.01,
    "nominalPricePlusDividend": 38.499,
    "realPrice": 269.6243,
    "realPricePlusDividend": 1475.3569
  },
  {
    "month": "1904-09-01",
    "price": 7.32,
    "nominalPricePlusDividend": 40.3495,
    "realPrice": 278.3109,
    "realPricePlusDividend": 1528.4289
  },
  {
    "month": "1904-10-01",
    "price": 7.75,
    "nominalPricePlusDividend": 42.8667,
    "realPrice": 294.6598,
    "realPricePlusDividend": 1623.7161
  },
  {
    "month": "1904-11-01",
    "price": 8.17,
    "nominalPricePlusDividend": 45.3358,
    "realPrice": 303.6496,
    "realPricePlusDividend": 1678.593
  },
  {
    "month": "1904-12-01",
    "price": 8.25,
    "nominalPricePlusDividend": 45.9246,
    "realPrice": 306.6229,
    "realPricePlusDividend": 1700.3295
  },
  {
    "month": "1905-01-01",
    "price": 8.43,
    "nominalPricePlusDividend": 47.0704,
    "realPrice": 313.3128,
    "realPricePlusDividend": 1742.7731
  },
  {
    "month": "1905-02-01",
    "price": 8.8,
    "nominalPricePlusDividend": 49.2814,
    "realPrice": 327.0644,
    "realPricePlusDividend": 1824.6544
  },
  {
    "month": "1905-03-01",
    "price": 9.05,
    "nominalPricePlusDividend": 50.8276,
    "realPrice": 340.1757,
    "realPricePlusDividend": 1903.2976
  },
  {
    "month": "1905-04-01",
    "price": 8.94,
    "nominalPricePlusDividend": 50.3573,
    "realPrice": 336.041,
    "realPricePlusDividend": 1885.7057
  },
  {
    "month": "1905-05-01",
    "price": 8.5,
    "nominalPricePlusDividend": 48.0275,
    "realPrice": 323.1753,
    "realPricePlusDividend": 1819.16
  },
  {
    "month": "1905-06-01",
    "price": 8.6,
    "nominalPricePlusDividend": 48.7424,
    "realPrice": 326.9773,
    "realPricePlusDividend": 1846.2605
  },
  {
    "month": "1905-07-01",
    "price": 8.87,
    "nominalPricePlusDividend": 50.4238,
    "realPrice": 337.2429,
    "realPricePlusDividend": 1909.9712
  },
  {
    "month": "1905-08-01",
    "price": 9.2,
    "nominalPricePlusDividend": 52.4522,
    "realPrice": 345.814,
    "realPricePlusDividend": 1964.2405
  },
  {
    "month": "1905-09-01",
    "price": 9.23,
    "nominalPricePlusDividend": 52.7768,
    "realPrice": 350.9303,
    "realPricePlusDividend": 1999.1416
  },
  {
    "month": "1905-10-01",
    "price": 9.36,
    "nominalPricePlusDividend": 53.675,
    "realPrice": 355.873,
    "realPricePlusDividend": 2033.1864
  },
  {
    "month": "1905-11-01",
    "price": 9.31,
    "nominalPricePlusDividend": 53.5444,
    "realPrice": 349.9487,
    "realPricePlusDividend": 2005.2063
  },
  {
    "month": "1905-12-01",
    "price": 9.54,
    "nominalPricePlusDividend": 55.0246,
    "realPrice": 354.5675,
    "realPricePlusDividend": 2037.5197
  },
  {
    "month": "1906-01-01",
    "price": 9.87,
    "nominalPricePlusDividend": 57.0866,
    "realPrice": 366.8324,
    "realPricePlusDividend": 2113.9676
  },
  {
    "month": "1906-02-01",
    "price": 9.8,
    "nominalPricePlusDividend": 56.8435,
    "realPrice": 364.2308,
    "realPricePlusDividend": 2105.0647
  },
  {
    "month": "1906-03-01",
    "price": 9.56,
    "nominalPricePlusDividend": 55.6166,
    "realPrice": 355.3109,
    "realPricePlusDividend": 2059.7232
  },
  {
    "month": "1906-04-01",
    "price": 9.43,
    "nominalPricePlusDividend": 55.0288,
    "realPrice": 350.4792,
    "realPricePlusDividend": 2038.0482
  },
  {
    "month": "1906-05-01",
    "price": 9.18,
    "nominalPricePlusDividend": 53.7417,
    "realPrice": 337.3959,
    "realPricePlusDividend": 1968.3559
  },
  {
    "month": "1906-06-01",
    "price": 9.3,
    "nominalPricePlusDividend": 54.6195,
    "realPrice": 341.8063,
    "realPricePlusDividend": 2000.5982
  },
  {
    "month": "1906-07-01",
    "price": 9.06,
    "nominalPricePlusDividend": 53.3886,
    "realPrice": 344.4668,
    "realPricePlusDividend": 2023.0366
  },
  {
    "month": "1906-08-01",
    "price": 9.73,
    "nominalPricePlusDividend": 57.5188,
    "realPrice": 361.6291,
    "realPricePlusDividend": 2130.672
  },
  {
    "month": "1906-09-01",
    "price": 10.03,
    "nominalPricePlusDividend": 59.4778,
    "realPrice": 368.6362,
    "realPricePlusDividend": 2178.8489
  },
  {
    "month": "1906-10-01",
    "price": 9.73,
    "nominalPricePlusDividend": 57.8879,
    "realPrice": 349.8345,
    "realPricePlusDividend": 2074.5863
  },
  {
    "month": "1906-11-01",
    "price": 9.93,
    "nominalPricePlusDividend": 59.2703,
    "realPrice": 353.1888,
    "realPricePlusDividend": 2101.3966
  },
  {
    "month": "1906-12-01",
    "price": 9.84,
    "nominalPricePlusDividend": 58.9291,
    "realPrice": 346.2637,
    "realPricePlusDividend": 2067.162
  },
  {
    "month": "1907-01-01",
    "price": 9.56,
    "nominalPricePlusDividend": 57.4519,
    "realPrice": 340.0287,
    "realPricePlusDividend": 2037.0656
  },
  {
    "month": "1907-02-01",
    "price": 9.26,
    "nominalPricePlusDividend": 55.851,
    "realPrice": 322.4231,
    "realPricePlusDividend": 1938.6517
  },
  {
    "month": "1907-03-01",
    "price": 8.35,
    "nominalPricePlusDividend": 50.5668,
    "realPrice": 293.8315,
    "realPricePlusDividend": 1773.9558
  },
  {
    "month": "1907-04-01",
    "price": 8.39,
    "nominalPricePlusDividend": 51.016,
    "realPrice": 295.239,
    "realPricePlusDividend": 1789.76
  },
  {
    "month": "1907-05-01",
    "price": 8.1,
    "nominalPricePlusDividend": 49.462,
    "realPrice": 279.0947,
    "realPricePlusDividend": 1699.1342
  },
  {
    "month": "1907-06-01",
    "price": 7.84,
    "nominalPricePlusDividend": 48.0864,
    "realPrice": 267.353,
    "realPricePlusDividend": 1634.9059
  },
  {
    "month": "1907-07-01",
    "price": 8.14,
    "nominalPricePlusDividend": 50.1411,
    "realPrice": 277.5833,
    "realPricePlusDividend": 1704.8112
  },
  {
    "month": "1907-08-01",
    "price": 7.53,
    "nominalPricePlusDividend": 46.6009,
    "realPrice": 256.7816,
    "realPricePlusDividend": 1584.4912
  },
  {
    "month": "1907-09-01",
    "price": 7.45,
    "nominalPricePlusDividend": 46.3259,
    "realPrice": 254.0535,
    "realPricePlusDividend": 1575.1863
  },
  {
    "month": "1907-10-01",
    "price": 6.64,
    "nominalPricePlusDividend": 41.5119,
    "realPrice": 224.1206,
    "realPricePlusDividend": 1397.141
  },
  {
    "month": "1907-11-01",
    "price": 6.25,
    "nominalPricePlusDividend": 39.2995,
    "realPrice": 219.9337,
    "realPricePlusDividend": 1379.0119
  },
  {
    "month": "1907-12-01",
    "price": 6.57,
    "nominalPricePlusDividend": 41.5404,
    "realPrice": 236.2192,
    "realPricePlusDividend": 1489.3775
  },
  {
    "month": "1908-01-01",
    "price": 6.85,
    "nominalPricePlusDividend": 43.5426,
    "realPrice": 248.9934,
    "realPricePlusDividend": 1578.2475
  },
  {
    "month": "1908-02-01",
    "price": 6.6,
    "nominalPricePlusDividend": 42.1848,
    "realPrice": 242.5722,
    "realPricePlusDividend": 1545.9462
  },
  {
    "month": "1908-03-01",
    "price": 6.87,
    "nominalPricePlusDividend": 44.1413,
    "realPrice": 252.4956,
    "realPricePlusDividend": 1617.5704
  },
  {
    "month": "1908-04-01",
    "price": 7.24,
    "nominalPricePlusDividend": 46.7489,
    "realPrice": 263.1696,
    "realPricePlusDividend": 1694.2198
  },
  {
    "month": "1908-05-01",
    "price": 7.63,
    "nominalPricePlusDividend": 49.4967,
    "realPrice": 277.3459,
    "realPricePlusDividend": 1793.7253
  },
  {
    "month": "1908-06-01",
    "price": 7.64,
    "nominalPricePlusDividend": 49.7905,
    "realPrice": 277.7094,
    "realPricePlusDividend": 1804.2921
  },
  {
    "month": "1908-07-01",
    "price": 7.92,
    "nominalPricePlusDividend": 51.8433,
    "realPrice": 284.7574,
    "realPricePlusDividend": 1858.1828
  },
  {
    "month": "1908-08-01",
    "price": 8.26,
    "nominalPricePlusDividend": 54.2962,
    "realPrice": 296.9818,
    "realPricePlusDividend": 1946.0219
  },
  {
    "month": "1908-09-01",
    "price": 8.17,
    "nominalPricePlusDividend": 53.931,
    "realPrice": 293.7459,
    "realPricePlusDividend": 1932.8558
  },
  {
    "month": "1908-10-01",
    "price": 8.27,
    "nominalPricePlusDividend": 54.8167,
    "realPrice": 294.1462,
    "realPricePlusDividend": 1943.4096
  },
  {
    "month": "1908-11-01",
    "price": 8.83,
    "nominalPricePlusDividend": 58.7532,
    "realPrice": 310.7224,
    "realPricePlusDividend": 2060.7299
  },
  {
    "month": "1908-12-01",
    "price": 9.03,
    "nominalPricePlusDividend": 60.3076,
    "realPrice": 314.4147,
    "realPricePlusDividend": 2092.9037
  },
  {
    "month": "1909-01-01",
    "price": 9.06,
    "nominalPricePlusDividend": 60.7306,
    "realPrice": 318.8159,
    "realPricePlusDividend": 2130.0611
  },
  {
    "month": "1909-02-01",
    "price": 8.8,
    "nominalPricePlusDividend": 59.213,
    "realPrice": 306.4064,
    "realPricePlusDividend": 2055.0233
  },
  {
    "month": "1909-03-01",
    "price": 8.92,
    "nominalPricePlusDividend": 60.2485,
    "realPrice": 310.5846,
    "realPricePlusDividend": 2091.0132
  },
  {
    "month": "1909-04-01",
    "price": 9.32,
    "nominalPricePlusDividend": 63.181,
    "realPrice": 317.8227,
    "realPricePlusDividend": 2147.6389
  },
  {
    "month": "1909-05-01",
    "price": 9.63,
    "nominalPricePlusDividend": 65.516,
    "realPrice": 325.0424,
    "realPricePlusDividend": 2204.3332
  },
  {
    "month": "1909-06-01",
    "price": 9.8,
    "nominalPricePlusDividend": 66.9088,
    "realPrice": 327.4385,
    "realPricePlusDividend": 2228.5018
  },
  {
    "month": "1909-07-01",
    "price": 9.94,
    "nominalPricePlusDividend": 68.1036,
    "realPrice": 332.1162,
    "realPricePlusDividend": 2268.3471
  },
  {
    "month": "1909-08-01",
    "price": 10.18,
    "nominalPricePlusDividend": 69.9897,
    "realPrice": 336.733,
    "realPricePlusDividend": 2307.9016
  },
  {
    "month": "1909-09-01",
    "price": 10.19,
    "nominalPricePlusDividend": 70.3029,
    "realPrice": 333.7287,
    "realPricePlusDividend": 2295.3418
  },
  {
    "month": "1909-10-01",
    "price": 10.23,
    "nominalPricePlusDividend": 70.8261,
    "realPrice": 328.5318,
    "realPricePlusDividend": 2267.5618
  },
  {
    "month": "1909-11-01",
    "price": 10.18,
    "nominalPricePlusDividend": 70.7299,
    "realPrice": 323.7819,
    "realPricePlusDividend": 2242.7546
  },
  {
    "month": "1909-12-01",
    "price": 10.3,
    "nominalPricePlusDividend": 71.8165,
    "realPrice": 324.4779,
    "realPricePlusDividend": 2255.5652
  },
  {
    "month": "1910-01-01",
    "price": 10.08,
    "nominalPricePlusDividend": 70.5382,
    "realPrice": 320.6013,
    "realPricePlusDividend": 2236.758
  },
  {
    "month": "1910-02-01",
    "price": 9.72,
    "nominalPricePlusDividend": 68.2771,
    "realPrice": 309.1512,
    "realPricePlusDividend": 2165.0903
  },
  {
    "month": "1910-03-01",
    "price": 9.96,
    "nominalPricePlusDividend": 70.2234,
    "realPrice": 310.8088,
    "realPricePlusDividend": 2184.8368
  },
  {
    "month": "1910-04-01",
    "price": 9.72,
    "nominalPricePlusDividend": 68.7942,
    "realPrice": 300.4841,
    "realPricePlusDividend": 2120.396
  },
  {
    "month": "1910-05-01",
    "price": 9.56,
    "nominalPricePlusDividend": 67.9272,
    "realPrice": 301.1659,
    "realPricePlusDividend": 2133.5773
  },
  {
    "month": "1910-06-01",
    "price": 9.1,
    "nominalPricePlusDividend": 64.9267,
    "realPrice": 289.4317,
    "realPricePlusDividend": 2058.9785
  },
  {
    "month": "1910-07-01",
    "price": 8.64,
    "nominalPricePlusDividend": 61.9152,
    "realPrice": 274.8011,
    "realPricePlusDividend": 1963.5117
  },
  {
    "month": "1910-08-01",
    "price": 8.85,
    "nominalPricePlusDividend": 63.6933,
    "realPrice": 284.2137,
    "realPricePlusDividend": 2039.5496
  },
  {
    "month": "1910-09-01",
    "price": 8.91,
    "nominalPricePlusDividend": 64.401,
    "realPrice": 288.9464,
    "realPricePlusDividend": 2082.4684
  },
  {
    "month": "1910-10-01",
    "price": 9.32,
    "nominalPricePlusDividend": 67.643,
    "realPrice": 311.4007,
    "realPricePlusDividend": 2253.6158
  },
  {
    "month": "1910-11-01",
    "price": 9.31,
    "nominalPricePlusDividend": 67.8517,
    "realPrice": 317.4816,
    "realPricePlusDividend": 2307.2242
  },
  {
    "month": "1910-12-01",
    "price": 9.05,
    "nominalPricePlusDividend": 66.2407,
    "realPrice": 308.6154,
    "realPricePlusDividend": 2252.4824
  },
  {
    "month": "1911-01-01",
    "price": 9.27,
    "nominalPricePlusDividend": 68.1377,
    "realPrice": 316.1176,
    "realPricePlusDividend": 2316.9727
  },
  {
    "month": "1911-02-01",
    "price": 9.43,
    "nominalPricePlusDividend": 69.6016,
    "realPrice": 331.836,
    "realPricePlusDividend": 2442.267
  },
  {
    "month": "1911-03-01",
    "price": 9.32,
    "nominalPricePlusDividend": 69.0788,
    "realPrice": 324.5122,
    "realPricePlusDividend": 2398.3868
  },
  {
    "month": "1911-04-01",
    "price": 9.28,
    "nominalPricePlusDividend": 69.0726,
    "realPrice": 333.6551,
    "realPricePlusDividend": 2476.3518
  },
  {
    "month": "1911-05-01",
    "price": 9.48,
    "nominalPricePlusDividend": 70.8528,
    "realPrice": 340.8459,
    "realPricePlusDividend": 2540.1575
  },
  {
    "month": "1911-06-01",
    "price": 9.67,
    "nominalPricePlusDividend": 72.5655,
    "realPrice": 347.6772,
    "realPricePlusDividend": 2601.5469
  },
  {
    "month": "1911-07-01",
    "price": 9.63,
    "nominalPricePlusDividend": 72.5593,
    "realPrice": 342.5185,
    "realPricePlusDividend": 2573.3539
  },
  {
    "month": "1911-08-01",
    "price": 9.17,
    "nominalPricePlusDividend": 69.3884,
    "realPrice": 315.9627,
    "realPricePlusDividend": 2383.9639
  },
  {
    "month": "1911-09-01",
    "price": 8.67,
    "nominalPricePlusDividend": 65.9014,
    "realPrice": 295.6569,
    "realPricePlusDividend": 2240.8172
  },
  {
    "month": "1911-10-01",
    "price": 8.72,
    "nominalPricePlusDividend": 66.5791,
    "realPrice": 297.362,
    "realPricePlusDividend": 2263.8479
  },
  {
    "month": "1911-11-01",
    "price": 9.07,
    "nominalPricePlusDividend": 69.5505,
    "realPrice": 312.5171,
    "realPricePlusDividend": 2389.4846
  },
  {
    "month": "1911-12-01",
    "price": 9.11,
    "nominalPricePlusDividend": 70.1576,
    "realPrice": 317.2002,
    "realPricePlusDividend": 2435.7027
  },
  {
    "month": "1912-01-01",
    "price": 9.12,
    "nominalPricePlusDividend": 70.5362,
    "realPrice": 314.2399,
    "realPricePlusDividend": 2423.3364
  },
  {
    "month": "1912-02-01",
    "price": 9.04,
    "nominalPricePlusDividend": 70.2209,
    "realPrice": 308.2743,
    "realPricePlusDividend": 2387.6531
  },
  {
    "month": "1912-03-01",
    "price": 9.3,
    "nominalPricePlusDividend": 72.5459,
    "realPrice": 310.7324,
    "realPricePlusDividend": 2416.866
  },
  {
    "month": "1912-04-01",
    "price": 9.59,
    "nominalPricePlusDividend": 75.1152,
    "realPrice": 310.9985,
    "realPricePlusDividend": 2428.8691
  },
  {
    "month": "1912-05-01",
    "price": 9.58,
    "nominalPricePlusDividend": 75.3458,
    "realPrice": 310.6742,
    "realPricePlusDividend": 2436.3299
  },
  {
    "month": "1912-06-01",
    "price": 9.58,
    "nominalPricePlusDividend": 75.6566,
    "realPrice": 313.7508,
    "realPricePlusDividend": 2470.6082
  },
  {
    "month": "1912-07-01",
    "price": 9.59,
    "nominalPricePlusDividend": 76.0482,
    "realPrice": 314.0783,
    "realPricePlusDividend": 2483.3974
  },
  {
    "month": "1912-08-01",
    "price": 9.81,
    "nominalPricePlusDividend": 78.1072,
    "realPrice": 318.133,
    "realPricePlusDividend": 2525.6282
  },
  {
    "month": "1912-09-01",
    "price": 9.86,
    "nominalPricePlusDividend": 78.8216,
    "realPrice": 316.6494,
    "realPricePlusDividend": 2523.9802
  },
  {
    "month": "1912-10-01",
    "price": 9.84,
    "nominalPricePlusDividend": 78.9798,
    "realPrice": 316.0071,
    "realPricePlusDividend": 2529.0484
  },
  {
    "month": "1912-11-01",
    "price": 9.73,
    "nominalPricePlusDividend": 78.4168,
    "realPrice": 312.4745,
    "realPricePlusDividend": 2511.0248
  },
  {
    "month": "1912-12-01",
    "price": 9.38,
    "nominalPricePlusDividend": 75.9179,
    "realPrice": 304.1883,
    "realPricePlusDividend": 2454.846
  },
  {
    "month": "1913-01-01",
    "price": 9.3,
    "nominalPricePlusDividend": 75.5941,
    "realPrice": 298.6652,
    "realPricePlusDividend": 2420.6254
  },
  {
    "month": "1913-02-01",
    "price": 8.97,
    "nominalPricePlusDividend": 73.2369,
    "realPrice": 288.0674,
    "realPricePlusDividend": 2345.1281
  },
  {
    "month": "1913-03-01",
    "price": 8.8,
    "nominalPricePlusDividend": 72.1755,
    "realPrice": 282.608,
    "realPricePlusDividend": 2311.1251
  },
  {
    "month": "1913-04-01",
    "price": 8.79,
    "nominalPricePlusDividend": 72.4216,
    "realPrice": 282.2868,
    "realPricePlusDividend": 2318.9884
  },
  {
    "month": "1913-05-01",
    "price": 8.55,
    "nominalPricePlusDividend": 70.7737,
    "realPrice": 277.41,
    "realPricePlusDividend": 2289.5714
  },
  {
    "month": "1913-06-01",
    "price": 8.12,
    "nominalPricePlusDividend": 67.5455,
    "realPrice": 260.7701,
    "realPricePlusDividend": 2162.8218
  },
  {
    "month": "1913-07-01",
    "price": 8.23,
    "nominalPricePlusDividend": 68.7932,
    "realPrice": 261.6329,
    "realPricePlusDividend": 2180.5094
  },
  {
    "month": "1913-08-01",
    "price": 8.45,
    "nominalPricePlusDividend": 70.9665,
    "realPrice": 268.6268,
    "realPricePlusDividend": 2249.3797
  },
  {
    "month": "1913-09-01",
    "price": 8.53,
    "nominalPricePlusDividend": 71.9743,
    "realPrice": 268.4583,
    "realPricePlusDividend": 2258.4947
  },
  {
    "month": "1913-10-01",
    "price": 8.26,
    "nominalPricePlusDividend": 70.0336,
    "realPrice": 259.9608,
    "realPricePlusDividend": 2197.5817
  },
  {
    "month": "1913-11-01",
    "price": 8.05,
    "nominalPricePlusDividend": 68.5923,
    "realPrice": 250.8432,
    "realPricePlusDividend": 2131.0269
  },
  {
    "month": "1913-12-01",
    "price": 8.04,
    "nominalPricePlusDividend": 68.8479,
    "realPrice": 253.0369,
    "realPricePlusDividend": 2160.3424
  },
  {
    "month": "1914-01-01",
    "price": 8.37,
    "nominalPricePlusDividend": 72.0163,
    "realPrice": 263.4227,
    "realPricePlusDividend": 2259.6333
  },
  {
    "month": "1914-02-01",
    "price": 8.48,
    "nominalPricePlusDividend": 73.3033,
    "realPrice": 269.5805,
    "realPricePlusDividend": 2323.1191
  },
  {
    "month": "1914-03-01",
    "price": 8.32,
    "nominalPricePlusDividend": 72.2588,
    "realPrice": 264.4941,
    "realPricePlusDividend": 2289.8865
  },
  {
    "month": "1914-04-01",
    "price": 8.12,
    "nominalPricePlusDividend": 70.8583,
    "realPrice": 260.7701,
    "realPricePlusDividend": 2268.2878
  },
  {
    "month": "1914-05-01",
    "price": 8.17,
    "nominalPricePlusDividend": 71.6292,
    "realPrice": 259.7255,
    "realPricePlusDividend": 2269.6713
  },
  {
    "month": "1914-06-01",
    "price": 8.13,
    "nominalPricePlusDividend": 71.6109,
    "realPrice": 258.4539,
    "realPricePlusDividend": 2268.9613
  },
  {
    "month": "1914-07-01",
    "price": 7.68,
    "nominalPricePlusDividend": 67.9775,
    "realPrice": 241.7069,
    "realPricePlusDividend": 2132.17
  },
  {
    "month": "1914-08-01",
    "price": 7.68,
    "nominalPricePlusDividend": 68.3057,
    "realPrice": 236.9675,
    "realPricePlusDividend": 2100.3279
  },
  {
    "month": "1914-09-01",
    "price": 7.68,
    "nominalPricePlusDividend": 68.6319,
    "realPrice": 236.9675,
    "realPricePlusDividend": 2110.2268
  },
  {
    "month": "1914-10-01",
    "price": 7.68,
    "nominalPricePlusDividend": 68.9558,
    "realPrice": 239.3137,
    "realPricePlusDividend": 2141.0488
  },
  {
    "month": "1914-11-01",
    "price": 7.68,
    "nominalPricePlusDividend": 69.2775,
    "realPrice": 236.9675,
    "realPricePlusDividend": 2129.8203
  },
  {
    "month": "1914-12-01",
    "price": 7.35,
    "nominalPricePlusDividend": 66.6202,
    "realPrice": 229.0307,
    "realPricePlusDividend": 2068.2736
  },
  {
    "month": "1915-01-01",
    "price": 7.48,
    "nominalPricePlusDividend": 68.1158,
    "realPrice": 233.0816,
    "realPricePlusDividend": 2114.7083
  },
  {
    "month": "1915-02-01",
    "price": 7.38,
    "nominalPricePlusDividend": 67.5245,
    "realPrice": 232.2652,
    "realPricePlusDividend": 2117.3206
  },
  {
    "month": "1915-03-01",
    "price": 7.57,
    "nominalPricePlusDividend": 69.5845,
    "realPrice": 240.6514,
    "realPricePlusDividend": 2203.9574
  },
  {
    "month": "1915-04-01",
    "price": 8.14,
    "nominalPricePlusDividend": 75.1476,
    "realPrice": 256.1841,
    "realPricePlusDividend": 2356.3625
  },
  {
    "month": "1915-05-01",
    "price": 7.95,
    "nominalPricePlusDividend": 73.7192,
    "realPrice": 247.7271,
    "realPricePlusDividend": 2288.6924
  },
  {
    "month": "1915-06-01",
    "price": 8.04,
    "nominalPricePlusDividend": 74.8816,
    "realPrice": 250.5316,
    "realPricePlusDividend": 2324.7829
  },
  {
    "month": "1915-07-01",
    "price": 8.01,
    "nominalPricePlusDividend": 74.932,
    "realPrice": 249.5968,
    "realPricePlusDividend": 2326.3531
  },
  {
    "month": "1915-08-01",
    "price": 8.35,
    "nominalPricePlusDividend": 78.4446,
    "realPrice": 260.1914,
    "realPricePlusDividend": 2435.4116
  },
  {
    "month": "1915-09-01",
    "price": 8.66,
    "nominalPricePlusDividend": 81.691,
    "realPrice": 269.8512,
    "realPricePlusDividend": 2536.2032
  },
  {
    "month": "1915-10-01",
    "price": 9.14,
    "nominalPricePlusDividend": 86.5549,
    "realPrice": 282.016,
    "realPricePlusDividend": 2660.87
  },
  {
    "month": "1915-11-01",
    "price": 9.46,
    "nominalPricePlusDividend": 89.9233,
    "realPrice": 289.0558,
    "realPricePlusDividend": 2737.5875
  },
  {
    "month": "1915-12-01",
    "price": 9.48,
    "nominalPricePlusDividend": 90.4534,
    "realPrice": 289.6669,
    "realPricePlusDividend": 2753.7295
  },
  {
    "month": "1916-01-01",
    "price": 9.33,
    "nominalPricePlusDividend": 89.3641,
    "realPrice": 282.3424,
    "realPricePlusDividend": 2694.6505
  },
  {
    "month": "1916-02-01",
    "price": 9.2,
    "nominalPricePlusDividend": 88.4707,
    "realPrice": 278.4084,
    "realPricePlusDividend": 2667.9598
  },
  {
    "month": "1916-03-01",
    "price": 9.17,
    "nominalPricePlusDividend": 88.5442,
    "realPrice": 274.8577,
    "realPricePlusDividend": 2644.9876
  },
  {
    "month": "1916-04-01",
    "price": 9.07,
    "nominalPricePlusDividend": 87.9508,
    "realPrice": 269.2956,
    "realPricePlusDividend": 2602.7156
  },
  {
    "month": "1916-05-01",
    "price": 9.27,
    "nominalPricePlusDividend": 90.2726,
    "realPrice": 272.6615,
    "realPricePlusDividend": 2646.7
  },
  {
    "month": "1916-06-01",
    "price": 9.36,
    "nominalPricePlusDividend": 91.542,
    "realPrice": 272.7595,
    "realPricePlusDividend": 2659.3027
  },
  {
    "month": "1916-07-01",
    "price": 9.23,
    "nominalPricePlusDividend": 90.674,
    "realPrice": 268.9712,
    "realPricePlusDividend": 2634.3255
  },
  {
    "month": "1916-08-01",
    "price": 9.3,
    "nominalPricePlusDividend": 91.7757,
    "realPrice": 268.5247,
    "realPricePlusDividend": 2642.1111
  },
  {
    "month": "1916-09-01",
    "price": 9.68,
    "nominalPricePlusDividend": 95.9506,
    "realPrice": 274.4607,
    "realPricePlusDividend": 2712.7628
  },
  {
    "month": "1916-10-01",
    "price": 9.98,
    "nominalPricePlusDividend": 99.36,
    "realPrice": 277.9585,
    "realPricePlusDividend": 2759.6649
  },
  {
    "month": "1916-11-01",
    "price": 10.21,
    "nominalPricePlusDividend": 102.0965,
    "realPrice": 279.4188,
    "realPricePlusDividend": 2786.5809
  },
  {
    "month": "1916-12-01",
    "price": 9.8,
    "nominalPricePlusDividend": 98.4543,
    "realPrice": 265.8863,
    "realPricePlusDividend": 2664.2314
  },
  {
    "month": "1917-01-01",
    "price": 9.57,
    "nominalPricePlusDividend": 96.6125,
    "realPrice": 257.4269,
    "realPricePlusDividend": 2592.2687
  },
  {
    "month": "1917-02-01",
    "price": 9.03,
    "nominalPricePlusDividend": 91.6412,
    "realPrice": 236.8287,
    "realPricePlusDividend": 2397.6299
  },
  {
    "month": "1917-03-01",
    "price": 9.31,
    "nominalPricePlusDividend": 94.9747,
    "realPrice": 244.1722,
    "realPricePlusDividend": 2485.0655
  },
  {
    "month": "1917-04-01",
    "price": 9.17,
    "nominalPricePlusDividend": 94.0502,
    "realPrice": 229.048,
    "realPricePlusDividend": 2343.9007
  },
  {
    "month": "1917-05-01",
    "price": 8.86,
    "nominalPricePlusDividend": 91.3864,
    "realPrice": 217.847,
    "realPricePlusDividend": 2242.1368
  },
  {
    "month": "1917-06-01",
    "price": 9.04,
    "nominalPricePlusDividend": 93.7709,
    "realPrice": 218.8532,
    "realPricePlusDividend": 2265.4512
  },
  {
    "month": "1917-07-01",
    "price": 8.79,
    "nominalPricePlusDividend": 91.718,
    "realPrice": 216.1258,
    "realPricePlusDividend": 2250.6844
  },
  {
    "month": "1917-08-01",
    "price": 8.53,
    "nominalPricePlusDividend": 89.5579,
    "realPrice": 206.5064,
    "realPricePlusDividend": 2164.0761
  },
  {
    "month": "1917-09-01",
    "price": 8.12,
    "nominalPricePlusDividend": 85.819,
    "realPrice": 192.1464,
    "realPricePlusDividend": 2027.1579
  },
  {
    "month": "1917-10-01",
    "price": 7.68,
    "nominalPricePlusDividend": 81.7478,
    "realPrice": 179.0421,
    "realPricePlusDividend": 1902.5843
  },
  {
    "month": "1917-11-01",
    "price": 7.04,
    "nominalPricePlusDividend": 75.5283,
    "realPrice": 164.122,
    "realPricePlusDividend": 1758.0364
  },
  {
    "month": "1917-12-01",
    "price": 6.8,
    "nominalPricePlusDividend": 73.5607,
    "realPrice": 156.2126,
    "realPricePlusDividend": 1687.4418
  },
  {
    "month": "1918-01-01",
    "price": 7.21,
    "nominalPricePlusDividend": 78.618,
    "realPrice": 162.0821,
    "realPricePlusDividend": 1764.5852
  },
  {
    "month": "1918-02-01",
    "price": 7.43,
    "nominalPricePlusDividend": 81.6348,
    "realPrice": 165.8431,
    "realPricePlusDividend": 1819.0793
  },
  {
    "month": "1918-03-01",
    "price": 7.28,
    "nominalPricePlusDividend": 80.6002,
    "realPrice": 163.6557,
    "realPricePlusDividend": 1808.6277
  },
  {
    "month": "1918-04-01",
    "price": 7.21,
    "nominalPricePlusDividend": 80.4341,
    "realPrice": 159.7992,
    "realPricePlusDividend": 1779.2561
  },
  {
    "month": "1918-05-01",
    "price": 7.44,
    "nominalPricePlusDividend": 83.6042,
    "realPrice": 161.4852,
    "realPricePlusDividend": 1810.898
  },
  {
    "month": "1918-06-01",
    "price": 7.45,
    "nominalPricePlusDividend": 84.3159,
    "realPrice": 159.5022,
    "realPricePlusDividend": 1801.2468
  },
  {
    "month": "1918-07-01",
    "price": 7.51,
    "nominalPricePlusDividend": 85.5891,
    "realPrice": 156.5275,
    "realPricePlusDividend": 1779.7969
  },
  {
    "month": "1918-08-01",
    "price": 7.58,
    "nominalPricePlusDividend": 86.9757,
    "realPrice": 154.9089,
    "realPricePlusDividend": 1773.1864
  },
  {
    "month": "1918-09-01",
    "price": 7.54,
    "nominalPricePlusDividend": 87.1001,
    "realPrice": 151.147,
    "realPricePlusDividend": 1741.5814
  },
  {
    "month": "1918-10-01",
    "price": 7.86,
    "nominalPricePlusDividend": 91.3742,
    "realPrice": 154.6074,
    "realPricePlusDividend": 1792.5811
  },
  {
    "month": "1918-11-01",
    "price": 8.06,
    "nominalPricePlusDividend": 94.2708,
    "realPrice": 155.6235,
    "realPricePlusDividend": 1815.1662
  },
  {
    "month": "1918-12-01",
    "price": 7.9,
    "nominalPricePlusDividend": 92.9647,
    "realPrice": 150.6853,
    "realPricePlusDividend": 1768.1198
  },
  {
    "month": "1919-01-01",
    "price": 7.85,
    "nominalPricePlusDividend": 92.9353,
    "realPrice": 149.7316,
    "realPricePlusDividend": 1767.483
  },
  {
    "month": "1919-02-01",
    "price": 7.88,
    "nominalPricePlusDividend": 93.8496,
    "realPrice": 153.0872,
    "realPricePlusDividend": 1817.843
  },
  {
    "month": "1919-03-01",
    "price": 8.12,
    "nominalPricePlusDividend": 97.267,
    "realPrice": 155.826,
    "realPricePlusDividend": 1860.9832
  },
  {
    "month": "1919-04-01",
    "price": 8.39,
    "nominalPricePlusDividend": 101.0603,
    "realPrice": 158.1151,
    "realPricePlusDividend": 1898.7465
  },
  {
    "month": "1919-05-01",
    "price": 8.97,
    "nominalPricePlusDividend": 108.6054,
    "realPrice": 167.045,
    "realPricePlusDividend": 2016.2789
  },
  {
    "month": "1919-06-01",
    "price": 9.21,
    "nominalPricePlusDividend": 112.0694,
    "realPrice": 171.5145,
    "realPricePlusDividend": 2080.5133
  },
  {
    "month": "1919-07-01",
    "price": 9.51,
    "nominalPricePlusDividend": 116.2776,
    "realPrice": 172.0121,
    "realPricePlusDividend": 2096.5311
  },
  {
    "month": "1919-08-01",
    "price": 8.87,
    "nominalPricePlusDividend": 109.0095,
    "realPrice": 157.7169,
    "realPricePlusDividend": 1932.0939
  },
  {
    "month": "1919-09-01",
    "price": 9.01,
    "nominalPricePlusDividend": 111.2864,
    "realPrice": 159.3062,
    "realPricePlusDividend": 1961.2959
  },
  {
    "month": "1919-10-01",
    "price": 9.47,
    "nominalPricePlusDividend": 117.5239,
    "realPrice": 164.6642,
    "realPricePlusDividend": 2036.8215
  },
  {
    "month": "1919-11-01",
    "price": 9.19,
    "nominalPricePlusDividend": 114.6041,
    "realPrice": 156.3405,
    "realPricePlusDividend": 1943.1994
  },
  {
    "month": "1919-12-01",
    "price": 8.92,
    "nominalPricePlusDividend": 111.7913,
    "realPrice": 148.5357,
    "realPricePlusDividend": 1855.3187
  },
  {
    "month": "1920-01-01",
    "price": 8.83,
    "nominalPricePlusDividend": 111.2169,
    "realPrice": 143.9896,
    "realPricePlusDividend": 1807.4888
  },
  {
    "month": "1920-02-01",
    "price": 8.1,
    "nominalPricePlusDividend": 102.5768,
    "realPrice": 130.7309,
    "realPricePlusDividend": 1649.9322
  },
  {
    "month": "1920-03-01",
    "price": 8.67,
    "nominalPricePlusDividend": 110.351,
    "realPrice": 138.5099,
    "realPricePlusDividend": 1756.9173
  },
  {
    "month": "1920-04-01",
    "price": 8.6,
    "nominalPricePlusDividend": 110.0169,
    "realPrice": 133.3307,
    "realPricePlusDividend": 1699.786
  },
  {
    "month": "1920-05-01",
    "price": 8.06,
    "nominalPricePlusDividend": 103.6667,
    "realPrice": 123.139,
    "realPricePlusDividend": 1578.3105
  },
  {
    "month": "1920-06-01",
    "price": 7.92,
    "nominalPricePlusDividend": 102.4252,
    "realPrice": 119.2633,
    "realPricePlusDividend": 1536.9853
  },
  {
    "month": "1920-07-01",
    "price": 7.91,
    "nominalPricePlusDividend": 102.8563,
    "realPrice": 119.6853,
    "realPricePlusDividend": 1550.8344
  },
  {
    "month": "1920-08-01",
    "price": 7.6,
    "nominalPricePlusDividend": 99.3869,
    "realPrice": 117.8271,
    "realPricePlusDividend": 1535.3938
  },
  {
    "month": "1920-09-01",
    "price": 7.87,
    "nominalPricePlusDividend": 103.4808,
    "realPrice": 123.8433,
    "realPricePlusDividend": 1622.577
  },
  {
    "month": "1920-10-01",
    "price": 7.88,
    "nominalPricePlusDividend": 104.1766,
    "realPrice": 124.6238,
    "realPricePlusDividend": 1641.6529
  },
  {
    "month": "1920-11-01",
    "price": 7.48,
    "nominalPricePlusDividend": 99.454,
    "realPrice": 118.8952,
    "realPricePlusDividend": 1575.1058
  },
  {
    "month": "1920-12-01",
    "price": 6.81,
    "nominalPricePlusDividend": 91.1126,
    "realPrice": 110.4773,
    "realPricePlusDividend": 1472.7079
  },
  {
    "month": "1921-01-01",
    "price": 7.11,
    "nominalPricePlusDividend": 95.695,
    "realPrice": 117.7725,
    "realPricePlusDividend": 1579.2484
  },
  {
    "month": "1921-02-01",
    "price": 7.06,
    "nominalPricePlusDividend": 95.5894,
    "realPrice": 120.7577,
    "realPricePlusDividend": 1628.8525
  },
  {
    "month": "1921-03-01",
    "price": 6.88,
    "nominalPricePlusDividend": 93.7183,
    "realPrice": 118.3219,
    "realPricePlusDividend": 1605.6007
  },
  {
    "month": "1921-04-01",
    "price": 6.91,
    "nominalPricePlusDividend": 94.6917,
    "realPrice": 120.151,
    "realPricePlusDividend": 1640.1058
  },
  {
    "month": "1921-05-01",
    "price": 7.12,
    "nominalPricePlusDividend": 98.1328,
    "realPrice": 126.6002,
    "realPricePlusDividend": 1738.0208
  },
  {
    "month": "1921-06-01",
    "price": 6.55,
    "nominalPricePlusDividend": 90.8385,
    "realPrice": 117.1268,
    "realPricePlusDividend": 1617.8732
  },
  {
    "month": "1921-07-01",
    "price": 6.53,
    "nominalPricePlusDividend": 91.1217,
    "realPrice": 116.1095,
    "realPricePlusDividend": 1613.6466
  },
  {
    "month": "1921-08-01",
    "price": 6.45,
    "nominalPricePlusDividend": 90.5644,
    "realPrice": 114.687,
    "realPricePlusDividend": 1603.6795
  },
  {
    "month": "1921-09-01",
    "price": 6.61,
    "nominalPricePlusDividend": 93.3688,
    "realPrice": 118.8752,
    "realPricePlusDividend": 1672.1302
  },
  {
    "month": "1921-10-01",
    "price": 6.7,
    "nominalPricePlusDividend": 95.1962,
    "realPrice": 120.4938,
    "realPricePlusDividend": 1704.7549
  },
  {
    "month": "1921-11-01",
    "price": 7.06,
    "nominalPricePlusDividend": 100.8657,
    "realPrice": 127.6978,
    "realPricePlusDividend": 1816.562
  },
  {
    "month": "1921-12-01",
    "price": 7.31,
    "nominalPricePlusDividend": 104.9901,
    "realPrice": 132.9839,
    "realPricePlusDividend": 1901.6656
  },
  {
    "month": "1922-01-01",
    "price": 7.3,
    "nominalPricePlusDividend": 105.3971,
    "realPrice": 135.9452,
    "realPricePlusDividend": 1954.2986
  },
  {
    "month": "1922-02-01",
    "price": 7.46,
    "nominalPricePlusDividend": 108.2657,
    "realPrice": 138.9248,
    "realPricePlusDividend": 2007.5645
  },
  {
    "month": "1922-03-01",
    "price": 7.74,
    "nominalPricePlusDividend": 112.8956,
    "realPrice": 145.8654,
    "realPricePlusDividend": 2118.5677
  },
  {
    "month": "1922-04-01",
    "price": 8.21,
    "nominalPricePlusDividend": 120.3253,
    "realPrice": 154.7229,
    "realPricePlusDividend": 2258.0718
  },
  {
    "month": "1922-05-01",
    "price": 8.53,
    "nominalPricePlusDividend": 125.5975,
    "realPrice": 160.7535,
    "realPricePlusDividend": 2357.0879
  },
  {
    "month": "1922-06-01",
    "price": 8.45,
    "nominalPricePlusDividend": 125.0095,
    "realPrice": 159.2458,
    "realPricePlusDividend": 2346.1332
  },
  {
    "month": "1922-07-01",
    "price": 8.51,
    "nominalPricePlusDividend": 126.495,
    "realPrice": 159.4219,
    "realPricePlusDividend": 2359.9626
  },
  {
    "month": "1922-08-01",
    "price": 8.83,
    "nominalPricePlusDividend": 131.8576,
    "realPrice": 167.4096,
    "realPricePlusDividend": 2489.7265
  },
  {
    "month": "1922-09-01",
    "price": 9.06,
    "nominalPricePlusDividend": 135.906,
    "realPrice": 171.7702,
    "realPricePlusDividend": 2566.2502
  },
  {
    "month": "1922-10-01",
    "price": 9.26,
    "nominalPricePlusDividend": 139.528,
    "realPrice": 174.5108,
    "realPricePlusDividend": 2618.9481
  },
  {
    "month": "1922-11-01",
    "price": 8.8,
    "nominalPricePlusDividend": 133.2268,
    "realPrice": 164.8546,
    "realPricePlusDividend": 2485.867
  },
  {
    "month": "1922-12-01",
    "price": 8.78,
    "nominalPricePlusDividend": 133.5621,
    "realPrice": 163.5067,
    "realPricePlusDividend": 2477.4583
  },
  {
    "month": "1923-01-01",
    "price": 8.9,
    "nominalPricePlusDividend": 136.0341,
    "realPrice": 166.728,
    "realPricePlusDividend": 2538.353
  },
  {
    "month": "1923-02-01",
    "price": 9.28,
    "nominalPricePlusDividend": 142.4941,
    "realPrice": 173.8467,
    "realPricePlusDividend": 2658.9137
  },
  {
    "month": "1923-03-01",
    "price": 9.43,
    "nominalPricePlusDividend": 145.4541,
    "realPrice": 176.6567,
    "realPricePlusDividend": 2714.1701
  },
  {
    "month": "1923-04-01",
    "price": 9.1,
    "nominalPricePlusDividend": 141.026,
    "realPrice": 169.466,
    "realPricePlusDividend": 2615.9919
  },
  {
    "month": "1923-05-01",
    "price": 8.67,
    "nominalPricePlusDividend": 135.0294,
    "realPrice": 161.4582,
    "realPricePlusDividend": 2504.777
  },
  {
    "month": "1923-06-01",
    "price": 8.34,
    "nominalPricePlusDividend": 130.5626,
    "realPrice": 154.3992,
    "realPricePlusDividend": 2407.6932
  },
  {
    "month": "1923-07-01",
    "price": 8.06,
    "nominalPricePlusDividend": 126.8575,
    "realPrice": 147.4804,
    "realPricePlusDividend": 2312.1894
  },
  {
    "month": "1923-08-01",
    "price": 8.1,
    "nominalPricePlusDividend": 128.1714,
    "realPrice": 149.0791,
    "realPricePlusDividend": 2349.8174
  },
  {
    "month": "1923-09-01",
    "price": 8.15,
    "nominalPricePlusDividend": 129.6526,
    "realPrice": 149.1272,
    "realPricePlusDividend": 2363.1758
  },
  {
    "month": "1923-10-01",
    "price": 8.03,
    "nominalPricePlusDividend": 128.4396,
    "realPrice": 146.0822,
    "realPricePlusDividend": 2327.5562
  },
  {
    "month": "1923-11-01",
    "price": 8.27,
    "nominalPricePlusDividend": 132.9804,
    "realPrice": 150.4483,
    "realPricePlusDividend": 2409.864
  },
  {
    "month": "1923-12-01",
    "price": 8.55,
    "nominalPricePlusDividend": 138.1907,
    "realPrice": 155.542,
    "realPricePlusDividend": 2504.3065
  },
  {
    "month": "1924-01-01",
    "price": 8.83,
    "nominalPricePlusDividend": 143.4301,
    "realPrice": 160.6358,
    "realPricePlusDividend": 2599.2775
  },
  {
    "month": "1924-02-01",
    "price": 8.87,
    "nominalPricePlusDividend": 144.7996,
    "realPrice": 162.3017,
    "realPricePlusDividend": 2639.3715
  },
  {
    "month": "1924-03-01",
    "price": 8.7,
    "nominalPricePlusDividend": 142.7499,
    "realPrice": 160.122,
    "realPricePlusDividend": 2617.2492
  },
  {
    "month": "1924-04-01",
    "price": 8.5,
    "nominalPricePlusDividend": 140.1998,
    "realPrice": 157.3613,
    "realPricePlusDividend": 2585.638
  },
  {
    "month": "1924-05-01",
    "price": 8.47,
    "nominalPricePlusDividend": 140.4427,
    "realPrice": 156.8059,
    "realPricePlusDividend": 2590.1375
  },
  {
    "month": "1924-06-01",
    "price": 8.63,
    "nominalPricePlusDividend": 143.8395,
    "realPrice": 159.768,
    "realPricePlusDividend": 2652.8063
  },
  {
    "month": "1924-07-01",
    "price": 9.03,
    "nominalPricePlusDividend": 151.2564,
    "realPrice": 166.1956,
    "realPricePlusDividend": 2773.3058
  },
  {
    "month": "1924-08-01",
    "price": 9.34,
    "nominalPricePlusDividend": 157.2052,
    "realPrice": 172.9122,
    "realPricePlusDividend": 2899.3529
  },
  {
    "month": "1924-09-01",
    "price": 9.25,
    "nominalPricePlusDividend": 156.4524,
    "realPrice": 170.2446,
    "realPricePlusDividend": 2868.618
  },
  {
    "month": "1924-10-01",
    "price": 9.13,
    "nominalPricePlusDividend": 155.1909,
    "realPrice": 167.0591,
    "realPricePlusDividend": 2828.9674
  },
  {
    "month": "1924-11-01",
    "price": 9.64,
    "nominalPricePlusDividend": 164.6343,
    "realPrice": 176.391,
    "realPricePlusDividend": 3001.1297
  },
  {
    "month": "1924-12-01",
    "price": 10.16,
    "nominalPricePlusDividend": 174.2953,
    "realPrice": 184.8312,
    "realPricePlusDividend": 3158.8983
  },
  {
    "month": "1925-01-01",
    "price": 10.58,
    "nominalPricePlusDividend": 182.2867,
    "realPrice": 192.4719,
    "realPricePlusDividend": 3303.8204
  },
  {
    "month": "1925-02-01",
    "price": 10.67,
    "nominalPricePlusDividend": 184.633,
    "realPrice": 195.2377,
    "realPricePlusDividend": 3365.8875
  },
  {
    "month": "1925-03-01",
    "price": 10.39,
    "nominalPricePlusDividend": 180.593,
    "realPrice": 189.0154,
    "realPricePlusDividend": 3273.2947
  },
  {
    "month": "1925-04-01",
    "price": 10.28,
    "nominalPricePlusDividend": 179.4958,
    "realPrice": 188.1016,
    "realPricePlusDividend": 3272.4114
  },
  {
    "month": "1925-05-01",
    "price": 10.61,
    "nominalPricePlusDividend": 186.0824,
    "realPrice": 193.0177,
    "realPricePlusDividend": 3372.9687
  },
  {
    "month": "1925-06-01",
    "price": 10.8,
    "nominalPricePlusDividend": 190.2489,
    "realPrice": 194.2287,
    "realPricePlusDividend": 3409.1685
  },
  {
    "month": "1925-07-01",
    "price": 11.1,
    "nominalPricePlusDividend": 196.3777,
    "realPrice": 197.3683,
    "realPricePlusDividend": 3479.3174
  },
  {
    "month": "1925-08-01",
    "price": 11.25,
    "nominalPricePlusDividend": 199.8854,
    "realPrice": 200.0355,
    "realPricePlusDividend": 3541.5489
  },
  {
    "month": "1925-09-01",
    "price": 11.51,
    "nominalPricePlusDividend": 205.3686,
    "realPrice": 204.6585,
    "realPricePlusDividend": 3638.7874
  },
  {
    "month": "1925-10-01",
    "price": 11.89,
    "nominalPricePlusDividend": 213.0224,
    "realPrice": 211.4153,
    "realPricePlusDividend": 3774.4863
  },
  {
    "month": "1925-11-01",
    "price": 12.26,
    "nominalPricePlusDividend": 220.5347,
    "realPrice": 214.361,
    "realPricePlusDividend": 3842.553
  },
  {
    "month": "1925-12-01",
    "price": 12.46,
    "nominalPricePlusDividend": 225.0255,
    "realPrice": 219.075,
    "realPricePlusDividend": 3942.7896
  },
  {
    "month": "1926-01-01",
    "price": 12.65,
    "nominalPricePlusDividend": 229.3598,
    "realPrice": 222.4156,
    "realPricePlusDividend": 4018.9081
  },
  {
    "month": "1926-02-01",
    "price": 12.67,
    "nominalPricePlusDividend": 230.6403,
    "realPrice": 222.7673,
    "realPricePlusDividend": 4041.52
  },
  {
    "month": "1926-03-01",
    "price": 11.81,
    "nominalPricePlusDividend": 215.9181,
    "realPrice": 208.8131,
    "realPricePlusDividend": 3804.9738
  },
  {
    "month": "1926-04-01",
    "price": 11.48,
    "nominalPricePlusDividend": 210.8333,
    "realPrice": 201.8444,
    "realPricePlusDividend": 3694.7858
  },
  {
    "month": "1926-05-01",
    "price": 11.56,
    "nominalPricePlusDividend": 213.2667,
    "realPrice": 204.3928,
    "realPricePlusDividend": 3758.6038
  },
  {
    "month": "1926-06-01",
    "price": 12.11,
    "nominalPricePlusDividend": 224.3935,
    "realPrice": 215.3271,
    "realPricePlusDividend": 3977.2243
  },
  {
    "month": "1926-07-01",
    "price": 12.62,
    "nominalPricePlusDividend": 234.8396,
    "realPrice": 226.9599,
    "realPricePlusDividend": 4210.1245
  },
  {
    "month": "1926-08-01",
    "price": 13.12,
    "nominalPricePlusDividend": 245.1557,
    "realPrice": 237.308,
    "realPricePlusDividend": 4420.5094
  },
  {
    "month": "1926-09-01",
    "price": 13.32,
    "nominalPricePlusDividend": 249.9205,
    "realPrice": 239.5488,
    "realPricePlusDividend": 4480.8569
  },
  {
    "month": "1926-10-01",
    "price": 13.02,
    "nominalPricePlusDividend": 245.3354,
    "realPrice": 232.8231,
    "realPricePlusDividend": 4373.8378
  },
  {
    "month": "1926-11-01",
    "price": 13.19,
    "nominalPricePlusDividend": 249.5986,
    "realPrice": 234.5305,
    "realPricePlusDividend": 4424.8826
  },
  {
    "month": "1926-12-01",
    "price": 13.49,
    "nominalPricePlusDividend": 256.3519,
    "realPrice": 239.8648,
    "realPricePlusDividend": 4544.7854
  },
  {
    "month": "1927-01-01",
    "price": 13.4,
    "nominalPricePlusDividend": 255.7343,
    "realPrice": 240.9875,
    "realPricePlusDividend": 4585.8122
  },
  {
    "month": "1927-02-01",
    "price": 13.66,
    "nominalPricePlusDividend": 261.8043,
    "realPrice": 247.0753,
    "realPricePlusDividend": 4721.7998
  },
  {
    "month": "1927-03-01",
    "price": 13.87,
    "nominalPricePlusDividend": 266.9524,
    "realPrice": 252.3238,
    "realPricePlusDividend": 4842.6424
  },
  {
    "month": "1927-04-01",
    "price": 14.21,
    "nominalPricePlusDividend": 274.635,
    "realPrice": 258.5091,
    "realPricePlusDividend": 4982.1734
  },
  {
    "month": "1927-05-01",
    "price": 14.7,
    "nominalPricePlusDividend": 285.2595,
    "realPrice": 265.8863,
    "realPricePlusDividend": 5145.3323
  },
  {
    "month": "1927-06-01",
    "price": 14.89,
    "nominalPricePlusDividend": 290.1162,
    "realPrice": 266.2624,
    "realPricePlusDividend": 5173.631
  },
  {
    "month": "1927-07-01",
    "price": 15.22,
    "nominalPricePlusDividend": 297.7312,
    "realPrice": 276.883,
    "realPricePlusDividend": 5401.6648
  },
  {
    "month": "1927-08-01",
    "price": 16.03,
    "nominalPricePlusDividend": 314.7772,
    "realPrice": 293.3141,
    "realPricePlusDividend": 5744.2932
  },
  {
    "month": "1927-09-01",
    "price": 16.94,
    "nominalPricePlusDividend": 333.863,
    "realPrice": 308.1734,
    "realPricePlusDividend": 6057.5335
  },
  {
    "month": "1927-10-01",
    "price": 16.68,
    "nominalPricePlusDividend": 329.9705,
    "realPrice": 301.6995,
    "realPricePlusDividend": 5952.6676
  },
  {
    "month": "1927-11-01",
    "price": 17.06,
    "nominalPricePlusDividend": 338.7353,
    "realPrice": 310.3564,
    "realPricePlusDividend": 6146.2698
  },
  {
    "month": "1927-12-01",
    "price": 17.46,
    "nominalPricePlusDividend": 347.9405,
    "realPrice": 317.6332,
    "realPricePlusDividend": 6313.4625
  },
  {
    "month": "1928-01-01",
    "price": 17.53,
    "nominalPricePlusDividend": 350.6141,
    "realPrice": 318.9067,
    "realPricePlusDividend": 6362.1437
  },
  {
    "month": "1928-02-01",
    "price": 17.32,
    "nominalPricePlusDividend": 347.7085,
    "realPrice": 318.7716,
    "realPricePlusDividend": 6383.3799
  },
  {
    "month": "1928-03-01",
    "price": 18.25,
    "nominalPricePlusDividend": 367.6892,
    "realPrice": 335.888,
    "realPricePlusDividend": 6750.3635
  },
  {
    "month": "1928-04-01",
    "price": 19.4,
    "nominalPricePlusDividend": 392.185,
    "realPrice": 357.0536,
    "realPricePlusDividend": 7200.2495
  },
  {
    "month": "1928-05-01",
    "price": 20,
    "nominalPricePlusDividend": 405.6566,
    "realPrice": 365.9564,
    "realPricePlusDividend": 7404.4451
  },
  {
    "month": "1928-06-01",
    "price": 19.02,
    "nominalPricePlusDividend": 387.1372,
    "realPrice": 350.0598,
    "realPricePlusDividend": 7107.9051
  },
  {
    "month": "1928-07-01",
    "price": 19.16,
    "nominalPricePlusDividend": 391.3607,
    "realPrice": 352.6364,
    "realPricePlusDividend": 7185.6201
  },
  {
    "month": "1928-08-01",
    "price": 19.78,
    "nominalPricePlusDividend": 405.415,
    "realPrice": 364.0474,
    "realPricePlusDividend": 7443.8323
  },
  {
    "month": "1928-09-01",
    "price": 21.17,
    "nominalPricePlusDividend": 435.3109,
    "realPrice": 385.1257,
    "realPricePlusDividend": 7900.5199
  },
  {
    "month": "1928-10-01",
    "price": 21.6,
    "nominalPricePlusDividend": 445.5751,
    "realPrice": 395.2329,
    "realPricePlusDividend": 8133.9929
  },
  {
    "month": "1928-11-01",
    "price": 23.06,
    "nominalPricePlusDividend": 477.131,
    "realPrice": 421.9477,
    "realPricePlusDividend": 8710.215
  },
  {
    "month": "1928-12-01",
    "price": 23.15,
    "nominalPricePlusDividend": 480.4472,
    "realPrice": 426.0717,
    "realPricePlusDividend": 8822.217
  },
  {
    "month": "1929-01-01",
    "price": 24.86,
    "nominalPricePlusDividend": 517.406,
    "realPrice": 457.5439,
    "realPricePlusDividend": 9501.1505
  },
  {
    "month": "1929-02-01",
    "price": 24.99,
    "nominalPricePlusDividend": 521.6032,
    "realPrice": 459.9366,
    "realPricePlusDividend": 9578.502
  },
  {
    "month": "1929-03-01",
    "price": 25.43,
    "nominalPricePlusDividend": 532.3004,
    "realPrice": 470.7878,
    "realPricePlusDividend": 9832.7188
  },
  {
    "month": "1929-04-01",
    "price": 25.28,
    "nominalPricePlusDividend": 530.6956,
    "realPrice": 470.7802,
    "realPricePlusDividend": 9861.3626
  },
  {
    "month": "1929-05-01",
    "price": 25.66,
    "nominalPricePlusDividend": 540.2298,
    "realPrice": 475.0458,
    "realPricePlusDividend": 9979.7562
  },
  {
    "month": "1929-06-01",
    "price": 26.15,
    "nominalPricePlusDividend": 552.1249,
    "realPrice": 481.2862,
    "realPricePlusDividend": 10140.1299
  },
  {
    "month": "1929-07-01",
    "price": 28.48,
    "nominalPricePlusDividend": 602.9211,
    "realPrice": 518.1096,
    "realPricePlusDividend": 10945.2986
  },
  {
    "month": "1929-08-01",
    "price": 30.1,
    "nominalPricePlusDividend": 638.8396,
    "realPrice": 547.5808,
    "realPricePlusDividend": 11597.6294
  },
  {
    "month": "1929-09-01",
    "price": 31.3,
    "nominalPricePlusDividend": 665.9531,
    "realPrice": 569.4112,
    "realPricePlusDividend": 12090.1306
  },
  {
    "month": "1929-10-01",
    "price": 27.99,
    "nominalPricePlusDividend": 597.1947,
    "realPrice": 509.1955,
    "realPricePlusDividend": 10842.1236
  },
  {
    "month": "1929-11-01",
    "price": 20.58,
    "nominalPricePlusDividend": 440.784,
    "realPrice": 374.3924,
    "realPricePlusDividend": 8002.7504
  },
  {
    "month": "1929-12-01",
    "price": 21.4,
    "nominalPricePlusDividend": 460.0603,
    "realPrice": 391.5733,
    "realPricePlusDividend": 8401.5661
  },
  {
    "month": "1930-01-01",
    "price": 21.71,
    "nominalPricePlusDividend": 468.4625,
    "realPrice": 399.5687,
    "realPricePlusDividend": 8605.0141
  },
  {
    "month": "1930-02-01",
    "price": 23.07,
    "nominalPricePlusDividend": 499.5545,
    "realPrice": 427.0969,
    "realPricePlusDividend": 9230.0909
  },
  {
    "month": "1930-03-01",
    "price": 23.94,
    "nominalPricePlusDividend": 520.1468,
    "realPrice": 445.8258,
    "realPricePlusDividend": 9667.4127
  },
  {
    "month": "1930-04-01",
    "price": 25.46,
    "nominalPricePlusDividend": 554.9327,
    "realPrice": 471.3432,
    "realPricePlusDividend": 10253.2508
  },
  {
    "month": "1930-05-01",
    "price": 23.94,
    "nominalPricePlusDividend": 523.5703,
    "realPrice": 445.8258,
    "realPricePlusDividend": 9731.0032
  },
  {
    "month": "1930-06-01",
    "price": 21.52,
    "nominalPricePlusDividend": 472.4201,
    "realPrice": 403.1445,
    "realPricePlusDividend": 8832.5752
  },
  {
    "month": "1930-07-01",
    "price": 21.06,
    "nominalPricePlusDividend": 464.1056,
    "realPrice": 399.2805,
    "realPricePlusDividend": 8781.6439
  },
  {
    "month": "1930-08-01",
    "price": 20.79,
    "nominalPricePlusDividend": 459.9475,
    "realPrice": 396.5504,
    "realPricePlusDividend": 8755.6922
  },
  {
    "month": "1930-09-01",
    "price": 20.78,
    "nominalPricePlusDividend": 461.5269,
    "realPrice": 393.9719,
    "realPricePlusDividend": 8732.8097
  },
  {
    "month": "1930-10-01",
    "price": 17.92,
    "nominalPricePlusDividend": 399.8151,
    "realPrice": 341.8077,
    "realPricePlusDividend": 7610.9518
  },
  {
    "month": "1930-11-01",
    "price": 16.62,
    "nominalPricePlusDividend": 372.6296,
    "realPrice": 318.9444,
    "realPricePlusDividend": 7136.6761
  },
  {
    "month": "1930-12-01",
    "price": 15.51,
    "nominalPricePlusDividend": 349.5723,
    "realPrice": 303.1892,
    "realPricePlusDividend": 6819.8072
  },
  {
    "month": "1931-01-01",
    "price": 15.98,
    "nominalPricePlusDividend": 362.006,
    "realPrice": 316.306,
    "realPricePlusDividend": 7150.6653
  },
  {
    "month": "1931-02-01",
    "price": 17.2,
    "nominalPricePlusDividend": 391.4685,
    "realPrice": 344.7915,
    "realPricePlusDividend": 7830.5791
  },
  {
    "month": "1931-03-01",
    "price": 17.53,
    "nominalPricePlusDividend": 400.7873,
    "realPrice": 353.6593,
    "realPricePlusDividend": 8067.8138
  },
  {
    "month": "1931-04-01",
    "price": 15.86,
    "nominalPricePlusDividend": 364.3971,
    "realPrice": 322.0322,
    "realPricePlusDividend": 7382.0406
  },
  {
    "month": "1931-05-01",
    "price": 14.33,
    "nominalPricePlusDividend": 331.0184,
    "realPrice": 294.7695,
    "realPricePlusDividend": 6792.9243
  },
  {
    "month": "1931-06-01",
    "price": 13.87,
    "nominalPricePlusDividend": 322.1506,
    "realPrice": 289.0862,
    "realPricePlusDividend": 6697.9224
  },
  {
    "month": "1931-07-01",
    "price": 14.33,
    "nominalPricePlusDividend": 334.5767,
    "realPrice": 298.6737,
    "realPricePlusDividend": 6955.6895
  },
  {
    "month": "1931-08-01",
    "price": 13.9,
    "nominalPricePlusDividend": 326.2623,
    "realPrice": 289.7114,
    "realPricePlusDividend": 6782.2422
  },
  {
    "month": "1931-09-01",
    "price": 11.83,
    "nominalPricePlusDividend": 279.3832,
    "realPrice": 248.2111,
    "realPricePlusDividend": 5845.8555
  },
  {
    "month": "1931-10-01",
    "price": 10.25,
    "nominalPricePlusDividend": 243.7617,
    "realPrice": 216.5037,
    "realPricePlusDividend": 5134.1329
  },
  {
    "month": "1931-11-01",
    "price": 10.39,
    "nominalPricePlusDividend": 248.7691,
    "realPrice": 222.4467,
    "realPricePlusDividend": 5310.2673
  },
  {
    "month": "1931-12-01",
    "price": 8.44,
    "nominalPricePlusDividend": 203.7426,
    "realPrice": 181.9355,
    "realPricePlusDividend": 4378.291
  },
  {
    "month": "1932-01-01",
    "price": 8.3,
    "nominalPricePlusDividend": 202.0126,
    "realPrice": 182.6711,
    "realPricePlusDividend": 4430.9554
  },
  {
    "month": "1932-02-01",
    "price": 8.23,
    "nominalPricePlusDividend": 201.9179,
    "realPrice": 183.6997,
    "realPricePlusDividend": 4490.4472
  },
  {
    "month": "1932-03-01",
    "price": 8.26,
    "nominalPricePlusDividend": 204.2215,
    "realPrice": 185.6863,
    "realPricePlusDividend": 4572.8438
  },
  {
    "month": "1932-04-01",
    "price": 6.28,
    "nominalPricePlusDividend": 156.7923,
    "realPrice": 142.1912,
    "realPricePlusDividend": 3534.7973
  },
  {
    "month": "1932-05-01",
    "price": 5.51,
    "nominalPricePlusDividend": 139.0518,
    "realPrice": 126.5782,
    "realPricePlusDividend": 3179.298
  },
  {
    "month": "1932-06-01",
    "price": 4.77,
    "nominalPricePlusDividend": 121.8211,
    "realPrice": 110.3843,
    "realPricePlusDividend": 2804.4729
  },
  {
    "month": "1932-07-01",
    "price": 5.01,
    "nominalPricePlusDividend": 129.3552,
    "realPrice": 115.9382,
    "realPricePlusDividend": 2976.5609
  },
  {
    "month": "1932-08-01",
    "price": 7.53,
    "nominalPricePlusDividend": 195.7826,
    "realPrice": 175.5452,
    "realPricePlusDividend": 4537.1075
  },
  {
    "month": "1932-09-01",
    "price": 8.26,
    "nominalPricePlusDividend": 216.0774,
    "realPrice": 194.0006,
    "realPricePlusDividend": 5043.3977
  },
  {
    "month": "1932-10-01",
    "price": 7.12,
    "nominalPricePlusDividend": 187.52,
    "realPrice": 168.483,
    "realPricePlusDividend": 4408.3446
  },
  {
    "month": "1932-11-01",
    "price": 7.05,
    "nominalPricePlusDividend": 186.8908,
    "realPrice": 168.0904,
    "realPricePlusDividend": 4425.4131
  },
  {
    "month": "1932-12-01",
    "price": 6.82,
    "nominalPricePlusDividend": 181.9571,
    "realPrice": 163.8479,
    "realPricePlusDividend": 4340.0329
  },
  {
    "month": "1933-01-01",
    "price": 7.09,
    "nominalPricePlusDividend": 190.2724,
    "realPrice": 172.9754,
    "realPricePlusDividend": 4608.4212
  },
  {
    "month": "1933-02-01",
    "price": 6.25,
    "nominalPricePlusDividend": 168.8366,
    "realPrice": 154.8831,
    "realPricePlusDividend": 4153.3249
  },
  {
    "month": "1933-03-01",
    "price": 6.23,
    "nominalPricePlusDividend": 169.3993,
    "realPrice": 155.6128,
    "realPricePlusDividend": 4199.9227
  },
  {
    "month": "1933-04-01",
    "price": 6.89,
    "nominalPricePlusDividend": 188.4443,
    "realPrice": 172.0983,
    "realPricePlusDividend": 4671.7841
  },
  {
    "month": "1933-05-01",
    "price": 8.87,
    "nominalPricePlusDividend": 243.6921,
    "realPrice": 221.5546,
    "realPricePlusDividend": 6041.1284
  },
  {
    "month": "1933-06-01",
    "price": 10.39,
    "nominalPricePlusDividend": 286.5397,
    "realPrice": 257.4777,
    "realPricePlusDividend": 7047.0678
  },
  {
    "month": "1933-07-01",
    "price": 11.23,
    "nominalPricePlusDividend": 310.7858,
    "realPrice": 269.7965,
    "realPricePlusDividend": 7409.6698
  },
  {
    "month": "1933-08-01",
    "price": 10.67,
    "nominalPricePlusDividend": 296.3604,
    "realPrice": 254.4007,
    "realPricePlusDividend": 7011.9051
  },
  {
    "month": "1933-09-01",
    "price": 10.58,
    "nominalPricePlusDividend": 294.9253,
    "realPrice": 252.2549,
    "realPricePlusDividend": 6977.6409
  },
  {
    "month": "1933-10-01",
    "price": 9.55,
    "nominalPricePlusDividend": 267.2703,
    "realPrice": 227.697,
    "realPricePlusDividend": 6323.0381
  },
  {
    "month": "1933-11-01",
    "price": 9.78,
    "nominalPricePlusDividend": 274.7566,
    "realPrice": 233.1808,
    "realPricePlusDividend": 6499.837
  },
  {
    "month": "1933-12-01",
    "price": 9.97,
    "nominalPricePlusDividend": 281.1362,
    "realPrice": 237.7109,
    "realPricePlusDividend": 6650.4446
  },
  {
    "month": "1934-01-01",
    "price": 10.54,
    "nominalPricePlusDividend": 298.2432,
    "realPrice": 251.3011,
    "realPricePlusDividend": 7055.127
  },
  {
    "month": "1934-02-01",
    "price": 11.32,
    "nominalPricePlusDividend": 321.3537,
    "realPrice": 267.8691,
    "realPricePlusDividend": 7544.6781
  },
  {
    "month": "1934-03-01",
    "price": 10.74,
    "nominalPricePlusDividend": 305.9335,
    "realPrice": 254.1443,
    "realPricePlusDividend": 7182.6536
  },
  {
    "month": "1934-04-01",
    "price": 10.92,
    "nominalPricePlusDividend": 312.1113,
    "realPrice": 258.4037,
    "realPricePlusDividend": 7327.7023
  },
  {
    "month": "1934-05-01",
    "price": 9.81,
    "nominalPricePlusDividend": 281.4415,
    "realPrice": 232.1374,
    "realPricePlusDividend": 6607.656
  },
  {
    "month": "1934-06-01",
    "price": 9.94,
    "nominalPricePlusDividend": 286.2331,
    "realPrice": 233.4583,
    "realPricePlusDividend": 6670.0096
  },
  {
    "month": "1934-07-01",
    "price": 9.47,
    "nominalPricePlusDividend": 273.7668,
    "realPrice": 222.4196,
    "realPricePlusDividend": 6379.5184
  },
  {
    "month": "1934-08-01",
    "price": 9.1,
    "nominalPricePlusDividend": 264.1445,
    "realPrice": 213.7295,
    "realPricePlusDividend": 6155.3054
  },
  {
    "month": "1934-09-01",
    "price": 8.88,
    "nominalPricePlusDividend": 258.8391,
    "realPrice": 205.4953,
    "realPricePlusDividend": 5942.9814
  },
  {
    "month": "1934-10-01",
    "price": 8.95,
    "nominalPricePlusDividend": 261.9665,
    "realPrice": 208.6494,
    "realPricePlusDividend": 6059.3483
  },
  {
    "month": "1934-11-01",
    "price": 9.2,
    "nominalPricePlusDividend": 270.3775,
    "realPrice": 214.4776,
    "realPricePlusDividend": 6253.9094
  },
  {
    "month": "1934-12-01",
    "price": 9.26,
    "nominalPricePlusDividend": 273.241,
    "realPrice": 217.4873,
    "realPricePlusDividend": 6367.3146
  },
  {
    "month": "1935-01-01",
    "price": 9.26,
    "nominalPricePlusDividend": 274.3475,
    "realPrice": 214.289,
    "realPricePlusDividend": 6299.0462
  },
  {
    "month": "1935-02-01",
    "price": 8.98,
    "nominalPricePlusDividend": 267.1629,
    "realPrice": 206.2926,
    "realPricePlusDividend": 6089.2754
  },
  {
    "month": "1935-03-01",
    "price": 8.41,
    "nominalPricePlusDividend": 251.3206,
    "realPrice": 193.1983,
    "realPricePlusDividend": 5728.153
  },
  {
    "month": "1935-04-01",
    "price": 9.04,
    "nominalPricePlusDividend": 271.2678,
    "realPrice": 206.166,
    "realPricePlusDividend": 6137.7673
  },
  {
    "month": "1935-05-01",
    "price": 9.75,
    "nominalPricePlusDividend": 293.6901,
    "realPrice": 222.3583,
    "realPricePlusDividend": 6644.8728
  },
  {
    "month": "1935-06-01",
    "price": 10.12,
    "nominalPricePlusDividend": 305.9481,
    "realPrice": 232.4811,
    "realPricePlusDividend": 6972.5148
  },
  {
    "month": "1935-07-01",
    "price": 10.65,
    "nominalPricePlusDividend": 323.0796,
    "realPrice": 244.6565,
    "realPricePlusDividend": 7362.9013
  },
  {
    "month": "1935-08-01",
    "price": 11.37,
    "nominalPricePlusDividend": 346.0339,
    "realPrice": 261.1967,
    "realPricePlusDividend": 7885.9868
  },
  {
    "month": "1935-09-01",
    "price": 11.61,
    "nominalPricePlusDividend": 354.454,
    "realPrice": 266.7101,
    "realPricePlusDividend": 8077.839
  },
  {
    "month": "1935-10-01",
    "price": 11.92,
    "nominalPricePlusDividend": 365.0377,
    "realPrice": 273.8315,
    "realPricePlusDividend": 8319.5788
  },
  {
    "month": "1935-11-01",
    "price": 13.04,
    "nominalPricePlusDividend": 400.485,
    "realPrice": 297.39,
    "realPricePlusDividend": 9061.8542
  },
  {
    "month": "1935-12-01",
    "price": 13.04,
    "nominalPricePlusDividend": 401.6623,
    "realPrice": 297.39,
    "realPricePlusDividend": 9089.0318
  },
  {
    "month": "1936-01-01",
    "price": 13.76,
    "nominalPricePlusDividend": 425.0464,
    "realPrice": 313.8103,
    "realPricePlusDividend": 9618.7191
  },
  {
    "month": "1936-02-01",
    "price": 14.55,
    "nominalPricePlusDividend": 450.685,
    "realPrice": 331.827,
    "realPricePlusDividend": 10199.4581
  },
  {
    "month": "1936-03-01",
    "price": 14.86,
    "nominalPricePlusDividend": 461.5521,
    "realPrice": 341.3705,
    "realPricePlusDividend": 10522.1785
  },
  {
    "month": "1936-04-01",
    "price": 14.88,
    "nominalPricePlusDividend": 463.4675,
    "realPrice": 341.83,
    "realPricePlusDividend": 10566.782
  },
  {
    "month": "1936-05-01",
    "price": 14.09,
    "nominalPricePlusDividend": 440.2024,
    "realPrice": 323.6818,
    "realPricePlusDividend": 10037.2913
  },
  {
    "month": "1936-06-01",
    "price": 14.69,
    "nominalPricePlusDividend": 460.3362,
    "realPrice": 335.0198,
    "realPricePlusDividend": 10421.2475
  },
  {
    "month": "1936-07-01",
    "price": 15.56,
    "nominalPricePlusDividend": 489.0354,
    "realPrice": 352.3081,
    "realPricePlusDividend": 10992.4267
  },
  {
    "month": "1936-08-01",
    "price": 15.87,
    "nominalPricePlusDividend": 500.2713,
    "realPrice": 356.7604,
    "realPricePlusDividend": 11165.7804
  },
  {
    "month": "1936-09-01",
    "price": 16.05,
    "nominalPricePlusDividend": 507.4953,
    "realPrice": 360.8069,
    "realPricePlusDividend": 11328.1365
  },
  {
    "month": "1936-10-01",
    "price": 16.89,
    "nominalPricePlusDividend": 535.6632,
    "realPrice": 379.6902,
    "realPricePlusDividend": 11958.9893
  },
  {
    "month": "1936-11-01",
    "price": 17.36,
    "nominalPricePlusDividend": 552.2782,
    "realPrice": 390.2559,
    "realPricePlusDividend": 12332.0331
  },
  {
    "month": "1936-12-01",
    "price": 17.06,
    "nominalPricePlusDividend": 544.5458,
    "realPrice": 383.5118,
    "realPricePlusDividend": 12161.4808
  },
  {
    "month": "1937-01-01",
    "price": 17.59,
    "nominalPricePlusDividend": 563.3783,
    "realPrice": 392.6219,
    "realPricePlusDividend": 12493.3625
  },
  {
    "month": "1937-02-01",
    "price": 18.11,
    "nominalPricePlusDividend": 581.9814,
    "realPrice": 404.2287,
    "realPricePlusDividend": 12906.4283
  },
  {
    "month": "1937-03-01",
    "price": 18.09,
    "nominalPricePlusDividend": 583.3204,
    "realPrice": 400.9387,
    "realPricePlusDividend": 12845.5473
  },
  {
    "month": "1937-04-01",
    "price": 17.01,
    "nominalPricePlusDividend": 550.5106,
    "realPrice": 374.3657,
    "realPricePlusDividend": 12039.9479
  },
  {
    "month": "1937-05-01",
    "price": 16.25,
    "nominalPricePlusDividend": 528.0177,
    "realPrice": 355.1556,
    "realPricePlusDividend": 11469.508
  },
  {
    "month": "1937-06-01",
    "price": 15.64,
    "nominalPricePlusDividend": 510.39,
    "realPrice": 341.8236,
    "realPricePlusDividend": 11088.294
  },
  {
    "month": "1937-07-01",
    "price": 16.57,
    "nominalPricePlusDividend": 543.0237,
    "realPrice": 359.6519,
    "realPricePlusDividend": 11714.4634
  },
  {
    "month": "1937-08-01",
    "price": 16.74,
    "nominalPricePlusDividend": 550.8251,
    "realPrice": 363.3417,
    "realPricePlusDividend": 11881.317
  },
  {
    "month": "1937-09-01",
    "price": 14.37,
    "nominalPricePlusDividend": 475.0163,
    "realPrice": 309.7645,
    "realPricePlusDividend": 10174.501
  },
  {
    "month": "1937-10-01",
    "price": 12.28,
    "nominalPricePlusDividend": 408.0501,
    "realPrice": 264.7118,
    "realPricePlusDividend": 8740.6564
  },
  {
    "month": "1937-11-01",
    "price": 11.2,
    "nominalPricePlusDividend": 374.3228,
    "realPrice": 243.096,
    "realPricePlusDividend": 8074.0248
  },
  {
    "month": "1937-12-01",
    "price": 11.02,
    "nominalPricePlusDividend": 370.5072,
    "realPrice": 240.8501,
    "realPricePlusDividend": 8047.7537
  },
  {
    "month": "1938-01-01",
    "price": 11.31,
    "nominalPricePlusDividend": 382.4988,
    "realPrice": 250.6698,
    "realPricePlusDividend": 8424.7554
  },
  {
    "month": "1938-02-01",
    "price": 11.04,
    "nominalPricePlusDividend": 375.6034,
    "realPrice": 246.421,
    "realPricePlusDividend": 8331.0627
  },
  {
    "month": "1938-03-01",
    "price": 10.31,
    "nominalPricePlusDividend": 352.9976,
    "realPrice": 230.1269,
    "realPricePlusDividend": 7829.164
  },
  {
    "month": "1938-04-01",
    "price": 9.89,
    "nominalPricePlusDividend": 340.843,
    "realPrice": 219.1976,
    "realPricePlusDividend": 7505.4397
  },
  {
    "month": "1938-05-01",
    "price": 9.98,
    "nominalPricePlusDividend": 346.1465,
    "realPrice": 222.761,
    "realPricePlusDividend": 7675.3624
  },
  {
    "month": "1938-06-01",
    "price": 10.21,
    "nominalPricePlusDividend": 356.3013,
    "realPrice": 227.8948,
    "realPricePlusDividend": 7899.6053
  },
  {
    "month": "1938-07-01",
    "price": 12.24,
    "nominalPricePlusDividend": 429.2947,
    "realPrice": 273.2059,
    "realPricePlusDividend": 9516.1663
  },
  {
    "month": "1938-08-01",
    "price": 12.31,
    "nominalPricePlusDividend": 433.8348,
    "realPrice": 274.7684,
    "realPricePlusDividend": 9615.0109
  },
  {
    "month": "1938-09-01",
    "price": 11.75,
    "nominalPricePlusDividend": 416.1156,
    "realPrice": 262.2688,
    "realPricePlusDividend": 9220.5051
  },
  {
    "month": "1938-10-01",
    "price": 13.06,
    "nominalPricePlusDividend": 464.4559,
    "realPrice": 293.5911,
    "realPricePlusDividend": 10361.8121
  },
  {
    "month": "1938-11-01",
    "price": 13.07,
    "nominalPricePlusDividend": 466.6193,
    "realPrice": 293.8159,
    "realPricePlusDividend": 10406.7165
  },
  {
    "month": "1938-12-01",
    "price": 12.69,
    "nominalPricePlusDividend": 454.7188,
    "realPrice": 285.2735,
    "realPricePlusDividend": 10137.9388
  },
  {
    "month": "1939-01-01",
    "price": 12.5,
    "nominalPricePlusDividend": 449.4334,
    "realPrice": 281.0022,
    "realPricePlusDividend": 10020.2733
  },
  {
    "month": "1939-02-01",
    "price": 12.4,
    "nominalPricePlusDividend": 447.376,
    "realPrice": 280.7596,
    "realPricePlusDividend": 10046.3336
  },
  {
    "month": "1939-03-01",
    "price": 12.39,
    "nominalPricePlusDividend": 448.5686,
    "realPrice": 280.5332,
    "realPricePlusDividend": 10073.2876
  },
  {
    "month": "1939-04-01",
    "price": 10.83,
    "nominalPricePlusDividend": 393.6591,
    "realPrice": 246.9887,
    "realPricePlusDividend": 8904.4449
  },
  {
    "month": "1939-05-01",
    "price": 11.23,
    "nominalPricePlusDividend": 409.7839,
    "realPrice": 256.1111,
    "realPricePlusDividend": 9269.3574
  },
  {
    "month": "1939-06-01",
    "price": 11.43,
    "nominalPricePlusDividend": 418.6834,
    "realPrice": 260.6723,
    "realPricePlusDividend": 9470.8409
  },
  {
    "month": "1939-07-01",
    "price": 11.71,
    "nominalPricePlusDividend": 430.5577,
    "realPrice": 267.058,
    "realPricePlusDividend": 9740.0788
  },
  {
    "month": "1939-08-01",
    "price": 11.54,
    "nominalPricePlusDividend": 425.9617,
    "realPrice": 263.181,
    "realPricePlusDividend": 9636.7435
  },
  {
    "month": "1939-09-01",
    "price": 12.77,
    "nominalPricePlusDividend": 473.0549,
    "realPrice": 285.0359,
    "realPricePlusDividend": 10475.0765
  },
  {
    "month": "1939-10-01",
    "price": 12.9,
    "nominalPricePlusDividend": 479.5994,
    "realPrice": 289.9943,
    "realPricePlusDividend": 10697.1686
  },
  {
    "month": "1939-11-01",
    "price": 12.67,
    "nominalPricePlusDividend": 472.8454,
    "realPrice": 284.8239,
    "realPricePlusDividend": 10547.8441
  },
  {
    "month": "1939-12-01",
    "price": 12.37,
    "nominalPricePlusDividend": 463.5153,
    "realPrice": 278.0798,
    "realPricePlusDividend": 10341.0413
  },
  {
    "month": "1940-01-01",
    "price": 12.3,
    "nominalPricePlusDividend": 462.8284,
    "realPrice": 278.4954,
    "realPricePlusDividend": 10400.1696
  },
  {
    "month": "1940-02-01",
    "price": 12.22,
    "nominalPricePlusDividend": 461.7727,
    "realPrice": 274.7078,
    "realPricePlusDividend": 10302.498
  },
  {
    "month": "1940-03-01",
    "price": 12.15,
    "nominalPricePlusDividend": 461.1009,
    "realPrice": 273.1342,
    "realPricePlusDividend": 10287.6782
  },
  {
    "month": "1940-04-01",
    "price": 12.27,
    "nominalPricePlusDividend": 467.6474,
    "realPrice": 275.8318,
    "realPricePlusDividend": 10434.1415
  },
  {
    "month": "1940-05-01",
    "price": 10.58,
    "nominalPricePlusDividend": 405.2584,
    "realPrice": 237.8403,
    "realPricePlusDividend": 9042.5241
  },
  {
    "month": "1940-06-01",
    "price": 9.67,
    "nominalPricePlusDividend": 372.4551,
    "realPrice": 215.8416,
    "realPricePlusDividend": 8252.0476
  },
  {
    "month": "1940-07-01",
    "price": 9.99,
    "nominalPricePlusDividend": 386.8667,
    "realPrice": 224.577,
    "realPricePlusDividend": 8632.9802
  },
  {
    "month": "1940-08-01",
    "price": 10.2,
    "nominalPricePlusDividend": 397.1182,
    "realPrice": 229.2978,
    "realPricePlusDividend": 8862.1521
  },
  {
    "month": "1940-09-01",
    "price": 10.63,
    "nominalPricePlusDividend": 416.0116,
    "realPrice": 238.9643,
    "realPricePlusDividend": 9284.1907
  },
  {
    "month": "1940-10-01",
    "price": 10.73,
    "nominalPricePlusDividend": 422.1102,
    "realPrice": 241.2123,
    "realPricePlusDividend": 9420.2222
  },
  {
    "month": "1940-11-01",
    "price": 10.98,
    "nominalPricePlusDividend": 434.1415,
    "realPrice": 246.8324,
    "realPricePlusDividend": 9688.6505
  },
  {
    "month": "1940-12-01",
    "price": 10.53,
    "nominalPricePlusDividend": 418.5564,
    "realPrice": 235.0374,
    "realPricePlusDividend": 9274.5217
  },
  {
    "month": "1941-01-01",
    "price": 10.55,
    "nominalPricePlusDividend": 421.5707,
    "realPrice": 235.4839,
    "realPricePlusDividend": 9341.4846
  },
  {
    "month": "1941-02-01",
    "price": 9.89,
    "nominalPricePlusDividend": 397.4397,
    "realPrice": 220.7522,
    "realPricePlusDividend": 8806.9437
  },
  {
    "month": "1941-03-01",
    "price": 9.95,
    "nominalPricePlusDividend": 402.1169,
    "realPrice": 220.5274,
    "realPricePlusDividend": 8848.0073
  },
  {
    "month": "1941-04-01",
    "price": 9.64,
    "nominalPricePlusDividend": 391.8788,
    "realPrice": 212.1626,
    "realPricePlusDividend": 8562.6031
  },
  {
    "month": "1941-05-01",
    "price": 9.43,
    "nominalPricePlusDividend": 385.6569,
    "realPrice": 206.0995,
    "realPricePlusDividend": 8368.3051
  },
  {
    "month": "1941-06-01",
    "price": 9.76,
    "nominalPricePlusDividend": 401.493,
    "realPrice": 208.9586,
    "realPricePlusDividend": 8534.3037
  },
  {
    "month": "1941-07-01",
    "price": 10.26,
    "nominalPricePlusDividend": 424.4267,
    "realPrice": 219.6635,
    "realPricePlusDividend": 9021.9586
  },
  {
    "month": "1941-08-01",
    "price": 10.21,
    "nominalPricePlusDividend": 424.7484,
    "realPrice": 215.6588,
    "realPricePlusDividend": 8907.7721
  },
  {
    "month": "1941-09-01",
    "price": 10.24,
    "nominalPricePlusDividend": 428.4116,
    "realPrice": 213.4277,
    "realPricePlusDividend": 8865.7598
  },
  {
    "month": "1941-10-01",
    "price": 9.83,
    "nominalPricePlusDividend": 413.6989,
    "realPrice": 202.2041,
    "realPricePlusDividend": 8449.5385
  },
  {
    "month": "1941-11-01",
    "price": 9.37,
    "nominalPricePlusDividend": 396.8063,
    "realPrice": 191.4902,
    "realPricePlusDividend": 8052.0538
  },
  {
    "month": "1941-12-01",
    "price": 8.76,
    "nominalPricePlusDividend": 373.4676,
    "realPrice": 177.869,
    "realPricePlusDividend": 7529.7285
  },
  {
    "month": "1942-01-01",
    "price": 8.93,
    "nominalPricePlusDividend": 383.2377,
    "realPrice": 179.011,
    "realPricePlusDividend": 7627.7357
  },
  {
    "month": "1942-02-01",
    "price": 8.65,
    "nominalPricePlusDividend": 373.7366,
    "realPrice": 172.3006,
    "realPricePlusDividend": 7391.0073
  },
  {
    "month": "1942-03-01",
    "price": 8.18,
    "nominalPricePlusDividend": 355.9379,
    "realPrice": 160.9019,
    "realPricePlusDividend": 6950.492
  },
  {
    "month": "1942-04-01",
    "price": 7.84,
    "nominalPricePlusDividend": 343.6454,
    "realPrice": 153.2562,
    "realPricePlusDividend": 6667.9989
  },
  {
    "month": "1942-05-01",
    "price": 7.93,
    "nominalPricePlusDividend": 350.0742,
    "realPrice": 153.1135,
    "realPricePlusDividend": 6708.6241
  },
  {
    "month": "1942-06-01",
    "price": 8.33,
    "nominalPricePlusDividend": 370.1972,
    "realPrice": 160.8367,
    "realPricePlusDividend": 7093.4759
  },
  {
    "month": "1942-07-01",
    "price": 8.64,
    "nominalPricePlusDividend": 386.4183,
    "realPrice": 165.805,
    "realPricePlusDividend": 7358.1382
  },
  {
    "month": "1942-08-01",
    "price": 8.59,
    "nominalPricePlusDividend": 386.5922,
    "realPrice": 163.8464,
    "realPricePlusDividend": 7315.8282
  },
  {
    "month": "1942-09-01",
    "price": 8.68,
    "nominalPricePlusDividend": 393.0179,
    "realPrice": 165.5631,
    "realPricePlusDividend": 7436.4158
  },
  {
    "month": "1942-10-01",
    "price": 9.32,
    "nominalPricePlusDividend": 424.3356,
    "realPrice": 175.6415,
    "realPricePlusDividend": 7932.0624
  },
  {
    "month": "1942-11-01",
    "price": 9.47,
    "nominalPricePlusDividend": 433.4795,
    "realPrice": 177.4061,
    "realPricePlusDividend": 8053.9876
  },
  {
    "month": "1942-12-01",
    "price": 9.52,
    "nominalPricePlusDividend": 438.0569,
    "realPrice": 177.2875,
    "realPricePlusDividend": 8090.1087
  },
  {
    "month": "1943-01-01",
    "price": 10.09,
    "nominalPricePlusDividend": 466.5474,
    "realPrice": 187.9024,
    "realPricePlusDividend": 8616.2152
  },
  {
    "month": "1943-02-01",
    "price": 10.69,
    "nominalPricePlusDividend": 496.564,
    "realPrice": 199.0759,
    "realPricePlusDividend": 9170.4996
  },
  {
    "month": "1943-03-01",
    "price": 11.07,
    "nominalPricePlusDividend": 516.4993,
    "realPrice": 202.5569,
    "realPricePlusDividend": 9372.2299
  },
  {
    "month": "1943-04-01",
    "price": 11.44,
    "nominalPricePlusDividend": 536.0566,
    "realPrice": 206.921,
    "realPricePlusDividend": 9615.2433
  },
  {
    "month": "1943-05-01",
    "price": 11.89,
    "nominalPricePlusDividend": 559.4466,
    "realPrice": 213.8315,
    "realPricePlusDividend": 9977.3867
  },
  {
    "month": "1943-06-01",
    "price": 12.1,
    "nominalPricePlusDividend": 571.6409,
    "realPrice": 217.6081,
    "realPricePlusDividend": 10194.8028
  },
  {
    "month": "1943-07-01",
    "price": 12.35,
    "nominalPricePlusDividend": 585.7745,
    "realPrice": 223.3806,
    "realPricePlusDividend": 10507.0769
  },
  {
    "month": "1943-08-01",
    "price": 11.74,
    "nominalPricePlusDividend": 559.1867,
    "realPrice": 213.5747,
    "realPricePlusDividend": 10088.3223
  },
  {
    "month": "1943-09-01",
    "price": 11.99,
    "nominalPricePlusDividend": 573.4627,
    "realPrice": 216.8691,
    "realPricePlusDividend": 10286.5919
  },
  {
    "month": "1943-10-01",
    "price": 11.88,
    "nominalPricePlusDividend": 570.593,
    "realPrice": 214.8795,
    "realPricePlusDividend": 10235.2902
  },
  {
    "month": "1943-11-01",
    "price": 11.33,
    "nominalPricePlusDividend": 546.5915,
    "realPrice": 204.9314,
    "realPricePlusDividend": 9804.9259
  },
  {
    "month": "1943-12-01",
    "price": 11.48,
    "nominalPricePlusDividend": 556.2669,
    "realPrice": 207.6445,
    "realPricePlusDividend": 9978.6606
  },
  {
    "month": "1944-01-01",
    "price": 11.85,
    "nominalPricePlusDividend": 576.6585,
    "realPrice": 214.3369,
    "realPricePlusDividend": 10344.6333
  },
  {
    "month": "1944-02-01",
    "price": 11.77,
    "nominalPricePlusDividend": 575.2526,
    "realPrice": 212.8899,
    "realPricePlusDividend": 10319.5901
  },
  {
    "month": "1944-03-01",
    "price": 12.1,
    "nominalPricePlusDividend": 593.8928,
    "realPrice": 218.8588,
    "realPricePlusDividend": 10654.1569
  },
  {
    "month": "1944-04-01",
    "price": 11.89,
    "nominalPricePlusDividend": 586.1215,
    "realPrice": 213.8315,
    "realPricePlusDividend": 10454.8343
  },
  {
    "month": "1944-05-01",
    "price": 12.1,
    "nominalPricePlusDividend": 599.0341,
    "realPrice": 217.6081,
    "realPricePlusDividend": 10685.3371
  },
  {
    "month": "1944-06-01",
    "price": 12.67,
    "nominalPricePlusDividend": 629.8385,
    "realPrice": 226.5644,
    "realPricePlusDividend": 11171.1538
  },
  {
    "month": "1944-07-01",
    "price": 13,
    "nominalPricePlusDividend": 648.8529,
    "realPrice": 231.1521,
    "realPricePlusDividend": 11443.56
  },
  {
    "month": "1944-08-01",
    "price": 12.81,
    "nominalPricePlusDividend": 642.0039,
    "realPrice": 227.7737,
    "realPricePlusDividend": 11322.9419
  },
  {
    "month": "1944-09-01",
    "price": 12.6,
    "nominalPricePlusDividend": 634.1383,
    "realPrice": 224.0397,
    "realPricePlusDividend": 11184.3919
  },
  {
    "month": "1944-10-01",
    "price": 12.91,
    "nominalPricePlusDividend": 652.4243,
    "realPrice": 229.5518,
    "realPricePlusDividend": 11506.8344
  },
  {
    "month": "1944-11-01",
    "price": 12.82,
    "nominalPricePlusDividend": 650.5713,
    "realPrice": 227.9516,
    "realPricePlusDividend": 11474.0823
  },
  {
    "month": "1944-12-01",
    "price": 13.1,
    "nominalPricePlusDividend": 667.4868,
    "realPrice": 231.6216,
    "realPricePlusDividend": 11706.2126
  },
  {
    "month": "1945-01-01",
    "price": 13.49,
    "nominalPricePlusDividend": 690.076,
    "realPrice": 238.5172,
    "realPricePlusDividend": 12102.554
  },
  {
    "month": "1945-02-01",
    "price": 13.94,
    "nominalPricePlusDividend": 715.8381,
    "realPrice": 246.4737,
    "realPricePlusDividend": 12554.5461
  },
  {
    "month": "1945-03-01",
    "price": 13.93,
    "nominalPricePlusDividend": 718.0918,
    "realPrice": 246.2969,
    "realPricePlusDividend": 12594.2506
  },
  {
    "month": "1945-04-01",
    "price": 14.28,
    "nominalPricePlusDividend": 738.9266,
    "realPrice": 252.4852,
    "realPricePlusDividend": 12959.5889
  },
  {
    "month": "1945-05-01",
    "price": 14.82,
    "nominalPricePlusDividend": 769.6721,
    "realPrice": 260.5691,
    "realPricePlusDividend": 13423.3304
  },
  {
    "month": "1945-06-01",
    "price": 15.09,
    "nominalPricePlusDividend": 786.5076,
    "realPrice": 262.3847,
    "realPricePlusDividend": 13565.3063
  },
  {
    "month": "1945-07-01",
    "price": 14.78,
    "nominalPricePlusDividend": 773.1733,
    "realPrice": 256.9944,
    "realPricePlusDividend": 13335.4992
  },
  {
    "month": "1945-08-01",
    "price": 14.83,
    "nominalPricePlusDividend": 778.637,
    "realPrice": 257.8638,
    "realPricePlusDividend": 13429.9132
  },
  {
    "month": "1945-09-01",
    "price": 15.84,
    "nominalPricePlusDividend": 834.5394,
    "realPrice": 275.4257,
    "realPricePlusDividend": 14394.2934
  },
  {
    "month": "1945-10-01",
    "price": 16.5,
    "nominalPricePlusDividend": 872.2096,
    "realPrice": 286.9017,
    "realPricePlusDividend": 15043.9615
  },
  {
    "month": "1945-11-01",
    "price": 17.04,
    "nominalPricePlusDividend": 903.662,
    "realPrice": 296.2912,
    "realPricePlusDividend": 15586.3813
  },
  {
    "month": "1945-12-01",
    "price": 17.33,
    "nominalPricePlusDividend": 921.958,
    "realPrice": 299.6781,
    "realPricePlusDividend": 15814.5029
  },
  {
    "month": "1946-01-01",
    "price": 18.02,
    "nominalPricePlusDividend": 961.592,
    "realPrice": 311.6099,
    "realPricePlusDividend": 16494.7848
  },
  {
    "month": "1946-02-01",
    "price": 18.07,
    "nominalPricePlusDividend": 967.2247,
    "realPrice": 314.2009,
    "realPricePlusDividend": 16683.5058
  },
  {
    "month": "1946-03-01",
    "price": 17.53,
    "nominalPricePlusDividend": 941.3238,
    "realPrice": 301.4801,
    "realPricePlusDividend": 16059.7249
  },
  {
    "month": "1946-04-01",
    "price": 18.66,
    "nominalPricePlusDividend": 1005.0453,
    "realPrice": 319.1697,
    "realPricePlusDividend": 17053.5973
  },
  {
    "month": "1946-05-01",
    "price": 18.7,
    "nominalPricePlusDividend": 1010.2519,
    "realPrice": 318.1249,
    "realPricePlusDividend": 17049.2064
  },
  {
    "month": "1946-06-01",
    "price": 18.58,
    "nominalPricePlusDividend": 1006.8304,
    "realPrice": 312.7029,
    "realPricePlusDividend": 16809.6611
  },
  {
    "month": "1946-07-01",
    "price": 18.05,
    "nominalPricePlusDividend": 981.1809,
    "realPrice": 286.9061,
    "realPricePlusDividend": 15471.5135
  },
  {
    "month": "1946-08-01",
    "price": 17.7,
    "nominalPricePlusDividend": 965.2507,
    "realPrice": 275.7717,
    "realPricePlusDividend": 14919.091
  },
  {
    "month": "1946-09-01",
    "price": 15.09,
    "nominalPricePlusDividend": 826.0377,
    "realPrice": 232.8021,
    "realPricePlusDividend": 12642.3791
  },
  {
    "month": "1946-10-01",
    "price": 14.75,
    "nominalPricePlusDividend": 810.5734,
    "realPrice": 223.1806,
    "realPricePlusDividend": 12167.5154
  },
  {
    "month": "1946-11-01",
    "price": 14.69,
    "nominalPricePlusDividend": 810.4666,
    "realPrice": 217.0551,
    "realPricePlusDividend": 11880.704
  },
  {
    "month": "1946-12-01",
    "price": 15.13,
    "nominalPricePlusDividend": 837.9756,
    "realPrice": 221.4768,
    "realPricePlusDividend": 12170.0666
  },
  {
    "month": "1947-01-01",
    "price": 15.21,
    "nominalPricePlusDividend": 845.6833,
    "realPrice": 222.6479,
    "realPricePlusDividend": 12282.1599
  },
  {
    "month": "1947-02-01",
    "price": 15.8,
    "nominalPricePlusDividend": 881.7928,
    "realPrice": 231.2844,
    "realPricePlusDividend": 12806.7425
  },
  {
    "month": "1947-03-01",
    "price": 15.16,
    "nominalPricePlusDividend": 849.4077,
    "realPrice": 217.8627,
    "realPricePlusDividend": 12111.2242
  },
  {
    "month": "1947-04-01",
    "price": 14.6,
    "nominalPricePlusDividend": 821.3929,
    "realPrice": 209.815,
    "realPricePlusDividend": 11712.5925
  },
  {
    "month": "1947-05-01",
    "price": 14.34,
    "nominalPricePlusDividend": 810.2035,
    "realPrice": 206.0786,
    "realPricePlusDividend": 11553.8546
  },
  {
    "month": "1947-06-01",
    "price": 14.84,
    "nominalPricePlusDividend": 841.9688,
    "realPrice": 212.2946,
    "realPricePlusDividend": 11953.0807
  },
  {
    "month": "1947-07-01",
    "price": 15.77,
    "nominalPricePlusDividend": 898.3269,
    "realPrice": 223.5664,
    "realPricePlusDividend": 12638.8701
  },
  {
    "month": "1947-08-01",
    "price": 15.46,
    "nominalPricePlusDividend": 884.3232,
    "realPrice": 216.2493,
    "realPricePlusDividend": 12276.5382
  },
  {
    "month": "1947-09-01",
    "price": 15.06,
    "nominalPricePlusDividend": 865.161,
    "realPrice": 206.0748,
    "realPricePlusDividend": 11749.9931
  },
  {
    "month": "1947-10-01",
    "price": 15.45,
    "nominalPricePlusDividend": 891.3475,
    "realPrice": 211.4114,
    "realPricePlusDividend": 12106.6454
  },
  {
    "month": "1947-11-01",
    "price": 15.27,
    "nominalPricePlusDividend": 884.8411,
    "realPrice": 208.0438,
    "realPricePlusDividend": 11967.2494
  },
  {
    "month": "1947-12-01",
    "price": 15.03,
    "nominalPricePlusDividend": 874.9097,
    "realPrice": 202.1487,
    "realPricePlusDividend": 11682.22
  },
  {
    "month": "1948-01-01",
    "price": 14.83,
    "nominalPricePlusDividend": 867.3423,
    "realPrice": 196.934,
    "realPricePlusDividend": 11434.712
  },
  {
    "month": "1948-02-01",
    "price": 14.1,
    "nominalPricePlusDividend": 828.758,
    "realPrice": 188.8335,
    "realPricePlusDividend": 11019.1533
  },
  {
    "month": "1948-03-01",
    "price": 14.3,
    "nominalPricePlusDividend": 844.6605,
    "realPrice": 192.3304,
    "realPricePlusDividend": 11278.7218
  },
  {
    "month": "1948-04-01",
    "price": 15.4,
    "nominalPricePlusDividend": 913.8183,
    "realPrice": 203.644,
    "realPricePlusDividend": 11997.0232
  },
  {
    "month": "1948-05-01",
    "price": 16.15,
    "nominalPricePlusDividend": 962.5256,
    "realPrice": 212.6681,
    "realPricePlusDividend": 12583.521
  },
  {
    "month": "1948-06-01",
    "price": 16.82,
    "nominalPricePlusDividend": 1006.6786,
    "realPrice": 219.6528,
    "realPricePlusDividend": 13051.4534
  },
  {
    "month": "1948-07-01",
    "price": 16.42,
    "nominalPricePlusDividend": 986.978,
    "realPrice": 211.7928,
    "realPricePlusDividend": 12639.0531
  },
  {
    "month": "1948-08-01",
    "price": 15.94,
    "nominalPricePlusDividend": 962.4171,
    "realPrice": 204.7623,
    "realPricePlusDividend": 12274.5704
  },
  {
    "month": "1948-09-01",
    "price": 15.76,
    "nominalPricePlusDividend": 955.8929,
    "realPrice": 202.4501,
    "realPricePlusDividend": 12191.7072
  },
  {
    "month": "1948-10-01",
    "price": 16.19,
    "nominalPricePlusDividend": 986.3711,
    "realPrice": 208.8261,
    "realPricePlusDividend": 12633.202
  },
  {
    "month": "1948-11-01",
    "price": 15.29,
    "nominalPricePlusDividend": 936.0575,
    "realPrice": 198.8474,
    "realPricePlusDividend": 12089.1003
  },
  {
    "month": "1948-12-01",
    "price": 15.19,
    "nominalPricePlusDividend": 934.578,
    "realPrice": 198.3666,
    "realPricePlusDividend": 12121.3076
  },
  {
    "month": "1949-01-01",
    "price": 15.36,
    "nominalPricePlusDividend": 949.8056,
    "realPrice": 201.4224,
    "realPricePlusDividend": 12371.1548
  },
  {
    "month": "1949-02-01",
    "price": 14.77,
    "nominalPricePlusDividend": 918.2004,
    "realPrice": 195.3131,
    "realPricePlusDividend": 12061.0299
  },
  {
    "month": "1949-03-01",
    "price": 14.91,
    "nominalPricePlusDividend": 931.8943,
    "realPrice": 197.1644,
    "realPricePlusDividend": 12241.9415
  },
  {
    "month": "1949-04-01",
    "price": 14.89,
    "nominalPricePlusDividend": 935.7486,
    "realPrice": 196.0761,
    "realPricePlusDividend": 12241.9477
  },
  {
    "month": "1949-05-01",
    "price": 14.78,
    "nominalPricePlusDividend": 934.0378,
    "realPrice": 195.4453,
    "realPricePlusDividend": 12271.724
  },
  {
    "month": "1949-06-01",
    "price": 13.97,
    "nominalPricePlusDividend": 888.1505,
    "realPrice": 183.9612,
    "realPricePlusDividend": 11620.8299
  },
  {
    "month": "1949-07-01",
    "price": 14.76,
    "nominalPricePlusDividend": 943.7791,
    "realPrice": 196.0044,
    "realPricePlusDividend": 12453.2594
  },
  {
    "month": "1949-08-01",
    "price": 15.29,
    "nominalPricePlusDividend": 983.1388,
    "realPrice": 202.1894,
    "realPricePlusDividend": 12918.4661
  },
  {
    "month": "1949-09-01",
    "price": 15.49,
    "nominalPricePlusDividend": 1001.5355,
    "realPrice": 203.9771,
    "realPricePlusDividend": 13105.4958
  },
  {
    "month": "1949-10-01",
    "price": 15.89,
    "nominalPricePlusDividend": 1033.0019,
    "realPrice": 211.0101,
    "realPricePlusDividend": 13633.5717
  },
  {
    "month": "1949-11-01",
    "price": 16.11,
    "nominalPricePlusDividend": 1053.1187,
    "realPrice": 213.0328,
    "realPricePlusDividend": 13842.931
  },
  {
    "month": "1949-12-01",
    "price": 16.54,
    "nominalPricePlusDividend": 1087.2567,
    "realPrice": 220.5725,
    "realPricePlusDividend": 14415.0643
  },
  {
    "month": "1950-01-01",
    "price": 16.88,
    "nominalPricePlusDividend": 1115.8514,
    "realPrice": 226.0645,
    "realPricePlusDividend": 14857.7373
  },
  {
    "month": "1950-02-01",
    "price": 17.21,
    "nominalPricePlusDividend": 1144.0011,
    "realPrice": 230.484,
    "realPricePlusDividend": 15233.1618
  },
  {
    "month": "1950-03-01",
    "price": 17.35,
    "nominalPricePlusDividend": 1159.733,
    "realPrice": 231.3744,
    "realPricePlusDividend": 15377.8154
  },
  {
    "month": "1950-04-01",
    "price": 17.84,
    "nominalPricePlusDividend": 1199.0035,
    "realPrice": 237.9089,
    "realPricePlusDividend": 15899.1429
  },
  {
    "month": "1950-05-01",
    "price": 18.44,
    "nominalPricePlusDividend": 1245.9376,
    "realPrice": 244.8727,
    "realPricePlusDividend": 16452.4006
  },
  {
    "month": "1950-06-01",
    "price": 18.74,
    "nominalPricePlusDividend": 1272.9081,
    "realPrice": 247.8109,
    "realPricePlusDividend": 16738.5262
  },
  {
    "month": "1950-07-01",
    "price": 17.38,
    "nominalPricePlusDividend": 1187.3231,
    "realPrice": 226.9659,
    "realPricePlusDividend": 15421.7923
  },
  {
    "month": "1950-08-01",
    "price": 18.43,
    "nominalPricePlusDividend": 1266.1326,
    "realPrice": 238.6969,
    "realPricePlusDividend": 16313.1103
  },
  {
    "month": "1950-09-01",
    "price": 19.08,
    "nominalPricePlusDividend": 1318.1534,
    "realPrice": 246.1027,
    "realPricePlusDividend": 16916.7912
  },
  {
    "month": "1950-10-01",
    "price": 19.87,
    "nominalPricePlusDividend": 1380.388,
    "realPrice": 254.2088,
    "realPricePlusDividend": 17574.7337
  },
  {
    "month": "1950-11-01",
    "price": 19.83,
    "nominalPricePlusDividend": 1385.5791,
    "realPrice": 252.6699,
    "realPricePlusDividend": 17572.6742
  },
  {
    "month": "1950-12-01",
    "price": 19.75,
    "nominalPricePlusDividend": 1388.2769,
    "realPrice": 248.6308,
    "realPricePlusDividend": 17398.8528
  },
  {
    "month": "1951-01-01",
    "price": 21.21,
    "nominalPricePlusDividend": 1499.5148,
    "realPrice": 262.8057,
    "realPricePlusDividend": 18498.056
  },
  {
    "month": "1951-02-01",
    "price": 22,
    "nominalPricePlusDividend": 1564.1254,
    "realPrice": 269.4123,
    "realPricePlusDividend": 19070.8954
  },
  {
    "month": "1951-03-01",
    "price": 21.63,
    "nominalPricePlusDividend": 1546.7264,
    "realPrice": 263.8546,
    "realPricePlusDividend": 18786.6965
  },
  {
    "month": "1951-04-01",
    "price": 21.92,
    "nominalPricePlusDividend": 1576.5216,
    "realPrice": 267.3921,
    "realPricePlusDividend": 19149.3913
  },
  {
    "month": "1951-05-01",
    "price": 21.93,
    "nominalPricePlusDividend": 1586.4308,
    "realPrice": 266.4813,
    "realPricePlusDividend": 19196.1542
  },
  {
    "month": "1951-06-01",
    "price": 21.55,
    "nominalPricePlusDividend": 1568.2652,
    "realPrice": 261.8637,
    "realPricePlusDividend": 18977.1506
  },
  {
    "month": "1951-07-01",
    "price": 21.93,
    "nominalPricePlusDividend": 1605.3796,
    "realPrice": 266.4813,
    "realPricePlusDividend": 19425.1148
  },
  {
    "month": "1951-08-01",
    "price": 22.89,
    "nominalPricePlusDividend": 1685.0915,
    "realPrice": 278.1466,
    "realPricePlusDividend": 20388.4761
  },
  {
    "month": "1951-09-01",
    "price": 23.48,
    "nominalPricePlusDividend": 1737.932,
    "realPrice": 283.1297,
    "realPricePlusDividend": 20865.5306
  },
  {
    "month": "1951-10-01",
    "price": 23.36,
    "nominalPricePlusDividend": 1738.4255,
    "realPrice": 280.6075,
    "realPricePlusDividend": 20788.925
  },
  {
    "month": "1951-11-01",
    "price": 22.71,
    "nominalPricePlusDividend": 1699.2522,
    "realPrice": 270.7329,
    "realPricePlusDividend": 20163.6724
  },
  {
    "month": "1951-12-01",
    "price": 23.41,
    "nominalPricePlusDividend": 1760.6494,
    "realPrice": 278.0247,
    "realPricePlusDividend": 20810.5284
  },
  {
    "month": "1952-01-01",
    "price": 24.19,
    "nominalPricePlusDividend": 1828.1498,
    "realPrice": 287.2882,
    "realPricePlusDividend": 21608.46
  },
  {
    "month": "1952-02-01",
    "price": 23.75,
    "nominalPricePlusDividend": 1803.7979,
    "realPrice": 284.2076,
    "realPricePlusDividend": 21482.8514
  },
  {
    "month": "1952-03-01",
    "price": 23.81,
    "nominalPricePlusDividend": 1817.3212,
    "realPrice": 284.9256,
    "realPricePlusDividend": 21644.0021
  },
  {
    "month": "1952-04-01",
    "price": 23.74,
    "nominalPricePlusDividend": 1821.0103,
    "realPrice": 283.0118,
    "realPricePlusDividend": 21606.3815
  },
  {
    "month": "1952-05-01",
    "price": 23.73,
    "nominalPricePlusDividend": 1829.384,
    "realPrice": 282.8926,
    "realPricePlusDividend": 21706.3329
  },
  {
    "month": "1952-06-01",
    "price": 24.38,
    "nominalPricePlusDividend": 1888.7446,
    "realPrice": 289.5447,
    "realPricePlusDividend": 22326.6952
  },
  {
    "month": "1952-07-01",
    "price": 25.08,
    "nominalPricePlusDividend": 1952.3354,
    "realPrice": 295.627,
    "realPricePlusDividend": 22905.3621
  },
  {
    "month": "1952-08-01",
    "price": 25.18,
    "nominalPricePlusDividend": 1969.526,
    "realPrice": 296.8057,
    "realPricePlusDividend": 23106.8833
  },
  {
    "month": "1952-09-01",
    "price": 24.78,
    "nominalPricePlusDividend": 1947.6902,
    "realPrice": 292.0908,
    "realPricePlusDividend": 22850.536
  },
  {
    "month": "1952-10-01",
    "price": 24.26,
    "nominalPricePlusDividend": 1916.316,
    "realPrice": 285.9613,
    "realPricePlusDividend": 22481.2615
  },
  {
    "month": "1952-11-01",
    "price": 25.03,
    "nominalPricePlusDividend": 1986.5959,
    "realPrice": 295.0376,
    "realPricePlusDividend": 23304.5561
  },
  {
    "month": "1952-12-01",
    "price": 26.04,
    "nominalPricePlusDividend": 2076.1721,
    "realPrice": 306.9428,
    "realPricePlusDividend": 24354.1692
  },
  {
    "month": "1953-01-01",
    "price": 26.18,
    "nominalPricePlusDividend": 2096.7026,
    "realPrice": 309.7532,
    "realPricePlusDividend": 24687.297
  },
  {
    "month": "1953-02-01",
    "price": 25.86,
    "nominalPricePlusDividend": 2080.4848,
    "realPrice": 307.1217,
    "realPricePlusDividend": 24588.6165
  },
  {
    "month": "1953-03-01",
    "price": 25.99,
    "nominalPricePlusDividend": 2100.3966,
    "realPrice": 307.5052,
    "realPricePlusDividend": 24730.4598
  },
  {
    "month": "1953-04-01",
    "price": 24.71,
    "nominalPricePlusDividend": 2006.4485,
    "realPrice": 292.3606,
    "realPricePlusDividend": 23624.3949
  },
  {
    "month": "1953-05-01",
    "price": 24.84,
    "nominalPricePlusDividend": 2026.568,
    "realPrice": 292.798,
    "realPricePlusDividend": 23772.0163
  },
  {
    "month": "1953-06-01",
    "price": 23.95,
    "nominalPricePlusDividend": 1963.5891,
    "realPrice": 281.2539,
    "realPricePlusDividend": 22947.4133
  },
  {
    "month": "1953-07-01",
    "price": 24.29,
    "nominalPricePlusDividend": 2001.1665,
    "realPrice": 285.2466,
    "realPricePlusDividend": 23386.3915
  },
  {
    "month": "1953-08-01",
    "price": 24.39,
    "nominalPricePlusDividend": 2019.1542,
    "realPrice": 285.3562,
    "realPricePlusDividend": 23508.7141
  },
  {
    "month": "1953-09-01",
    "price": 23.27,
    "nominalPricePlusDividend": 1936.23,
    "realPrice": 272.2525,
    "realPricePlusDividend": 22543.0711
  },
  {
    "month": "1953-10-01",
    "price": 23.97,
    "nominalPricePlusDividend": 2004.3212,
    "realPrice": 279.4036,
    "realPricePlusDividend": 23250.0449
  },
  {
    "month": "1953-11-01",
    "price": 24.5,
    "nominalPricePlusDividend": 2058.6032,
    "realPrice": 286.6432,
    "realPricePlusDividend": 23969.1231
  },
  {
    "month": "1953-12-01",
    "price": 24.83,
    "nominalPricePlusDividend": 2096.4142,
    "realPrice": 290.5041,
    "realPricePlusDividend": 24410.0118
  },
  {
    "month": "1954-01-01",
    "price": 25.46,
    "nominalPricePlusDividend": 2159.8076,
    "realPrice": 297.8749,
    "realPricePlusDividend": 25148.5141
  },
  {
    "month": "1954-02-01",
    "price": 26.02,
    "nominalPricePlusDividend": 2217.6108,
    "realPrice": 304.4267,
    "realPricePlusDividend": 25821.9361
  },
  {
    "month": "1954-03-01",
    "price": 26.57,
    "nominalPricePlusDividend": 2274.8787,
    "realPrice": 310.8616,
    "realPricePlusDividend": 26489.1362
  },
  {
    "month": "1954-04-01",
    "price": 27.63,
    "nominalPricePlusDividend": 2376.1224,
    "realPrice": 324.4695,
    "realPricePlusDividend": 27770.5387
  },
  {
    "month": "1954-05-01",
    "price": 28.73,
    "nominalPricePlusDividend": 2481.207,
    "realPrice": 336.133,
    "realPricePlusDividend": 28890.1598
  },
  {
    "month": "1954-06-01",
    "price": 28.96,
    "nominalPricePlusDividend": 2511.554,
    "realPrice": 338.8239,
    "realPricePlusDividend": 29242.7683
  },
  {
    "month": "1954-07-01",
    "price": 30.13,
    "nominalPricePlusDividend": 2623.5015,
    "realPrice": 352.5126,
    "realPricePlusDividend": 30546.5844
  },
  {
    "month": "1954-08-01",
    "price": 30.73,
    "nominalPricePlusDividend": 2686.3148,
    "realPrice": 359.5324,
    "realPricePlusDividend": 31278.3265
  },
  {
    "month": "1954-09-01",
    "price": 31.45,
    "nominalPricePlusDividend": 2759.9148,
    "realPrice": 369.3292,
    "realPricePlusDividend": 32255.5834
  },
  {
    "month": "1954-10-01",
    "price": 32.18,
    "nominalPricePlusDividend": 2834.7264,
    "realPrice": 377.9019,
    "realPricePlusDividend": 33131.7241
  },
  {
    "month": "1954-11-01",
    "price": 33.44,
    "nominalPricePlusDividend": 2956.6817,
    "realPrice": 392.6985,
    "realPricePlusDividend": 34558.9222
  },
  {
    "month": "1954-12-01",
    "price": 34.97,
    "nominalPricePlusDividend": 3103.1355,
    "realPrice": 412.204,
    "realPricePlusDividend": 36408.3994
  },
  {
    "month": "1955-01-01",
    "price": 35.6,
    "nominalPricePlusDividend": 3170.4278,
    "realPrice": 419.63,
    "realPricePlusDividend": 37198.3039
  },
  {
    "month": "1955-02-01",
    "price": 36.79,
    "nominalPricePlusDividend": 3287.8841,
    "realPrice": 433.657,
    "realPricePlusDividend": 38576.785
  },
  {
    "month": "1955-03-01",
    "price": 36.5,
    "nominalPricePlusDividend": 3273.5354,
    "realPrice": 430.2386,
    "realPricePlusDividend": 38408.8115
  },
  {
    "month": "1955-04-01",
    "price": 37.76,
    "nominalPricePlusDividend": 3398.1988,
    "realPrice": 445.0907,
    "realPricePlusDividend": 39871.5914
  },
  {
    "month": "1955-05-01",
    "price": 37.6,
    "nominalPricePlusDividend": 3395.5239,
    "realPrice": 443.2047,
    "realPricePlusDividend": 39840.2957
  },
  {
    "month": "1955-06-01",
    "price": 39.78,
    "nominalPricePlusDividend": 3604.1821,
    "realPrice": 468.9012,
    "realPricePlusDividend": 42288.6077
  },
  {
    "month": "1955-07-01",
    "price": 42.69,
    "nominalPricePlusDividend": 3879.6903,
    "realPrice": 501.3248,
    "realPricePlusDividend": 45352.61
  },
  {
    "month": "1955-08-01",
    "price": 42.43,
    "nominalPricePlusDividend": 3868.0778,
    "realPrice": 498.2715,
    "realPricePlusDividend": 45218.1268
  },
  {
    "month": "1955-09-01",
    "price": 44.34,
    "nominalPricePlusDividend": 4054.381,
    "realPrice": 518.7656,
    "realPricePlusDividend": 47221.0941
  },
  {
    "month": "1955-10-01",
    "price": 42.11,
    "nominalPricePlusDividend": 3862.8175,
    "realPrice": 492.6753,
    "realPricePlusDividend": 44990.3439
  },
  {
    "month": "1955-11-01",
    "price": 44.95,
    "nominalPricePlusDividend": 4135.77,
    "realPrice": 525.9025,
    "realPricePlusDividend": 48169.8059
  },
  {
    "month": "1955-12-01",
    "price": 45.37,
    "nominalPricePlusDividend": 4186.9367,
    "realPrice": 532.797,
    "realPricePlusDividend": 48948.0925
  },
  {
    "month": "1956-01-01",
    "price": 44.15,
    "nominalPricePlusDividend": 4086.9621,
    "realPrice": 518.4701,
    "realPricePlusDividend": 47781.7962
  },
  {
    "month": "1956-02-01",
    "price": 44.43,
    "nominalPricePlusDividend": 4125.7643,
    "realPrice": 521.7582,
    "realPricePlusDividend": 48237.9214
  },
  {
    "month": "1956-03-01",
    "price": 47.49,
    "nominalPricePlusDividend": 4423.0707,
    "realPrice": 557.693,
    "realPricePlusDividend": 51716.4719
  },
  {
    "month": "1956-04-01",
    "price": 48.05,
    "nominalPricePlusDividend": 4488.6546,
    "realPrice": 562.1716,
    "realPricePlusDividend": 52290.0757
  },
  {
    "month": "1956-05-01",
    "price": 46.54,
    "nominalPricePlusDividend": 4361.2451,
    "realPrice": 542.4883,
    "realPricePlusDividend": 50619.5332
  },
  {
    "month": "1956-06-01",
    "price": 46.27,
    "nominalPricePlusDividend": 4349.8177,
    "realPrice": 535.3754,
    "realPricePlusDividend": 50117.5309
  },
  {
    "month": "1956-07-01",
    "price": 48.78,
    "nominalPricePlusDividend": 4599.8829,
    "realPrice": 560.2979,
    "realPricePlusDividend": 52612.8211
  },
  {
    "month": "1956-08-01",
    "price": 48.49,
    "nominalPricePlusDividend": 4586.7859,
    "realPrice": 559.0071,
    "realPricePlusDividend": 52656.1495
  },
  {
    "month": "1956-09-01",
    "price": 46.84,
    "nominalPricePlusDividend": 4445.1075,
    "realPrice": 538.0147,
    "realPricePlusDividend": 50844.4018
  },
  {
    "month": "1956-10-01",
    "price": 46.24,
    "nominalPricePlusDividend": 4402.7189,
    "realPrice": 529.1916,
    "realPricePlusDividend": 50173.1774
  },
  {
    "month": "1956-11-01",
    "price": 45.76,
    "nominalPricePlusDividend": 4371.351,
    "realPrice": 523.6982,
    "realPricePlusDividend": 49812.4576
  },
  {
    "month": "1956-12-01",
    "price": 46.44,
    "nominalPricePlusDividend": 4450.4268,
    "realPrice": 529.5548,
    "realPricePlusDividend": 50526.5511
  },
  {
    "month": "1957-01-01",
    "price": 45.43,
    "nominalPricePlusDividend": 4367.5323,
    "realPrice": 518.0378,
    "realPricePlusDividend": 49584.8982
  },
  {
    "month": "1957-02-01",
    "price": 43.47,
    "nominalPricePlusDividend": 4193.0158,
    "realPrice": 493.8985,
    "realPricePlusDividend": 47431.2101
  },
  {
    "month": "1957-03-01",
    "price": 44.03,
    "nominalPricePlusDividend": 4260.9649,
    "realPrice": 498.4616,
    "realPricePlusDividend": 48025.9313
  },
  {
    "month": "1957-04-01",
    "price": 45.05,
    "nominalPricePlusDividend": 4373.6261,
    "realPrice": 508.181,
    "realPricePlusDividend": 49118.8314
  },
  {
    "month": "1957-05-01",
    "price": 46.78,
    "nominalPricePlusDividend": 4555.5774,
    "realPrice": 525.8114,
    "realPricePlusDividend": 50979.314
  },
  {
    "month": "1957-06-01",
    "price": 47.55,
    "nominalPricePlusDividend": 4644.6017,
    "realPrice": 532.5642,
    "realPricePlusDividend": 51790.3438
  },
  {
    "month": "1957-07-01",
    "price": 48.51,
    "nominalPricePlusDividend": 4752.4548,
    "realPrice": 539.4766,
    "realPricePlusDividend": 52619.1356
  },
  {
    "month": "1957-08-01",
    "price": 45.84,
    "nominalPricePlusDividend": 4505.0842,
    "realPrice": 509.7837,
    "realPricePlusDividend": 49880.9191
  },
  {
    "month": "1957-09-01",
    "price": 43.98,
    "nominalPricePlusDividend": 4336.6185,
    "realPrice": 489.0988,
    "realPricePlusDividend": 48016.3135
  },
  {
    "month": "1957-10-01",
    "price": 41.24,
    "nominalPricePlusDividend": 4080.9046,
    "realPrice": 458.6274,
    "realPricePlusDividend": 45185.6445
  },
  {
    "month": "1957-11-01",
    "price": 40.35,
    "nominalPricePlusDividend": 4007.4305,
    "realPrice": 447.1497,
    "realPricePlusDividend": 44216.5349
  },
  {
    "month": "1957-12-01",
    "price": 40.33,
    "nominalPricePlusDividend": 4020.1762,
    "realPrice": 446.9281,
    "realPricePlusDividend": 44357.8359
  },
  {
    "month": "1958-01-01",
    "price": 41.12,
    "nominalPricePlusDividend": 4113.7942,
    "realPrice": 452.4961,
    "realPricePlusDividend": 45072.5323
  },
  {
    "month": "1958-02-01",
    "price": 41.26,
    "nominalPricePlusDividend": 4142.6679,
    "realPrice": 454.0367,
    "realPricePlusDividend": 45388.0353
  },
  {
    "month": "1958-03-01",
    "price": 42.11,
    "nominalPricePlusDividend": 4242.8767,
    "realPrice": 460.1724,
    "realPricePlusDividend": 46162.2801
  },
  {
    "month": "1958-04-01",
    "price": 42.34,
    "nominalPricePlusDividend": 4280.9124,
    "realPrice": 461.0848,
    "realPricePlusDividend": 46413.4929
  },
  {
    "month": "1958-05-01",
    "price": 43.7,
    "nominalPricePlusDividend": 4433.2204,
    "realPrice": 475.8953,
    "realPricePlusDividend": 48063.355
  },
  {
    "month": "1958-06-01",
    "price": 44.75,
    "nominalPricePlusDividend": 4554.4773,
    "realPrice": 487.3298,
    "realPricePlusDividend": 49376.5209
  },
  {
    "month": "1958-07-01",
    "price": 45.98,
    "nominalPricePlusDividend": 4694.3346,
    "realPrice": 498.998,
    "realPricePlusDividend": 50717.0291
  },
  {
    "month": "1958-08-01",
    "price": 47.7,
    "nominalPricePlusDividend": 4884.6569,
    "realPrice": 519.4555,
    "realPricePlusDividend": 52955.6182
  },
  {
    "month": "1958-09-01",
    "price": 48.96,
    "nominalPricePlusDividend": 5028.4488,
    "realPrice": 533.1769,
    "realPricePlusDividend": 54514.2589
  },
  {
    "month": "1958-10-01",
    "price": 50.95,
    "nominalPricePlusDividend": 5247.6389,
    "realPrice": 554.8481,
    "realPricePlusDividend": 56890.915
  },
  {
    "month": "1958-11-01",
    "price": 52.5,
    "nominalPricePlusDividend": 5422.1883,
    "realPrice": 569.7563,
    "realPricePlusDividend": 58580.9233
  },
  {
    "month": "1958-12-01",
    "price": 53.49,
    "nominalPricePlusDividend": 5539.4395,
    "realPrice": 582.5089,
    "realPricePlusDividend": 60055.1618
  },
  {
    "month": "1959-01-01",
    "price": 55.62,
    "nominalPricePlusDividend": 5775.1255,
    "realPrice": 603.6161,
    "realPricePlusDividend": 62394.803
  },
  {
    "month": "1959-02-01",
    "price": 54.77,
    "nominalPricePlusDividend": 5702.0683,
    "realPrice": 596.4481,
    "realPricePlusDividend": 61819.0353
  },
  {
    "month": "1959-03-01",
    "price": 56.16,
    "nominalPricePlusDividend": 5862.0785,
    "realPrice": 611.5853,
    "realPricePlusDividend": 63554.1678
  },
  {
    "month": "1959-04-01",
    "price": 57.1,
    "nominalPricePlusDividend": 5975.5937,
    "realPrice": 619.6778,
    "realPricePlusDividend": 64561.8333
  },
  {
    "month": "1959-05-01",
    "price": 57.96,
    "nominalPricePlusDividend": 6081.0881,
    "realPrice": 629.0109,
    "realPricePlusDividend": 65701.9997
  },
  {
    "month": "1959-06-01",
    "price": 57.46,
    "nominalPricePlusDividend": 6044.2208,
    "realPrice": 621.4417,
    "realPricePlusDividend": 65079.6398
  },
  {
    "month": "1959-07-01",
    "price": 59.74,
    "nominalPricePlusDividend": 6299.745,
    "realPrice": 643.8877,
    "realPricePlusDividend": 67599.0111
  },
  {
    "month": "1959-08-01",
    "price": 59.4,
    "nominalPricePlusDividend": 6279.6797,
    "realPrice": 640.2232,
    "realPricePlusDividend": 67384.0771
  },
  {
    "month": "1959-09-01",
    "price": 57.05,
    "nominalPricePlusDividend": 6047.1283,
    "realPrice": 612.7959,
    "realPricePlusDividend": 64667.5971
  },
  {
    "month": "1959-10-01",
    "price": 57,
    "nominalPricePlusDividend": 6057.8163,
    "realPrice": 610.1763,
    "realPricePlusDividend": 64561.9212
  },
  {
    "month": "1959-11-01",
    "price": 57.23,
    "nominalPricePlusDividend": 6098.3494,
    "realPrice": 612.6384,
    "realPricePlusDividend": 64994.2801
  },
  {
    "month": "1959-12-01",
    "price": 59.06,
    "nominalPricePlusDividend": 6309.5426,
    "realPrice": 632.2283,
    "realPricePlusDividend": 67245.4844
  },
  {
    "month": "1960-01-01",
    "price": 58.03,
    "nominalPricePlusDividend": 6215.7969,
    "realPrice": 623.3224,
    "realPricePlusDividend": 66475.6902
  },
  {
    "month": "1960-02-01",
    "price": 55.78,
    "nominalPricePlusDividend": 5991.4536,
    "realPrice": 597.1164,
    "realPricePlusDividend": 63861.6919
  },
  {
    "month": "1960-03-01",
    "price": 55.02,
    "nominalPricePlusDividend": 5926.8571,
    "realPrice": 588.9807,
    "realPricePlusDividend": 63176.3937
  },
  {
    "month": "1960-04-01",
    "price": 55.73,
    "nominalPricePlusDividend": 6020.7546,
    "realPrice": 594.5588,
    "realPricePlusDividend": 63959.7718
  },
  {
    "month": "1960-05-01",
    "price": 55.22,
    "nominalPricePlusDividend": 5983.1527,
    "realPrice": 589.1178,
    "realPricePlusDividend": 63560.3603
  },
  {
    "month": "1960-06-01",
    "price": 57.26,
    "nominalPricePlusDividend": 6221.7661,
    "realPrice": 608.8179,
    "realPricePlusDividend": 65871.9503
  },
  {
    "month": "1960-07-01",
    "price": 55.84,
    "nominalPricePlusDividend": 6085.1284,
    "realPrice": 593.7197,
    "realPricePlusDividend": 64425.0433
  },
  {
    "month": "1960-08-01",
    "price": 56.51,
    "nominalPricePlusDividend": 6175.8496,
    "realPrice": 600.8435,
    "realPricePlusDividend": 65385.2561
  },
  {
    "month": "1960-09-01",
    "price": 54.81,
    "nominalPricePlusDividend": 6007.8197,
    "realPrice": 582.7683,
    "realPricePlusDividend": 63606.0023
  },
  {
    "month": "1960-10-01",
    "price": 53.73,
    "nominalPricePlusDividend": 5907.2509,
    "realPrice": 567.451,
    "realPricePlusDividend": 62121.2418
  },
  {
    "month": "1960-11-01",
    "price": 55.47,
    "nominalPricePlusDividend": 6116.418,
    "realPrice": 585.8274,
    "realPricePlusDividend": 64320.5839
  },
  {
    "month": "1960-12-01",
    "price": 56.8,
    "nominalPricePlusDividend": 6280.989,
    "realPrice": 599.8738,
    "realPricePlusDividend": 66050.9414
  },
  {
    "month": "1961-01-01",
    "price": 59.72,
    "nominalPricePlusDividend": 6621.8543,
    "realPrice": 630.7123,
    "realPricePlusDividend": 69634.8809
  },
  {
    "month": "1961-02-01",
    "price": 62.17,
    "nominalPricePlusDividend": 6911.5019,
    "realPrice": 656.5872,
    "realPricePlusDividend": 72680.1865
  },
  {
    "month": "1961-03-01",
    "price": 64.12,
    "nominalPricePlusDividend": 7146.2889,
    "realPrice": 677.1814,
    "realPricePlusDividend": 75148.5612
  },
  {
    "month": "1961-04-01",
    "price": 65.83,
    "nominalPricePlusDividend": 7354.8895,
    "realPrice": 695.241,
    "realPricePlusDividend": 77341.8705
  },
  {
    "month": "1961-05-01",
    "price": 66.5,
    "nominalPricePlusDividend": 7447.8079,
    "realPrice": 702.317,
    "realPricePlusDividend": 78318.6905
  },
  {
    "month": "1961-06-01",
    "price": 65.62,
    "nominalPricePlusDividend": 7367.3566,
    "realPrice": 693.0232,
    "realPricePlusDividend": 77472.4085
  },
  {
    "month": "1961-07-01",
    "price": 65.44,
    "nominalPricePlusDividend": 7365.2983,
    "realPrice": 686.5147,
    "realPricePlusDividend": 76934.7943
  },
  {
    "month": "1961-08-01",
    "price": 67.79,
    "nominalPricePlusDividend": 7648.0499,
    "realPrice": 713.5464,
    "realPricePlusDividend": 80155.8527
  },
  {
    "month": "1961-09-01",
    "price": 67.26,
    "nominalPricePlusDividend": 7606.62,
    "realPrice": 705.6078,
    "realPricePlusDividend": 79456.2736
  },
  {
    "month": "1961-10-01",
    "price": 68,
    "nominalPricePlusDividend": 7708.7804,
    "realPrice": 713.371,
    "realPricePlusDividend": 80525.0877
  },
  {
    "month": "1961-11-01",
    "price": 71.08,
    "nominalPricePlusDividend": 8076.648,
    "realPrice": 745.6825,
    "realPricePlusDividend": 84369.4724
  },
  {
    "month": "1961-12-01",
    "price": 71.74,
    "nominalPricePlusDividend": 8170.5801,
    "realPrice": 752.6064,
    "realPricePlusDividend": 85352.3779
  },
  {
    "month": "1962-01-01",
    "price": 69.07,
    "nominalPricePlusDividend": 7885.6614,
    "realPrice": 724.5961,
    "realPricePlusDividend": 82376.3925
  },
  {
    "month": "1962-02-01",
    "price": 70.22,
    "nominalPricePlusDividend": 8036.2378,
    "realPrice": 734.2131,
    "realPricePlusDividend": 83670.8255
  },
  {
    "month": "1962-03-01",
    "price": 70.29,
    "nominalPricePlusDividend": 8063.6407,
    "realPrice": 734.945,
    "realPricePlusDividend": 83956.4969
  },
  {
    "month": "1962-04-01",
    "price": 68.05,
    "nominalPricePlusDividend": 7826.1711,
    "realPrice": 709.1678,
    "realPricePlusDividend": 81214.5715
  },
  {
    "month": "1962-05-01",
    "price": 62.99,
    "nominalPricePlusDividend": 7263.8548,
    "realPrice": 656.4361,
    "realPricePlusDividend": 75379.6016
  },
  {
    "month": "1962-06-01",
    "price": 55.63,
    "nominalPricePlusDividend": 6434.8494,
    "realPrice": 579.7355,
    "realPricePlusDividend": 66777.0783
  },
  {
    "month": "1962-07-01",
    "price": 56.97,
    "nominalPricePlusDividend": 6609.7074,
    "realPrice": 591.7406,
    "realPricePlusDividend": 68365.6346
  },
  {
    "month": "1962-08-01",
    "price": 58.52,
    "nominalPricePlusDividend": 6809.5211,
    "realPrice": 607.8403,
    "realPricePlusDividend": 70432.7087
  },
  {
    "month": "1962-09-01",
    "price": 58,
    "nominalPricePlusDividend": 6769.1175,
    "realPrice": 600.4574,
    "realPricePlusDividend": 69784.849
  },
  {
    "month": "1962-10-01",
    "price": 56.17,
    "nominalPricePlusDividend": 6575.7697,
    "realPrice": 581.5119,
    "realPricePlusDividend": 67792.928
  },
  {
    "month": "1962-11-01",
    "price": 60.04,
    "nominalPricePlusDividend": 7049.2816,
    "realPrice": 621.5769,
    "realPricePlusDividend": 72675.9607
  },
  {
    "month": "1962-12-01",
    "price": 62.64,
    "nominalPricePlusDividend": 7375.2241,
    "realPrice": 648.494,
    "realPricePlusDividend": 76037.6912
  },
  {
    "month": "1963-01-01",
    "price": 65.06,
    "nominalPricePlusDividend": 7681.0534,
    "realPrice": 673.5476,
    "realPricePlusDividend": 79191.1081
  },
  {
    "month": "1963-02-01",
    "price": 65.92,
    "nominalPricePlusDividend": 7803.6073,
    "realPrice": 682.4509,
    "realPricePlusDividend": 80454.9831
  },
  {
    "month": "1963-03-01",
    "price": 65.67,
    "nominalPricePlusDividend": 7795.1563,
    "realPrice": 677.6337,
    "realPricePlusDividend": 80104.7039
  },
  {
    "month": "1963-04-01",
    "price": 68.76,
    "nominalPricePlusDividend": 8183.2127,
    "realPrice": 709.5187,
    "realPricePlusDividend": 84093.8222
  },
  {
    "month": "1963-05-01",
    "price": 70.14,
    "nominalPricePlusDividend": 8368.9364,
    "realPrice": 723.7586,
    "realPricePlusDividend": 86003.7568
  },
  {
    "month": "1963-06-01",
    "price": 70.11,
    "nominalPricePlusDividend": 8387.066,
    "realPrice": 721.0848,
    "realPricePlusDividend": 85909.7643
  },
  {
    "month": "1963-07-01",
    "price": 69.07,
    "nominalPricePlusDividend": 8284.5853,
    "realPrice": 708.0744,
    "realPricePlusDividend": 84583.6304
  },
  {
    "month": "1963-08-01",
    "price": 70.98,
    "nominalPricePlusDividend": 8535.703,
    "realPrice": 727.6548,
    "realPricePlusDividend": 87147.4876
  },
  {
    "month": "1963-09-01",
    "price": 72.85,
    "nominalPricePlusDividend": 8782.6935,
    "realPrice": 746.8252,
    "realPricePlusDividend": 89669.2064
  },
  {
    "month": "1963-10-01",
    "price": 73.03,
    "nominalPricePlusDividend": 8826.597,
    "realPrice": 746.2397,
    "realPricePlusDividend": 89826.9064
  },
  {
    "month": "1963-11-01",
    "price": 72.62,
    "nominalPricePlusDividend": 8799.5371,
    "realPrice": 742.0503,
    "realPricePlusDividend": 89553.5711
  },
  {
    "month": "1963-12-01",
    "price": 74.17,
    "nominalPricePlusDividend": 9010.1415,
    "realPrice": 755.4359,
    "realPricePlusDividend": 91402.1965
  },
  {
    "month": "1964-01-01",
    "price": 76.45,
    "nominalPricePlusDividend": 9310.1961,
    "realPrice": 778.6581,
    "realPricePlusDividend": 94447.4221
  },
  {
    "month": "1964-02-01",
    "price": 77.39,
    "nominalPricePlusDividend": 9447.9783,
    "realPrice": 788.2322,
    "realPricePlusDividend": 95846.5175
  },
  {
    "month": "1964-03-01",
    "price": 78.8,
    "nominalPricePlusDividend": 9643.6497,
    "realPrice": 802.5933,
    "realPricePlusDividend": 97832.8996
  },
  {
    "month": "1964-04-01",
    "price": 79.94,
    "nominalPricePlusDividend": 9806.9268,
    "realPrice": 814.2044,
    "realPricePlusDividend": 99490.6769
  },
  {
    "month": "1964-05-01",
    "price": 80.72,
    "nominalPricePlusDividend": 9926.6066,
    "realPrice": 822.1489,
    "realPricePlusDividend": 100706.1848
  },
  {
    "month": "1964-06-01",
    "price": 80.24,
    "nominalPricePlusDividend": 9891.7976,
    "realPrice": 814.6237,
    "realPricePlusDividend": 100030.6859
  },
  {
    "month": "1964-07-01",
    "price": 83.22,
    "nominalPricePlusDividend": 10283.615,
    "realPrice": 842.161,
    "realPricePlusDividend": 103660.254
  },
  {
    "month": "1964-08-01",
    "price": 82,
    "nominalPricePlusDividend": 10157.5722,
    "realPrice": 832.4918,
    "realPricePlusDividend": 102721.722
  },
  {
    "month": "1964-09-01",
    "price": 83.41,
    "nominalPricePlusDividend": 10357.2139,
    "realPrice": 844.0837,
    "realPricePlusDividend": 104405.5801
  },
  {
    "month": "1964-10-01",
    "price": 84.85,
    "nominalPricePlusDividend": 10561.2704,
    "realPrice": 858.6561,
    "realPricePlusDividend": 106464.2703
  },
  {
    "month": "1964-11-01",
    "price": 85.44,
    "nominalPricePlusDividend": 10660.224,
    "realPrice": 861.8555,
    "realPricePlusDividend": 107119.056
  },
  {
    "month": "1964-12-01",
    "price": 83.96,
    "nominalPricePlusDividend": 10501.352,
    "realPrice": 846.9263,
    "realPricePlusDividend": 105524.3355
  },
  {
    "month": "1965-01-01",
    "price": 86.12,
    "nominalPricePlusDividend": 10797.5729,
    "realPrice": 868.7148,
    "realPricePlusDividend": 108502.307
  },
  {
    "month": "1965-02-01",
    "price": 86.75,
    "nominalPricePlusDividend": 10902.8558,
    "realPrice": 875.0698,
    "realPricePlusDividend": 109561.6243
  },
  {
    "month": "1965-03-01",
    "price": 86.83,
    "nominalPricePlusDividend": 10939.443,
    "realPrice": 873.0784,
    "realPricePlusDividend": 109579.4244
  },
  {
    "month": "1965-04-01",
    "price": 87.97,
    "nominalPricePlusDividend": 11109.8403,
    "realPrice": 881.7242,
    "realPricePlusDividend": 110933.5599
  },
  {
    "month": "1965-05-01",
    "price": 89.28,
    "nominalPricePlusDividend": 11302.3292,
    "realPrice": 894.8543,
    "realPricePlusDividend": 112857.2898
  },
  {
    "month": "1965-06-01",
    "price": 85.04,
    "nominalPricePlusDividend": 10792.8931,
    "realPrice": 846.9621,
    "realPricePlusDividend": 107090.007
  },
  {
    "month": "1965-07-01",
    "price": 84.91,
    "nominalPricePlusDividend": 10803.9982,
    "realPrice": 845.6673,
    "realPricePlusDividend": 107201.5343
  },
  {
    "month": "1965-08-01",
    "price": 86.49,
    "nominalPricePlusDividend": 11032.8899,
    "realPrice": 861.4035,
    "realPricePlusDividend": 109474.0275
  },
  {
    "month": "1965-09-01",
    "price": 89.38,
    "nominalPricePlusDividend": 11429.645,
    "realPrice": 890.1866,
    "realPricePlusDividend": 113412.1775
  },
  {
    "month": "1965-10-01",
    "price": 91.39,
    "nominalPricePlusDividend": 11715.0238,
    "realPrice": 907.334,
    "realPricePlusDividend": 115878.8749
  },
  {
    "month": "1965-11-01",
    "price": 92.15,
    "nominalPricePlusDividend": 11841.0745,
    "realPrice": 914.8794,
    "realPricePlusDividend": 117127.3914
  },
  {
    "month": "1965-12-01",
    "price": 91.73,
    "nominalPricePlusDividend": 11816.0174,
    "realPrice": 907.8458,
    "realPricePlusDividend": 116513.6753
  },
  {
    "month": "1966-01-01",
    "price": 93.32,
    "nominalPricePlusDividend": 12050.0277,
    "realPrice": 923.5819,
    "realPricePlusDividend": 118822.8559
  },
  {
    "month": "1966-02-01",
    "price": 92.69,
    "nominalPricePlusDividend": 11998.1622,
    "realPrice": 911.6134,
    "realPricePlusDividend": 117573.65
  },
  {
    "month": "1966-03-01",
    "price": 88.88,
    "nominalPricePlusDividend": 11534.7527,
    "realPrice": 871.4186,
    "realPricePlusDividend": 112682.1051
  },
  {
    "month": "1966-04-01",
    "price": 91.6,
    "nominalPricePlusDividend": 11917.8169,
    "realPrice": 892.5257,
    "realPricePlusDividend": 115704.6501
  },
  {
    "month": "1966-05-01",
    "price": 86.78,
    "nominalPricePlusDividend": 11321.0226,
    "realPrice": 845.5609,
    "realPricePlusDividend": 109911.9593
  },
  {
    "month": "1966-06-01",
    "price": 86.06,
    "nominalPricePlusDividend": 11257.6786,
    "realPrice": 835.9574,
    "realPricePlusDividend": 108960.9493
  },
  {
    "month": "1966-07-01",
    "price": 85.84,
    "nominalPricePlusDividend": 11259.7498,
    "realPrice": 831.2548,
    "realPricePlusDividend": 108647.3277
  },
  {
    "month": "1966-08-01",
    "price": 80.65,
    "nominalPricePlusDividend": 10610.1236,
    "realPrice": 776.2193,
    "realPricePlusDividend": 101754.4474
  },
  {
    "month": "1966-09-01",
    "price": 77.81,
    "nominalPricePlusDividend": 10267.9642,
    "realPrice": 748.8856,
    "realPricePlusDividend": 98474.6804
  },
  {
    "month": "1966-10-01",
    "price": 77.13,
    "nominalPricePlusDividend": 10210.0108,
    "realPrice": 737.8282,
    "realPricePlusDividend": 97322.4802
  },
  {
    "month": "1966-11-01",
    "price": 80.99,
    "nominalPricePlusDividend": 10752.7812,
    "realPrice": 774.753,
    "realPricePlusDividend": 102495.0521
  },
  {
    "month": "1966-12-01",
    "price": 81.33,
    "nominalPricePlusDividend": 10829.7491,
    "realPrice": 778.0055,
    "realPricePlusDividend": 103227.5532
  },
  {
    "month": "1967-01-01",
    "price": 84.45,
    "nominalPricePlusDividend": 11277.0494,
    "realPrice": 807.8515,
    "realPricePlusDividend": 107491.7576
  },
  {
    "month": "1967-02-01",
    "price": 87.36,
    "nominalPricePlusDividend": 11697.6853,
    "realPrice": 835.6887,
    "realPricePlusDividend": 111501.8241
  },
  {
    "month": "1967-03-01",
    "price": 89.42,
    "nominalPricePlusDividend": 12005.7717,
    "realPrice": 852.8026,
    "realPricePlusDividend": 114092.3096
  },
  {
    "month": "1967-04-01",
    "price": 90.96,
    "nominalPricePlusDividend": 12244.9831,
    "realPrice": 864.8688,
    "realPricePlusDividend": 116013.5499
  },
  {
    "month": "1967-05-01",
    "price": 92.59,
    "nominalPricePlusDividend": 12496.9458,
    "realPrice": 877.7156,
    "realPricePlusDividend": 118043.653
  },
  {
    "month": "1967-06-01",
    "price": 91.43,
    "nominalPricePlusDividend": 12372.9976,
    "realPrice": 864.1165,
    "realPricePlusDividend": 116521.4369
  },
  {
    "month": "1967-07-01",
    "price": 93.01,
    "nominalPricePlusDividend": 12619.5193,
    "realPrice": 876.4174,
    "realPricePlusDividend": 118487.4607
  },
  {
    "month": "1967-08-01",
    "price": 94.49,
    "nominalPricePlusDividend": 12853.189,
    "realPrice": 887.7053,
    "realPricePlusDividend": 120321.4407
  },
  {
    "month": "1967-09-01",
    "price": 95.81,
    "nominalPricePlusDividend": 13065.7689,
    "realPrice": 897.4275,
    "realPricePlusDividend": 121947.6705
  },
  {
    "month": "1967-10-01",
    "price": 95.66,
    "nominalPricePlusDividend": 13078.4969,
    "realPrice": 893.3636,
    "realPricePlusDividend": 121703.7917
  },
  {
    "month": "1967-11-01",
    "price": 92.66,
    "nominalPricePlusDividend": 12701.6094,
    "realPrice": 862.7866,
    "realPricePlusDividend": 117846.4591
  },
  {
    "month": "1967-12-01",
    "price": 95.3,
    "nominalPricePlusDividend": 13096.8498,
    "realPrice": 884.7509,
    "realPricePlusDividend": 121154.6224
  },
  {
    "month": "1968-01-01",
    "price": 95.04,
    "nominalPricePlusDividend": 13094.5593,
    "realPrice": 877.1621,
    "realPricePlusDividend": 120423.5684
  },
  {
    "month": "1968-02-01",
    "price": 90.75,
    "nominalPricePlusDividend": 12537.1266,
    "realPrice": 835.1189,
    "realPricePlusDividend": 114960.6281
  },
  {
    "month": "1968-03-01",
    "price": 89.09,
    "nominalPricePlusDividend": 12341.6442,
    "realPrice": 817.4527,
    "realPricePlusDividend": 112838.7837
  },
  {
    "month": "1968-04-01",
    "price": 95.67,
    "nominalPricePlusDividend": 13287.2273,
    "realPrice": 875.2762,
    "realPricePlusDividend": 121131.9716
  },
  {
    "month": "1968-05-01",
    "price": 97.87,
    "nominalPricePlusDividend": 13627.0737,
    "realPrice": 892.8084,
    "realPricePlusDividend": 123871.005
  },
  {
    "month": "1968-06-01",
    "price": 100.5,
    "nominalPricePlusDividend": 14027.8041,
    "realPrice": 911.5162,
    "realPricePlusDividend": 126779.6529
  },
  {
    "month": "1968-07-01",
    "price": 100.3,
    "nominalPricePlusDividend": 14034.6668,
    "realPrice": 904.489,
    "realPricePlusDividend": 126115.7162
  },
  {
    "month": "1968-08-01",
    "price": 98.11,
    "nominalPricePlusDividend": 13763.2474,
    "realPrice": 882.2121,
    "realPricePlusDividend": 123324.3012
  },
  {
    "month": "1968-09-01",
    "price": 101.3,
    "nominalPricePlusDividend": 14246.0187,
    "realPrice": 908.3017,
    "realPricePlusDividend": 127287.3746
  },
  {
    "month": "1968-10-01",
    "price": 103.8,
    "nominalPricePlusDividend": 14633.1082,
    "realPrice": 925.4446,
    "realPricePlusDividend": 130006.1437
  },
  {
    "month": "1968-11-01",
    "price": 105.4,
    "nominalPricePlusDividend": 14894.4193,
    "realPrice": 937.0551,
    "realPricePlusDividend": 131954.8395
  },
  {
    "month": "1968-12-01",
    "price": 106.5,
    "nominalPricePlusDividend": 15085.8595,
    "realPrice": 944.1675,
    "realPricePlusDividend": 133275.306
  },
  {
    "month": "1969-01-01",
    "price": 102,
    "nominalPricePlusDividend": 14484.668,
    "realPrice": 901.733,
    "realPricePlusDividend": 127605.2216
  },
  {
    "month": "1969-02-01",
    "price": 101.5,
    "nominalPricePlusDividend": 14450.113,
    "realPrice": 892.2998,
    "realPricePlusDividend": 126590.1866
  },
  {
    "month": "1969-03-01",
    "price": 99.3,
    "nominalPricePlusDividend": 14173.5678,
    "realPrice": 865.7048,
    "realPricePlusDividend": 123136.2049
  },
  {
    "month": "1969-04-01",
    "price": 101.3,
    "nominalPricePlusDividend": 14495.9106,
    "realPrice": 878.2752,
    "realPricePlusDividend": 125243.3206
  },
  {
    "month": "1969-05-01",
    "price": 104.6,
    "nominalPricePlusDividend": 15005.2231,
    "realPrice": 904.3949,
    "realPricePlusDividend": 129288.1204
  },
  {
    "month": "1969-06-01",
    "price": 99.14,
    "nominalPricePlusDividend": 14259.2656,
    "realPrice": 852.5024,
    "realPricePlusDividend": 122189.9722
  },
  {
    "month": "1969-07-01",
    "price": 94.71,
    "nominalPricePlusDividend": 13659.6161,
    "realPrice": 809.9828,
    "realPricePlusDividend": 116415.5331
  },
  {
    "month": "1969-08-01",
    "price": 94.18,
    "nominalPricePlusDividend": 13620.8755,
    "realPrice": 801.0964,
    "realPricePlusDividend": 115458.0762
  },
  {
    "month": "1969-09-01",
    "price": 94.51,
    "nominalPricePlusDividend": 13706.486,
    "realPrice": 801.7365,
    "realPricePlusDividend": 115870.7968
  },
  {
    "month": "1969-10-01",
    "price": 95.52,
    "nominalPricePlusDividend": 13891.0326,
    "realPrice": 805.9596,
    "realPricePlusDividend": 116801.1081
  },
  {
    "month": "1969-11-01",
    "price": 96.21,
    "nominalPricePlusDividend": 14029.5907,
    "realPrice": 807.452,
    "realPricePlusDividend": 117336.8669
  },
  {
    "month": "1969-12-01",
    "price": 91.11,
    "nominalPricePlusDividend": 13324.255,
    "realPrice": 760.5933,
    "realPricePlusDividend": 110846.4523
  },
  {
    "month": "1970-01-01",
    "price": 90.31,
    "nominalPricePlusDividend": 13245.7709,
    "realPrice": 751.9203,
    "realPricePlusDividend": 109901.8754
  },
  {
    "month": "1970-02-01",
    "price": 87.16,
    "nominalPricePlusDividend": 12822.4241,
    "realPrice": 721.874,
    "realPricePlusDividend": 105829.2304
  },
  {
    "month": "1970-03-01",
    "price": 88.65,
    "nominalPricePlusDividend": 13080.4451,
    "realPrice": 730.3704,
    "realPricePlusDividend": 107393.4252
  },
  {
    "month": "1970-04-01",
    "price": 85.95,
    "nominalPricePlusDividend": 12721.0341,
    "realPrice": 702.6078,
    "realPricePlusDividend": 103628.6019
  },
  {
    "month": "1970-05-01",
    "price": 76.06,
    "nominalPricePlusDividend": 11296.4032,
    "realPrice": 620.1501,
    "realPricePlusDividend": 91784.6755
  },
  {
    "month": "1970-06-01",
    "price": 75.59,
    "nominalPricePlusDividend": 11265.9155,
    "realPrice": 613.1411,
    "realPricePlusDividend": 91064.9789
  },
  {
    "month": "1970-07-01",
    "price": 75.72,
    "nominalPricePlusDividend": 11324.7862,
    "realPrice": 611.0458,
    "realPricePlusDividend": 91071.2639
  },
  {
    "month": "1970-08-01",
    "price": 77.92,
    "nominalPricePlusDividend": 11693.4965,
    "realPrice": 628.7994,
    "realPricePlusDividend": 94036.2048
  },
  {
    "month": "1970-09-01",
    "price": 82.58,
    "nominalPricePlusDividend": 12432.6773,
    "realPrice": 663.0047,
    "realPricePlusDividend": 99470.2679
  },
  {
    "month": "1970-10-01",
    "price": 84.37,
    "nominalPricePlusDividend": 12742.1894,
    "realPrice": 673.9375,
    "realPricePlusDividend": 101426.9539
  },
  {
    "month": "1970-11-01",
    "price": 84.28,
    "nominalPricePlusDividend": 12768.5353,
    "realPrice": 669.8185,
    "realPricePlusDividend": 101121.2203
  },
  {
    "month": "1970-12-01",
    "price": 90.05,
    "nominalPricePlusDividend": 13682.5515,
    "realPrice": 712.0794,
    "realPricePlusDividend": 107813.1846
  },
  {
    "month": "1971-01-01",
    "price": 93.49,
    "nominalPricePlusDividend": 14244.9973,
    "realPrice": 739.2816,
    "realPricePlusDividend": 112243.5768
  },
  {
    "month": "1971-02-01",
    "price": 97.11,
    "nominalPricePlusDividend": 14836.3168,
    "realPrice": 765.9825,
    "realPricePlusDividend": 116608.4331
  },
  {
    "month": "1971-03-01",
    "price": 99.6,
    "nominalPricePlusDividend": 15256.4576,
    "realPrice": 783.659,
    "realPricePlusDividend": 119609.3613
  },
  {
    "month": "1971-04-01",
    "price": 103,
    "nominalPricePlusDividend": 15816.9588,
    "realPrice": 808.3895,
    "realPricePlusDividend": 123693.6147
  },
  {
    "month": "1971-05-01",
    "price": 101.6,
    "nominalPricePlusDividend": 15641.7267,
    "realPrice": 793.4443,
    "realPricePlusDividend": 121715.3892
  },
  {
    "month": "1971-06-01",
    "price": 99.72,
    "nominalPricePlusDividend": 15392.1074,
    "realPrice": 773.0081,
    "realPricePlusDividend": 118887.1786
  },
  {
    "month": "1971-07-01",
    "price": 99,
    "nominalPricePlusDividend": 15320.8476,
    "realPrice": 765.5412,
    "realPricePlusDividend": 118045.2349
  },
  {
    "month": "1971-08-01",
    "price": 97.24,
    "nominalPricePlusDividend": 15088.4127,
    "realPrice": 750.0886,
    "realPricePlusDividend": 115968.6284
  },
  {
    "month": "1971-09-01",
    "price": 99.4,
    "nominalPricePlusDividend": 15463.5713,
    "realPrice": 766.7504,
    "realPricePlusDividend": 118851.2873
  },
  {
    "month": "1971-10-01",
    "price": 97.29,
    "nominalPricePlusDividend": 15175.3795,
    "realPrice": 748.6394,
    "realPricePlusDividend": 116349.9842
  },
  {
    "month": "1971-11-01",
    "price": 92.78,
    "nominalPricePlusDividend": 14511.9841,
    "realPrice": 713.9353,
    "realPricePlusDividend": 111262.5969
  },
  {
    "month": "1971-12-01",
    "price": 99.17,
    "nominalPricePlusDividend": 15551.5648,
    "realPrice": 759.3925,
    "realPricePlusDividend": 118651.679
  },
  {
    "month": "1972-01-01",
    "price": 103.3,
    "nominalPricePlusDividend": 16239.339,
    "realPrice": 791.0179,
    "realPricePlusDividend": 123898.6423
  },
  {
    "month": "1972-02-01",
    "price": 105.2,
    "nominalPricePlusDividend": 16578.2481,
    "realPrice": 801.666,
    "realPricePlusDividend": 125871.3926
  },
  {
    "month": "1972-03-01",
    "price": 107.7,
    "nominalPricePlusDividend": 17012.5341,
    "realPrice": 818.7346,
    "realPricePlusDividend": 128856.2807
  },
  {
    "month": "1972-04-01",
    "price": 108.8,
    "nominalPricePlusDividend": 17226.7046,
    "realPrice": 825.1038,
    "realPricePlusDividend": 130163.59
  },
  {
    "month": "1972-05-01",
    "price": 107.7,
    "nominalPricePlusDividend": 17093.0446,
    "realPrice": 814.7984,
    "realPricePlusDividend": 128842.7462
  },
  {
    "month": "1972-06-01",
    "price": 108,
    "nominalPricePlusDividend": 17181.2608,
    "realPrice": 815.1086,
    "realPricePlusDividend": 129196.6719
  },
  {
    "month": "1972-07-01",
    "price": 107.2,
    "nominalPricePlusDividend": 17094.6916,
    "realPrice": 805.2089,
    "realPricePlusDividend": 127931.9978
  },
  {
    "month": "1972-08-01",
    "price": 111,
    "nominalPricePlusDividend": 17741.501,
    "realPrice": 831.7666,
    "realPricePlusDividend": 132456.2946
  },
  {
    "month": "1972-09-01",
    "price": 109.4,
    "nominalPricePlusDividend": 17526.7472,
    "realPrice": 817.83,
    "realPricePlusDividend": 130542.0252
  },
  {
    "month": "1972-10-01",
    "price": 109.6,
    "nominalPricePlusDividend": 17599.9088,
    "realPrice": 815.4512,
    "realPricePlusDividend": 130469.0004
  },
  {
    "month": "1972-11-01",
    "price": 115.1,
    "nominalPricePlusDividend": 18524.6444,
    "realPrice": 854.3528,
    "realPricePlusDividend": 137002.0839
  },
  {
    "month": "1972-12-01",
    "price": 117.5,
    "nominalPricePlusDividend": 18952.8447,
    "realPrice": 870.1151,
    "realPricePlusDividend": 139840.946
  },
  {
    "month": "1973-01-01",
    "price": 118.4,
    "nominalPricePlusDividend": 19140.3569,
    "realPrice": 874.7217,
    "realPricePlusDividend": 140893.1614
  },
  {
    "month": "1973-02-01",
    "price": 114.2,
    "nominalPricePlusDividend": 18503.9167,
    "realPrice": 837.7928,
    "realPricePlusDividend": 135255.9793
  },
  {
    "month": "1973-03-01",
    "price": 112.4,
    "nominalPricePlusDividend": 18254.9744,
    "realPrice": 816.9702,
    "realPricePlusDividend": 132203.8369
  },
  {
    "month": "1973-04-01",
    "price": 110.3,
    "nominalPricePlusDividend": 17956.8152,
    "realPrice": 796.1902,
    "realPricePlusDividend": 129150.9062
  },
  {
    "month": "1973-05-01",
    "price": 107.2,
    "nominalPricePlusDividend": 17495.3683,
    "realPrice": 768.5251,
    "realPricePlusDividend": 124973.2921
  },
  {
    "month": "1973-06-01",
    "price": 104.8,
    "nominalPricePlusDividend": 17147.2471,
    "realPrice": 746.2199,
    "realPricePlusDividend": 121656.3744
  },
  {
    "month": "1973-07-01",
    "price": 105.8,
    "nominalPricePlusDividend": 17354.7702,
    "realPrice": 751.6397,
    "realPricePlusDividend": 122851.9122
  },
  {
    "month": "1973-08-01",
    "price": 103.8,
    "nominalPricePlusDividend": 17070.9463,
    "realPrice": 724.3502,
    "realPricePlusDividend": 118700.3351
  },
  {
    "month": "1973-09-01",
    "price": 105.6,
    "nominalPricePlusDividend": 17411.5612,
    "realPrice": 735.2809,
    "realPricePlusDividend": 120802.0223
  },
  {
    "month": "1973-10-01",
    "price": 109.8,
    "nominalPricePlusDividend": 18148.9968,
    "realPrice": 757.8187,
    "realPricePlusDividend": 124816.8302
  },
  {
    "month": "1973-11-01",
    "price": 102,
    "nominalPricePlusDividend": 16905.2709,
    "realPrice": 699.3833,
    "realPricePlusDividend": 115506.3945
  },
  {
    "month": "1973-12-01",
    "price": 94.78,
    "nominalPricePlusDividend": 15754.8193,
    "realPrice": 645.658,
    "realPricePlusDividend": 106949.8246
  },
  {
    "month": "1974-01-01",
    "price": 96.11,
    "nominalPricePlusDividend": 16022.7188,
    "realPrice": 649.0983,
    "realPricePlusDividend": 107836.1891
  },
  {
    "month": "1974-02-01",
    "price": 93.45,
    "nominalPricePlusDividend": 15626.4992,
    "realPrice": 623.1105,
    "realPricePlusDividend": 103834.0258
  },
  {
    "month": "1974-03-01",
    "price": 97.44,
    "nominalPricePlusDividend": 16341.3551,
    "realPrice": 641.5598,
    "realPricePlusDividend": 107222.4386
  },
  {
    "month": "1974-04-01",
    "price": 92.46,
    "nominalPricePlusDividend": 15554.251,
    "realPrice": 606.2342,
    "realPricePlusDividend": 101634.0356
  },
  {
    "month": "1974-05-01",
    "price": 89.67,
    "nominalPricePlusDividend": 15133.4036,
    "realPrice": 580.6824,
    "realPricePlusDividend": 97664.6987
  },
  {
    "month": "1974-06-01",
    "price": 89.79,
    "nominalPricePlusDividend": 15202.5984,
    "realPrice": 576.7129,
    "realPricePlusDividend": 97311.6767
  },
  {
    "month": "1974-07-01",
    "price": 79.31,
    "nominalPricePlusDividend": 13477.5829,
    "realPrice": 505.2761,
    "realPricePlusDividend": 85573.5461
  },
  {
    "month": "1974-08-01",
    "price": 76.03,
    "nominalPricePlusDividend": 12970.1839,
    "realPrice": 478.567,
    "realPricePlusDividend": 81365.877
  },
  {
    "month": "1974-09-01",
    "price": 68.12,
    "nominalPricePlusDividend": 11671.4027,
    "realPrice": 423.6936,
    "realPricePlusDividend": 72352.2037
  },
  {
    "month": "1974-10-01",
    "price": 69.44,
    "nominalPricePlusDividend": 11948.8241,
    "realPrice": 427.6777,
    "realPricePlusDividend": 73347.0159
  },
  {
    "month": "1974-11-01",
    "price": 71.74,
    "nominalPricePlusDividend": 12396.1211,
    "realPrice": 438.4115,
    "realPricePlusDividend": 75501.5301
  },
  {
    "month": "1974-12-01",
    "price": 67.07,
    "nominalPricePlusDividend": 11640.9707,
    "realPrice": 406.7136,
    "realPricePlusDividend": 70355.4789
  },
  {
    "month": "1975-01-01",
    "price": 72.56,
    "nominalPricePlusDividend": 12645.9091,
    "realPrice": 438.316,
    "realPricePlusDividend": 76137.2753
  },
  {
    "month": "1975-02-01",
    "price": 80.1,
    "nominalPricePlusDividend": 14012.6196,
    "realPrice": 480.1766,
    "realPricePlusDividend": 83724.602
  },
  {
    "month": "1975-03-01",
    "price": 83.78,
    "nominalPricePlusDividend": 14709.5574,
    "realPrice": 500.3311,
    "realPricePlusDividend": 87556.7732
  },
  {
    "month": "1975-04-01",
    "price": 84.72,
    "nominalPricePlusDividend": 14928.2929,
    "realPrice": 504.032,
    "realPricePlusDividend": 88523.4996
  },
  {
    "month": "1975-05-01",
    "price": 90.1,
    "nominalPricePlusDividend": 15930.3747,
    "realPrice": 533.0169,
    "realPricePlusDividend": 93933.7362
  },
  {
    "month": "1975-06-01",
    "price": 92.4,
    "nominalPricePlusDividend": 16391.4991,
    "realPrice": 542.544,
    "realPricePlusDividend": 95932.1487
  },
  {
    "month": "1975-07-01",
    "price": 92.49,
    "nominalPricePlusDividend": 16462.3101,
    "realPrice": 537.0606,
    "realPricePlusDividend": 95279.5349
  },
  {
    "month": "1975-08-01",
    "price": 85.71,
    "nominalPricePlusDividend": 15310.5654,
    "realPrice": 496.7747,
    "realPricePlusDividend": 88449.8735
  },
  {
    "month": "1975-09-01",
    "price": 84.67,
    "nominalPricePlusDividend": 15180.0151,
    "realPrice": 488.0504,
    "realPricePlusDividend": 87213.3615
  },
  {
    "month": "1975-10-01",
    "price": 88.57,
    "nominalPricePlusDividend": 15934.6532,
    "realPrice": 507.7408,
    "realPricePlusDividend": 91047.3744
  },
  {
    "month": "1975-11-01",
    "price": 90.07,
    "nominalPricePlusDividend": 16259.991,
    "realPrice": 512.605,
    "realPricePlusDividend": 92232.9546
  },
  {
    "month": "1975-12-01",
    "price": 88.7,
    "nominalPricePlusDividend": 16068.1819,
    "realPrice": 502.9889,
    "realPricePlusDividend": 90815.1738
  },
  {
    "month": "1976-01-01",
    "price": 96.86,
    "nominalPricePlusDividend": 17601.9355,
    "realPrice": 548.2738,
    "realPricePlusDividend": 99304.6293
  },
  {
    "month": "1976-02-01",
    "price": 100.6,
    "nominalPricePlusDividend": 18337.3686,
    "realPrice": 567.4029,
    "realPricePlusDividend": 103082.7293
  },
  {
    "month": "1976-03-01",
    "price": 101.1,
    "nominalPricePlusDividend": 18484.5091,
    "realPrice": 569.2029,
    "realPricePlusDividend": 103723.8042
  },
  {
    "month": "1976-04-01",
    "price": 101.9,
    "nominalPricePlusDividend": 18686.9977,
    "realPrice": 571.6617,
    "realPricePlusDividend": 104487.7312
  },
  {
    "month": "1976-05-01",
    "price": 101.2,
    "nominalPricePlusDividend": 18615.3753,
    "realPrice": 563.7153,
    "realPricePlusDividend": 103351.8652
  },
  {
    "month": "1976-06-01",
    "price": 101.8,
    "nominalPricePlusDividend": 18783.0221,
    "realPrice": 564.0625,
    "realPricePlusDividend": 103733.3468
  },
  {
    "month": "1976-07-01",
    "price": 104.2,
    "nominalPricePlusDividend": 19283.6567,
    "realPrice": 574.3272,
    "realPricePlusDividend": 105940.7335
  },
  {
    "month": "1976-08-01",
    "price": 103.3,
    "nominalPricePlusDividend": 19175.5485,
    "realPrice": 566.3908,
    "realPricePlusDividend": 104798.2646
  },
  {
    "month": "1976-09-01",
    "price": 105.5,
    "nominalPricePlusDividend": 19643.026,
    "realPrice": 576.4449,
    "realPricePlusDividend": 106982.4151
  },
  {
    "month": "1976-10-01",
    "price": 101.9,
    "nominalPricePlusDividend": 19032.4785,
    "realPrice": 553.8899,
    "realPricePlusDividend": 103125.203
  },
  {
    "month": "1976-11-01",
    "price": 101.2,
    "nominalPricePlusDividend": 18962.697,
    "realPrice": 549.1365,
    "realPricePlusDividend": 102575.0633
  },
  {
    "month": "1976-12-01",
    "price": 104.7,
    "nominalPricePlusDividend": 19680.7207,
    "realPrice": 566.176,
    "realPricePlusDividend": 106098.3406
  },
  {
    "month": "1977-01-01",
    "price": 103.8,
    "nominalPricePlusDividend": 19574.9861,
    "realPrice": 558.4307,
    "realPricePlusDividend": 104990.5662
  },
  {
    "month": "1977-02-01",
    "price": 101,
    "nominalPricePlusDividend": 19111.3323,
    "realPrice": 537.8506,
    "realPricePlusDividend": 101466.4873
  },
  {
    "month": "1977-03-01",
    "price": 100.6,
    "nominalPricePlusDividend": 19100.9776,
    "realPrice": 532.1191,
    "realPricePlusDividend": 100733.1167
  },
  {
    "month": "1977-04-01",
    "price": 99.05,
    "nominalPricePlusDividend": 18872.9747,
    "realPrice": 519.5544,
    "realPricePlusDividend": 98705.4388
  },
  {
    "month": "1977-05-01",
    "price": 98.76,
    "nominalPricePlusDividend": 18885.1482,
    "realPrice": 515.456,
    "realPricePlusDividend": 98281.8702
  },
  {
    "month": "1977-06-01",
    "price": 99.29,
    "nominalPricePlusDividend": 19055.0707,
    "realPrice": 514.8072,
    "realPricePlusDividend": 98516.8296
  },
  {
    "month": "1977-07-01",
    "price": 100.2,
    "nominalPricePlusDividend": 19299.4403,
    "realPrice": 516.9704,
    "realPricePlusDividend": 99292.8257
  },
  {
    "month": "1977-08-01",
    "price": 97.75,
    "nominalPricePlusDividend": 18898.2782,
    "realPrice": 502.6818,
    "realPricePlusDividend": 96914.4589
  },
  {
    "month": "1977-09-01",
    "price": 96.23,
    "nominalPricePlusDividend": 18676.1603,
    "realPrice": 493.2532,
    "realPricePlusDividend": 95466.7105
  },
  {
    "month": "1977-10-01",
    "price": 93.74,
    "nominalPricePlusDividend": 18265.6845,
    "realPrice": 478.93,
    "realPricePlusDividend": 93069.4535
  },
  {
    "month": "1977-11-01",
    "price": 94.28,
    "nominalPricePlusDividend": 18444.8968,
    "realPrice": 479.3544,
    "realPricePlusDividend": 93531.2082
  },
  {
    "month": "1977-12-01",
    "price": 93.82,
    "nominalPricePlusDividend": 18430.1151,
    "realPrice": 475.4793,
    "realPricePlusDividend": 93159.3638
  },
  {
    "month": "1978-01-01",
    "price": 90.25,
    "nominalPricePlusDividend": 17805.2683,
    "realPrice": 454.4593,
    "realPricePlusDividend": 89427.9086
  },
  {
    "month": "1978-02-01",
    "price": 88.98,
    "nominalPricePlusDividend": 17632.2026,
    "realPrice": 445.2148,
    "realPricePlusDividend": 87998.4812
  },
  {
    "month": "1978-03-01",
    "price": 88.82,
    "nominalPricePlusDividend": 17679.0453,
    "realPrice": 440.9093,
    "realPricePlusDividend": 87539.384
  },
  {
    "month": "1978-04-01",
    "price": 92.71,
    "nominalPricePlusDividend": 18532.942,
    "realPrice": 456.6185,
    "realPricePlusDividend": 91051.8767
  },
  {
    "month": "1978-05-01",
    "price": 97.41,
    "nominalPricePlusDividend": 19553.0546,
    "realPrice": 475.3042,
    "realPricePlusDividend": 95172.4335
  },
  {
    "month": "1978-06-01",
    "price": 97.66,
    "nominalPricePlusDividend": 19684.7553,
    "realPrice": 471.408,
    "realPricePlusDividend": 94787.1663
  },
  {
    "month": "1978-07-01",
    "price": 97.19,
    "nominalPricePlusDividend": 19672.4935,
    "realPrice": 465.5689,
    "realPricePlusDividend": 94009.5612
  },
  {
    "month": "1978-08-01",
    "price": 103.9,
    "nominalPricePlusDividend": 21114.122,
    "realPrice": 495.4495,
    "realPricePlusDividend": 100442.4331
  },
  {
    "month": "1978-09-01",
    "price": 103.9,
    "nominalPricePlusDividend": 21198.513,
    "realPrice": 491.7243,
    "realPricePlusDividend": 100088.0014
  },
  {
    "month": "1978-10-01",
    "price": 100.6,
    "nominalPricePlusDividend": 20610.5722,
    "realPrice": 471.8492,
    "realPricePlusDividend": 96442.6383
  },
  {
    "month": "1978-11-01",
    "price": 94.71,
    "nominalPricePlusDividend": 19489.8411,
    "realPrice": 442.2458,
    "realPricePlusDividend": 90793.2234
  },
  {
    "month": "1978-12-01",
    "price": 96.11,
    "nominalPricePlusDividend": 19864.5973,
    "realPrice": 446.7944,
    "realPricePlusDividend": 92129.678
  },
  {
    "month": "1979-01-01",
    "price": 99.71,
    "nominalPricePlusDividend": 20695.992,
    "realPrice": 459.458,
    "realPricePlusDividend": 95145.2064
  },
  {
    "month": "1979-02-01",
    "price": 98.23,
    "nominalPricePlusDividend": 20477.2448,
    "realPrice": 447.3978,
    "realPricePlusDividend": 93052.4751
  },
  {
    "month": "1979-03-01",
    "price": 100.1,
    "nominalPricePlusDividend": 20956.6501,
    "realPrice": 451.3427,
    "realPricePlusDividend": 94278.7268
  },
  {
    "month": "1979-04-01",
    "price": 102.1,
    "nominalPricePlusDividend": 21466.0858,
    "realPrice": 455.144,
    "realPricePlusDividend": 95479.2829
  },
  {
    "month": "1979-05-01",
    "price": 99.73,
    "nominalPricePlusDividend": 21059.7276,
    "realPrice": 438.9829,
    "realPricePlusDividend": 92495.7358
  },
  {
    "month": "1979-06-01",
    "price": 101.7,
    "nominalPricePlusDividend": 21568.8757,
    "realPrice": 442.7009,
    "realPricePlusDividend": 93686.6988
  },
  {
    "month": "1979-07-01",
    "price": 102.7,
    "nominalPricePlusDividend": 21875.3361,
    "realPrice": 442.1614,
    "realPricePlusDividend": 93981.6687
  },
  {
    "month": "1979-08-01",
    "price": 107.4,
    "nominalPricePlusDividend": 22972.2389,
    "realPrice": 458.0108,
    "realPricePlusDividend": 97761.7681
  },
  {
    "month": "1979-09-01",
    "price": 108.6,
    "nominalPricePlusDividend": 23326.1149,
    "realPrice": 458.1617,
    "realPricePlusDividend": 98206.8444
  },
  {
    "month": "1979-10-01",
    "price": 104.5,
    "nominalPricePlusDividend": 22544.103,
    "realPrice": 437.3471,
    "realPricePlusDividend": 94160.0185
  },
  {
    "month": "1979-11-01",
    "price": 103.7,
    "nominalPricePlusDividend": 22471.413,
    "realPrice": 429.9964,
    "realPricePlusDividend": 92993.6594
  },
  {
    "month": "1979-12-01",
    "price": 107.8,
    "nominalPricePlusDividend": 23461.0532,
    "realPrice": 442.3349,
    "realPricePlusDividend": 96079.2634
  },
  {
    "month": "1980-01-01",
    "price": 110.9,
    "nominalPricePlusDividend": 24238.1915,
    "realPrice": 448.6211,
    "realPricePlusDividend": 97861.4471
  },
  {
    "month": "1980-02-01",
    "price": 115.3,
    "nominalPricePlusDividend": 25303.6665,
    "realPrice": 459.9177,
    "realPricePlusDividend": 100741.9674
  },
  {
    "month": "1980-03-01",
    "price": 104.7,
    "nominalPricePlusDividend": 23082.5547,
    "realPrice": 411.3788,
    "realPricePlusDividend": 90525.216
  },
  {
    "month": "1980-04-01",
    "price": 103,
    "nominalPricePlusDividend": 22814.3238,
    "realPrice": 400.2027,
    "realPricePlusDividend": 88481.8259
  },
  {
    "month": "1980-05-01",
    "price": 107.7,
    "nominalPricePlusDividend": 23963.2848,
    "realPrice": 414.3718,
    "realPricePlusDividend": 92031.6514
  },
  {
    "month": "1980-06-01",
    "price": 114.6,
    "nominalPricePlusDividend": 25607.8093,
    "realPrice": 436.1209,
    "realPricePlusDividend": 97279.8709
  },
  {
    "month": "1980-07-01",
    "price": 119.8,
    "nominalPricePlusDividend": 26880.3789,
    "realPrice": 455.91,
    "realPricePlusDividend": 102116.5899
  },
  {
    "month": "1980-08-01",
    "price": 123.5,
    "nominalPricePlusDividend": 27822.4511,
    "realPrice": 466.6054,
    "realPricePlusDividend": 104936.5657
  },
  {
    "month": "1980-09-01",
    "price": 126.5,
    "nominalPricePlusDividend": 28611.4423,
    "realPrice": 473.9571,
    "realPricePlusDividend": 107015.504
  },
  {
    "month": "1980-10-01",
    "price": 130.2,
    "nominalPricePlusDividend": 29562.7068,
    "realPrice": 483.2178,
    "realPricePlusDividend": 109531.8378
  },
  {
    "month": "1980-11-01",
    "price": 135.7,
    "nominalPricePlusDividend": 30926.9356,
    "realPrice": 499.5069,
    "realPricePlusDividend": 113649.7163
  },
  {
    "month": "1980-12-01",
    "price": 133.5,
    "nominalPricePlusDividend": 30541.9633,
    "realPrice": 486.8535,
    "realPricePlusDividend": 111196.0508
  },
  {
    "month": "1981-01-01",
    "price": 133,
    "nominalPricePlusDividend": 30545.0137,
    "realPrice": 481.1275,
    "realPricePlusDividend": 110314.5056
  },
  {
    "month": "1981-02-01",
    "price": 128.4,
    "nominalPricePlusDividend": 29607.2281,
    "realPrice": 459.7312,
    "realPricePlusDividend": 105834.936
  },
  {
    "month": "1981-03-01",
    "price": 133.2,
    "nominalPricePlusDividend": 30833.9451,
    "realPrice": 473.684,
    "realPricePlusDividend": 109474.8348
  },
  {
    "month": "1981-04-01",
    "price": 134.4,
    "nominalPricePlusDividend": 31232.8727,
    "realPrice": 474.7329,
    "realPricePlusDividend": 110146.3268
  },
  {
    "month": "1981-05-01",
    "price": 131.7,
    "nominalPricePlusDividend": 30727.7529,
    "realPrice": 461.5696,
    "realPricePlusDividend": 107522.0916
  },
  {
    "month": "1981-06-01",
    "price": 132.3,
    "nominalPricePlusDividend": 30991.2706,
    "realPrice": 459.5782,
    "realPricePlusDividend": 107488.4563
  },
  {
    "month": "1981-07-01",
    "price": 129.1,
    "nominalPricePlusDividend": 30366.4088,
    "realPrice": 443.5663,
    "realPricePlusDividend": 104173.6853
  },
  {
    "month": "1981-08-01",
    "price": 129.6,
    "nominalPricePlusDividend": 30610.1188,
    "realPrice": 441.9072,
    "realPricePlusDividend": 104215.6056
  },
  {
    "month": "1981-09-01",
    "price": 118.3,
    "nominalPricePlusDividend": 28068.6576,
    "realPrice": 399.4815,
    "realPricePlusDividend": 94642.3282
  },
  {
    "month": "1981-10-01",
    "price": 119.8,
    "nominalPricePlusDividend": 28553.4727,
    "realPrice": 403.6805,
    "realPricePlusDividend": 96072.6653
  },
  {
    "month": "1981-11-01",
    "price": 122.9,
    "nominalPricePlusDividend": 29422.5635,
    "realPrice": 412.8004,
    "realPricePlusDividend": 98681.6883
  },
  {
    "month": "1981-12-01",
    "price": 123.8,
    "nominalPricePlusDividend": 29769.564,
    "realPrice": 414.4962,
    "realPricePlusDividend": 99528.6417
  },
  {
    "month": "1982-01-01",
    "price": 117.3,
    "nominalPricePlusDividend": 28339.3985,
    "realPrice": 391.4841,
    "realPricePlusDividend": 94447.0862
  },
  {
    "month": "1982-02-01",
    "price": 114.5,
    "nominalPricePlusDividend": 27797.0119,
    "realPrice": 380.9273,
    "realPricePlusDividend": 92347.0258
  },
  {
    "month": "1982-03-01",
    "price": 110.8,
    "nominalPricePlusDividend": 27034.1114,
    "realPrice": 369.008,
    "realPricePlusDividend": 89908.9091
  },
  {
    "month": "1982-04-01",
    "price": 116.3,
    "nominalPricePlusDividend": 28512.6918,
    "realPrice": 385.6926,
    "realPricePlusDividend": 94427.9646
  },
  {
    "month": "1982-05-01",
    "price": 116.4,
    "nominalPricePlusDividend": 28675.1137,
    "realPrice": 382.3977,
    "realPricePlusDividend": 94075.0424
  },
  {
    "month": "1982-06-01",
    "price": 109.7,
    "nominalPricePlusDividend": 27163.7578,
    "realPrice": 355.9284,
    "realPricePlusDividend": 88015.5529
  },
  {
    "month": "1982-07-01",
    "price": 109.4,
    "nominalPricePlusDividend": 27229.9958,
    "realPrice": 353.1348,
    "realPricePlusDividend": 87777.9254
  },
  {
    "month": "1982-08-01",
    "price": 109.7,
    "nominalPricePlusDividend": 27446.1957,
    "realPrice": 353.3783,
    "realPricePlusDividend": 88293.9583
  },
  {
    "month": "1982-09-01",
    "price": 122.4,
    "nominalPricePlusDividend": 30766.1902,
    "realPrice": 393.4835,
    "realPricePlusDividend": 98772.3416
  },
  {
    "month": "1982-10-01",
    "price": 132.7,
    "nominalPricePlusDividend": 33498.6586,
    "realPrice": 425.292,
    "realPricePlusDividend": 107215.9238
  },
  {
    "month": "1982-11-01",
    "price": 138.1,
    "nominalPricePlusDividend": 35006.0702,
    "realPrice": 443.5018,
    "realPricePlusDividend": 112268.9658
  },
  {
    "month": "1982-12-01",
    "price": 139.4,
    "nominalPricePlusDividend": 35480.5772,
    "realPrice": 449.5114,
    "realPricePlusDividend": 114256.8849
  },
  {
    "month": "1983-01-01",
    "price": 144.3,
    "nominalPricePlusDividend": 36873.4571,
    "realPrice": 464.3605,
    "realPricePlusDividend": 118499.7124
  },
  {
    "month": "1983-02-01",
    "price": 146.8,
    "nominalPricePlusDividend": 37658.867,
    "realPrice": 471.923,
    "realPricePlusDividend": 120900.3644
  },
  {
    "month": "1983-03-01",
    "price": 151.9,
    "nominalPricePlusDividend": 39114.6138,
    "realPrice": 488.3182,
    "realPricePlusDividend": 125574.1164
  },
  {
    "month": "1983-04-01",
    "price": 157.7,
    "nominalPricePlusDividend": 40756.4061,
    "realPrice": 503.3645,
    "realPricePlusDividend": 129916.0107
  },
  {
    "month": "1983-05-01",
    "price": 164.1,
    "nominalPricePlusDividend": 42559.4743,
    "realPrice": 520.6246,
    "realPricePlusDividend": 134842.9442
  },
  {
    "month": "1983-06-01",
    "price": 166.4,
    "nominalPricePlusDividend": 43305.7564,
    "realPrice": 526.3299,
    "realPricePlusDividend": 136793.708
  },
  {
    "month": "1983-07-01",
    "price": 167,
    "nominalPricePlusDividend": 43612.4188,
    "realPrice": 526.1127,
    "realPricePlusDividend": 137211.4467
  },
  {
    "month": "1983-08-01",
    "price": 162.4,
    "nominalPricePlusDividend": 42562.5869,
    "realPrice": 510.0892,
    "realPricePlusDividend": 133508.2455
  },
  {
    "month": "1983-09-01",
    "price": 167.2,
    "nominalPricePlusDividend": 43973.0404,
    "realPrice": 522.5581,
    "realPricePlusDividend": 137248.2728
  },
  {
    "month": "1983-10-01",
    "price": 167.7,
    "nominalPricePlusDividend": 44257.9535,
    "realPrice": 522.564,
    "realPricePlusDividend": 137728.5645
  },
  {
    "month": "1983-11-01",
    "price": 165.2,
    "nominalPricePlusDividend": 43752.7829,
    "realPrice": 513.7565,
    "realPricePlusDividend": 135888.7468
  },
  {
    "month": "1983-12-01",
    "price": 164.4,
    "nominalPricePlusDividend": 43696.7236,
    "realPrice": 510.7639,
    "realPricePlusDividend": 135581.9953
  },
  {
    "month": "1984-01-01",
    "price": 166.4,
    "nominalPricePlusDividend": 44385.3545,
    "realPrice": 513.9335,
    "realPricePlusDividend": 136909.0977
  },
  {
    "month": "1984-02-01",
    "price": 157.3,
    "nominalPricePlusDividend": 42116.2955,
    "realPrice": 483.4556,
    "realPricePlusDividend": 129277.0539
  },
  {
    "month": "1984-03-01",
    "price": 157.4,
    "nominalPricePlusDividend": 42302.6015,
    "realPrice": 482.8199,
    "realPricePlusDividend": 129597.1287
  },
  {
    "month": "1984-04-01",
    "price": 157.6,
    "nominalPricePlusDividend": 42517.1604,
    "realPrice": 481.0889,
    "realPricePlusDividend": 129624.9811
  },
  {
    "month": "1984-05-01",
    "price": 156.6,
    "nominalPricePlusDividend": 42409.7733,
    "realPrice": 476.6494,
    "realPricePlusDividend": 128924.6682
  },
  {
    "month": "1984-06-01",
    "price": 153.1,
    "nominalPricePlusDividend": 41625.9118,
    "realPrice": 464.6482,
    "realPricePlusDividend": 126177.8886
  },
  {
    "month": "1984-07-01",
    "price": 151.1,
    "nominalPricePlusDividend": 41247.7622,
    "realPrice": 456.8162,
    "realPricePlusDividend": 124552.0497
  },
  {
    "month": "1984-08-01",
    "price": 164.4,
    "nominalPricePlusDividend": 45045.2618,
    "realPrice": 495.1232,
    "realPricePlusDividend": 135499.2094
  },
  {
    "month": "1984-09-01",
    "price": 166.1,
    "nominalPricePlusDividend": 45679.0343,
    "realPrice": 497.861,
    "realPricePlusDividend": 136752.1723
  },
  {
    "month": "1984-10-01",
    "price": 164.8,
    "nominalPricePlusDividend": 45490.653,
    "realPrice": 492.5572,
    "realPricePlusDividend": 135802.8676
  },
  {
    "month": "1984-11-01",
    "price": 166.3,
    "nominalPricePlusDividend": 46075.6182,
    "realPrice": 497.0404,
    "realPricePlusDividend": 137551.8292
  },
  {
    "month": "1984-12-01",
    "price": 164.5,
    "nominalPricePlusDividend": 45749.6071,
    "realPrice": 491.6605,
    "realPricePlusDividend": 136581.2467
  },
  {
    "month": "1985-01-01",
    "price": 171.6,
    "nominalPricePlusDividend": 47898.7262,
    "realPrice": 511.9088,
    "realPricePlusDividend": 142728.374
  },
  {
    "month": "1985-02-01",
    "price": 180.9,
    "nominalPricePlusDividend": 50670.7983,
    "realPrice": 537.1066,
    "realPricePlusDividend": 150278.5779
  },
  {
    "month": "1985-03-01",
    "price": 179.4,
    "nominalPricePlusDividend": 50428.4306,
    "realPrice": 530.6505,
    "realPricePlusDividend": 148999.7162
  },
  {
    "month": "1985-04-01",
    "price": 180.6,
    "nominalPricePlusDividend": 50945.1768,
    "realPrice": 531.7014,
    "realPricePlusDividend": 149823.531
  },
  {
    "month": "1985-05-01",
    "price": 184.9,
    "nominalPricePlusDividend": 52338.8506,
    "realPrice": 542.3317,
    "realPricePlusDividend": 153349.4002
  },
  {
    "month": "1985-06-01",
    "price": 188.9,
    "nominalPricePlusDividend": 53653.0618,
    "realPrice": 552.5193,
    "realPricePlusDividend": 156762.7077
  },
  {
    "month": "1985-07-01",
    "price": 192.5,
    "nominalPricePlusDividend": 54858.7645,
    "realPrice": 562.0045,
    "realPricePlusDividend": 159989.6389
  },
  {
    "month": "1985-08-01",
    "price": 188.3,
    "nominalPricePlusDividend": 53846.45,
    "realPrice": 548.7245,
    "realPricePlusDividend": 156748.0259
  },
  {
    "month": "1985-09-01",
    "price": 184.1,
    "nominalPricePlusDividend": 52831.4475,
    "realPrice": 534.9992,
    "realPricePlusDividend": 153368.8135
  },
  {
    "month": "1985-10-01",
    "price": 186.2,
    "nominalPricePlusDividend": 53621.5756,
    "realPrice": 539.1107,
    "realPricePlusDividend": 155090.3019
  },
  {
    "month": "1985-11-01",
    "price": 197.5,
    "nominalPricePlusDividend": 57064.3573,
    "realPrice": 570.2541,
    "realPricePlusDividend": 164594.212
  },
  {
    "month": "1985-12-01",
    "price": 207.3,
    "nominalPricePlusDividend": 60085.6381,
    "realPrice": 596.9074,
    "realPricePlusDividend": 172833.5612
  },
  {
    "month": "1986-01-01",
    "price": 208.2,
    "nominalPricePlusDividend": 60537.319,
    "realPrice": 597.8579,
    "realPricePlusDividend": 173658.1131
  },
  {
    "month": "1986-02-01",
    "price": 219.4,
    "nominalPricePlusDividend": 63986.2791,
    "realPrice": 631.7485,
    "realPricePlusDividend": 184057.6062
  },
  {
    "month": "1986-03-01",
    "price": 232.3,
    "nominalPricePlusDividend": 67942.4044,
    "realPrice": 671.9672,
    "realPricePlusDividend": 196337.5886
  },
  {
    "month": "1986-04-01",
    "price": 238,
    "nominalPricePlusDividend": 69804.9953,
    "realPrice": 689.7233,
    "realPricePlusDividend": 202092.5683
  },
  {
    "month": "1986-05-01",
    "price": 238.5,
    "nominalPricePlusDividend": 70148.3173,
    "realPrice": 689.2683,
    "realPricePlusDividend": 202528.0877
  },
  {
    "month": "1986-06-01",
    "price": 245.3,
    "nominalPricePlusDividend": 72346.2325,
    "realPrice": 705.0359,
    "realPricePlusDividend": 207730.2942
  },
  {
    "month": "1986-07-01",
    "price": 240.2,
    "nominalPricePlusDividend": 71041.169,
    "realPrice": 690.3776,
    "realPricePlusDividend": 203985.2225
  },
  {
    "month": "1986-08-01",
    "price": 245,
    "nominalPricePlusDividend": 72661.5142,
    "realPrice": 702.8898,
    "realPricePlusDividend": 208259.6499
  },
  {
    "month": "1986-09-01",
    "price": 238.3,
    "nominalPricePlusDividend": 70876.7761,
    "realPrice": 680.566,
    "realPricePlusDividend": 202224.7871
  },
  {
    "month": "1986-10-01",
    "price": 237.4,
    "nominalPricePlusDividend": 70813.0773,
    "realPrice": 677.381,
    "realPricePlusDividend": 201860.1776
  },
  {
    "month": "1986-11-01",
    "price": 245.1,
    "nominalPricePlusDividend": 73314.8676,
    "realPrice": 698.7182,
    "realPricePlusDividend": 208802.8015
  },
  {
    "month": "1986-12-01",
    "price": 248.6,
    "nominalPricePlusDividend": 74567.7744,
    "realPrice": 708.0544,
    "realPricePlusDividend": 212179.2331
  },
  {
    "month": "1987-01-01",
    "price": 264.5,
    "nominalPricePlusDividend": 79543.9585,
    "realPrice": 748.598,
    "realPricePlusDividend": 224914.4873
  },
  {
    "month": "1987-02-01",
    "price": 280.9,
    "nominalPricePlusDividend": 84683.9919,
    "realPrice": 792.1644,
    "realPricePlusDividend": 238590.4879
  },
  {
    "month": "1987-03-01",
    "price": 292.5,
    "nominalPricePlusDividend": 88390.1099,
    "realPrice": 821.1983,
    "realPricePlusDividend": 247921.9602
  },
  {
    "month": "1987-04-01",
    "price": 289.3,
    "nominalPricePlusDividend": 87633.1279,
    "realPrice": 807.8901,
    "realPricePlusDividend": 244493.4688
  },
  {
    "month": "1987-05-01",
    "price": 289.1,
    "nominalPricePlusDividend": 87784.5851,
    "realPrice": 804.4763,
    "realPricePlusDividend": 244053.1642
  },
  {
    "month": "1987-06-01",
    "price": 301.4,
    "nominalPricePlusDividend": 91733.525,
    "realPrice": 835.7477,
    "realPricePlusDividend": 254136.2853
  },
  {
    "month": "1987-07-01",
    "price": 310.1,
    "nominalPricePlusDividend": 94597.5346,
    "realPrice": 857.605,
    "realPricePlusDividend": 261382.1725
  },
  {
    "month": "1987-08-01",
    "price": 329.4,
    "nominalPricePlusDividend": 100702.8702,
    "realPrice": 906.2027,
    "realPricePlusDividend": 276794.8103
  },
  {
    "month": "1987-09-01",
    "price": 318.7,
    "nominalPricePlusDividend": 97651.1444,
    "realPrice": 872.1918,
    "realPricePlusDividend": 267008.7199
  },
  {
    "month": "1987-10-01",
    "price": 280.2,
    "nominalPricePlusDividend": 86075.6895,
    "realPrice": 764.833,
    "realPricePlusDividend": 234748.0123
  },
  {
    "month": "1987-11-01",
    "price": 245,
    "nominalPricePlusDividend": 75485.4409,
    "realPrice": 668.1717,
    "realPricePlusDividend": 205690.1776
  },
  {
    "month": "1987-12-01",
    "price": 241,
    "nominalPricePlusDividend": 74477.9413,
    "realPrice": 657.2628,
    "realPricePlusDividend": 202947.425
  },
  {
    "month": "1988-01-01",
    "price": 250.5,
    "nominalPricePlusDividend": 77640.6785,
    "realPrice": 681.4001,
    "realPricePlusDividend": 211019.4465
  },
  {
    "month": "1988-02-01",
    "price": 258.1,
    "nominalPricePlusDividend": 80224.9991,
    "realPrice": 700.2576,
    "realPricePlusDividend": 217481.8011
  },
  {
    "month": "1988-03-01",
    "price": 265.7,
    "nominalPricePlusDividend": 82817.9184,
    "realPrice": 717.7834,
    "realPricePlusDividend": 223549.7074
  },
  {
    "month": "1988-04-01",
    "price": 262.6,
    "nominalPricePlusDividend": 82084.1315,
    "realPrice": 705.7739,
    "realPricePlusDividend": 220439.2937
  },
  {
    "month": "1988-05-01",
    "price": 256.1,
    "nominalPricePlusDividend": 80287.9115,
    "realPrice": 685.9611,
    "realPricePlusDividend": 214887.0433
  },
  {
    "month": "1988-06-01",
    "price": 270.7,
    "nominalPricePlusDividend": 85103.7407,
    "realPrice": 721.9948,
    "realPricePlusDividend": 226816.7854
  },
  {
    "month": "1988-07-01",
    "price": 269.1,
    "nominalPricePlusDividend": 84842.54,
    "realPrice": 714.6989,
    "realPricePlusDividend": 225170.9117
  },
  {
    "month": "1988-08-01",
    "price": 263.7,
    "nominalPricePlusDividend": 83384.5334,
    "realPrice": 697.4145,
    "realPricePlusDividend": 220375.8989
  },
  {
    "month": "1988-09-01",
    "price": 268,
    "nominalPricePlusDividend": 84991.4941,
    "realPrice": 704.0537,
    "realPricePlusDividend": 223127.2591
  },
  {
    "month": "1988-10-01",
    "price": 277.4,
    "nominalPricePlusDividend": 88222.5451,
    "realPrice": 726.323,
    "realPricePlusDividend": 230844.1964
  },
  {
    "month": "1988-11-01",
    "price": 271,
    "nominalPricePlusDividend": 86440.2313,
    "realPrice": 708.9759,
    "realPricePlusDividend": 225997.8013
  },
  {
    "month": "1988-12-01",
    "price": 276.5,
    "nominalPricePlusDividend": 88450.7907,
    "realPrice": 722.1641,
    "realPricePlusDividend": 230877.2056
  },
  {
    "month": "1989-01-01",
    "price": 285.4,
    "nominalPricePlusDividend": 91557.7647,
    "realPrice": 741.7159,
    "realPricePlusDividend": 237806.4257
  },
  {
    "month": "1989-02-01",
    "price": 294,
    "nominalPricePlusDividend": 94579.0354,
    "realPrice": 760.9245,
    "realPricePlusDividend": 244648.3419
  },
  {
    "month": "1989-03-01",
    "price": 292.7,
    "nominalPricePlusDividend": 94426.1398,
    "realPrice": 753.2238,
    "realPricePlusDividend": 242861.6204
  },
  {
    "month": "1989-04-01",
    "price": 302.3,
    "nominalPricePlusDividend": 97792.2419,
    "realPrice": 772.8726,
    "realPricePlusDividend": 249888.8195
  },
  {
    "month": "1989-05-01",
    "price": 313.9,
    "nominalPricePlusDividend": 101816.6881,
    "realPrice": 797.9919,
    "realPricePlusDividend": 258707.6744
  },
  {
    "month": "1989-06-01",
    "price": 323.7,
    "nominalPricePlusDividend": 105270.9439,
    "realPrice": 820.916,
    "realPricePlusDividend": 266849.0801
  },
  {
    "month": "1989-07-01",
    "price": 331.9,
    "nominalPricePlusDividend": 108218.7146,
    "realPrice": 839.6817,
    "realPricePlusDividend": 273662.3654
  },
  {
    "month": "1989-08-01",
    "price": 346.6,
    "nominalPricePlusDividend": 113294.9869,
    "realPrice": 875.464,
    "realPricePlusDividend": 286046.7095
  },
  {
    "month": "1989-09-01",
    "price": 347.3,
    "nominalPricePlusDividend": 113811.0876,
    "realPrice": 874.425,
    "realPricePlusDividend": 286441.7114
  },
  {
    "month": "1989-10-01",
    "price": 347.4,
    "nominalPricePlusDividend": 114136.8786,
    "realPrice": 870.4984,
    "realPricePlusDividend": 285892.8628
  },
  {
    "month": "1989-11-01",
    "price": 340.2,
    "nominalPricePlusDividend": 112066.9484,
    "realPrice": 850.4257,
    "realPricePlusDividend": 280046.7176
  },
  {
    "month": "1989-12-01",
    "price": 348.6,
    "nominalPricePlusDividend": 115133.8917,
    "realPrice": 870.0417,
    "realPricePlusDividend": 287262.6885
  },
  {
    "month": "1990-01-01",
    "price": 339.97,
    "nominalPricePlusDividend": 112588.0213,
    "realPrice": 839.8446,
    "realPricePlusDividend": 278048.5379
  },
  {
    "month": "1990-02-01",
    "price": 330.45,
    "nominalPricePlusDividend": 109742.7151,
    "realPrice": 812.5004,
    "realPricePlusDividend": 269756.2984
  },
  {
    "month": "1990-03-01",
    "price": 338.46,
    "nominalPricePlusDividend": 112713.6337,
    "realPrice": 827.6688,
    "realPricePlusDividend": 275557.0765
  },
  {
    "month": "1990-04-01",
    "price": 338.18,
    "nominalPricePlusDividend": 112934.5364,
    "realPrice": 825.701,
    "realPricePlusDividend": 275675.4927
  },
  {
    "month": "1990-05-01",
    "price": 350.25,
    "nominalPricePlusDividend": 117283.5607,
    "realPrice": 853.1854,
    "realPricePlusDividend": 285633.5237
  },
  {
    "month": "1990-06-01",
    "price": 360.39,
    "nominalPricePlusDividend": 121001.3994,
    "realPrice": 873.1551,
    "realPricePlusDividend": 293106.0213
  },
  {
    "month": "1990-07-01",
    "price": 360.03,
    "nominalPricePlusDividend": 121206.7672,
    "realPrice": 868.9382,
    "realPricePlusDividend": 292481.0369
  },
  {
    "month": "1990-08-01",
    "price": 330.75,
    "nominalPricePlusDividend": 111678.4283,
    "realPrice": 790.9914,
    "realPricePlusDividend": 267033.7191
  },
  {
    "month": "1990-09-01",
    "price": 315.41,
    "nominalPricePlusDividend": 106830.3999,
    "realPrice": 748.0529,
    "realPricePlusDividend": 253326.1141
  },
  {
    "month": "1990-10-01",
    "price": 307.12,
    "nominalPricePlusDividend": 104356.4547,
    "realPrice": 724.0268,
    "realPricePlusDividend": 245982.0158
  },
  {
    "month": "1990-11-01",
    "price": 315.29,
    "nominalPricePlusDividend": 107470.258,
    "realPrice": 741.6208,
    "realPricePlusDividend": 252758.255
  },
  {
    "month": "1990-12-01",
    "price": 328.75,
    "nominalPricePlusDividend": 112399.4947,
    "realPrice": 773.2812,
    "realPricePlusDividend": 264355.2019
  },
  {
    "month": "1991-01-01",
    "price": 325.49,
    "nominalPricePlusDividend": 111629.3658,
    "realPrice": 761.0626,
    "realPricePlusDividend": 260983.3903
  },
  {
    "month": "1991-02-01",
    "price": 362.26,
    "nominalPricePlusDividend": 124585.935,
    "realPrice": 845.7817,
    "realPricePlusDividend": 290842.2246
  },
  {
    "month": "1991-03-01",
    "price": 372.28,
    "nominalPricePlusDividend": 128379.1038,
    "realPrice": 867.8881,
    "realPricePlusDividend": 299251.8467
  },
  {
    "month": "1991-04-01",
    "price": 379.68,
    "nominalPricePlusDividend": 131278.9675,
    "realPrice": 883.8302,
    "realPricePlusDividend": 305558.8843
  },
  {
    "month": "1991-05-01",
    "price": 377.99,
    "nominalPricePlusDividend": 131044.1374,
    "realPrice": 877.3006,
    "realPricePlusDividend": 304112.0247
  },
  {
    "month": "1991-06-01",
    "price": 378.29,
    "nominalPricePlusDividend": 131498.8749,
    "realPrice": 875.4145,
    "realPricePlusDividend": 304269.2365
  },
  {
    "month": "1991-07-01",
    "price": 380.23,
    "nominalPricePlusDividend": 132525.205,
    "realPrice": 878.6119,
    "realPricePlusDividend": 306195.4145
  },
  {
    "month": "1991-08-01",
    "price": 389.4,
    "nominalPricePlusDividend": 136075.467,
    "realPrice": 897.1665,
    "realPricePlusDividend": 313479.2331
  },
  {
    "month": "1991-09-01",
    "price": 387.2,
    "nominalPricePlusDividend": 135663.021,
    "realPrice": 888.1964,
    "realPricePlusDividend": 311164.0018
  },
  {
    "month": "1991-10-01",
    "price": 386.88,
    "nominalPricePlusDividend": 135909.4474,
    "realPrice": 886.1706,
    "realPricePlusDividend": 311272.4606
  },
  {
    "month": "1991-11-01",
    "price": 385.92,
    "nominalPricePlusDividend": 135930.9146,
    "realPrice": 881.4057,
    "realPricePlusDividend": 310414.9416
  },
  {
    "month": "1991-12-01",
    "price": 388.51,
    "nominalPricePlusDividend": 137202.0587,
    "realPrice": 886.6776,
    "realPricePlusDividend": 313087.5454
  },
  {
    "month": "1992-01-01",
    "price": 416.08,
    "nominalPricePlusDividend": 147297.4218,
    "realPrice": 948.224,
    "realPricePlusDividend": 335639.2856
  },
  {
    "month": "1992-02-01",
    "price": 412.56,
    "nominalPricePlusDividend": 146412.3911,
    "realPrice": 936.8104,
    "realPricePlusDividend": 332420.5218
  },
  {
    "month": "1992-03-01",
    "price": 407.36,
    "nominalPricePlusDividend": 144930.1443,
    "realPrice": 920.3543,
    "realPricePlusDividend": 327403.0744
  },
  {
    "month": "1992-04-01",
    "price": 407.41,
    "nominalPricePlusDividend": 145313.1997,
    "realPrice": 919.1476,
    "realPricePlusDividend": 327796.5511
  },
  {
    "month": "1992-05-01",
    "price": 414.81,
    "nominalPricePlusDividend": 148318.786,
    "realPrice": 934.5028,
    "realPricePlusDividend": 334096.3132
  },
  {
    "month": "1992-06-01",
    "price": 408.27,
    "nominalPricePlusDividend": 146347.4475,
    "realPrice": 916.489,
    "realPricePlusDividend": 328478.876
  },
  {
    "month": "1992-07-01",
    "price": 415.05,
    "nominalPricePlusDividend": 149145.8058,
    "realPrice": 929.7194,
    "realPricePlusDividend": 334045.3711
  },
  {
    "month": "1992-08-01",
    "price": 417.93,
    "nominalPricePlusDividend": 150550.3415,
    "realPrice": 933.5129,
    "realPricePlusDividend": 336234.2284
  },
  {
    "month": "1992-09-01",
    "price": 418.48,
    "nominalPricePlusDividend": 151119.7038,
    "realPrice": 932.0953,
    "realPricePlusDividend": 336551.3866
  },
  {
    "month": "1992-10-01",
    "price": 412.5,
    "nominalPricePlusDividend": 149333.3848,
    "realPrice": 915.5362,
    "realPricePlusDividend": 331398.3596
  },
  {
    "month": "1992-11-01",
    "price": 422.84,
    "nominalPricePlusDividend": 153450.3614,
    "realPrice": 937.1638,
    "realPricePlusDividend": 340053.6063
  },
  {
    "month": "1992-12-01",
    "price": 435.64,
    "nominalPricePlusDividend": 158470.0295,
    "realPrice": 966.2136,
    "realPricePlusDividend": 351424.1356
  },
  {
    "month": "1993-01-01",
    "price": 435.23,
    "nominalPricePlusDividend": 158696.4724,
    "realPrice": 960.5657,
    "realPricePlusDividend": 350199.0722
  },
  {
    "month": "1993-02-01",
    "price": 441.7,
    "nominalPricePlusDividend": 161432.7921,
    "realPrice": 971.4391,
    "realPricePlusDividend": 354993.6506
  },
  {
    "month": "1993-03-01",
    "price": 450.16,
    "nominalPricePlusDividend": 164903.8438,
    "realPrice": 986.5981,
    "realPricePlusDividend": 361364.9132
  },
  {
    "month": "1993-04-01",
    "price": 443.08,
    "nominalPricePlusDividend": 162691.2545,
    "realPrice": 968.3836,
    "realPricePlusDividend": 355525.6418
  },
  {
    "month": "1993-05-01",
    "price": 445.25,
    "nominalPricePlusDividend": 163870.3175,
    "realPrice": 971.7767,
    "realPricePlusDividend": 357605.201
  },
  {
    "month": "1993-06-01",
    "price": 448.06,
    "nominalPricePlusDividend": 165288.0948,
    "realPrice": 976.5551,
    "realPricePlusDividend": 360199.1999
  },
  {
    "month": "1993-07-01",
    "price": 447.29,
    "nominalPricePlusDividend": 165388.9267,
    "realPrice": 974.8769,
    "realPricePlusDividend": 360417.6876
  },
  {
    "month": "1993-08-01",
    "price": 454.13,
    "nominalPricePlusDividend": 168303.85,
    "realPrice": 987.0506,
    "realPricePlusDividend": 365755.5029
  },
  {
    "month": "1993-09-01",
    "price": 459.24,
    "nominalPricePlusDividend": 170584.3196,
    "realPrice": 996.0935,
    "realPricePlusDividend": 369943.6793
  },
  {
    "month": "1993-10-01",
    "price": 463.9,
    "nominalPricePlusDividend": 172702.8181,
    "realPrice": 1002.0574,
    "realPricePlusDividend": 372995.7592
  },
  {
    "month": "1993-11-01",
    "price": 462.89,
    "nominalPricePlusDividend": 172715.8481,
    "realPrice": 999.19,
    "realPricePlusDividend": 372768.143
  },
  {
    "month": "1993-12-01",
    "price": 465.95,
    "nominalPricePlusDividend": 174248.1482,
    "realPrice": 1005.7953,
    "realPricePlusDividend": 376075.3535
  },
  {
    "month": "1994-01-01",
    "price": 472.99,
    "nominalPricePlusDividend": 177272.8871,
    "realPrice": 1018.1983,
    "realPricePlusDividend": 381558.421
  },
  {
    "month": "1994-02-01",
    "price": 471.58,
    "nominalPricePlusDividend": 177138.6897,
    "realPrice": 1011.703,
    "realPricePlusDividend": 379971.7357
  },
  {
    "month": "1994-03-01",
    "price": 463.81,
    "nominalPricePlusDividend": 174616.5569,
    "realPrice": 991.6538,
    "realPricePlusDividend": 373290.9738
  },
  {
    "month": "1994-04-01",
    "price": 447.23,
    "nominalPricePlusDividend": 168773.2278,
    "realPrice": 954.9074,
    "realPricePlusDividend": 360311.3275
  },
  {
    "month": "1994-05-01",
    "price": 450.9,
    "nominalPricePlusDividend": 170559.2567,
    "realPrice": 962.0907,
    "realPricePlusDividend": 363879.0639
  },
  {
    "month": "1994-06-01",
    "price": 454.83,
    "nominalPricePlusDividend": 172449.212,
    "realPrice": 967.1975,
    "realPricePlusDividend": 366669.8618
  },
  {
    "month": "1994-07-01",
    "price": 451.4,
    "nominalPricePlusDividend": 171554.4158,
    "realPrice": 957.3163,
    "realPricePlusDividend": 363784.8304
  },
  {
    "month": "1994-08-01",
    "price": 464.24,
    "nominalPricePlusDividend": 176841.8567,
    "realPrice": 980.5824,
    "realPricePlusDividend": 373487.6312
  },
  {
    "month": "1994-09-01",
    "price": 466.96,
    "nominalPricePlusDividend": 178287.4772,
    "realPrice": 983.6869,
    "realPricePlusDividend": 375532.6737
  },
  {
    "month": "1994-10-01",
    "price": 463.81,
    "nominalPricePlusDividend": 177495.869,
    "realPrice": 976.3976,
    "realPricePlusDividend": 373620.1591
  },
  {
    "month": "1994-11-01",
    "price": 461.01,
    "nominalPricePlusDividend": 176839.3404,
    "realPrice": 969.2065,
    "realPricePlusDividend": 371745.1717
  },
  {
    "month": "1994-12-01",
    "price": 455.19,
    "nominalPricePlusDividend": 175025.4883,
    "realPrice": 956.9708,
    "realPricePlusDividend": 367935.7679
  },
  {
    "month": "1995-01-01",
    "price": 465.25,
    "nominalPricePlusDividend": 179315.6679,
    "realPrice": 974.2159,
    "realPricePlusDividend": 375449.0622
  },
  {
    "month": "1995-02-01",
    "price": 481.92,
    "nominalPricePlusDividend": 186163.9013,
    "realPrice": 1005.1098,
    "realPricePlusDividend": 388236.6487
  },
  {
    "month": "1995-03-01",
    "price": 493.15,
    "nominalPricePlusDividend": 190926.2905,
    "realPrice": 1025.1347,
    "realPricePlusDividend": 396851.4679
  },
  {
    "month": "1995-04-01",
    "price": 507.91,
    "nominalPricePlusDividend": 197065.6267,
    "realPrice": 1052.3417,
    "realPricePlusDividend": 408267.7242
  },
  {
    "month": "1995-05-01",
    "price": 523.81,
    "nominalPricePlusDividend": 203662.9112,
    "realPrice": 1083.1458,
    "realPricePlusDividend": 421106.7906
  },
  {
    "month": "1995-06-01",
    "price": 539.35,
    "nominalPricePlusDividend": 210136.1777,
    "realPrice": 1113.0858,
    "realPricePlusDividend": 433638.8393
  },
  {
    "month": "1995-07-01",
    "price": 557.37,
    "nominalPricePlusDividend": 217590.7165,
    "realPrice": 1150.2746,
    "realPricePlusDividend": 449026.1114
  },
  {
    "month": "1995-08-01",
    "price": 559.11,
    "nominalPricePlusDividend": 218707.227,
    "realPrice": 1150.8469,
    "realPricePlusDividend": 450152.7948
  },
  {
    "month": "1995-09-01",
    "price": 578.77,
    "nominalPricePlusDividend": 226838.0277,
    "realPrice": 1188.9813,
    "realPricePlusDividend": 465977.0286
  },
  {
    "month": "1995-10-01",
    "price": 582.92,
    "nominalPricePlusDividend": 228908.0777,
    "realPrice": 1193.6112,
    "realPricePlusDividend": 468703.0084
  },
  {
    "month": "1995-11-01",
    "price": 595.53,
    "nominalPricePlusDividend": 234306.6124,
    "realPrice": 1220.2258,
    "realPricePlusDividend": 480072.4988
  },
  {
    "month": "1995-12-01",
    "price": 614.57,
    "nominalPricePlusDividend": 242247.5867,
    "realPrice": 1260.0587,
    "realPricePlusDividend": 496669.4955
  },
  {
    "month": "1996-01-01",
    "price": 614.42,
    "nominalPricePlusDividend": 242641.4324,
    "realPrice": 1252.408,
    "realPricePlusDividend": 494582.7118
  },
  {
    "month": "1996-02-01",
    "price": 649.54,
    "nominalPricePlusDividend": 256967.9375,
    "realPrice": 1319.7215,
    "realPricePlusDividend": 522099.6244
  },
  {
    "month": "1996-03-01",
    "price": 647.07,
    "nominalPricePlusDividend": 256452.2101,
    "realPrice": 1307.9479,
    "realPricePlusDividend": 518380.063
  },
  {
    "month": "1996-04-01",
    "price": 647.17,
    "nominalPricePlusDividend": 256957.5288,
    "realPrice": 1303.1283,
    "realPricePlusDividend": 517409.9968
  },
  {
    "month": "1996-05-01",
    "price": 661.23,
    "nominalPricePlusDividend": 263008.4306,
    "realPrice": 1328.8886,
    "realPricePlusDividend": 528581.9102
  },
  {
    "month": "1996-06-01",
    "price": 668.5,
    "nominalPricePlusDividend": 266371.2384,
    "realPrice": 1342.6419,
    "realPricePlusDividend": 535001.0505
  },
  {
    "month": "1996-07-01",
    "price": 644.07,
    "nominalPricePlusDividend": 257110.6706,
    "realPrice": 1291.104,
    "realPricePlusDividend": 515421.868
  },
  {
    "month": "1996-08-01",
    "price": 662.68,
    "nominalPricePlusDividend": 265018.7589,
    "realPrice": 1325.8761,
    "realPricePlusDividend": 530268.9455
  },
  {
    "month": "1996-09-01",
    "price": 674.88,
    "nominalPricePlusDividend": 270382.0148,
    "realPrice": 1346.0071,
    "realPricePlusDividend": 539293.1372
  },
  {
    "month": "1996-10-01",
    "price": 701.46,
    "nominalPricePlusDividend": 281520.3959,
    "realPrice": 1394.6004,
    "realPricePlusDividend": 559739.6009
  },
  {
    "month": "1996-11-01",
    "price": 735.67,
    "nominalPricePlusDividend": 295743.0367,
    "realPrice": 1459.8481,
    "realPricePlusDividend": 586909.6845
  },
  {
    "month": "1996-12-01",
    "price": 743.25,
    "nominalPricePlusDividend": 299286.711,
    "realPrice": 1474.8896,
    "realPricePlusDividend": 593946.0431
  },
  {
    "month": "1997-01-01",
    "price": 766.22,
    "nominalPricePlusDividend": 309036.0956,
    "realPrice": 1515.6925,
    "realPricePlusDividend": 611368.7501
  },
  {
    "month": "1997-02-01",
    "price": 798.39,
    "nominalPricePlusDividend": 322513.6655,
    "realPrice": 1574.3816,
    "realPricePlusDividend": 636034.7567
  },
  {
    "month": "1997-03-01",
    "price": 792.16,
    "nominalPricePlusDividend": 320502.1949,
    "realPrice": 1558.1911,
    "realPricePlusDividend": 630489.7778
  },
  {
    "month": "1997-04-01",
    "price": 763.93,
    "nominalPricePlusDividend": 309588.3054,
    "realPrice": 1500.7863,
    "realPricePlusDividend": 608260.4417
  },
  {
    "month": "1997-05-01",
    "price": 833.09,
    "nominalPricePlusDividend": 338125.6317,
    "realPrice": 1637.6775,
    "realPricePlusDividend": 664744.5305
  },
  {
    "month": "1997-06-01",
    "price": 876.29,
    "nominalPricePlusDividend": 356170.8061,
    "realPrice": 1720.4503,
    "realPricePlusDividend": 699347.8616
  },
  {
    "month": "1997-07-01",
    "price": 925.29,
    "nominalPricePlusDividend": 376600.4949,
    "realPrice": 1814.3899,
    "realPricePlusDividend": 738542.7427
  },
  {
    "month": "1997-08-01",
    "price": 927.24,
    "nominalPricePlusDividend": 377910.2706,
    "realPrice": 1814.8215,
    "realPricePlusDividend": 739730.8938
  },
  {
    "month": "1997-09-01",
    "price": 937.02,
    "nominalPricePlusDividend": 382414.9912,
    "realPrice": 1829.4124,
    "realPricePlusDividend": 746693.353
  },
  {
    "month": "1997-10-01",
    "price": 951.16,
    "nominalPricePlusDividend": 388707.1548,
    "realPrice": 1852.4224,
    "realPricePlusDividend": 757102.8433
  },
  {
    "month": "1997-11-01",
    "price": 938.92,
    "nominalPricePlusDividend": 384229.0801,
    "realPrice": 1829.7167,
    "realPricePlusDividend": 748846.3168
  },
  {
    "month": "1997-12-01",
    "price": 962.37,
    "nominalPricePlusDividend": 394352.043,
    "realPrice": 1877.7402,
    "realPricePlusDividend": 769530.7616
  },
  {
    "month": "1998-01-01",
    "price": 963.36,
    "nominalPricePlusDividend": 395287.0056,
    "realPrice": 1876.1823,
    "realPricePlusDividend": 769925.0453
  },
  {
    "month": "1998-02-01",
    "price": 1023.74,
    "nominalPricePlusDividend": 420593.9059,
    "realPrice": 1990.0804,
    "realPricePlusDividend": 817700.6428
  },
  {
    "month": "1998-03-01",
    "price": 1076.83,
    "nominalPricePlusDividend": 442939.5235,
    "realPrice": 2089.412,
    "realPricePlusDividend": 859552.4022
  },
  {
    "month": "1998-04-01",
    "price": 1112.2,
    "nominalPricePlusDividend": 458024.6054,
    "realPrice": 2154.0576,
    "realPricePlusDividend": 887190.8051
  },
  {
    "month": "1998-05-01",
    "price": 1108.42,
    "nominalPricePlusDividend": 457008.4431,
    "realPrice": 2142.7808,
    "realPricePlusDividend": 883596.331
  },
  {
    "month": "1998-06-01",
    "price": 1108.39,
    "nominalPricePlusDividend": 457540.6617,
    "realPrice": 2140.0937,
    "realPricePlusDividend": 883544.9726
  },
  {
    "month": "1998-07-01",
    "price": 1156.58,
    "nominalPricePlusDividend": 477982.0517,
    "realPrice": 2230.4029,
    "realPricePlusDividend": 921890.5084
  },
  {
    "month": "1998-08-01",
    "price": 1074.62,
    "nominalPricePlusDividend": 444661.8885,
    "realPrice": 2069.8109,
    "realPricePlusDividend": 856578.5613
  },
  {
    "month": "1998-09-01",
    "price": 1020.64,
    "nominalPricePlusDividend": 422880.3476,
    "realPrice": 1963.4375,
    "realPricePlusDividend": 813625.7896
  },
  {
    "month": "1998-10-01",
    "price": 1032.47,
    "nominalPricePlusDividend": 428339.1269,
    "realPrice": 1981.3509,
    "realPricePlusDividend": 822118.6394
  },
  {
    "month": "1998-11-01",
    "price": 1144.43,
    "nominalPricePlusDividend": 475346.7086,
    "realPrice": 2196.2065,
    "realPricePlusDividend": 912340.6025
  },
  {
    "month": "1998-12-01",
    "price": 1190.05,
    "nominalPricePlusDividend": 494855.4364,
    "realPrice": 2285.1465,
    "realPricePlusDividend": 950363.017
  },
  {
    "month": "1999-01-01",
    "price": 1248.77,
    "nominalPricePlusDividend": 519834.1903,
    "realPrice": 2392.0634,
    "realPricePlusDividend": 995907.7772
  },
  {
    "month": "1999-02-01",
    "price": 1246.58,
    "nominalPricePlusDividend": 519487.4084,
    "realPrice": 2384.9652,
    "realPricePlusDividend": 994037.2999
  },
  {
    "month": "1999-03-01",
    "price": 1281.66,
    "nominalPricePlusDividend": 534674.6739,
    "realPrice": 2444.6499,
    "realPricePlusDividend": 1020001.6811
  },
  {
    "month": "1999-04-01",
    "price": 1334.76,
    "nominalPricePlusDividend": 557398.4658,
    "realPrice": 2527.5512,
    "realPricePlusDividend": 1055672.7359
  },
  {
    "month": "1999-05-01",
    "price": 1332.07,
    "nominalPricePlusDividend": 556847.5791,
    "realPrice": 2522.4573,
    "realPricePlusDividend": 1054627.7838
  },
  {
    "month": "1999-06-01",
    "price": 1322.55,
    "nominalPricePlusDividend": 553440.9685,
    "realPrice": 2504.4299,
    "realPricePlusDividend": 1048174.3036
  },
  {
    "month": "1999-07-01",
    "price": 1380.99,
    "nominalPricePlusDividend": 578469.7127,
    "realPrice": 2607.2503,
    "realPricePlusDividend": 1092293.2854
  },
  {
    "month": "1999-08-01",
    "price": 1327.49,
    "nominalPricePlusDividend": 556636.0346,
    "realPrice": 2500.2452,
    "realPricePlusDividend": 1048552.4511
  },
  {
    "month": "1999-09-01",
    "price": 1318.17,
    "nominalPricePlusDividend": 553307.2585,
    "realPrice": 2470.8622,
    "realPricePlusDividend": 1037318.2575
  },
  {
    "month": "1999-10-01",
    "price": 1300.01,
    "nominalPricePlusDividend": 546266.5831,
    "realPrice": 2432.4756,
    "realPricePlusDividend": 1022291.5424
  },
  {
    "month": "1999-11-01",
    "price": 1391,
    "nominalPricePlusDividend": 585084.0113,
    "realPrice": 2601.1824,
    "realPricePlusDividend": 1094283.9468
  },
  {
    "month": "1999-12-01",
    "price": 1428.68,
    "nominalPricePlusDividend": 601517.4457,
    "realPrice": 2671.6443,
    "realPricePlusDividend": 1125018.9018
  },
  {
    "month": "2000-01-01",
    "price": 1425.59,
    "nominalPricePlusDividend": 600802.0452,
    "realPrice": 2657.9695,
    "realPricePlusDividend": 1120352.3492
  },
  {
    "month": "2000-02-01",
    "price": 1388.87,
    "nominalPricePlusDividend": 585913.7061,
    "realPrice": 2574.2558,
    "realPricePlusDividend": 1086154.4856
  },
  {
    "month": "2000-03-01",
    "price": 1442.21,
    "nominalPricePlusDividend": 609004.2933,
    "realPrice": 2651.2613,
    "realPricePlusDividend": 1119727.0831
  },
  {
    "month": "2000-04-01",
    "price": 1461.36,
    "nominalPricePlusDividend": 617680.5667,
    "realPrice": 2684.8971,
    "realPricePlusDividend": 1135013.5675
  },
  {
    "month": "2000-05-01",
    "price": 1418.48,
    "nominalPricePlusDividend": 600145.8878,
    "realPrice": 2603.0762,
    "realPricePlusDividend": 1101503.9144
  },
  {
    "month": "2000-06-01",
    "price": 1461.96,
    "nominalPricePlusDividend": 619131.3839,
    "realPrice": 2668.8614,
    "realPricePlusDividend": 1130414.6656
  },
  {
    "month": "2000-07-01",
    "price": 1473,
    "nominalPricePlusDividend": 624396.121,
    "realPrice": 2682.7908,
    "realPricePlusDividend": 1137379.0247
  },
  {
    "month": "2000-08-01",
    "price": 1485.46,
    "nominalPricePlusDividend": 630263.6406,
    "realPrice": 2705.4843,
    "realPricePlusDividend": 1148058.019
  },
  {
    "month": "2000-09-01",
    "price": 1468.05,
    "nominalPricePlusDividend": 623458.9954,
    "realPrice": 2659.9215,
    "realPricePlusDividend": 1129769.7067
  },
  {
    "month": "2000-10-01",
    "price": 1390.14,
    "nominalPricePlusDividend": 590950.4109,
    "realPrice": 2514.4157,
    "realPricePlusDividend": 1069011.3453
  },
  {
    "month": "2000-11-01",
    "price": 1378.04,
    "nominalPricePlusDividend": 586384.9404,
    "realPrice": 2491.0982,
    "realPricePlusDividend": 1060140.01
  },
  {
    "month": "2000-12-01",
    "price": 1330.93,
    "nominalPricePlusDividend": 566916.5278,
    "realPrice": 2407.3196,
    "realPricePlusDividend": 1025528.3647
  },
  {
    "month": "2001-01-01",
    "price": 1335.63,
    "nominalPricePlusDividend": 569496.0414,
    "realPrice": 2400.6443,
    "realPricePlusDividend": 1023714.8714
  },
  {
    "month": "2001-02-01",
    "price": 1305.75,
    "nominalPricePlusDividend": 557330.1378,
    "realPrice": 2337.5933,
    "realPricePlusDividend": 997848.654
  },
  {
    "month": "2001-03-01",
    "price": 1185.85,
    "nominalPricePlusDividend": 506725.102,
    "realPrice": 2118.1253,
    "realPricePlusDividend": 905177.5215
  },
  {
    "month": "2001-04-01",
    "price": 1189.84,
    "nominalPricePlusDividend": 508998.7452,
    "realPrice": 2116.8424,
    "realPricePlusDividend": 905633.693
  },
  {
    "month": "2001-05-01",
    "price": 1270.37,
    "nominalPricePlusDividend": 544014.4637,
    "realPrice": 2249.9382,
    "realPricePlusDividend": 963570.2599
  },
  {
    "month": "2001-06-01",
    "price": 1238.71,
    "nominalPricePlusDividend": 531019.8497,
    "realPrice": 2190.168,
    "realPricePlusDividend": 938961.3518
  },
  {
    "month": "2001-07-01",
    "price": 1204.45,
    "nominalPricePlusDividend": 516893.5154,
    "realPrice": 2135.5916,
    "realPricePlusDividend": 916557.0226
  },
  {
    "month": "2001-08-01",
    "price": 1178.5,
    "nominalPricePlusDividend": 506318.7049,
    "realPrice": 2089.5801,
    "realPricePlusDividend": 897805.3133
  },
  {
    "month": "2001-09-01",
    "price": 1044.64,
    "nominalPricePlusDividend": 449371.3958,
    "realPrice": 1843.9244,
    "realPricePlusDividend": 793250.5923
  },
  {
    "month": "2001-10-01",
    "price": 1076.59,
    "nominalPricePlusDividend": 463679.5226,
    "realPrice": 1906.7366,
    "realPricePlusDividend": 821270.1283
  },
  {
    "month": "2001-11-01",
    "price": 1129.68,
    "nominalPricePlusDividend": 487109.9268,
    "realPrice": 2004.1472,
    "realPricePlusDividend": 864227.6432
  },
  {
    "month": "2001-12-01",
    "price": 1144.93,
    "nominalPricePlusDividend": 494251.1989,
    "realPrice": 2039.2486,
    "realPricePlusDividend": 880369.9938
  },
  {
    "month": "2002-01-01",
    "price": 1140.21,
    "nominalPricePlusDividend": 492779.8663,
    "realPrice": 2026.2549,
    "realPricePlusDividend": 875765.0239
  },
  {
    "month": "2002-02-01",
    "price": 1100.67,
    "nominalPricePlusDividend": 476258.0941,
    "realPrice": 1948.288,
    "realPricePlusDividend": 843068.6449
  },
  {
    "month": "2002-03-01",
    "price": 1153.79,
    "nominalPricePlusDividend": 499810.3461,
    "realPrice": 2030.893,
    "realPricePlusDividend": 879810.6495
  },
  {
    "month": "2002-04-01",
    "price": 1111.93,
    "nominalPricePlusDividend": 482244.8507,
    "realPrice": 1946.3259,
    "realPricePlusDividend": 844174.04
  },
  {
    "month": "2002-05-01",
    "price": 1079.25,
    "nominalPricePlusDividend": 468643.7549,
    "realPrice": 1889.1227,
    "realPricePlusDividend": 820370.2352
  },
  {
    "month": "2002-06-01",
    "price": 1014.02,
    "nominalPricePlusDividend": 440895.5527,
    "realPrice": 1773.9573,
    "realPricePlusDividend": 771372.4719
  },
  {
    "month": "2002-07-01",
    "price": 903.59,
    "nominalPricePlusDividend": 393461.8083,
    "realPrice": 1579.0122,
    "realPricePlusDividend": 687613.3555
  },
  {
    "month": "2002-08-01",
    "price": 912.55,
    "nominalPricePlusDividend": 397942.5153,
    "realPrice": 1589.3748,
    "realPricePlusDividend": 693128.1184
  },
  {
    "month": "2002-09-01",
    "price": 867.81,
    "nominalPricePlusDividend": 379009.4842,
    "realPrice": 1508.9466,
    "realPricePlusDividend": 659050.24
  },
  {
    "month": "2002-10-01",
    "price": 854.63,
    "nominalPricePlusDividend": 373828.2626,
    "realPrice": 1483.5703,
    "realPricePlusDividend": 648969.3024
  },
  {
    "month": "2002-11-01",
    "price": 909.93,
    "nominalPricePlusDividend": 398596.5411,
    "realPrice": 1579.5667,
    "realPricePlusDividend": 691971.4532
  },
  {
    "month": "2002-12-01",
    "price": 899.18,
    "nominalPricePlusDividend": 394470.8226,
    "realPrice": 1564.357,
    "realPricePlusDividend": 686327.5497
  },
  {
    "month": "2003-01-01",
    "price": 895.84,
    "nominalPricePlusDividend": 393593.0558,
    "realPrice": 1551.6841,
    "realPricePlusDividend": 681786.9174
  },
  {
    "month": "2003-02-01",
    "price": 837.03,
    "nominalPricePlusDividend": 368344.7068,
    "realPrice": 1438.7339,
    "realPricePlusDividend": 633174.4368
  },
  {
    "month": "2003-03-01",
    "price": 846.63,
    "nominalPricePlusDividend": 373162.2804,
    "realPrice": 1446.5446,
    "realPricePlusDividend": 637626.7094
  },
  {
    "month": "2003-04-01",
    "price": 890.03,
    "nominalPricePlusDividend": 392887.1118,
    "realPrice": 1524.0069,
    "realPricePlusDividend": 672789.1961
  },
  {
    "month": "2003-05-01",
    "price": 935.96,
    "nominalPricePlusDividend": 413758.1069,
    "realPrice": 1605.2734,
    "realPricePlusDividend": 709684.9705
  },
  {
    "month": "2003-06-01",
    "price": 988,
    "nominalPricePlusDividend": 437359.6343,
    "realPrice": 1692.6828,
    "realPricePlusDividend": 749347.4135
  },
  {
    "month": "2003-07-01",
    "price": 992.54,
    "nominalPricePlusDividend": 439965.864,
    "realPrice": 1698.6116,
    "realPricePlusDividend": 753000.2812
  },
  {
    "month": "2003-08-01",
    "price": 989.53,
    "nominalPricePlusDividend": 439234.0946,
    "realPrice": 1687.0388,
    "realPricePlusDividend": 748904.5222
  },
  {
    "month": "2003-09-01",
    "price": 1019.44,
    "nominalPricePlusDividend": 453119.0789,
    "realPrice": 1732.4012,
    "realPricePlusDividend": 770083.0442
  },
  {
    "month": "2003-10-01",
    "price": 1038.73,
    "nominalPricePlusDividend": 462307.559,
    "realPrice": 1767.0903,
    "realPricePlusDividend": 786563.641
  },
  {
    "month": "2003-11-01",
    "price": 1049.9,
    "nominalPricePlusDividend": 467904.1906,
    "realPrice": 1790.9331,
    "realPricePlusDividend": 798258.3477
  },
  {
    "month": "2003-12-01",
    "price": 1080.64,
    "nominalPricePlusDividend": 482239.8875,
    "realPrice": 1845.3702,
    "realPricePlusDividend": 823623.5436
  },
  {
    "month": "2004-01-01",
    "price": 1132.52,
    "nominalPricePlusDividend": 506038.2397,
    "realPrice": 1924.5655,
    "realPricePlusDividend": 860080.6547
  },
  {
    "month": "2004-02-01",
    "price": 1143.36,
    "nominalPricePlusDividend": 511537.1659,
    "realPrice": 1932.5517,
    "realPricePlusDividend": 864769.0608
  },
  {
    "month": "2004-03-01",
    "price": 1123.98,
    "nominalPricePlusDividend": 503530.6029,
    "realPrice": 1887.6296,
    "realPricePlusDividend": 845794.3939
  },
  {
    "month": "2004-04-01",
    "price": 1133.36,
    "nominalPricePlusDividend": 508405.4692,
    "realPrice": 1897.3079,
    "realPricePlusDividend": 851267.7575
  },
  {
    "month": "2004-05-01",
    "price": 1102.78,
    "nominalPricePlusDividend": 495368.6647,
    "realPrice": 1835.3764,
    "realPricePlusDividend": 824624.5521
  },
  {
    "month": "2004-06-01",
    "price": 1132.76,
    "nominalPricePlusDividend": 509524.7004,
    "realPrice": 1879.3097,
    "realPricePlusDividend": 845517.2188
  },
  {
    "month": "2004-07-01",
    "price": 1105.85,
    "nominalPricePlusDividend": 498117.5653,
    "realPrice": 1837.5706,
    "realPricePlusDividend": 827907.114
  },
  {
    "month": "2004-08-01",
    "price": 1088.94,
    "nominalPricePlusDividend": 491205.8346,
    "realPrice": 1808.5167,
    "realPricePlusDividend": 815998.3743
  },
  {
    "month": "2004-09-01",
    "price": 1117.66,
    "nominalPricePlusDividend": 504874.2485,
    "realPrice": 1852.3052,
    "realPricePlusDividend": 836947.778
  },
  {
    "month": "2004-10-01",
    "price": 1117.21,
    "nominalPricePlusDividend": 505392.2258,
    "realPrice": 1841.8603,
    "realPricePlusDividend": 833421.7447
  },
  {
    "month": "2004-11-01",
    "price": 1168.94,
    "nominalPricePlusDividend": 529519.1254,
    "realPrice": 1926.1347,
    "realPricePlusDividend": 872755.2671
  },
  {
    "month": "2004-12-01",
    "price": 1199.21,
    "nominalPricePlusDividend": 543961.4804,
    "realPrice": 1983.281,
    "realPricePlusDividend": 899861.1357
  },
  {
    "month": "2005-01-01",
    "price": 1181.41,
    "nominalPricePlusDividend": 536622.2348,
    "realPrice": 1949.7447,
    "realPricePlusDividend": 885872.5948
  },
  {
    "month": "2005-02-01",
    "price": 1199.63,
    "nominalPricePlusDividend": 545643.9639,
    "realPrice": 1968.4596,
    "realPricePlusDividend": 895614.4409
  },
  {
    "month": "2005-03-01",
    "price": 1194.9,
    "nominalPricePlusDividend": 544249.3631,
    "realPrice": 1945.4833,
    "realPricePlusDividend": 886407.5885
  },
  {
    "month": "2005-04-01",
    "price": 1164.43,
    "nominalPricePlusDividend": 531138.8397,
    "realPrice": 1883.2082,
    "realPricePlusDividend": 859288.3261
  },
  {
    "month": "2005-05-01",
    "price": 1178.28,
    "nominalPricePlusDividend": 538234.1672,
    "realPrice": 1907.568,
    "realPricePlusDividend": 871675.6264
  },
  {
    "month": "2005-06-01",
    "price": 1202.25,
    "nominalPricePlusDividend": 549971.4261,
    "realPrice": 1945.3734,
    "realPricePlusDividend": 890238.759
  },
  {
    "month": "2005-07-01",
    "price": 1222.24,
    "nominalPricePlusDividend": 559913.7597,
    "realPrice": 1968.6102,
    "realPricePlusDividend": 902167.033
  },
  {
    "month": "2005-08-01",
    "price": 1224.27,
    "nominalPricePlusDividend": 561649.5944,
    "realPrice": 1961.8397,
    "realPricePlusDividend": 900365.234
  },
  {
    "month": "2005-09-01",
    "price": 1225.92,
    "nominalPricePlusDividend": 563220.4748,
    "realPrice": 1940.7676,
    "realPricePlusDividend": 891992.4335
  },
  {
    "month": "2005-10-01",
    "price": 1191.96,
    "nominalPricePlusDividend": 548440.3326,
    "realPrice": 1883.216,
    "realPricePlusDividend": 866853.6208
  },
  {
    "month": "2005-11-01",
    "price": 1237.37,
    "nominalPricePlusDividend": 570167.0285,
    "realPrice": 1970.7904,
    "realPricePlusDividend": 908504.7924
  },
  {
    "month": "2005-12-01",
    "price": 1262.07,
    "nominalPricePlusDividend": 582392.1563,
    "realPrice": 2018.302,
    "realPricePlusDividend": 931769.9475
  },
  {
    "month": "2006-01-01",
    "price": 1278.73,
    "nominalPricePlusDividend": 590934.5109,
    "realPrice": 2029.4761,
    "realPricePlusDividend": 938294.6698
  },
  {
    "month": "2006-02-01",
    "price": 1276.65,
    "nominalPricePlusDividend": 590836.1808,
    "realPrice": 2022.096,
    "realPricePlusDividend": 936259.328
  },
  {
    "month": "2006-03-01",
    "price": 1293.74,
    "nominalPricePlusDividend": 599616.8204,
    "realPrice": 2037.8833,
    "realPricePlusDividend": 944951.5328
  },
  {
    "month": "2006-04-01",
    "price": 1302.17,
    "nominalPricePlusDividend": 604403.75,
    "realPrice": 2033.8571,
    "realPricePlusDividend": 944470.6505
  },
  {
    "month": "2006-05-01",
    "price": 1290.01,
    "nominalPricePlusDividend": 599649.2947,
    "realPrice": 2004.9144,
    "realPricePlusDividend": 932424.8992
  },
  {
    "month": "2006-06-01",
    "price": 1253.17,
    "nominalPricePlusDividend": 583424.0262,
    "realPrice": 1943.8186,
    "realPricePlusDividend": 905418.0835
  },
  {
    "month": "2006-07-01",
    "price": 1260.24,
    "nominalPricePlusDividend": 587624.9163,
    "realPrice": 1949.0215,
    "realPricePlusDividend": 909259.7973
  },
  {
    "month": "2006-08-01",
    "price": 1287.15,
    "nominalPricePlusDividend": 601091.8647,
    "realPrice": 1986.734,
    "realPricePlusDividend": 928284.2977
  },
  {
    "month": "2006-09-01",
    "price": 1317.74,
    "nominalPricePlusDividend": 616306.5428,
    "realPrice": 2043.9745,
    "realPricePlusDividend": 956482.7928
  },
  {
    "month": "2006-10-01",
    "price": 1363.38,
    "nominalPricePlusDividend": 638591.6518,
    "realPrice": 2126.2952,
    "realPricePlusDividend": 996484.2447
  },
  {
    "month": "2006-11-01",
    "price": 1388.64,
    "nominalPricePlusDividend": 651373.9768,
    "realPrice": 2168.9144,
    "realPricePlusDividend": 1017957.2237
  },
  {
    "month": "2006-12-01",
    "price": 1416.42,
    "nominalPricePlusDividend": 665367.2157,
    "realPrice": 2209.0151,
    "realPricePlusDividend": 1038293.4187
  },
  {
    "month": "2007-01-01",
    "price": 1424.16,
    "nominalPricePlusDividend": 669977.0562,
    "realPrice": 2214.3269,
    "realPricePlusDividend": 1042315.437
  },
  {
    "month": "2007-02-01",
    "price": 1444.8,
    "nominalPricePlusDividend": 680670.2119,
    "realPrice": 2234.4634,
    "realPricePlusDividend": 1053325.7203
  },
  {
    "month": "2007-03-01",
    "price": 1406.95,
    "nominalPricePlusDividend": 663831.1725,
    "realPrice": 2156.2917,
    "realPricePlusDividend": 1018007.9692
  },
  {
    "month": "2007-04-01",
    "price": 1463.64,
    "nominalPricePlusDividend": 691581.0408,
    "realPrice": 2228.6969,
    "realPricePlusDividend": 1053729.5112
  },
  {
    "month": "2007-05-01",
    "price": 1511.14,
    "nominalPricePlusDividend": 715037.7624,
    "realPrice": 2287.05,
    "realPricePlusDividend": 1082863.6242
  },
  {
    "month": "2007-06-01",
    "price": 1514.19,
    "nominalPricePlusDividend": 717503.9384,
    "realPrice": 2287.2334,
    "realPricePlusDividend": 1084507.8993
  },
  {
    "month": "2007-07-01",
    "price": 1520.71,
    "nominalPricePlusDividend": 721626.857,
    "realPrice": 2297.6666,
    "realPricePlusDividend": 1091030.9968
  },
  {
    "month": "2007-08-01",
    "price": 1454.62,
    "nominalPricePlusDividend": 691310.5347,
    "realPrice": 2201.8481,
    "realPricePlusDividend": 1047129.7097
  },
  {
    "month": "2007-09-01",
    "price": 1497.12,
    "nominalPricePlusDividend": 712566.5602,
    "realPrice": 2259.9518,
    "realPricePlusDividend": 1076373.6661
  },
  {
    "month": "2007-10-01",
    "price": 1539.66,
    "nominalPricePlusDividend": 733883.9353,
    "realPrice": 2319.2061,
    "realPricePlusDividend": 1106220.9481
  },
  {
    "month": "2007-11-01",
    "price": 1463.39,
    "nominalPricePlusDividend": 698611.1979,
    "realPrice": 2191.3043,
    "realPricePlusDividend": 1046847.189
  },
  {
    "month": "2007-12-01",
    "price": 1479.22,
    "nominalPricePlusDividend": 707261.5474,
    "realPrice": 2216.4953,
    "realPricePlusDividend": 1060533.387
  },
  {
    "month": "2008-01-01",
    "price": 1378.76,
    "nominalPricePlusDividend": 660333.3478,
    "realPrice": 2055.7457,
    "realPricePlusDividend": 985276.3831
  },
  {
    "month": "2008-02-01",
    "price": 1354.87,
    "nominalPricePlusDividend": 650005.9608,
    "realPrice": 2014.2757,
    "realPricePlusDividend": 967067.3519
  },
  {
    "month": "2008-03-01",
    "price": 1316.94,
    "nominalPricePlusDividend": 632932.6717,
    "realPrice": 1941.06,
    "realPricePlusDividend": 933582.3228
  },
  {
    "month": "2008-04-01",
    "price": 1370.47,
    "nominalPricePlusDividend": 659793.0846,
    "realPrice": 2007.782,
    "realPricePlusDividend": 967340.5826
  },
  {
    "month": "2008-05-01",
    "price": 1403.22,
    "nominalPricePlusDividend": 676700.9701,
    "realPrice": 2038.595,
    "realPricePlusDividend": 983850.3413
  },
  {
    "month": "2008-06-01",
    "price": 1341.25,
    "nominalPricePlusDividend": 647964.3081,
    "realPrice": 1929.1253,
    "realPricePlusDividend": 932677.2342
  },
  {
    "month": "2008-07-01",
    "price": 1257.33,
    "nominalPricePlusDividend": 608577.9818,
    "realPrice": 1798.9764,
    "realPricePlusDividend": 871409.1607
  },
  {
    "month": "2008-08-01",
    "price": 1281.47,
    "nominalPricePlusDividend": 621422.2327,
    "realPrice": 1840.8636,
    "realPricePlusDividend": 893366.7058
  },
  {
    "month": "2008-09-01",
    "price": 1216.95,
    "nominalPricePlusDividend": 591298.565,
    "realPrice": 1750.6001,
    "realPricePlusDividend": 851237.9279
  },
  {
    "month": "2008-10-01",
    "price": 968.8,
    "nominalPricePlusDividend": 471894.1863,
    "realPrice": 1407.854,
    "realPricePlusDividend": 686263.2212
  },
  {
    "month": "2008-11-01",
    "price": 883.04,
    "nominalPricePlusDividend": 431286.0495,
    "realPrice": 1308.2855,
    "realPricePlusDividend": 639443.521
  },
  {
    "month": "2008-12-01",
    "price": 877.56,
    "nominalPricePlusDividend": 429771.2985,
    "realPrice": 1313.754,
    "realPricePlusDividend": 643844.8329
  },
  {
    "month": "2009-01-01",
    "price": 865.58,
    "nominalPricePlusDividend": 425062.9106,
    "realPrice": 1290.2038,
    "realPricePlusDividend": 634006.1128
  },
  {
    "month": "2009-02-01",
    "price": 805.23,
    "nominalPricePlusDividend": 396573.0415,
    "realPrice": 1194.3089,
    "realPricePlusDividend": 588559.4456
  },
  {
    "month": "2009-03-01",
    "price": 757.13,
    "nominalPricePlusDividend": 374018.2018,
    "realPrice": 1120.2434,
    "realPricePlusDividend": 553713.5972
  },
  {
    "month": "2009-04-01",
    "price": 848.15,
    "nominalPricePlusDividend": 420103.79,
    "realPrice": 1251.7909,
    "realPricePlusDividend": 620355.8207
  },
  {
    "month": "2009-05-01",
    "price": 902.41,
    "nominalPricePlusDividend": 448081.9534,
    "realPrice": 1328.0372,
    "realPricePlusDividend": 659728.3133
  },
  {
    "month": "2009-06-01",
    "price": 926.12,
    "nominalPricePlusDividend": 460936.802,
    "realPrice": 1351.3225,
    "realPricePlusDividend": 672839.154
  },
  {
    "month": "2009-07-01",
    "price": 935.82,
    "nominalPricePlusDividend": 466825.9251,
    "realPrice": 1367.6445,
    "realPricePlusDividend": 682481.4057
  },
  {
    "month": "2009-08-01",
    "price": 1009.73,
    "nominalPricePlusDividend": 504735.6679,
    "realPrice": 1472.3572,
    "realPricePlusDividend": 736216.3105
  },
  {
    "month": "2009-09-01",
    "price": 1044.55,
    "nominalPricePlusDividend": 523160.2524,
    "realPrice": 1522.1786,
    "realPricePlusDividend": 762577.368
  },
  {
    "month": "2009-10-01",
    "price": 1067.66,
    "nominalPricePlusDividend": 535732.3593,
    "realPrice": 1554.3588,
    "realPricePlusDividend": 780119.2601
  },
  {
    "month": "2009-11-01",
    "price": 1088.07,
    "nominalPricePlusDividend": 546952.3398,
    "realPrice": 1582.9525,
    "realPricePlusDividend": 795861.9082
  },
  {
    "month": "2009-12-01",
    "price": 1110.38,
    "nominalPricePlusDividend": 559126.7201,
    "realPrice": 1618.2597,
    "realPricePlusDividend": 814979.6969
  },
  {
    "month": "2010-01-01",
    "price": 1123.58,
    "nominalPricePlusDividend": 566713.8901,
    "realPrice": 1631.9203,
    "realPricePlusDividend": 823212.9804
  },
  {
    "month": "2010-02-01",
    "price": 1089.16,
    "nominalPricePlusDividend": 550287.8392,
    "realPrice": 1581.5335,
    "realPricePlusDividend": 799140.8367
  },
  {
    "month": "2010-03-01",
    "price": 1152.05,
    "nominalPricePlusDividend": 582991.6414,
    "realPrice": 1666.0129,
    "realPricePlusDividend": 843159.424
  },
  {
    "month": "2010-04-01",
    "price": 1197.32,
    "nominalPricePlusDividend": 606823.9328,
    "realPrice": 1728.477,
    "realPricePlusDividend": 876106.3526
  },
  {
    "month": "2010-05-01",
    "price": 1125.06,
    "nominalPricePlusDividend": 571128.1424,
    "realPrice": 1622.9028,
    "realPricePlusDividend": 823932.4434
  },
  {
    "month": "2010-06-01",
    "price": 1083.36,
    "nominalPricePlusDividend": 550889.8506,
    "realPrice": 1564.2776,
    "realPricePlusDividend": 795513.3505
  },
  {
    "month": "2010-07-01",
    "price": 1079.8,
    "nominalPricePlusDividend": 550013.5335,
    "realPrice": 1558.8083,
    "realPricePlusDividend": 794084.6257
  },
  {
    "month": "2010-08-01",
    "price": 1087.28,
    "nominalPricePlusDividend": 554763.5141,
    "realPrice": 1567.4424,
    "realPricePlusDividend": 799842.4238
  },
  {
    "month": "2010-09-01",
    "price": 1122.08,
    "nominalPricePlusDividend": 573465.4494,
    "realPrice": 1616.6702,
    "realPricePlusDividend": 826329.939
  },
  {
    "month": "2010-10-01",
    "price": 1171.58,
    "nominalPricePlusDividend": 599715.4664,
    "realPrice": 1685.8895,
    "realPricePlusDividend": 863085.6766
  },
  {
    "month": "2010-11-01",
    "price": 1198.89,
    "nominalPricePlusDividend": 614653.8656,
    "realPrice": 1724.4629,
    "realPricePlusDividend": 884218.1719
  },
  {
    "month": "2010-12-01",
    "price": 1241.53,
    "nominalPricePlusDividend": 637480.4883,
    "realPrice": 1782.732,
    "realPricePlusDividend": 915488.197
  },
  {
    "month": "2011-01-01",
    "price": 1282.62,
    "nominalPricePlusDividend": 659551.2942,
    "realPrice": 1833.0028,
    "realPricePlusDividend": 942706.0806
  },
  {
    "month": "2011-02-01",
    "price": 1321.12,
    "nominalPricePlusDividend": 680332.8581,
    "realPrice": 1878.7586,
    "realPricePlusDividend": 967649.8108
  },
  {
    "month": "2011-03-01",
    "price": 1304.49,
    "nominalPricePlusDividend": 672764.4205,
    "realPrice": 1837.1945,
    "realPricePlusDividend": 947656.5326
  },
  {
    "month": "2011-04-01",
    "price": 1331.51,
    "nominalPricePlusDividend": 687706.4034,
    "realPrice": 1863.2502,
    "realPricePlusDividend": 962521.9566
  },
  {
    "month": "2011-05-01",
    "price": 1338.31,
    "nominalPricePlusDividend": 692240.0035,
    "realPrice": 1863.9972,
    "realPricePlusDividend": 964346.8877
  },
  {
    "month": "2011-06-01",
    "price": 1287.29,
    "nominalPricePlusDividend": 666886.0199,
    "realPrice": 1794.8588,
    "realPricePlusDividend": 930038.7989
  },
  {
    "month": "2011-07-01",
    "price": 1325.19,
    "nominalPricePlusDividend": 687571.0616,
    "realPrice": 1846.0668,
    "realPricePlusDividend": 958051.9201
  },
  {
    "month": "2011-08-01",
    "price": 1185.31,
    "nominalPricePlusDividend": 616059.223,
    "realPrice": 1646.665,
    "realPricePlusDividend": 856062.2926
  },
  {
    "month": "2011-09-01",
    "price": 1173.88,
    "nominalPricePlusDividend": 611197.0063,
    "realPrice": 1628.3136,
    "realPricePlusDividend": 848032.7565
  },
  {
    "month": "2011-10-01",
    "price": 1207.22,
    "nominalPricePlusDividend": 629648.4692,
    "realPrice": 1678.0215,
    "realPricePlusDividend": 875462.6621
  },
  {
    "month": "2011-11-01",
    "price": 1226.42,
    "nominalPricePlusDividend": 640775.1286,
    "realPrice": 1706.1485,
    "realPricePlusDividend": 891708.2123
  },
  {
    "month": "2011-12-01",
    "price": 1243.32,
    "nominalPricePlusDividend": 650737.5866,
    "realPrice": 1733.9359,
    "realPricePlusDividend": 907834.1074
  },
  {
    "month": "2012-01-01",
    "price": 1300.58,
    "nominalPricePlusDividend": 681859.489,
    "realPrice": 1805.8447,
    "realPricePlusDividend": 947100.6167
  },
  {
    "month": "2012-02-01",
    "price": 1352.49,
    "nominalPricePlusDividend": 710242.6311,
    "realPrice": 1869.6891,
    "realPricePlusDividend": 982216.2064
  },
  {
    "month": "2012-03-01",
    "price": 1389.24,
    "nominalPricePlusDividend": 730724.873,
    "realPrice": 1906.0171,
    "realPricePlusDividend": 1002940.928
  },
  {
    "month": "2012-04-01",
    "price": 1386.43,
    "nominalPricePlusDividend": 730445.6606,
    "realPrice": 1896.4327,
    "realPricePlusDividend": 999554.9921
  },
  {
    "month": "2012-05-01",
    "price": 1341.27,
    "nominalPricePlusDividend": 707867.9342,
    "realPrice": 1836.8159,
    "realPricePlusDividend": 969814.2064
  },
  {
    "month": "2012-06-01",
    "price": 1323.48,
    "nominalPricePlusDividend": 699710.3855,
    "realPrice": 1815.1149,
    "realPricePlusDividend": 960062.7377
  },
  {
    "month": "2012-07-01",
    "price": 1359.78,
    "nominalPricePlusDividend": 720149.5334,
    "realPrice": 1867.9436,
    "realPricePlusDividend": 989743.0801
  },
  {
    "month": "2012-08-01",
    "price": 1403.45,
    "nominalPricePlusDividend": 744546.0448,
    "realPrice": 1917.2637,
    "realPricePlusDividend": 1017632.376
  },
  {
    "month": "2012-09-01",
    "price": 1443.42,
    "nominalPricePlusDividend": 767040.0175,
    "realPrice": 1963.1072,
    "realPricePlusDividend": 1043742.2618
  },
  {
    "month": "2012-10-01",
    "price": 1437.82,
    "nominalPricePlusDividend": 765374.5069,
    "realPrice": 1956.2518,
    "realPricePlusDividend": 1041911.8022
  },
  {
    "month": "2012-11-01",
    "price": 1394.51,
    "nominalPricePlusDividend": 743657.0516,
    "realPrice": 1906.3581,
    "realPricePlusDividend": 1017197.8472
  },
  {
    "month": "2012-12-01",
    "price": 1422.29,
    "nominalPricePlusDividend": 759835.5723,
    "realPrice": 1949.585,
    "realPricePlusDividend": 1042164.7712
  },
  {
    "month": "2013-01-01",
    "price": 1480.4,
    "nominalPricePlusDividend": 792271.14,
    "realPrice": 2023.2551,
    "realPricePlusDividend": 1083462.8105
  },
  {
    "month": "2013-02-01",
    "price": 1512.31,
    "nominalPricePlusDividend": 810754.9989,
    "realPrice": 2050.0762,
    "realPricePlusDividend": 1099747.8646
  },
  {
    "month": "2013-03-01",
    "price": 1550.83,
    "nominalPricePlusDividend": 832827.431,
    "realPrice": 2096.8115,
    "realPricePlusDividend": 1126756.5583
  },
  {
    "month": "2013-04-01",
    "price": 1570.7,
    "nominalPricePlusDividend": 844935.0046,
    "realPrice": 2125.887,
    "realPricePlusDividend": 1144347.4425
  },
  {
    "month": "2013-05-01",
    "price": 1639.84,
    "nominalPricePlusDividend": 883584.6113,
    "realPrice": 2215.521,
    "realPricePlusDividend": 1194586.6375
  },
  {
    "month": "2013-06-01",
    "price": 1618.77,
    "nominalPricePlusDividend": 873708.123,
    "realPrice": 2181.8185,
    "realPricePlusDividend": 1178426.4366
  },
  {
    "month": "2013-07-01",
    "price": 1668.68,
    "nominalPricePlusDividend": 902142.7544,
    "realPrice": 2248.2026,
    "realPricePlusDividend": 1216318.6444
  },
  {
    "month": "2013-08-01",
    "price": 1670.09,
    "nominalPricePlusDividend": 904420.9199,
    "realPrice": 2247.3988,
    "realPricePlusDividend": 1217944.8951
  },
  {
    "month": "2013-09-01",
    "price": 1687.17,
    "nominalPricePlusDividend": 915205.844,
    "realPrice": 2267.7456,
    "realPricePlusDividend": 1231056.5481
  },
  {
    "month": "2013-10-01",
    "price": 1720.03,
    "nominalPricePlusDividend": 934585.7845,
    "realPrice": 2317.8823,
    "realPricePlusDividend": 1260379.449
  },
  {
    "month": "2013-11-01",
    "price": 1783.54,
    "nominalPricePlusDividend": 970660.7401,
    "realPrice": 2408.3862,
    "realPricePlusDividend": 1311717.9551
  },
  {
    "month": "2013-12-01",
    "price": 1807.78,
    "nominalPricePlusDividend": 985430.9124,
    "realPrice": 2441.328,
    "realPricePlusDividend": 1331801.0126
  },
  {
    "month": "2014-01-01",
    "price": 1822.36,
    "nominalPricePlusDividend": 994967.9883,
    "realPrice": 2451.896,
    "realPricePlusDividend": 1339728.3071
  },
  {
    "month": "2014-02-01",
    "price": 1817.04,
    "nominalPricePlusDividend": 993674.1727,
    "realPrice": 2435.731,
    "realPricePlusDividend": 1333078.6356
  },
  {
    "month": "2014-03-01",
    "price": 1863.52,
    "nominalPricePlusDividend": 1020724.6598,
    "realPrice": 2482.0527,
    "realPricePlusDividend": 1360628.0977
  },
  {
    "month": "2014-04-01",
    "price": 1864.26,
    "nominalPricePlusDividend": 1022783.7061,
    "realPrice": 2474.8792,
    "realPricePlusDividend": 1358912.8201
  },
  {
    "month": "2014-05-01",
    "price": 1889.77,
    "nominalPricePlusDividend": 1038453.108,
    "realPrice": 2500.0132,
    "realPricePlusDividend": 1374949.6176
  },
  {
    "month": "2014-06-01",
    "price": 1947.09,
    "nominalPricePlusDividend": 1071645.3699,
    "realPrice": 2571.0553,
    "realPricePlusDividend": 1416279.9562
  },
  {
    "month": "2014-07-01",
    "price": 1973.1,
    "nominalPricePlusDividend": 1087675.2768,
    "realPrice": 2606.4175,
    "realPricePlusDividend": 1438045.1245
  },
  {
    "month": "2014-08-01",
    "price": 1961.53,
    "nominalPricePlusDividend": 1083031.4382,
    "realPrice": 2595.4696,
    "realPricePlusDividend": 1434320.4609
  },
  {
    "month": "2014-09-01",
    "price": 1993.23,
    "nominalPricePlusDividend": 1102288.1034,
    "realPrice": 2635.4312,
    "realPricePlusDividend": 1458744.4166
  },
  {
    "month": "2014-10-01",
    "price": 1937.27,
    "nominalPricePlusDividend": 1073115.1263,
    "realPrice": 2567.8927,
    "realPricePlusDividend": 1423730.1238
  },
  {
    "month": "2014-11-01",
    "price": 2044.57,
    "nominalPricePlusDividend": 1134343.3434,
    "realPrice": 2724.8336,
    "realPricePlusDividend": 1513149.1687
  },
  {
    "month": "2014-12-01",
    "price": 2054.27,
    "nominalPricePlusDividend": 1141533.8063,
    "realPrice": 2753.3729,
    "realPricePlusDividend": 1531440.1684
  },
  {
    "month": "2015-01-01",
    "price": 2028.18,
    "nominalPricePlusDividend": 1128862.2608,
    "realPrice": 2731.257,
    "realPricePlusDividend": 1521625.776
  },
  {
    "month": "2015-02-01",
    "price": 2082.2,
    "nominalPricePlusDividend": 1160779.6906,
    "realPrice": 2791.878,
    "realPricePlusDividend": 1557906.9334
  },
  {
    "month": "2015-03-01",
    "price": 2079.99,
    "nominalPricePlusDividend": 1161422.3383,
    "realPrice": 2772.4141,
    "realPricePlusDividend": 1549571.5156
  },
  {
    "month": "2015-04-01",
    "price": 2094.86,
    "nominalPricePlusDividend": 1171624.3844,
    "realPrice": 2786.5696,
    "realPricePlusDividend": 1560027.2135
  },
  {
    "month": "2015-05-01",
    "price": 2111.94,
    "nominalPricePlusDividend": 1183093.4615,
    "realPrice": 2795.0423,
    "realPricePlusDividend": 1567324.7777
  },
  {
    "month": "2015-06-01",
    "price": 2099.29,
    "nominalPricePlusDividend": 1177941.0887,
    "realPrice": 2768.6026,
    "realPricePlusDividend": 1555067.2121
  },
  {
    "month": "2015-07-01",
    "price": 2094.14,
    "nominalPricePlusDividend": 1177003.0931,
    "realPrice": 2761.6255,
    "realPricePlusDividend": 1553736.7259
  },
  {
    "month": "2015-08-01",
    "price": 2039.87,
    "nominalPricePlusDividend": 1148467.8595,
    "realPrice": 2693.8728,
    "realPricePlusDividend": 1518230.1896
  },
  {
    "month": "2015-09-01",
    "price": 1944.41,
    "nominalPricePlusDividend": 1096705.3164,
    "realPrice": 2571.811,
    "realPricePlusDividend": 1452074.6304
  },
  {
    "month": "2015-10-01",
    "price": 2024.81,
    "nominalPricePlusDividend": 1144051.3936,
    "realPrice": 2679.3585,
    "realPricePlusDividend": 1515458.1958
  },
  {
    "month": "2015-11-01",
    "price": 2080.62,
    "nominalPricePlusDividend": 1177600.3567,
    "realPrice": 2759.0333,
    "realPricePlusDividend": 1563212.2915
  },
  {
    "month": "2015-12-01",
    "price": 2054.08,
    "nominalPricePlusDividend": 1164611.7799,
    "realPrice": 2733.1791,
    "realPricePlusDividend": 1551285.7503
  },
  {
    "month": "2016-01-01",
    "price": 1918.6,
    "nominalPricePlusDividend": 1089848.1087,
    "realPrice": 2548.6948,
    "realPricePlusDividend": 1449309.4195
  },
  {
    "month": "2016-02-01",
    "price": 1904.42,
    "nominalPricePlusDividend": 1083854.935,
    "realPrice": 2527.7774,
    "realPricePlusDividend": 1440160.3628
  },
  {
    "month": "2016-03-01",
    "price": 2021.95,
    "nominalPricePlusDividend": 1152817.6713,
    "realPrice": 2672.2707,
    "realPricePlusDividend": 1525232.3728
  },
  {
    "month": "2016-04-01",
    "price": 2075.54,
    "nominalPricePlusDividend": 1185456.9398,
    "realPrice": 2730.153,
    "realPricePlusDividend": 1561022.789
  },
  {
    "month": "2016-05-01",
    "price": 2065.55,
    "nominalPricePlusDividend": 1181848.821,
    "realPrice": 2706.064,
    "realPricePlusDividend": 1550008.5592
  },
  {
    "month": "2016-06-01",
    "price": 2083.89,
    "nominalPricePlusDividend": 1194453.1232,
    "realPrice": 2721.1539,
    "realPricePlusDividend": 1561418.9331
  },
  {
    "month": "2016-07-01",
    "price": 2148.9,
    "nominalPricePlusDividend": 1233839.4854,
    "realPrice": 2810.5922,
    "realPricePlusDividend": 1615527.6307
  },
  {
    "month": "2016-08-01",
    "price": 2170.95,
    "nominalPricePlusDividend": 1248636.3916,
    "realPrice": 2836.8264,
    "realPricePlusDividend": 1633409.5122
  },
  {
    "month": "2016-09-01",
    "price": 2157.69,
    "nominalPricePlusDividend": 1243158.9828,
    "realPrice": 2812.7375,
    "realPricePlusDividend": 1622351.8019
  },
  {
    "month": "2016-10-01",
    "price": 2143.02,
    "nominalPricePlusDividend": 1236868.8354,
    "realPrice": 2790.1353,
    "realPricePlusDividend": 1612142.8516
  },
  {
    "month": "2016-11-01",
    "price": 2164.99,
    "nominalPricePlusDividend": 1251725.6161,
    "realPrice": 2823.1307,
    "realPricePlusDividend": 1634058.7515
  },
  {
    "month": "2016-12-01",
    "price": 2246.63,
    "nominalPricePlusDividend": 1301118.2561,
    "realPrice": 2928.63,
    "realPricePlusDividend": 1697992.1023
  },
  {
    "month": "2017-01-01",
    "price": 2275.12,
    "nominalPricePlusDividend": 1319823.5841,
    "realPrice": 2948.5851,
    "realPricePlusDividend": 1712433.4054
  },
  {
    "month": "2017-02-01",
    "price": 2329.91,
    "nominalPricePlusDividend": 1353828.1168,
    "realPrice": 3010.1234,
    "realPricePlusDividend": 1751054.2058
  },
  {
    "month": "2017-03-01",
    "price": 2366.82,
    "nominalPricePlusDividend": 1377510.0483,
    "realPrice": 3055.3259,
    "realPricePlusDividend": 1780247.5372
  },
  {
    "month": "2017-04-01",
    "price": 2359.31,
    "nominalPricePlusDividend": 1375388.6263,
    "realPrice": 3036.626,
    "realPricePlusDividend": 1772263.3783
  },
  {
    "month": "2017-05-01",
    "price": 2395.35,
    "nominalPricePlusDividend": 1398665.3366,
    "realPrice": 3080.3796,
    "realPricePlusDividend": 1800730.7253
  },
  {
    "month": "2017-06-01",
    "price": 2433.99,
    "nominalPricePlusDividend": 1423511.6185,
    "realPrice": 3127.2332,
    "realPricePlusDividend": 1831071.5661
  },
  {
    "month": "2017-07-01",
    "price": 2454.1,
    "nominalPricePlusDividend": 1437574.2633,
    "realPrice": 3155.2478,
    "realPricePlusDividend": 1850452.5205
  },
  {
    "month": "2017-08-01",
    "price": 2456.22,
    "nominalPricePlusDividend": 1441136.6479,
    "realPrice": 3148.5453,
    "realPricePlusDividend": 1849515.1808
  },
  {
    "month": "2017-09-01",
    "price": 2492.84,
    "nominalPricePlusDividend": 1464962.4277,
    "realPrice": 3178.6566,
    "realPricePlusDividend": 1870205.3465
  },
  {
    "month": "2017-10-01",
    "price": 2557,
    "nominalPricePlusDividend": 1505026.2074,
    "realPrice": 3262.53,
    "realPricePlusDividend": 1922578.1929
  },
  {
    "month": "2017-11-01",
    "price": 2593.61,
    "nominalPricePlusDividend": 1528949.6366,
    "realPrice": 3309.161,
    "realPricePlusDividend": 1953102.7279
  },
  {
    "month": "2017-12-01",
    "price": 2664.34,
    "nominalPricePlusDividend": 1573036.6898,
    "realPrice": 3401.4041,
    "realPricePlusDividend": 2010613.4125
  },
  {
    "month": "2018-01-01",
    "price": 2789.8,
    "nominalPricePlusDividend": 1649516.1332,
    "realPrice": 3542.274,
    "realPricePlusDividend": 2096961.499
  },
  {
    "month": "2018-02-01",
    "price": 2705.16,
    "nominalPricePlusDividend": 1601899.7749,
    "realPrice": 3419.2992,
    "realPricePlusDividend": 2027253.5466
  },
  {
    "month": "2018-03-01",
    "price": 2702.77,
    "nominalPricePlusDividend": 1602934.2535,
    "realPrice": 3408.571,
    "realPricePlusDividend": 2024003.8143
  },
  {
    "month": "2018-04-01",
    "price": 2653.63,
    "nominalPricePlusDividend": 1576261.8779,
    "realPrice": 3333.3482,
    "realPricePlusDividend": 1982460.4211
  },
  {
    "month": "2018-05-01",
    "price": 2701.49,
    "nominalPricePlusDividend": 1607182.1639,
    "realPrice": 3379.4127,
    "realPricePlusDividend": 2012992.7684
  },
  {
    "month": "2018-06-01",
    "price": 2754.35,
    "nominalPricePlusDividend": 1641141.4369,
    "realPrice": 3440.0546,
    "realPricePlusDividend": 2052271.4144
  },
  {
    "month": "2018-07-01",
    "price": 2793.64,
    "nominalPricePlusDividend": 1667083.6485,
    "realPrice": 3488.8906,
    "realPricePlusDividend": 2084595.0883
  },
  {
    "month": "2018-08-01",
    "price": 2857.82,
    "nominalPricePlusDividend": 1707940.6167,
    "realPrice": 3567.0614,
    "realPricePlusDividend": 2134521.8143
  },
  {
    "month": "2018-09-01",
    "price": 2901.5,
    "nominalPricePlusDividend": 1736629.7105,
    "realPrice": 3617.3782,
    "realPricePlusDividend": 2167880.429
  },
  {
    "month": "2018-10-01",
    "price": 2785.46,
    "nominalPricePlusDividend": 1669787.0733,
    "realPrice": 3466.5834,
    "realPricePlusDividend": 2080787.127
  },
  {
    "month": "2018-11-01",
    "price": 2723.23,
    "nominalPricePlusDividend": 1635120.4851,
    "realPrice": 3400.5259,
    "realPricePlusDividend": 2044459.6665
  },
  {
    "month": "2018-12-01",
    "price": 2567.31,
    "nominalPricePlusDividend": 1544166.7092,
    "realPrice": 3216.0991,
    "realPricePlusDividend": 1936947.2903
  },
  {
    "month": "2019-01-01",
    "price": 2607.39,
    "nominalPricePlusDividend": 1570967.8285,
    "realPrice": 3260.0921,
    "realPricePlusDividend": 1966835.5672
  },
  {
    "month": "2019-02-01",
    "price": 2754.86,
    "nominalPricePlusDividend": 1662538.0124,
    "realPrice": 3429.9792,
    "realPricePlusDividend": 2072738.7552
  },
  {
    "month": "2019-03-01",
    "price": 2803.98,
    "nominalPricePlusDividend": 1694924.618,
    "realPrice": 3471.5525,
    "realPricePlusDividend": 2101281.826
  },
  {
    "month": "2019-04-01",
    "price": 2903.8,
    "nominalPricePlusDividend": 1758030.3838,
    "realPrice": 3576.2017,
    "realPricePlusDividend": 2168055.8408
  },
  {
    "month": "2019-05-01",
    "price": 2854.71,
    "nominalPricePlusDividend": 1731101.0758,
    "realPrice": 3508.2762,
    "realPricePlusDividend": 2130329.2865
  },
  {
    "month": "2019-06-01",
    "price": 2890.17,
    "nominalPricePlusDividend": 1755418.7039,
    "realPrice": 3551.1473,
    "realPricePlusDividend": 2159843.332
  },
  {
    "month": "2019-07-01",
    "price": 2996.1136,
    "nominalPricePlusDividend": 1822604.613,
    "realPrice": 3675.1791,
    "realPricePlusDividend": 2238785.575
  },
  {
    "month": "2019-08-01",
    "price": 2897.4982,
    "nominalPricePlusDividend": 1765476.6385,
    "realPrice": 3554.3927,
    "realPricePlusDividend": 2168741.1081
  },
  {
    "month": "2019-09-01",
    "price": 2982.156,
    "nominalPricePlusDividend": 1819945.6083,
    "realPrice": 3655.3795,
    "realPricePlusDividend": 2233919.9941
  },
  {
    "month": "2019-10-01",
    "price": 2977.68,
    "nominalPricePlusDividend": 1820124.013,
    "realPrice": 3641.5677,
    "realPricePlusDividend": 2229058.8078
  },
  {
    "month": "2019-11-01",
    "price": 3104.9045,
    "nominalPricePlusDividend": 1900822.7099,
    "realPrice": 3799.1948,
    "realPricePlusDividend": 2329153.246
  },
  {
    "month": "2019-12-01",
    "price": 3176.7495,
    "nominalPricePlusDividend": 1947760.1028,
    "realPrice": 3890.6448,
    "realPricePlusDividend": 2388856.6394
  },
  {
    "month": "2020-01-01",
    "price": 3278.2029,
    "nominalPricePlusDividend": 2012939.8981,
    "realPrice": 3999.3805,
    "realPricePlusDividend": 2459278.3783
  },
  {
    "month": "2020-02-01",
    "price": 3277.3142,
    "nominalPricePlusDividend": 2015397.2311,
    "realPrice": 3987.3685,
    "realPricePlusDividend": 2455573.2376
  },
  {
    "month": "2020-03-01",
    "price": 2652.3936,
    "nominalPricePlusDividend": 1634130.2493,
    "realPrice": 3234.0932,
    "realPricePlusDividend": 1995400.3011
  },
  {
    "month": "2020-04-01",
    "price": 2761.9752,
    "nominalPricePlusDividend": 1704702.0326,
    "realPrice": 3390.3785,
    "realPricePlusDividend": 2095583.5095
  },
  {
    "month": "2020-05-01",
    "price": 2919.615,
    "nominalPricePlusDividend": 1805064.0694,
    "realPrice": 3583.8145,
    "realPricePlusDividend": 2218911.3814
  },
  {
    "month": "2020-06-01",
    "price": 3104.6609,
    "nominalPricePlusDividend": 1922542.5463,
    "realPrice": 3790.2173,
    "realPricePlusDividend": 2350458.8232
  },
  {
    "month": "2020-07-01",
    "price": 3207.6191,
    "nominalPricePlusDividend": 1989378.4862,
    "realPrice": 3896.2023,
    "realPricePlusDividend": 2419907.4849
  },
  {
    "month": "2020-08-01",
    "price": 3391.71,
    "nominalPricePlusDividend": 2106622.6039,
    "realPrice": 4106.8624,
    "realPricePlusDividend": 2554447.2189
  },
  {
    "month": "2020-09-01",
    "price": 3365.5167,
    "nominalPricePlusDividend": 2093414.0246,
    "realPrice": 4069.4783,
    "realPricePlusDividend": 2534877.4681
  },
  {
    "month": "2020-10-01",
    "price": 3418.7014,
    "nominalPricePlusDividend": 2129546.3793,
    "realPrice": 4132.0731,
    "realPricePlusDividend": 2577542.5434
  },
  {
    "month": "2020-11-01",
    "price": 3548.9925,
    "nominalPricePlusDividend": 2213751.1259,
    "realPrice": 4292.1726,
    "realPricePlusDividend": 2681081.2974
  },
  {
    "month": "2020-12-01",
    "price": 3695.31,
    "nominalPricePlusDividend": 2308058.705,
    "realPrice": 4464.9263,
    "realPricePlusDividend": 2792650.8559
  },
  {
    "month": "2021-01-01",
    "price": 3793.7484,
    "nominalPricePlusDividend": 2372575.8644,
    "realPrice": 4564.4501,
    "realPricePlusDividend": 2858535.2412
  },
  {
    "month": "2021-02-01",
    "price": 3883.4321,
    "nominalPricePlusDividend": 2431689.2696,
    "realPrice": 4646.9141,
    "realPricePlusDividend": 2913786.3701
  },
  {
    "month": "2021-03-01",
    "price": 3910.5083,
    "nominalPricePlusDividend": 2451662.1358,
    "realPrice": 4646.4017,
    "realPricePlusDividend": 2917037.9897
  },
  {
    "month": "2021-04-01",
    "price": 4141.1762,
    "nominalPricePlusDividend": 2599288.6309,
    "realPrice": 4880.3662,
    "realPricePlusDividend": 3067475.1927
  },
  {
    "month": "2021-05-01",
    "price": 4167.8495,
    "nominalPricePlusDividend": 2619049.2423,
    "realPrice": 4872.7354,
    "realPricePlusDividend": 3066212.4207
  },
  {
    "month": "2021-06-01",
    "price": 4238.4895,
    "nominalPricePlusDividend": 2666465.1068,
    "realPrice": 4909.708,
    "realPricePlusDividend": 3092987.3849
  },
  {
    "month": "2021-07-01",
    "price": 4363.7129,
    "nominalPricePlusDividend": 2748277.6284,
    "realPrice": 5030.5624,
    "realPricePlusDividend": 3172647.2652
  },
  {
    "month": "2021-08-01",
    "price": 4454.2064,
    "nominalPricePlusDividend": 2808331.9429,
    "realPrice": 5124.2985,
    "realPricePlusDividend": 3235313.636
  },
  {
    "month": "2021-09-01",
    "price": 4445.5433,
    "nominalPricePlusDividend": 2805958.9352,
    "realPrice": 5100.4794,
    "realPricePlusDividend": 3223846.6608
  },
  {
    "month": "2021-10-01",
    "price": 4460.7071,
    "nominalPricePlusDividend": 2818646.81,
    "realPrice": 5075.7077,
    "realPricePlusDividend": 3211758.1149
  },
  {
    "month": "2021-11-01",
    "price": 4667.3867,
    "nominalPricePlusDividend": 2952384.3871,
    "realPrice": 5284.9152,
    "realPricePlusDividend": 3347716.5529
  },
  {
    "month": "2021-12-01",
    "price": 4674.7727,
    "nominalPricePlusDividend": 2960220.1226,
    "realPrice": 5277.0646,
    "realPricePlusDividend": 3346337.2332
  },
  {
    "month": "2022-01-01",
    "price": 4573.8155,
    "nominalPricePlusDividend": 2899477.8002,
    "realPrice": 5120.0174,
    "realPricePlusDividend": 3250347.5512
  },
  {
    "month": "2022-02-01",
    "price": 4435.9805,
    "nominalPricePlusDividend": 2815318.4315,
    "realPrice": 4920.776,
    "realPricePlusDividend": 3127463.3944
  },
  {
    "month": "2022-03-01",
    "price": 4391.2652,
    "nominalPricePlusDividend": 2790189.3608,
    "realPrice": 4806.9939,
    "realPricePlusDividend": 3058735.2227
  },
  {
    "month": "2022-04-01",
    "price": 4391.296,
    "nominalPricePlusDividend": 2793490.2058,
    "realPrice": 4780.3412,
    "realPricePlusDividend": 3045387.0519
  },
  {
    "month": "2022-05-01",
    "price": 4040.36,
    "nominalPricePlusDividend": 2573566.2563,
    "realPrice": 4350.3579,
    "realPricePlusDividend": 2775074.8872
  },
  {
    "month": "2022-06-01",
    "price": 3898.9467,
    "nominalPricePlusDividend": 2486852.9042,
    "realPrice": 4141.2106,
    "realPricePlusDividend": 2645269.9684
  },
  {
    "month": "2022-07-01",
    "price": 3911.7295,
    "nominalPricePlusDividend": 2498408.9449,
    "realPrice": 4155.2785,
    "realPricePlusDividend": 2657895.1474
  },
  {
    "month": "2022-08-01",
    "price": 4158.563,
    "nominalPricePlusDividend": 2659491.2098,
    "realPrice": 4419.0463,
    "realPricePlusDividend": 2830282.2069
  },
  {
    "month": "2022-09-01",
    "price": 3850.5205,
    "nominalPricePlusDividend": 2465949.2863,
    "realPrice": 4082.9271,
    "realPricePlusDividend": 2618697.9135
  },
  {
    "month": "2022-10-01",
    "price": 3726.051,
    "nominalPricePlusDividend": 2389722.475,
    "realPrice": 3934.9827,
    "realPricePlusDividend": 2527521.2073
  },
  {
    "month": "2022-11-01",
    "price": 3917.4886,
    "nominalPricePlusDividend": 2516021.5589,
    "realPrice": 4141.3377,
    "realPricePlusDividend": 2663818.2108
  },
  {
    "month": "2022-12-01",
    "price": 3912.381,
    "nominalPricePlusDividend": 2516294.2316,
    "realPrice": 4148.6751,
    "realPricePlusDividend": 2672335.8309
  },
  {
    "month": "2023-01-01",
    "price": 3960.6565,
    "nominalPricePlusDividend": 2550929.9222,
    "realPrice": 4166.5532,
    "realPricePlusDividend": 2687649.4062
  },
  {
    "month": "2023-02-01",
    "price": 4079.6847,
    "nominalPricePlusDividend": 2631206.9635,
    "realPrice": 4267.945,
    "realPricePlusDividend": 2756858.4985
  },
  {
    "month": "2023-03-01",
    "price": 3968.5591,
    "nominalPricePlusDividend": 2563179.0267,
    "realPrice": 4137.9917,
    "realPricePlusDividend": 2676738.4773
  },
  {
    "month": "2023-04-01",
    "price": 4121.4674,
    "nominalPricePlusDividend": 2665609.3325,
    "realPrice": 4275.7967,
    "realPricePlusDividend": 2769698.511
  },
  {
    "month": "2023-05-01",
    "price": 4146.1732,
    "nominalPricePlusDividend": 2685273.4059,
    "realPrice": 4290.622,
    "realPricePlusDividend": 2783124.9516
  },
  {
    "month": "2023-06-01",
    "price": 4345.3729,
    "nominalPricePlusDividend": 2817984.6311,
    "realPrice": 4482.2887,
    "realPricePlusDividend": 2911275.5315
  },
  {
    "month": "2023-07-01",
    "price": 4508.0755,
    "nominalPricePlusDividend": 2927210.8985,
    "realPrice": 4641.2645,
    "realPricePlusDividend": 3018365.7188
  },
  {
    "month": "2023-08-01",
    "price": 4457.3587,
    "nominalPricePlusDividend": 2898007.9672,
    "realPrice": 4569.0954,
    "realPricePlusDividend": 2975265.4314
  },
  {
    "month": "2023-09-01",
    "price": 4409.095,
    "nominalPricePlusDividend": 2870373.225,
    "realPrice": 4508.4178,
    "realPricePlusDividend": 2939594.1512
  },
  {
    "month": "2023-10-01",
    "price": 4269.4009,
    "nominalPricePlusDividend": 2783191.0185,
    "realPrice": 4367.2511,
    "realPricePlusDividend": 2851415.2541
  },
  {
    "month": "2023-11-01",
    "price": 4460.0633,
    "nominalPricePlusDividend": 2911265.7798,
    "realPrice": 4571.4956,
    "realPricePlusDividend": 2988664.6683
  },
  {
    "month": "2023-12-01",
    "price": 4685.0515,
    "nominalPricePlusDividend": 3061930.9736,
    "realPrice": 4806.8797,
    "realPricePlusDividend": 3146473.502
  },
  {
    "month": "2024-01-01",
    "price": 4815.6139,
    "nominalPricePlusDividend": 3151089.4067,
    "realPrice": 4914.0678,
    "realPricePlusDividend": 3220553.5545
  },
  {
    "month": "2024-02-01",
    "price": 5011.9615,
    "nominalPricePlusDividend": 3283412.207,
    "realPrice": 5082.9678,
    "realPricePlusDividend": 3335153.6624
  },
  {
    "month": "2024-03-01",
    "price": 5170.5725,
    "nominalPricePlusDividend": 3391177.7371,
    "realPrice": 5210.1466,
    "realPricePlusDividend": 3422497.5957
  },
  {
    "month": "2024-04-01",
    "price": 5112.4927,
    "nominalPricePlusDividend": 3356956.4071,
    "realPrice": 5131.6433,
    "realPricePlusDividend": 3374836.3032
  },
  {
    "month": "2024-05-01",
    "price": 5235.2255,
    "nominalPricePlusDividend": 3441441.3644,
    "realPrice": 5246.1187,
    "realPricePlusDividend": 3454047.1548
  },
  {
    "month": "2024-06-01",
    "price": 5415.1405,
    "nominalPricePlusDividend": 3563632.6349,
    "realPrice": 5424.5773,
    "realPricePlusDividend": 3575494.465
  },
  {
    "month": "2024-07-01",
    "price": 5538.0045,
    "nominalPricePlusDividend": 3648435.0209,
    "realPrice": 5541.2178,
    "realPricePlusDividend": 3656330.0023
  },
  {
    "month": "2024-08-01",
    "price": 5478.2146,
    "nominalPricePlusDividend": 3612996.8845,
    "realPrice": 5478.2146,
    "realPricePlusDividend": 3618716.5579
  }
]

for entry in data:
    entry["month"] = datetime.strptime(entry["month"], "%Y-%m-%d")


if __name__ == '__main__':
    n_periods = 10
    min_months_spacing = 12 * 5
    running_heap = []
    for i in range(0, len(data), 1):
        for j in range(i + 1, len(data)):
            if data[i]["month"] < datetime.strptime('1950-01-01', "%Y-%m-%d"):
                continue
            start_price = data[i]["price"]
            end_price = data[j]["price"]
            date_range = (data[i]["month"], data[j]["month"])

            years_difference = (
                data[j]["month"] - data[i]["month"]).days / 365
            months_difference = (
                data[j]["month"].year - data[i]["month"].year) * 12 + (
                data[j]["month"].month - data[i]["month"].month)

            if months_difference >= min_months_spacing:
                total_return = (end_price / start_price)
                annualized_return = pow(total_return, 1 / years_difference) - 1

                if len(running_heap) < n_periods:
                    heapq.heappush(running_heap, (-annualized_return, date_range))
                else:
                    heapq.heappushpop(running_heap, (-annualized_return, date_range))

    least_returns = sorted([(-annualized_return, date_range) for annualized_return, date_range in running_heap])

    for annualized_return, period in least_returns:
        print(f"Period: {period[0].strftime('%Y-%m-%d')} to {period[1].strftime('%Y-%m-%d')}")
        print(f"Annualized return: {annualized_return * 100:.2f}%")
