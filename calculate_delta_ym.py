import math

def calculate_delta_y(a1, b1, a2, b2, x):
    y1 = a1*x+b1
    y2 = a2*x+b2
    delta_y = abs(y2-y1)
    return delta_y
def calculate_delta_ym(delta_y1, delta_y2):
    if delta_y1 == delta_y2:
        return delta_y1
    elif delta_y1 == 0 or delta_y2 == 0:
        return 0
    else:
        return (delta_y2 - delta_y1) / math.log(delta_y2 / delta_y1)
def calculate_Nog(a1, b1, x0, xN, delta_ym):
    y1 = a1*x0+b1
    y2 = a1*xN+b1
    Nog = (y2-y1)/delta_ym
    return Nog
def calculate_delta_x(a1, b1, a2, b2, x):
    y = a1*x+b1
    x2 = (y-b2)/a2
    delta_x = abs(x2-x)
    return delta_x
def calculate_delta_xm(delta_x1, delta_x2):
    if delta_x1 == delta_x2:
        return delta_x1
    elif delta_x1 == 0 or delta_x2 == 0:
        return 0
    else:
        return (delta_x1 - delta_x2) / math.log(delta_x1 / delta_x2)
def calculate_Nol(x0, xN, delta_xm):
    return abs(x0-xN)/delta_xm

def main():
    a1, b1, a2, b2 = 0.5, 0.001, 0.4, 0 # 操作线和平衡线，1是操作线
    x0, xN = 0, 0.018 # 进口和出口的液相
    delta_y1 = calculate_delta_y(a1, b1, a2, b2, x0)
    delta_y2 = calculate_delta_y(a1, b1, a2, b2, xN)
    print(f"delta_y1: {delta_y1}, delta_y2: {delta_y2}")
    # 计算对数平均值
    delta_ym = calculate_delta_ym(delta_y1, delta_y2)
    print(f"对数平均值 delta_ym: {delta_ym}")

    # 计算Nog
    Nog = calculate_Nog(a1, b1, x0, xN, delta_ym)
    print(f"Nog: {Nog}")

    # 计算Nol
    delta_x1 = calculate_delta_x(a1, b1, a2, b2, x0)
    delta_x2 = calculate_delta_x(a1, b1, a2, b2, xN)
    print(f"delta_x1: {delta_x1}, delta_x2: {delta_x2}")
    delta_xm = calculate_delta_xm(delta_x1, delta_x2)
    print(f"对数平均值 delta_xm: {delta_xm}")
    Nol = calculate_Nol(x0, xN, delta_xm)
    print(f"Nol: {Nol}")




if __name__ == '__main__':
    main()


