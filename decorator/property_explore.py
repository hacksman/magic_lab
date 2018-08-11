#!/usr/bin/env python 
# coding:utf-8
# @Time :8/11/18 11:04


class BeforePayroll(object):
    def __init__(self, name, year, money):
        self.name = name
        self.year = year
        self.money = money

    def bonus(self):
        return self.year*self.money


class AfterPayroll(object):
    def __init__(self, name, year, money):
        self.name = name
        self.raw_year = year
        self.raw_money = money

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

    def bonus(self):
        return self.year*self.money


if __name__ == '__main__':
    xiao_ming_before = BeforePayroll("xiao_ming", 1, 3000)
    # change before
    print "change before:\t{} worked {} years, payroll is {} last year, bonus is {}".format(xiao_ming_before.name,
                                                                                            xiao_ming_before.year,
                                                                                            xiao_ming_before.money,
                                                                                            xiao_ming_before.bonus())
    xiao_ming_before.year += 1
    xiao_ming_before.money += 1000

    print "change before:\t{} worked {} years now and payroll is {}, bouns is {}".format(xiao_ming_before.name,
                                                                                         xiao_ming_before.year,
                                                                                         xiao_ming_before.money,
                                                                                         xiao_ming_before.bonus())

    xiao_ming_after = AfterPayroll("xiao_ming", 1, 3000)

    # change after
    print "change after:\t{} worked {} years, payroll is {}K last year, bonus is {}K".format(xiao_ming_after.name,
                                                                                             xiao_ming_after.year,
                                                                                             xiao_ming_after.money,
                                                                                             xiao_ming_after.bonus())
    xiao_ming_after.year += 1
    xiao_ming_after.money += 1000

    print "change after:\t{} worked {} years now and payroll is {}K, bouns is {}K".format(xiao_ming_after.name,
                                                                                          xiao_ming_after.year,
                                                                                          xiao_ming_after.money,
                                                                                          xiao_ming_after.bonus())
