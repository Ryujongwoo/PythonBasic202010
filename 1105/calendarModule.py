#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 인수로 년을 넘겨받아 윤년, 평년을 판단해서 윤년이면 True, 평년이면 False를 리턴하는 함수
# 윤년, 평년 판별식 => 년도가 4로 나눠 떨어지고 100으로 나눠 떨어지지 않거나 400으로 나눠 떨어지면 윤년
def isLeapYear(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


# In[10]:


# 인수로 년, 월을 넘겨받아 그 달의 마지막 날짜를 리턴하는 함수
def lastDay(year, month):
    # 12달의 마지막 날짜를 기억하는 리스트를 선언한다.
    m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 2월의 마지막 날짜를 확정한다.
    # if isLeapYear(year):
        # m[1] = 29
    m[1] = 29 if isLeapYear(year) else 28
    # 그 달의 마지막 날짜를 리턴한다
    return m[month - 1]


# In[26]:


# 인수로 년, 월, 일을 넘겨받아 1년 1월 1일 부터 지난 날짜의 합계를 리턴하는 함수
def totalDay(year, month, day):
    # 1년 1월 1일 부터 전년도 12월 31일 까지 지난 날짜를 계산한다.
    total = (year - 1) * 365 + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400
    # 전년도 까지 지난 날짜에 전달 까지 지난 날짜를 더해준다.
    for i in range(1, month):
        total += lastDay(year, i)
    # 전달 까지 지난 날짜에 일을 더해서 리턴시킨다.
    return total + day


# In[28]:


# 인수로 년, 월, 일을 넘겨받아 요일을 숫자로 리턴하는 함수
# 일요일(0), 월요일(1), 화요일(2), 수요일(3), 목요일(4), 금요일(5), 토요일(6)
def weekDay(year, month, day):
    return totalDay(year, month, day) % 7


# In[29]:



if __name__ == '__main__':
    print(isLeapYear(2100))
    print(lastDay(2020, 11))
    print(totalDay(2020, 11, 5))
    print(weekDay(2020, 11, 5))


# In[ ]:





# In[ ]:





# In[ ]:




