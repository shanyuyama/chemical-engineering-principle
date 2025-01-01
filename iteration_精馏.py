def iterate_equations_liquid(a, b, alpha, y1, x_F, y_F, max_iter=10, tol=1e-3):
    """
    在线性方程和非线性方程之间迭代计算
    :param a, b: 线性方程的系数 y = a*x + b
    :param alpha: 非线性方程的参数 y = alpha*x / (1 + (alpha - 1)*x)
    :param x0: 初始的 x 值
    :param max_iter: 最大迭代次数
    :param tol: 收敛容差
    :return: 最终的 x 值
    """
    y = y1
    for i in range(max_iter):
        # 平衡关系
        x = y / (alpha - (alpha - 1) * y)
        delta_x = abs(x - x_F)
        print(f"x{i+1} = {x}")
        # 在线性方程中计算 y
        y = a * x + b
        print(f"y{i+2} = {y}")
        # 检查是否收敛
        x_new = y / (alpha - (alpha - 1) * y)
        if abs(x_new - x_F) > delta_x:
            print(f"在第 {i+1} 级进料")
            return x, i
    print(f"达到最大迭代次数 {max_iter}，未收敛")
    return 0

def iterate_equations_vapor(a, b, alpha, y1, x_F, y_F, max_iter=10, tol=1e-3):
    """
    在线性方程和非线性方程之间迭代计算
    :param a, b: 线性方程的系数 y = a*x + b
    :param alpha: 非线性方程的参数 y = alpha*x / (1 + (alpha - 1)*x)
    :param x0: 初始的 x 值
    :param max_iter: 最大迭代次数
    :param tol: 收敛容差
    :return: 最终的 x 值
    """
    y = y1
    for i in range(max_iter):
        # 平衡关系
        x = y / (alpha - (alpha - 1) * y)
        print(f"x{i+1} = {x}")
        # 在线性方程中计算 y
        y = a * x + b
        print(f"y{i+2} = {y}")
        # 检查是否收敛
        if abs(y - y_F) < tol:
            print(f"在第 {i+2} 级进料")
            x = y / (alpha - (alpha - 1) * y)
            return x, i
    print(f"达到最大迭代次数 {max_iter}，未收敛")
    return 0

def iterate_equations_2(a, b, alpha, x, x_target, i, max_iter=10, tol=1e-4):
    """
    在线性方程和非线性方程之间迭代计算
    :param a, b: 线性方程的系数 y = a*x + b
    :param alpha: 非线性方程的参数 y = alpha*x / (1 + (alpha - 1)*x)
    :param x0: 初始的 x 值
    :param max_iter: 最大迭代次数
    :param tol: 收敛容差
    :return: 最终的 x 值
    """
    for j in range(max_iter):
        # 在线性方程中计算 y
        y = a * x + b
        print(f"y{j+i+1} = {y}")
        # 平衡关系
        x = y / (alpha - (alpha - 1) * y)
        print(f"x{j+i+2} = {x}")
        # 检查是否收敛
        if x - x_target <= 0:
            print(f"第 {j+i+2} 级完成")
            # x = y / (alpha - (alpha - 1) * y)
            return x
    print(f"达到最大迭代次数 {max_iter}，未收敛")
    return 0
# 示例参数
a, b = 0.375, 0.563  # 精馏操作线
alpha = 4    # 挥发性系数
y1 = 0.9     # y1 塔顶的气相摩尔分数
x_F = 0.43    # 泡点进料的 x 值
y_F = 0.43  # 饱和蒸汽进料的 y 值

# 调用函数进行迭代
x, i= iterate_equations_liquid(a, b, alpha, y1, x_F, y_F)
# x, i = iterate_equations_vapor(a, b, alpha, y1, x_F, y_F)
# print(f"最终的 x 值为: {result}")

a, b = 1.56, -0.0057  # 提馏操作线
alpha = 3    # 挥发性系数
x_target = 0.01

x = iterate_equations_2(a, b, alpha, x, x_target, i)