import calc

a = 10
b = 2

result_add = calc.add(a,b)
result_sub = calc.sub(a,b)
result_mul = calc.mul(a,b)
result_div = calc.div(a,b)

result = "add = {}, sub = {}, mul = {}, div = {}".format(result_add, result_sub, result_mul, result_div)

print(result)