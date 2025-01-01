def iterate_linear_equations(a1, b1, a2, b2, x1, y_target,max_iter=10, tol=1e-4):
    """
    在两个线性方程之间迭代计算
    :param a1, b1: 第一个线性方程的系数 y = a1*x + b1
    :param a2, b2: 第二个线性方程的系数 y = a2*x + b2
    :param x0: 初始的 x 值
    :param max_iter: 最大迭代次数
    :param tol: 收敛容差
    :return: 最终的 x 值
    """
    x = x1
    print(f"开始迭代计算，初始 x 值为 {x}")
    for i in range(max_iter):
        # 平衡线方程计算 y
        y = a1 * x + b1
        print(f"y{i+1} = {y}")
        # 操作线方程计算新的 x
        x_new = (y - b2) / a2
        print(f"x{i+2} = {x_new}")
        # 检查是否达到目标
        if y - y_target <= 0:
            print(f"迭代在第 {i+1} 次达到预设值")
            return y
        x = x_new
    print(f"达到最大迭代次数 {max_iter}，未达到预设值")
    return x

# 示例参数
a1, b1 = 0.4 , 0 # 第一个方程 y = 2x + 3
a2, b2 = 0.5, 0.001  # 第二个方程 y = 0.5x - 1
x1 = 0.018  # 初始 x 值
y_target = 0.001  # 目标 x 值

# 调用函数进行迭代
result = iterate_linear_equations(a1, b1, a2, b2, x1, y_target)
print(f"最终的 y 值为: {result}")
