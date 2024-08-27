my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
st_ = 0
while st_ < len(my_list):
      if my_list[st_] >= 0:
        print(my_list[st_])
      st_ += 1
      if my_list[st_] < 0:
          break
