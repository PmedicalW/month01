# season = int(input("请输入季度:"))
# if season < 1 or season > 4:
#     print("输入有误")
# elif season == 1:
#     print("有1,2,3月")
# elif season == 2:
#     print("有4,5,6月")
# elif season == 3:
#     print("有7,8,9月")
# else:
#     print("有10,11,12月")

# [(季度,月份)]
seasons = {
    1: "有1,2,3月",
    2: "有4,5,6月",
    3: "有7,8,9月",
    4: "有10,11,12月"
}

season = int(input("请输入季度:"))
# 判断键是否存在
if season not in seasons:
    print("输入有误")
else:
    value = seasons[season]
    print(value)