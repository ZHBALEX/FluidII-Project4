import numpy as np
import matplotlib.pyplot as plt
def read():

    x_coords = []
    y_coords = []

    with open("NACA65210.txt", "r") as file:
        # 跳过文件开头的注释行
        for line in file:
            if not line.startswith("#"):
                # 分割每一行的数据
                data = line.split()
                # 将第三列数据添加到x坐标数组
                x_coords.append(float(data[2]))
                # 将第四列数据添加到y坐标数组
                y_coords.append(float(data[3]))

        return x_coords, y_coords

def fitting(x, y):
    degree = 10

    # 拟合多项式
    coefficients = np.polyfit(x, y, degree)

    # 创建多项式函数
    polynomial = np.poly1d(coefficients)

    return polynomial, coefficients

def main():

    x,y = read()

    size = np.size(x)

    # # center for camber
    # x_new = np.full(int(size/2), 0, dtype='float')
    # y_new = np.zeros_like(x_new)

    # for i in range(0,int(size/2)-1):
    #     x_new[i] = (x[i] + x[-i-1])/2
    #     y_new[i] = (y[i] + y[-i-1])/2

    # plt.plot(x, y, label='airfoil')
    # plt.plot(x_new, y_new, label='camber')
    # plt.show()
    # ###########################


    x_pos = x[:int(size/2)+1]
    y_pos = y[:int(size/2)+1]

    x_neg = x[int(size/2):]
    y_neg = y[int(size/2):]

    fun_neg , coff_neg = fitting(x_neg, y_neg)
    fun_pos , coff_pos = fitting(x_pos, y_pos)

    # # degree = 10

    # # # 拟合多项式
    # # coefficients = np.polyfit(x_neg, y_neg, degree)

    # # # 创建多项式函数
    # # polynomial = np.poly1d(coefficients)

    # # # 打印多项式的系数
    # # print("拟合的多项式系数:", coefficients)

    # # 使用多项式函数计算新的y值
    # y_new = polynomial(x)
    plt.plot(x_neg, y_neg)
    plt.plot(x_neg, fun_neg(x_neg))

    plt.plot(x_pos, y_pos)
    plt.plot(x_pos, fun_pos(x_pos))

    # plt.plot((x_neg + x_pos)/2, (fun_neg+fun_pos)/2)


    plt.show()

if __name__ == '__main__':
    main()











