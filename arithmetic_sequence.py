def geometric_sum_formula(first_term, r, n):
    """
    使用等比数列求和公式计算和
    :param first_term: 首项
    :param r: 公比
    :param n: 项数
    :return: 等比数列的和
    """
    if r == 1:
        return first_term * n
    return first_term * (1 - r ** n) / (1 - r)

def geometric_sum_by_last(first_term, last_term, n):
    """
    已知首项和末项计算等比数列的和
    :param first_term: 首项a1
    :param last_term: 末项
    :param n: 项数
    :return: 等比数列的和
    """
    if n <= 0:
        raise ValueError("项数必须为正整数")
    if first_term == 0:
        raise ValueError("首项不能为0")
    
    # 计算公比
    r = (last_term / first_term) ** (1 / (n - 1))
    return geometric_sum_formula(first_term, r, n)

def generate_geometric_sequence(first_term, r, n):
    """
    生成等比数列
    :param first_term: 首项
    :param r: 公比
    :param n: 项数
    :return: 等比数列列表
    """
    if n <= 0:
        raise ValueError("项数必须为正整数")
    return [first_term * (r ** i) for i in range(n)]

if __name__ == "__main__":
    try:
        # 示例1：已知首项、公比和项数
        a1 = 2
        r = 2
        n = 5
        sequence = generate_geometric_sequence(a1, r, n)
        sum1 = geometric_sum_formula(a1, r, n)
        print(f"首项{a1}，公比{r}，项数{n}的等比数列为：")
        print(sequence)
        print(f"该等比数列的和为：{sum1}")
        
        # 示例2：已知首项、末项和项数
        a1 = 2
        an = 32
        n = 6
        sum2 = geometric_sum_by_last(a1, an, n)
        print(f"\n首项{a1}，末项{an}，项数{n}的等比数列的和为：{sum2}")
        
    except ValueError as e:
        print(f"错误：{e}")
    except ZeroDivisionError:
        print("错误：公比不能为1") 