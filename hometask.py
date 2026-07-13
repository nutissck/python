#8.1
"""def check_forbidden(text):
    for i in text:
        if i in "@#$%":
            return "Знайдено заборонений символ!"
            break
    else:
        return "Заборонених символів не знайдено"
a=input()
print(check_forbidden(a))"""
#8.2
"""def count_vowels(text):
    vowels = "аеєиіїоуюяАЕЄИІЇОУЮЯ"
    vowel_count = 0
    for i in text:
        if i in vowels:
            vowel_count += 1
    return vowel_count
print(count_vowels("Україна"))"""
#9
"""def filter_even(numbers):
    even_numbers = []
    for i in numbers:
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers
a=list(map(int,input().split()))
print(filter_even(a))"""
#10
"""def find_first_divisible(numbers, d):
    for i in numbers:
        if i % d == 0:
            return i
            break
    else:
        return None
n=list(map(int,input().split()))
d=int(input())
print(find_first_divisible(n,d))"""








