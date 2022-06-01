name1,name2 = input("ENTER TWO NAMES : ").lower().split()

flames = ["is FRIEND of ","LOVES","AFFECTION with","wants to MARRY","is ENEMY of","is SISTER of"]
comb_name = name1 + name2
comb_name_set = set(comb_name)
common_letter = 0
same_letter = 0
list = []
for i in comb_name_set :
    tot_letters = comb_name.count(i)
    if tot_letters > 1 :
        list.append(tot_letters)
for i in list :
        if i%2 == 0 :
            common_letter += i
        else :
            common_letter = common_letter + i - 1
            
# repetitive letters in name1
for i in set(name1) :
    rep_letters_nmae1 = name1.count(i)
    if rep_letters_nmae1 > 1 and i not in name2 :
        same_letter += rep_letters_nmae1
        
# repetitive letters in name2
for i in set(name2) :
    rep_letters_name2 = name2.count(i)
    if rep_letters_name2 > 1 and i not in name1 :
        same_letter += rep_letters_name2

value = len(comb_name) - common_letter + same_letter
print(value)
run = True
while run :
    split_index = (value%len(flames)-1)
    if split_index >= 0 :
        l_rem = flames[split_index+1:]
        r_rem = flames[:split_index]
        flames = l_rem + r_rem
    else :
        flames = flames[:len(flames)-1]
    if len(flames)  ==  1 :
        run = False
    
FLAMES = "".join(flames)
print(f'{name1} {FLAMES} {name2}')