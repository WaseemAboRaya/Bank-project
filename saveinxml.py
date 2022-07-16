import studentaccount
import business
import account
import person
import os

def personalInfo(a):
    st = ""
    st += "<personalInfo>"
    st += "<name>" + a.name + "</name>"
    st += "<id>" + str(a.id) + "</id>"
    st += "<phone>" + str(a.ph) + "</phone>"
    st += "<email>" + a.email + "</email>"
    st += "</personalInfo>"
    return st


def forStudentBankAccount(a: studentaccount.StudentBankAccount):
    st = "<account name='StudentBankAccount'>"
    st += personalInfo(a)
    st += "<balance>" + str(a.balance) + "</balance>"
    st += "<college>" + a.college_name + "</college>"
    st += "</account>"
    return st


def forBusinessBankAccount(a: business.BusinessBankAccount):
    st = "<account name='BusinessBankAccount'>"
    st += personalInfo(a)
    st += "<balance>" + str(a.balance) + "</balance>"
    st += "<business_info>" + a.business_info + "</business_info>"
    st += "</account>"
    return st


def forBankAccount(a: account.BankAccount):
    st = "<account name='BankAccount'>"
    st += personalInfo(a)
    st += "<balance>" + str(a.balance) + "</balance>"
    st += "</account>"
    return st


def hasXmlFile():
    return os.path.exists('./my_bank_account.xml')


def buildXmlFile():
    if not hasXmlFile():
        f = open("my_bank_account.xml", "w")
        f.close()
        f = open("my_bank_account.xml", "w")
        f.write("<accounts>" + "</accounts>")
        f.close()


def pushAccuntToXmlFile(a):
    f = open("my_bank_account.xml", "r")
    s = f.read()
    f.close()
    f = open("my_bank_account.xml", "w")
    if isinstance(a,business.BusinessBankAccount):
         f.write(s[:10] + forBusinessBankAccount(a) + s[10:])
    elif isinstance(a,studentaccount.StudentBankAccount):
        f.write(s[:10] + forStudentBankAccount(a) + s[10:])
    elif isinstance(a,account.BankAccount):
        f.write(s[:10] + forBankAccount(a) + s[10:])
    f.close()


# buildXmlFile()
# a = studentaccount.StudentBankAccount(205, "osama", 2504, "sdsa@", 2000, "haifa college")
# pushAccuntToXmlFile(a)
# q=business.BusinessBankAccount(205, "waseem", 2504, "sdsa@", 2000,"usiess is good")
# pushAccuntToXmlFile(q)
# s=account.BankAccount(205, "mohammed", 2504, "sdsa@", 2000)
# pushAccuntToXmlFile(s)