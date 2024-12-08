# -*- coding: utf8 -*-

import numpy as np


x = [100,200,300,400,500]
y = [115,225,335,445,555]

fit = np.polyfit(x, y, 1)

print('[傾き,切片]=', fit)
print('y = %.3fx + %.3f' % (fit[0] ,fit[1]))

func = np.poly1d(fit)

tg_x = 250
tg_y = func(tg_x)

print('tg_x = 250 --> tg_y = %.0f' % (tg_y))
print('%.0f' % (np.poly1d(fit)(250)))


'''

Polyfit関数
numpy.polyfit(説明変数xの配列、目的変数yの配列,次元)
polyfit関数の引数にx、yの配列を指定することで、
変数fitに傾きと切片の配列を返す

poly1dメソッド
numpy.poly1d（[配列]）
引数に[1,2]を指定するとx+2y、
[1,2,3]を指定するとx2+2X+3のように、
多項式を返す

'''

