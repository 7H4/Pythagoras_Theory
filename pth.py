from math import sqrt

print('ပိုက်သာဂိုရပ် သီဆိုရမ်')
print('ထောင့်မှန်တြိဂံ၏အနားများကိုတွက်ချက်ကြမယ်')
print('အနားများကို a b c လို့ယူဆပါ။c သည်ထောင့်မှန်ခံအနားဖြစ်သည်။')

formula = input('အနား a b c များထဲမှ မည်သည့်အနားကိုတွက်မည်နည်း။>>>> ')

if formula == 'c':
        side_a = int(input('အနားa၏အလျားကိုထည့်ပါ: '))
        side_b = int(input('အနားb၏အလျားကိုထည့်ပါ: '))

        side_c = sqrt(side_a * side_a + side_b * side_b)

        print('အနားc၏အလျား: ' )
        print(side_c)

elif formula == 'a':
    side_b = int(input('အနားb၏အလျားကိုထည့်ပါ: '))
    side_c = int(input('အနားc၏အလျားကိုထည့်ပါ: '))

    side_a = sqrt((side_c * side_c) - (side_b * side_b))

    print('အနားa၏အလျား' )
    print(side_a)


elif formula == 'b':
    side_a = int(input('အနားa၏အလျားကိုထည့်ပါ: '))
    side_c = int(input('အနားc၏အလျားကိုထည့်ပါ: '))

    side_b = sqrt(side_c * side_c - side_a * side_a)

    print('အနားb၏အလျား')
    print(side_b)


else:
        print('ကျေးဇူးပြု၍ a b c တစ်ခုသာရွေးချယ်ပါ။ ')
