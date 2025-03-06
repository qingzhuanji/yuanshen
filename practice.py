def fibonacci(n):
    """
    生成斐波那契数列的前n个数
    :param n: 要生成的斐波那契数列长度
    :return: 包含斐波那契数列的列表
    """
    # 输入验证
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n必须是正整数")
    
    # 初始化斐波那契数列
    fib_list = [1, 1]
    
    # 如果n小于等于2，直接返回对应长度的列表
    if n <= 2:
        return fib_list[:n]
    
    # 生成剩余的斐波那契数
    for i in range(2, n):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    
    return fib_list

# 测试代码
if __name__ == "__main__":
    try:
        n = 10  # 生成前10个斐波那契数
        result = fibonacci(n)
        print(f"斐波那契数列的前{n}个数是：{result}")
    except ValueError as e:
        print(f"错误：{e}")