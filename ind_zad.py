#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Напечатать в обратном порядке последовательность чисел
# признаком конца которой является 0


def reverse(string):
   if len(string) == 0:
      return string
   else:
      return reverse(string[1:]) + string[0]
        
      
if __name__ == '__main__':
   a = str(input("Введите строку: "))
   print(reverse(a))

# Проверка

    def is_palindrome(string):
        reversed_string = string[::-1]
        return string == reversed_string

    print(is_palindrome(''))













