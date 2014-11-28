#! /usr/bin/env python
#coding:utf-8

from sys import argv

script,input_file = argv

#打印文件的所有内容
def print_all(f):
    print f.read()


#回到文件的第一行初始化位置
def rewind(f):
    f.seek(0)

#打印文件的第一行内容
def print_a_line(line_count,f):
    print line_count,f.readline()



current_file = open(input_file)

print "Now let's rewind,kind of like a tape."

rewind(current_file)

print "Let's print three lines: "

current_line = 1

print_a_line(current_line,current_file)


current_line = current_line + 1

print_a_line(current_line,current_file)
