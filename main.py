import calculation

def main():
    radius = float(input("请输入圆的半径: "))
    area = calculation.calarea.circle_area(radius)
    circum = calculation.circle_circum(radius)
    print(f"圆的面积是: {area}")
    print(f"圆的周长是: {circum}")

if __name__ == "__main__":
    main()