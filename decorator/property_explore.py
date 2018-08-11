#!/usr/bin/env python 
# coding:utf-8
# @Time :8/11/18 11:04


class Payroll(object):
    def __init__(self, name, year, money):
        self.name = name
        # change before
        # self.year = year
        # self.money = money

        # change after
        self.raw_year = year
        self.raw_money = money

    # change after start
    @property
    def money(self):
        if self.raw_money / 1000 != 0:
            return self.raw_money / 1000
        else:
            return self.raw_money

    @money.setter
    def money(self, money):
        self.raw_money = money % 1000 + money // 1000

    @property
    def year(self):
        return self.raw_year

    @year.setter
    def year(self, year):
        self.raw_year = year
    # change after end

    def bonus(self):
        return self.year*self.money


if __name__ == '__main__':
    xiao_ming = Payroll("xiao_ming", 1, 3000)
    # # change before
    # print "{} worked {} years, payroll is {} last year, bonus is {}".format(xiao_ming.name,
    #                                                                         xiao_ming.year,
    #                                                                         xiao_ming.money,
    #                                                                         xiao_ming.bonus())

    # change after
    print "{} worked {} years, payroll is {}K last year, bonus is {}K".format(xiao_ming.name,
                                                                              xiao_ming.year,
                                                                              xiao_ming.money,
                                                                              xiao_ming.bonus())
    xiao_ming.year += 1
    xiao_ming.money += 1000

    # # change before
    # print "{} worked {} years now and payroll is {}, bouns is {}".format(xiao_ming.name,
    #                                                                      xiao_ming.year,
    #                                                                      xiao_ming.money,
    #                                                                      xiao_ming.bonus())

    # change after
    print "{} worked {} years now and payroll is {}K, bouns is {}K".format(xiao_ming.name,
                                                                           xiao_ming.year,
                                                                           xiao_ming.money,
                                                                           xiao_ming.bonus())